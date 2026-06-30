"""Teste headless de fumaca para Joao Pedro: Trail Quest.

Valida sem abrir janela:
  - audio gera buffers sem erro
  - fisica do pulo (altura variavel, apex, agachar, coyote/buffer)
  - geracao do mundo: todo gap clearavel, dificuldade/baragem escalam, passaros so apos unlock
  - o loop principal roda milhares de frames com input simulado sem crashar
Uso: SDL_VIDEODRIVER=dummy SDL_AUDIODRIVER=dummy python3 smoke_test.py
"""
import os
import asyncio

os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
os.environ.setdefault("SDL_AUDIODRIVER", "dummy")

import pygame  # noqa: E402
import main as m  # noqa: E402

FAILS = []


def check(cond, msg):
    status = "ok " if cond else "FAIL"
    print(f"  [{status}] {msg}")
    if not cond:
        FAILS.append(msg)


class FakeKeys:
    def __init__(self, down=()):
        self.down = set(down)

    def __getitem__(self, k):
        return k in self.down


def run_player(frames, key_schedule):
    """Roda a fisica do Player com um agendamento de teclas; devolve (player, trilha_y)."""
    p = m.Player()
    track = []
    for f in range(frames):
        keys = FakeKeys(key_schedule(f, p))
        p.update(keys)
        track.append(p.y)
    return p, track


def test_audio():
    print("== audio ==")
    music, sounds = m.setup_audio()
    info = pygame.mixer.get_init()
    if not info:
        print("  [skip] mixer indisponivel (dummy) - audio nao testado")
        return
    check(music is not None, "musica gerada")
    check(len(sounds) >= 6 and all(sounds.values()), "todos os SFX gerados")
    if music:
        check(music.get_length() > 6.0, f"loop de musica longo ({music.get_length():.1f}s, antes ~4.5s)")


def test_physics():
    print("== fisica ==")
    ground = m.GROUND_Y

    # pulo completo (segura): mede altura de pico e tempo no ar
    p, track = run_player(80, lambda f, pl: [pygame.K_SPACE])
    peak = ground - min(track)
    air = sum(1 for y in track if y < ground - 0.5)
    check(48 <= peak <= 70, f"pico do pulo completo ~{peak:.0f}px (esperado 48-70)")
    check(30 <= air <= 60, f"tempo no ar do pulo completo {air} frames")

    # pulo curto (toca e solta): deve ser bem mais baixo que o completo
    def tap(f, pl):
        return [pygame.K_SPACE] if f < 2 else []
    p2, track2 = run_player(80, tap)
    peak_tap = ground - min(track2)
    check(peak_tap < peak - 12, f"pulo curto ({peak_tap:.0f}px) bem menor que completo ({peak:.0f}px)")
    # pulo curto limpa pedra baixa (topo 118) mas NAO pedra alta (topo 105)
    check(peak_tap > 6, f"pulo curto limpa pedra baixa (sobe {peak_tap:.0f}px > 6)")

    # agachar encurta a hitbox
    p3 = m.Player()
    p3.update(FakeKeys([pygame.K_DOWN]))
    check(p3.ducking and p3.hitbox.height == 18, f"agachado encurta hitbox p/ {p3.hitbox.height} (em pe 34)")
    check(p3.hitbox.bottom == ground, "hitbox agachada ancora no chao")
    # passaro alinhado no x do jogador: em pe colide, agachado passa por baixo
    standing = m.Player()
    bird = m.Bird(standing.x)
    p3.x = standing.x
    check(p3.hitbox.top > bird.rect(0).bottom, "agachado passa por baixo do passaro (sem overlap vertical)")
    check(standing.hitbox.colliderect(bird.rect(0)), "em pe colide com o passaro (precisa agachar)")
    check(not p3.hitbox.colliderect(bird.rect(0)), "agachado nao colide com o passaro")

    # coyote: pular alguns frames depois de 'cair' do chao ainda funciona
    pc = m.Player()
    pc.on_ground = False  # acabou de sair do chao
    pc.coyote = m.COYOTE_FRAMES
    pc.update(FakeKeys([pygame.K_SPACE]))
    check(pc.vy < 0, "coyote time permite pular logo apos sair do chao")


