"""Renderiza frames do jogo em PNG (headless) para inspecao visual do HUD e elementos."""
import os

os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
os.environ.setdefault("SDL_AUDIODRIVER", "dummy")

import pygame  # noqa: E402
import main as m  # noqa: E402

OUT = "/tmp/trailquest"
os.makedirs(OUT, exist_ok=True)


def save(name):
    big = pygame.transform.scale(m.canvas, m.DISPLAY_SIZE)
    pygame.image.save(big, f"{OUT}/{name}.png")
    print(f"  salvo {OUT}/{name}.png")


def draw_gameplay(player, world, frame, score, coins, lives, stars, bottles, combo):
    camera = max(0, player.x - (74 + int(min(player.base_speed - m.BASE_SPEED, 1.6) * 12)))
    m.bg(camera)
    m.draw_world_decor(camera)
    world.draw(camera, frame)
    m.draw_joao_pedro(int(player.x - camera), int(player.y), frame, player.ducking)
    distance = int(player.x // 10)
    m.hud(score, coins, lives, distance, stars, bottles, 1018,
          True, player.speed, combo)
    return camera


# 1) Tela de titulo
m.bg(0)
m.hud(0, 0, 3, 0, 0, 0, 1018, True, m.BASE_SPEED, 0)
m.overlay_title()
save("01_titulo")

# 2) Gameplay raso (~50m), inicio tranquilo
world = m.World()
world.generate_until(20000)
p = m.Player()
p.x = 520  # ~52m
p.base_speed = m.speed_at(p.x)
p.speed = p.base_speed
draw_gameplay(p, world, 30, 12, 12, 3, 1, 0, 4)
save("02_inicio")

# 3) Gameplay profundo com passaro na tela + boost discreto + agachando
birds = sorted([o for o in world.obstacles if isinstance(o, m.Bird)], key=lambda o: o.x)
bird = birds[0] if birds else None
if bird:
    p2 = m.Player()
    p2.x = bird.x - 96
    p2.base_speed = m.speed_at(p2.x)
    p2.boost_timer = 60
    p2.speed = p2.base_speed + m.BOOST_BONUS
    p2.ducking = True    # agachando para o passaro
    p2.on_ground = True
    cam = draw_gameplay(p2, world, 44, 980, 140, 4, 9, 6, 17)
    print(f"  passaro em x={bird.x} ({bird.x/10:.0f}m), jogador x={p2.x}, cam={cam:.0f}")
    save("03_profundo_passaro")
else:
    print("  nenhum passaro encontrado")

# 4) Tela de game over (novo recorde)
m.bg(0)
m.overlay_end(1450, 9, 6, 1240, 1018, True)
save("04_gameover")

# 5) Game over normal
m.bg(0)
m.overlay_end(620, 3, 2, 540, 1018, False)
save("05_gameover_normal")

print("pronto")