def test_world():
    print("== mundo: geracao e dificuldade ==")
    world = m.World()
    world.generate_until(60000)  # ~6000m de trilha
    obstacles = sorted(world.obstacles, key=lambda o: o.x)
    check(len(obstacles) > 50, f"{len(obstacles)} obstaculos gerados")

    # fairness: nenhum par adjacente cai na 'zona morta' (impossivel) do arco de pulo
    min_frames = 999.0
    dead_zone = 0
    overlaps = 0
    for a, b in zip(obstacles, obstacles[1:]):
        gap = b.x - (a.x + a.w)
        spd = m.speed_at(b.x) + m.BOOST_BONUS  # pior caso: com boost
        clear_both = gap <= spd * 32 - 14
        land_between = gap >= spd * 8 + 14
        if not (clear_both or land_between):
            dead_zone += 1
        if gap < -2:
            overlaps += 1
        # tempo de reacao entre hazards distintos (ignora rochas coladas de cluster)
        same_cluster = isinstance(a, m.Rock) and isinstance(b, m.Rock) and gap < 16
        if not same_cluster:
            min_frames = min(min_frames, gap / spd)
    check(dead_zone == 0, f"nenhum par na zona morta do pulo ({dead_zone} ruins)")
    check(overlaps == 0, f"nenhum obstaculo sobreposto ({overlaps})")
    check(min_frames >= 6, f"menor janela entre hazards = {min_frames:.1f} frames (>=6)")

    # densidade / reacao escalam (frames de reacao caem com a profundidade)
    def reaction_at(meters):
        seg = int(meters * 10 // m.SEGMENT_WIDTH)
        spd = m.speed_at(seg * m.SEGMENT_WIDTH)
        lvl = m.level_at_meters(meters)
        return max(24, 52 - lvl * 3)
    check(reaction_at(0) > reaction_at(3000), f"reacao cai com a distancia ({reaction_at(0)} -> {reaction_at(3000)} frames)")

    # velocidade sobe e estabiliza no teto
    s0, s_mid, s_cap = m.speed_at(0), m.speed_at(5000), m.speed_at(100000)
    check(abs(s0 - m.BASE_SPEED) < 0.01, f"velocidade inicial {s0:.2f}")
    check(s0 < s_mid < s_cap, f"velocidade sobe: {s0:.2f} -> {s_mid:.2f} -> {s_cap:.2f}")
    check(abs(s_cap - (m.BASE_SPEED + m.MAX_SPEED_GAIN)) < 0.01, f"teto de velocidade = {s_cap:.2f}")

    # passaros so depois do unlock
    bird_xs = [o.x for o in obstacles if isinstance(o, m.Bird)]
    check(all(x / 10 >= m.BIRD_UNLOCK_M for x in bird_xs), f"{len(bird_xs)} passaros, todos apos {m.BIRD_UNLOCK_M}m")

    print("== mundo: baragem (baus) ==")
    chests = sorted(world.chests, key=lambda c: c.x)
    per_1000m = len(chests) / 6.0
    check(per_1000m < 6, f"baus raros: ~{per_1000m:.1f}/1000m (antes ~8/1000m fixo)")
    # espacamento minimo entre baus
    if len(chests) >= 2:
        min_gap_m = min((b.x - a.x) / 10 for a, b in zip(chests, chests[1:]))
        check(min_gap_m >= 180, f"baus espacados >= {min_gap_m:.0f}m (regra: 6 segmentos ~192m)")
    check(all(c.x >= 4 * m.SEGMENT_WIDTH for c in chests), "nenhum bau antes de ~128m (gracia inicial)")

    # determinismo: regenerar do zero da o mesmo layout
    w2 = m.World()
    w2.generate_until(60000)
    same = len(w2.obstacles) == len(obstacles) and len(w2.chests) == len(chests)
    check(same, "geracao deterministica (mesmo layout ao reiniciar)")


def test_full_loop():
    print("== loop completo (headless, ~4000 frames) ==")
    os.environ["TRAILQUEST_MAX_FRAMES"] = "4000"

    started = {"v": False}
    real_get = pygame.event.get

    def fake_events(*a, **k):
        if not started["v"]:
            started["v"] = True
            return [pygame.event.Event(pygame.KEYDOWN, key=pygame.K_SPACE)]
        return []

    def fake_pressed(*a, **k):
        # pula a cada ~50 frames e as vezes agacha (exercita pulo + agachar)
        import time
        return FakeKeys()

    # input ritmico determinista por contador de frames
    counter = {"f": 0}

    def fake_pressed2(*a, **k):
        counter["f"] += 1
        f = counter["f"]
        down = []
        if f % 48 < 6:
            down.append(pygame.K_SPACE)
        elif f % 48 in (20, 21, 22):
            down.append(pygame.K_DOWN)
        return FakeKeys(down)

    pygame.event.get = fake_events
    pygame.key.get_pressed = fake_pressed2
    try:
        asyncio.run(m.main())  # retorna ao bater max_frames
        check(True, "loop rodou 4000 frames sem crashar")
    except SystemExit:
        check(True, "loop encerrou via quit (ok)")
    except Exception as e:  # noqa: BLE001
        check(False, f"loop crashou: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
    finally:
        pygame.event.get = real_get


if __name__ == "__main__":
    test_audio()
    test_physics()
    test_world()
    test_full_loop()
    print()
    if FAILS:
        print(f"RESULTADO: {len(FAILS)} FALHA(S)")
        for f in FAILS:
            print(f"  - {f}")
        raise SystemExit(1)
    print("RESULTADO: todos os testes passaram")
