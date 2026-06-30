import asyncio
import math
import os
import random
import sys
from array import array
from pathlib import Path

import pygame

IS_WEB = sys.platform in ("emscripten", "wasi")

pygame.mixer.pre_init(22050, -16, 1, 512)
pygame.init()

VW, VH = 320, 180
SCALE = 3 if IS_WEB else 4
DISPLAY_SIZE = (VW * SCALE, VH * SCALE)
screen = pygame.display.set_mode(DISPLAY_SIZE)
pygame.display.set_caption("Joao Pedro: Trail Quest")
canvas = pygame.Surface((VW, VH))
clock = pygame.time.Clock()

FONT = pygame.font.SysFont("couriernew", 10, bold=True)
BIG = pygame.font.SysFont("couriernew", 18, bold=True)


def configure_browser_canvas():
    if not IS_WEB:
        return
    try:
        import platform as web_platform

        window = web_platform.window
        canvas_el = window.canvas
        style = canvas_el.style
        style.imageRendering = "pixelated"
        style.width = f"{DISPLAY_SIZE[0]}px"
        style.height = f"{DISPLAY_SIZE[1]}px"
        style.maxWidth = "100vw"
        style.maxHeight = "100vh"
        style.objectFit = "contain"

        body = window.document.body.style
        body.margin = "0"
        body.background = "#111218"
        body.display = "flex"
        body.alignItems = "center"
        body.justifyContent = "center"
        body.minHeight = "100vh"
    except Exception:
        pass


configure_browser_canvas()

SKY = (89, 191, 255)
SKY_DARK = (52, 145, 220)
CLOUD = (245, 248, 231)
MOUNTAIN = (102, 130, 150)
MOUNTAIN_DARK = (75, 100, 122)
TREE = (25, 117, 61)
TREE_DARK = (16, 78, 48)
DIRT = (154, 96, 45)
DIRT_DARK = (107, 62, 32)
GRASS = (61, 156, 67)
GRASS_DARK = (36, 105, 45)
BLACK = (17, 18, 24)
WHITE = (245, 245, 235)
YELLOW = (255, 208, 45)
GOLD = (224, 152, 30)
RED = (230, 56, 54)
BLUE = (46, 164, 235)
PINK = (224, 78, 133)
SKIN = (224, 152, 98)
BROWN = (84, 54, 32)
WOOD = (110, 66, 34)
WOOD_LIGHT = (174, 105, 47)
ORANGE = (238, 129, 36)
GREEN_LIGHT = (118, 205, 85)
CYAN = (67, 205, 238)
ROCK = (90, 83, 78)
ROCK_LIGHT = (140, 130, 118)
BIRD_BODY = (96, 96, 110)
BIRD_WING = (60, 60, 78)
SUN = (255, 228, 94)
SUN_EDGE = (248, 177, 58)
HILL = (68, 145, 91)
HILL_DARK = (46, 111, 75)
FLOWER = (255, 105, 152)

# --- Velocidade estilo chrome://dino: comeca viva e sobe continuamente ---
BASE_SPEED = 2.4          # velocidade inicial (px/frame)
SPEED_RAMP = 320.0        # metros (x/10) por +1.0 de velocidade
MAX_SPEED_GAIN = 2.2      # teto: velocidade base maxima = 4.6
BOOST_BONUS = 0.7
BOOST_FRAMES = 150        # boost mais curto/raro para a aceleracao "aparecer"

# --- Pulo com altura variavel + perdao (coyote/buffer) ---
JUMP_FORCE = -5.75
JUMP_CUT_VY = -2.4        # soltar o pulo enquanto sobe = pulo curto
APEX_BAND = 1.2           # perto do apice a gravidade afrouxa (flutua)
APEX_GRAVITY = 0.62
GRAVITY = 0.32
COYOTE_FRAMES = 6
JUMP_BUFFER_FRAMES = 6

MAX_LIVES = 5
START_LIVES = 3
SEGMENT_WIDTH = 320
GENERATE_AHEAD = 1100
CLEANUP_BEHIND = 260
GROUND_Y = 124
MUSHROOM_GROUND_Y = 111
MUSHROOM_JUMP_Y = 76
BIRD_UNLOCK_M = 900       # passaros (precisam de agachar) a partir de ~900m
BIRD_Y = 92
LEVEL_METERS = 250        # 1 nivel a cada 250m (HUD e dificuldade alinhados)
BEST_FILE = Path(__file__).with_name("recorde_trail.txt")


def speed_at(x):
    """Velocidade base deterministica para uma posicao x (px). Sobe e estabiliza no teto."""
    return BASE_SPEED + min((x / 10.0) / SPEED_RAMP, MAX_SPEED_GAIN)


def level_at_meters(distance):
    return int(distance // LEVEL_METERS)


def box(color, x, y, w, h):
    pygame.draw.rect(canvas, color, pygame.Rect(int(x), int(y), int(w), int(h)))


def text(msg, x, y, color=WHITE, font=FONT, center=False):
    img = font.render(msg, False, color)
    if center:
        x -= img.get_width() // 2
    shadow = font.render(msg, False, BLACK)
    canvas.blit(shadow, (x + 1, y + 1))
    canvas.blit(img, (x, y))


def heart(x, y):
    pixels = ["0110110", "1111111", "1111111", "0111110", "0011100", "0001000"]
    for py, row in enumerate(pixels):
        for px, c in enumerate(row):
            if c == "1":
                box(RED, x + px, y + py, 1, 1)


def coin(x, y, frame=0):
    wobble = int(math.sin(frame / 6) * 1)
    box(GOLD, x + 1 + wobble, y, 6 - abs(wobble), 8)
    box(YELLOW, x + 2 + wobble, y + 1, 3, 6)
    box(WHITE, x + 3 + wobble, y + 2, 1, 2)


def star_icon(x, y, frame=0, color=YELLOW):
    shimmer = WHITE if frame % 30 < 6 else color
    pixels = ["00100", "10101", "01110", "11111", "01010", "10001"]
    for py, row in enumerate(pixels):
        for px, c in enumerate(row):
            if c == "1":
                box(shimmer if py == 0 else color, x + px, y + py, 1, 1)


def wood_panel(x, y, w, h):
    box(BLACK, x - 2, y - 2, w + 4, h + 4)
    box(WOOD, x, y, w, h)
    box(WOOD_LIGHT, x + 2, y + 2, w - 4, 2)
    for px in range(x + 6, x + w - 4, 18):
        box(DIRT_DARK, px, y + 2, 2, h - 4)


def chest(x, y, opened=False):
    box(BLACK, x - 1, y - 1, 21, 16)
    if opened:
        box(WOOD_LIGHT, x + 1, y - 7, 17, 7)
        box(WOOD, x, y + 3, 19, 11)
        box(YELLOW, x + 7, y - 1, 5, 5)
    else:
        box(WOOD_LIGHT, x, y, 19, 6)
        box(WOOD, x, y + 6, 19, 8)
        box(YELLOW, x + 8, y + 4, 4, 5)
    box(GOLD, x, y + 6, 19, 2)


def mushroom(x, y):
    box(WHITE, x + 5, y + 6, 5, 7)
    pygame.draw.polygon(canvas, RED, [(x, y + 8), (x + 4, y), (x + 12, y), (x + 16, y + 8)])
    box(WHITE, x + 4, y + 4, 2, 2)
    box(WHITE, x + 10, y + 3, 2, 2)
    box(BLACK, x + 4, y + 13, 8, 1)


def bottle(x, y, frame=0):
    shine = WHITE if frame % 18 < 9 else CYAN
    box(BLACK, x - 1, y - 1, 9, 17)
    box(WHITE, x + 2, y, 4, 3)
    box(CYAN, x + 1, y + 3, 6, 10)
    box(WHITE, x + 2, y + 5, 4, 3)
    box(shine, x + 5, y + 5, 1, 5)
    box(YELLOW, x + 2, y + 13, 4, 2)


def draw_rock(sx, y, w, h):
    pygame.draw.polygon(canvas, ROCK, [(sx, y + h - 1), (sx + 3, y + 2), (sx + w - 5, y), (sx + w - 1, y + h - 1)])
    pygame.draw.polygon(canvas, ROCK_LIGHT, [(sx + 3, y + 3), (sx + 9, y + 1), (sx + 7, y + 6)])


def draw_bird(sx, y, frame):
    flap_up = frame % 16 < 8
    box(BIRD_BODY, sx + 4, y + 2, 9, 6)
    box(WHITE, sx + 5, y + 3, 4, 2)
    box(YELLOW, sx + 12, y + 3, 3, 2)
    box(BLACK, sx + 11, y + 2, 1, 1)
    if flap_up:
        pygame.draw.polygon(canvas, BIRD_WING, [(sx + 5, y + 3), (sx + 1, y - 3), (sx + 9, y + 3)])
    else:
        pygame.draw.polygon(canvas, BIRD_WING, [(sx + 5, y + 5), (sx + 1, y + 11), (sx + 9, y + 5)])


def draw_sun(camera):
    sx = 248 - int(camera * 0.025) % 420
    if sx < -32:
        sx += 420
    pygame.draw.circle(canvas, SUN_EDGE, (sx, 32), 14)
    pygame.draw.circle(canvas, SUN, (sx, 32), 11)
    for dx, dy in [(-20, 0), (20, 0), (0, -20), (0, 20)]:
        box(SUN, sx + dx, 31 + dy, 5 if dx else 2, 2 if dx else 5)


def draw_background_hills(camera):
    for i in range(-1, 6):
        x = i * 86 - int(camera * 0.20) % 86
        pygame.draw.polygon(canvas, HILL_DARK, [(x, 122), (x + 42, 82), (x + 88, 122)])
        pygame.draw.polygon(canvas, HILL, [(x + 16, 122), (x + 58, 92), (x + 104, 122)])


def draw_midground_details(camera):
    for i in range(-1, 8):
        x = i * 72 - int(camera * 0.46) % 72
        box(BROWN, x + 10, 116, 4, 14)
        box(WOOD_LIGHT, x + 8, 116, 8, 2)
        box(BROWN, x + 38, 116, 4, 14)
        box(WOOD_LIGHT, x + 36, 116, 8, 2)
        pygame.draw.line(canvas, WOOD, (x + 12, 120), (x + 40, 120), 1)
    for i in range(-1, 10):
        x = i * 45 - int(camera * 0.55) % 45
        y = 133 + (i % 3) * 4
        box(HILL_DARK, x + 2, y + 3, 14, 3)
        box(HILL, x + 5, y, 9, 5)


def draw_ground_details(camera):
    for i in range(-1, 34):
        x = i * 18 - int(camera * 0.92) % 18
        if i % 4 == 0:
            box(FLOWER, x + 6, 139, 2, 2)
            box(YELLOW, x + 7, 138, 1, 1)
        elif i % 4 == 1:
            box(ROCK_LIGHT, x + 5, 142, 3, 2)
        else:
            box(GRASS_DARK, x + 3, 136 + (i % 2) * 5, 5, 1)


def world_sign(label, sx, y, color=YELLOW):
    if sx < -58 or sx > VW + 24:
        return
    box(BROWN, sx + 22, y - 3, 5, 29)
    wood_panel(sx, y - 18, 52, 16)
    text(label, sx + 26, y - 14, color, center=True)


def finish_flag(sx, y):
    box(BLACK, sx, y - 36, 2, 36)
    pygame.draw.polygon(canvas, WHITE, [(sx + 2, y - 36), (sx + 22, y - 31), (sx + 2, y - 25)])
    pygame.draw.polygon(canvas, ORANGE, [(sx + 4, y - 34), (sx + 18, y - 31), (sx + 4, y - 28)])


def bg(camera):
    canvas.fill(SKY)
    box(SKY_DARK, 0, 0, VW, 18)
    draw_sun(camera)

    for cx, cy in [(35, 32), (82, 22), (210, 30), (272, 22)]:
        ox = int(-(camera * 0.06) % 120)
        x = (cx + ox) % (VW + 50) - 25
        box(CLOUD, x, cy, 18, 5)
        box(CLOUD, x + 6, cy - 4, 10, 5)

    for i in range(-1, 5):
        mx = i * 90 - int(camera * 0.12) % 90
        pygame.draw.polygon(canvas, MOUNTAIN_DARK, [(mx, 115), (mx + 45, 45), (mx + 90, 115)])
        pygame.draw.polygon(canvas, MOUNTAIN, [(mx + 16, 90), (mx + 45, 45), (mx + 72, 90)])
        pygame.draw.polygon(canvas, CLOUD, [(mx + 39, 55), (mx + 45, 45), (mx + 51, 55)])

    draw_background_hills(camera)

    for i in range(-1, 8):
        tx = i * 55 - int(camera * 0.30) % 55
        ty = 105 + (i % 2) * 10
        box(BROWN, tx + 15, ty + 8, 5, 28)
        pygame.draw.polygon(canvas, TREE_DARK, [(tx + 17, ty - 20), (tx, ty + 18), (tx + 34, ty + 18)])
        pygame.draw.polygon(canvas, TREE, [(tx + 17, ty - 10), (tx + 3, ty + 25), (tx + 31, ty + 25)])

    box(GRASS, 0, 122, VW, VH - 122)
    for i in range(0, VW, 8):
        box(GRASS_DARK, i, 126 + (i % 3) * 5, 4, 2)
    draw_midground_details(camera)
    draw_ground_details(camera)

    path = []
    for px in range(0, VW + 20, 8):
        y = 150 + math.sin((px + camera * 0.3) / 23) * 7
        path.append((px, y))
    pygame.draw.lines(canvas, DIRT_DARK, False, path, 24)
    pygame.draw.lines(canvas, DIRT, False, path, 18)


class Player:
    def __init__(self):
        self.x = 22
        self.y = GROUND_Y
        self.vy = 0
        self.on_ground = True
        self.ducking = False
        self.invuln = 0
        self.base_speed = BASE_SPEED
        self.speed = BASE_SPEED
        self.boost_timer = 0
        self.jump_held_prev = False
        self.coyote = COYOTE_FRAMES
        self.jump_buffer = 0
        self.land_timer = 0
        self.jump_timer = 0
        self.knock_vx = 0.0

    @property
    def hitbox(self):
        if self.ducking:
            return pygame.Rect(int(self.x) + 6, int(self.y) - 18, 18, 18)
        return pygame.Rect(int(self.x) + 6, int(self.y) - 34, 18, 34)

    def update(self, keys):
        jumped = False
        landed = False
        jump_key = keys[pygame.K_SPACE] or keys[pygame.K_UP] or keys[pygame.K_w]
        duck_key = keys[pygame.K_DOWN] or keys[pygame.K_s]

        self.base_speed = speed_at(self.x)
        self.speed = self.base_speed + (BOOST_BONUS if self.boost_timer else 0)
        self.x += self.speed + self.knock_vx
        if self.knock_vx:
            self.knock_vx *= 0.7
            if abs(self.knock_vx) < 0.4:
                self.knock_vx = 0.0

        self.ducking = self.on_ground and duck_key

        # coyote time: alguns frames de tolerancia apos sair do chao
        if self.on_ground:
            self.coyote = COYOTE_FRAMES
        elif self.coyote:
            self.coyote -= 1

        # buffer de pulo: registra a tecla um pouco antes de pousar
        if jump_key and not self.jump_held_prev:
            self.jump_buffer = JUMP_BUFFER_FRAMES
        elif self.jump_buffer:
            self.jump_buffer -= 1

        if self.jump_buffer and (self.on_ground or self.coyote):
            self.vy = JUMP_FORCE
            self.on_ground = False
            self.ducking = False
            self.jump_buffer = 0
            self.coyote = 0
            self.jump_timer = 4
            jumped = True

        # altura variavel: soltar enquanto sobe corta o pulo
        if (not jump_key) and self.vy < JUMP_CUT_VY:
            self.vy = JUMP_CUT_VY

        # gravidade com "apex hang" (flutua no topo, da tempo de reacao)
        g = GRAVITY * (APEX_GRAVITY if abs(self.vy) < APEX_BAND else 1.0)
        self.vy += g
        self.y += self.vy

        if self.y >= GROUND_Y:
            if not self.on_ground:
                landed = True
                self.land_timer = 6
            self.y = GROUND_Y
            self.vy = 0
            self.on_ground = True

        self.x = max(8, self.x)
        if self.invuln:
            self.invuln -= 1
        if self.boost_timer:
            self.boost_timer -= 1
        if self.land_timer:
            self.land_timer -= 1
        if self.jump_timer:
            self.jump_timer -= 1
        self.jump_held_prev = jump_key
        return jumped, landed


class Coin:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.got = False

    def rect(self, camera):
        return pygame.Rect(self.x - camera, self.y, 8, 9)

    def draw(self, camera, frame):
        if not self.got:
            coin(int(self.x - camera), int(self.y), frame)


class Rock:
    def __init__(self, x, tall=False):
        self.x = x
        self.tall = tall
        self.w = 16 if tall else 14
        self.h = 25 if tall else 12
        self.y = 130 - self.h
        self.scored = False

    def rect(self, camera):
        return pygame.Rect(int(self.x - camera), self.y, self.w, self.h)

    def draw(self, camera, frame=0):
        draw_rock(int(self.x - camera), self.y, self.w, self.h)


class LogObstacle:
    def __init__(self, x):
        self.x = x
        self.y = 118
        self.w = 25
        self.scored = False

    def rect(self, camera):
        return pygame.Rect(self.x - camera, self.y + 2, 25, 9)

    def draw(self, camera, frame=0):
        sx = int(self.x - camera)
        box(BLACK, sx - 1, self.y + 1, 27, 11)
        box(WOOD, sx, self.y + 3, 25, 7)
        box(WOOD_LIGHT, sx + 2, self.y + 4, 18, 2)
        box(DIRT_DARK, sx + 20, self.y + 3, 3, 7)


class Bird:
    def __init__(self, x):
        self.x = x
        self.y = BIRD_Y
        self.w = 16
        self.scored = False

    def rect(self, camera):
        return pygame.Rect(int(self.x - camera) + 2, self.y + 1, 12, 8)

    def draw(self, camera, frame=0):
        draw_bird(int(self.x - camera), self.y, frame)


class MushroomBoost:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.got = False

    def rect(self, camera):
        return pygame.Rect(self.x - camera - 1, self.y - 1, 18, 17)

    def draw(self, camera):
        if not self.got:
            mushroom(int(self.x - camera), self.y)


class StarPickup:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.got = False

    def rect(self, camera):
        return pygame.Rect(self.x - camera, self.y, 10, 10)

    def draw(self, camera, frame):
        if not self.got:
            star_icon(int(self.x - camera), int(self.y), frame)


class ChestPickup:
    def __init__(self, x):
        self.x = x
        self.y = 108
        self.opened = False
        self.effect_timer = 0

    def rect(self, camera):
        return pygame.Rect(self.x - camera, self.y - 7, 20, 22)

    def draw(self, camera, frame):
        chest(int(self.x - camera), self.y, self.opened)
        if self.effect_timer:
            lift = int((70 - self.effect_timer) / 5)
            bottle(int(self.x - camera) + 6, self.y - 22 - lift, frame)
            self.effect_timer -= 1


def draw_joao_pedro(x, y, frame, ducking=False, squash=0):
    # Bicicleta
    pygame.draw.circle(canvas, BLACK, (int(x + 5), int(y - 5)), 5, 1)
    pygame.draw.circle(canvas, BLACK, (int(x + 19), int(y - 5)), 5, 1)
    spoke = frame % 12
    pygame.draw.line(canvas, BLACK, (x + 5, y - 10), (x + 5, y), 1)
    pygame.draw.line(canvas, BLACK, (x + 19, y - 10), (x + 19, y), 1)
    pygame.draw.line(canvas, BLACK, (x + 1 + spoke // 3, y - 5), (x + 9 - spoke // 3, y - 5), 1)
    pygame.draw.line(canvas, BLACK, (x + 15 + spoke // 3, y - 5), (x + 23 - spoke // 3, y - 5), 1)
    pygame.draw.line(canvas, CYAN, (x + 5, y - 5), (x + 11, y - 12), 2)
    pygame.draw.line(canvas, BLUE, (x + 19, y - 5), (x + 11, y - 12), 2)
    pygame.draw.line(canvas, CYAN, (x + 8, y - 13), (x + 16, y - 13), 2)
    pygame.draw.line(canvas, BLUE, (x + 16, y - 13), (x + 20, y - 16), 1)
    pygame.draw.line(canvas, BLUE, (x + 8, y - 13), (x + 9, y - 17), 1)
    box(BLACK, x + 8, y - 18, 4, 2)
    pygame.draw.line(canvas, BLACK, (x + 20, y - 16), (x + 23, y - 17), 1)

    if ducking:
        # João Pedro agachado (passa por baixo do passaro)
        box(SKIN, x + 8, y - 16, 8, 6)
        box(BROWN, x + 9, y - 17, 6, 2)
        box(WHITE, x + 6, y - 13, 12, 7)
        box(YELLOW, x + 11, y - 11, 3, 3)
        box(SKIN, x + 16, y - 12, 3, 2)
        box(BLACK, x + 10, y - 14, 1, 1)
        box(BLACK, x + 13, y - 14, 1, 1)
        box(RED, x + 11, y - 12, 2, 1)
        box(BLUE, x + 7, y - 7, 4, 2)
        box(BLUE, x + 14, y - 7, 4, 2)
        return

    top = y - 31 + squash  # squash desce o corpo alguns px no pouso
    box(SKIN, x + 8, top, 8, 8)          # rosto
    box(BROWN, x + 9, top - 2, 6, 2)     # cabelo
    box(WHITE, x + 7, top + 7, 10, 10 - squash)  # roupa
    box(YELLOW, x + 10, top + 10, 3, 3)  # estrela na roupa
    box(SKIN, x + 5, top + 9, 2, 6)      # braco
    box(SKIN, x + 17, top + 9, 2, 6)     # braco

    if frame % 12 < 6:
        pygame.draw.line(canvas, SKIN, (x + 10, y - 14), (x + 8, y - 8), 2)
        pygame.draw.line(canvas, SKIN, (x + 14, y - 14), (x + 17, y - 8), 2)
    else:
        pygame.draw.line(canvas, SKIN, (x + 10, y - 14), (x + 13, y - 8), 2)
        pygame.draw.line(canvas, SKIN, (x + 14, y - 14), (x + 10, y - 8), 2)
    box(BLUE, x + 7, y - 8, 4, 2)
    box(BLUE, x + 15, y - 8, 4, 2)

    box(BLACK, x + 10, top + 3, 1, 1)    # olhos
    box(BLACK, x + 13, top + 3, 1, 1)
    box(RED, x + 11, top + 6, 2, 1)      # sorriso


def draw_rafael_amanda(x, y):
    # Rafael
    box(BLACK, x + 4, y - 34, 12, 20)
    box(SKIN, x + 6, y - 46, 9, 9)
    box(BROWN, x + 5, y - 48, 11, 3)
    box(BLACK, x + 8, y - 42, 1, 1)
    box(BLACK, x + 12, y - 42, 1, 1)
    box(WHITE, x + 9, y - 39, 3, 1)
    box(WHITE, x + 8, y - 28, 4, 2)
    text("Rafael", x + 2, y - 58, BLUE)

    # Amanda
    box(PINK, x + 22, y - 34, 12, 20)
    box(SKIN, x + 24, y - 46, 9, 9)
    box(BROWN, x + 23, y - 48, 11, 4)
    box(BROWN, x + 31, y - 43, 3, 12)
    box(BLACK, x + 26, y - 42, 1, 1)
    box(BLACK, x + 30, y - 42, 1, 1)
    box(WHITE, x + 27, y - 39, 3, 1)
    heart(x + 26, y - 28)
    text("Amanda", x + 18, y - 58, PINK)


def hud(score, coins, hearts_left, distance, stars_found, bottles_found,
        best_distance, music_on, current_speed, combo):
    for i in range(hearts_left):
        heart(8 + i * 11, 8)
    coin(8, 23)
    text(f"x {coins}", 21, 23)
    star_icon(9, 39)
    text(f"x {stars_found}", 21, 37)
    bottle(8, 52)
    text(f"x {bottles_found}", 21, 55)

    # velocimetro estilo dino (mostra a aceleracao)
    pct = max(0.0, min(1.0, (current_speed - BASE_SPEED) / (MAX_SPEED_GAIN + BOOST_BONUS)))
    box(BLACK, 72, 23, 42, 6)
    bar_color = CYAN
    box(bar_color, 73, 24, int(40 * pct), 4)
    text(f"{current_speed:.1f}x", 72, 31, bar_color)
    text("PULO/AGACHA", 72, 43, WHITE)
    if combo >= 3:
        text(f"COMBO x{combo}", 72, 55, ORANGE)

    text(f"PTS {score}", VW // 2, 18, YELLOW, center=True)
    text("JOAO PEDRO: TRAIL QUEST", VW // 2, 7, YELLOW, center=True)

    box(BLACK, 221, 19, 91, 51)
    box((42, 47, 55), 224, 22, 85, 45)
    text("TRAIL MODE", 266, 25, WHITE, center=True)
    box(SKY, 229, 37, 34, 20)
    pygame.draw.polygon(canvas, TREE_DARK, [(230, 57), (242, 41), (254, 57)])
    pygame.draw.polygon(canvas, GREEN_LIGHT, [(239, 57), (254, 45), (263, 57)])
    pygame.draw.lines(canvas, DIRT, False, [(231, 57), (241, 51), (250, 51), (261, 45)], 3)
    finish_flag(261, 50)
    level = 1 + level_at_meters(distance)
    text(f"LVL {level}", 268, 37, YELLOW)
    text(f"{distance}m", 268, 47, WHITE)
    box(BLACK, 268, 57, 40, 4)
    fill = int(38 * ((distance % LEVEL_METERS) / LEVEL_METERS))
    box(YELLOW, 269, 58, fill, 2)
    text(f"REC {best_distance}m", 226, 62, CYAN)
    text("M", 301, 62, YELLOW if music_on else RED)


def overlay_title():
    box(BLACK, 25, 28, 270, 126)
    wood_panel(29, 32, 262, 118)
    text("JOAO PEDRO", VW // 2, 44, YELLOW, BIG, center=True)
    text("TRAIL QUEST", VW // 2, 64, WHITE, BIG, center=True)
    text("Trail!", VW // 2, 88, CYAN, center=True)
    text("ESPACO/W/cima: pula  |  baixo/S: agacha", VW // 2, 102, center=True)
    text("ESPACO para comecar  |  M musica", VW // 2, 128, WHITE, center=True)
    text("desenvolvido por @rafaelcotote", VW // 2, 166, CYAN, center=True)


def overlay_end(score, stars_found, bottles_found, distance, best_distance, beaten):
    box(BLACK, 40, 38, 240, 112)
    wood_panel(44, 42, 232, 104)
    text("NOVO RECORDE!" if beaten else "FIM DA CORRIDA", VW // 2, 58, GOLD if beaten else RED, BIG, center=True)
    text(f"Distancia: {distance}m", VW // 2, 84, YELLOW, center=True)
    text(f"Recorde: {best_distance}m", VW // 2, 96, CYAN, center=True)
    text(f"Pontos {score} | Estrelas {stars_found}", VW // 2, 110, WHITE, center=True)
    text(f"Mamadeiras: {bottles_found}", VW // 2, 122, PINK, center=True)
    text("R reinicia | ESC sai", VW // 2, 136, center=True)


# ---------------------------------------------------------------------------
# Audio: vozes mais suaves (triangulo + pulso), envelope ADSR, low-pass leve.
# ---------------------------------------------------------------------------

def _tri(freq, t):
    if freq <= 0:
        return 0.0
    p = (t * freq) % 1.0
    return 4.0 * abs(p - 0.5) - 1.0


def _pulse(freq, t, duty=0.5):
    if freq <= 0:
        return 0.0
    return 1.0 if (t * freq) % 1.0 < duty else -1.0


def _voice(freq, t, duty=0.5, tri_mix=0.6):
    return _tri(freq, t) * tri_mix + _pulse(freq, t, duty) * (1.0 - tri_mix)


def make_sound_from_notes(notes, step=0.16, volume=0.16):
    mixer_info = pygame.mixer.get_init()
    if not mixer_info:
        return None
    sample_rate, sample_format, channels = mixer_info
    if sample_format != -16:
        return None

    total_per_step = int(sample_rate * step)
    attack = max(140, int(sample_rate * 0.008))
    decay = int(sample_rate * 0.05)
    sustain = 0.6
    release = int(sample_rate * 0.045)

    buf = []
    for index, note in enumerate(notes):
        bass_note = 98 if index % 8 == 0 else 0  # batida grave suave so nos tempos fortes
        duty = 0.5 if index % 2 == 0 else 0.42
        for i in range(total_per_step):
            t = i / sample_rate
            if i < attack:
                env = i / attack
            elif i < attack + decay:
                env = 1.0 - (1.0 - sustain) * (i - attack) / decay
            else:
                env = sustain
            rel = total_per_step - i
            if rel < release:
                env *= rel / release
            value = _voice(note, t, duty, 0.6) * 0.82
            if bass_note:
                value += _tri(bass_note, t) * 0.22
            buf.append(value * env)

    n = len(buf)
    samples = array("h")
    for i in range(n):
        prev = buf[i - 1] if i > 0 else buf[i]
        nxt = buf[i + 1] if i < n - 1 else buf[i]
        s = 0.25 * prev + 0.5 * buf[i] + 0.25 * nxt
        if s > 1.0:
            s = 1.0
        elif s < -1.0:
            s = -1.0
        sample = int(s * 32767 * volume)
        for _ in range(channels):
            samples.append(sample)
    return pygame.mixer.Sound(buffer=samples.tobytes())


def make_tone(freq, duration=0.08, volume=0.2, slide=0, tri_mix=0.6):
    mixer_info = pygame.mixer.get_init()
    if not mixer_info:
        return None
    sample_rate, sample_format, channels = mixer_info
    if sample_format != -16:
        return None

    samples = array("h")
    total = int(sample_rate * duration)
    for i in range(total):
        t = i / sample_rate
        current = freq + slide * (i / max(1, total))
        fade = min(1, i / max(1, int(sample_rate * 0.006)))
        fade *= min(1, (total - i) / max(1, int(sample_rate * 0.02)))
        fade *= math.exp(-3.0 * i / total)
        value = int(_voice(current, t, 0.5, tri_mix) * 32767 * volume * fade)
        for _ in range(channels):
            samples.append(value)
    return pygame.mixer.Sound(buffer=samples.tobytes())


def setup_audio():
    if not pygame.mixer.get_init():
        return None, {}
    # 64 passos em la-menor pentatonica (A C D E G): A/A'/B/A-retorno, com pausas
    music_notes = [
    220, 0, 220, 247, 262, 330, 294, 262,
    220, 0, 330, 370, 440, 370, 330, 294,

    247, 0, 247, 262, 294, 370, 330, 294,
    247, 0, 370, 392, 494, 440, 392, 330,

    262, 0, 262, 294, 330, 392, 370, 330,
    262, 0, 392, 440, 523, 494, 440, 392,

    330, 0, 370, 440, 392, 330, 294, 262,
    220, 0, 220, 247, 262, 330, 294, 220,
    ]
    sounds = {
        "jump": make_tone(520, 0.09, 0.16, 150, tri_mix=0.55),
        "coin": make_tone(1046, 0.07, 0.14, 120, tri_mix=0.8),
        "hit": make_tone(150, 0.16, 0.22, -70, tri_mix=0.3),
        "star": make_tone(1320, 0.13, 0.18, 240, tri_mix=0.8),
        "bottle": make_tone(900, 0.18, 0.18, 150, tri_mix=0.7),
        "level": make_tone(880, 0.20, 0.18, 320, tri_mix=0.75),
    }
    return make_sound_from_notes(music_notes, 0.16, 0.16), sounds


def play_sfx(sounds, name):
    sound = sounds.get(name)
    if sound:
        sound.play()


class World:
    def __init__(self):
        self.coins = []
        self.obstacles = []
        self.mushrooms = []
        self.stars = []
        self.chests = []
        self.next_segment = 0
        self.last_obstacle_x = -999.0
        self.last_chest_segment = -999
        self.generate_until(GENERATE_AHEAD)

    def generate_until(self, target_x):
        while self.next_segment * SEGMENT_WIDTH < target_x:
            self._generate_segment(self.next_segment)
            self.next_segment += 1

    def _generate_segment(self, segment):
        base = segment * SEGMENT_WIDTH
        rng = random.Random(segment * 9173 + 41)
        seg_speed = speed_at(base)
        level = level_at_meters(base / 10.0)

        # min_gap = "frames de reacao" * velocidade; frames caem com o nivel (fica mais dificil)
        reaction = max(24, 52 - level * 3)
        min_gap = int(seg_speed * reaction)
        if segment == 0:
            min_gap = max(min_gap, 150)

        for index, offset in enumerate([70, 125, 185, 245]):
            x = base + offset + rng.randint(-8, 8)
            arc = 88 if (segment + index) % 3 else 76
            y = arc + int(math.sin((segment + index) * 1.7) * 7)
            self.coins.append(Coin(x, y))

        if segment == 0:
            slots = [base + 235]
        else:
            slots = [base + 70, base + 200]
            if level >= 2:
                slots.append(base + 135)
            if level >= 4:
                slots.append(base + 285)
        for slot in sorted(slots):
            self._add_obstacle(slot + rng.randint(-6, 6), segment, level, seg_speed, rng, min_gap)

        if rng.random() < max(0.20, 0.42 - level * 0.03):
            y = MUSHROOM_GROUND_Y if rng.random() < 0.5 else MUSHROOM_JUMP_Y
            self.mushrooms.append(MushroomBoost(base + 55 + rng.randint(-8, 8), y))

        if rng.random() < 0.38:
            self.stars.append(StarPickup(base + 145 + rng.randint(-10, 10), 74))

        # bau: raro, anti-agrupado, fica mais raro com a distancia, com periodo de gracia inicial
        chest_chance = max(0.05, 0.16 - level * 0.012)
        if segment >= 4 and segment - self.last_chest_segment >= 6 and rng.random() < chest_chance:
            self.chests.append(ChestPickup(base + 178 + rng.randint(-8, 8)))
            self.last_chest_segment = segment

    def _add_obstacle(self, x, segment, level, seg_speed, rng, min_gap):
        # rola SEMPRE os dados (consumo de rng constante mesmo se o slot for descartado)
        type_roll = rng.random()
        cluster_roll = rng.random()
        tall_roll = rng.random()
        bird_roll = rng.random()
        if x - self.last_obstacle_x < min_gap:
            return

        base_m = (segment * SEGMENT_WIDTH) / 10.0
        if base_m >= BIRD_UNLOCK_M and bird_roll < 0.22:
            self.obstacles.append(Bird(x))
            self.last_obstacle_x = x
            return

        cluster = 1
        if level >= 2 and cluster_roll < 0.30:
            cluster = 2
        if level >= 5 and cluster_roll < 0.12:
            cluster = 3
        if cluster > 1:
            inner = 18
            for i in range(cluster):
                self.obstacles.append(Rock(x + i * inner))
            self.last_obstacle_x = x + (cluster - 1) * inner
            return

        if segment > 5 and type_roll < 0.32:
            self.obstacles.append(LogObstacle(x))
        else:
            tall = level >= 1 and tall_roll < (0.40 if level >= 4 else 0.26)
            self.obstacles.append(Rock(x, tall=tall))
        self.last_obstacle_x = x

    def cleanup(self, camera):
        cutoff = camera - CLEANUP_BEHIND
        self.coins = [item for item in self.coins if item.x > cutoff and not item.got]
        self.mushrooms = [item for item in self.mushrooms if item.x > cutoff and not item.got]
        self.stars = [item for item in self.stars if item.x > cutoff and not item.got]
        self.chests = [item for item in self.chests if item.x > cutoff]
        self.obstacles = [item for item in self.obstacles if item.x > cutoff]

    def draw(self, camera, frame):
        for c in self.coins:
            c.draw(camera, frame)
        for s in self.stars:
            s.draw(camera, frame)
        for m in self.mushrooms:
            m.draw(camera)
        for ch in self.chests:
            ch.draw(camera, frame)
        for obstacle in self.obstacles:
            obstacle.draw(camera, frame)


def draw_world_decor(camera):
    labels = [("TRAIL", YELLOW), ("AVENTURA", WHITE), ("DIVERSAO", CYAN), ("FAMILIA", PINK)]
    first_marker = int(camera // 520) * 520
    for marker in range(first_marker, first_marker + 1560, 520):
        label, color = labels[(marker // 520) % len(labels)]
        y = 119 if (marker // 520) % 2 == 0 else 115
        world_sign(label, int(marker + 165 - camera), y, color)

    first_family = int(camera // 1800) * 1800
    for fx in range(first_family + 1420, first_family + 3600, 1800):
        sx = int(fx - camera)
        if -80 < sx < VW + 80:
            draw_rafael_amanda(sx, 124)


def add_popup(popups, msg, x, y, color):
    popups.append({"msg": msg, "x": x, "y": y, "color": color, "ttl": 50})


def draw_popups(popups, camera):
    for popup in popups[:]:
        lift = int((50 - popup["ttl"]) * 0.4)
        text(popup["msg"], int(popup["x"] - camera), int(popup["y"] - lift), popup["color"], center=True)
        popup["ttl"] -= 1
        if popup["ttl"] <= 0:
            popups.remove(popup)


def spawn_dust(particles, x, count=5):
    for _ in range(count):
        particles.append({
            "x": x + random.uniform(4, 18),
            "y": GROUND_Y - 1,
            "vx": random.uniform(-1.1, 0.2),
            "vy": random.uniform(-1.4, -0.3),
            "ttl": 16,
            "color": DIRT if random.random() < 0.5 else DIRT_DARK,
        })
    del particles[:-60]


def update_and_draw_particles(particles, camera):
    for p in particles[:]:
        p["x"] += p["vx"]
        p["y"] += p["vy"]
        p["vy"] += 0.18
        p["ttl"] -= 1
        if p["ttl"] <= 0:
            particles.remove(p)
        else:
            box(p["color"], int(p["x"] - camera), int(p["y"]), 1, 1)


def load_best_distance():
    try:
        return max(0, int(BEST_FILE.read_text().strip()))
    except (OSError, ValueError):
        return 0


def save_best_distance(distance):
    try:
        BEST_FILE.write_text(str(max(0, int(distance))))
    except OSError:
        pass


async def main():
    max_frames = int(os.environ.get("TRAILQUEST_MAX_FRAMES", "0"))  # 0 = roda infinito (smoke test usa >0)
    player, world = Player(), World()
    lives, score, coins, stars_found, bottles_found, combo = START_LIVES, 0, 0, 0, 0, 0
    state = "title"
    frame = 0
    best_distance = load_best_distance()
    start_best = best_distance  # recorde a bater nesta corrida (best_distance sobe ao vivo)
    distance = 0
    prev_level = 0
    popups = []
    particles = []
    shake = 0
    hit_flash = 0
    music_sound, sounds = setup_audio()
    music_on = False
    music_channel = None
    if music_sound:
        music_channel = pygame.mixer.Channel(0)
        music_channel.set_volume(0.22)
        music_channel.play(music_sound, loops=-1)
        music_on = True

    def quit_game():
        save_best_distance(best_distance)
        if not IS_WEB:
            pygame.quit()
        return True

    while True:
        frame += 1
        if max_frames and frame > max_frames:
            return
        keys = pygame.key.get_pressed()

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                if quit_game():
                    return
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_ESCAPE:
                    if quit_game():
                        return
                if ev.key == pygame.K_m and music_channel:
                    music_on = not music_on
                    if music_on:
                        music_channel.unpause()
                    else:
                        music_channel.pause()
                if state == "title" and ev.key == pygame.K_SPACE:
                    state = "play"
                if state == "gameover" and ev.key == pygame.K_r:
                    player, world = Player(), World()
                    lives, score, coins, stars_found, bottles_found, combo = START_LIVES, 0, 0, 0, 0, 0
                    distance = 0
                    start_best = best_distance
                    prev_level = 0
                    popups = []
                    particles = []
                    shake = 0
                    hit_flash = 0
                    state = "play"

        if state == "play":
            jumped, landed = player.update(keys)
            if jumped:
                play_sfx(sounds, "jump")
                spawn_dust(particles, player.x, 3)
            if landed:
                spawn_dust(particles, player.x, 5)

        camera = 0 if state == "title" else max(0, player.x - (74 + int(min(player.base_speed - BASE_SPEED, 1.6) * 12)))

        if state == "play":
            world.generate_until(player.x + GENERATE_AHEAD)
            world.cleanup(camera)
            distance = max(distance, int(player.x // 10))
            best_distance = max(best_distance, distance)

            level = level_at_meters(distance)
            if level > prev_level:
                prev_level = level
                add_popup(popups, "LEVEL UP!", player.x + 60, 64, YELLOW)
                play_sfx(sounds, "level")

            phit = player.hitbox.move(-camera, 0)
            for c in world.coins:
                if not c.got and phit.colliderect(c.rect(camera)):
                    c.got = True
                    coins += 1
                    score += 1
                    play_sfx(sounds, "coin")
            for s in world.stars:
                if not s.got and phit.colliderect(s.rect(camera)):
                    s.got = True
                    stars_found += 1
                    score += 5
                    add_popup(popups, "+5", s.x + 4, s.y - 8, YELLOW)
                    play_sfx(sounds, "star")
            for mushroom_boost in world.mushrooms:
                if not mushroom_boost.got and phit.colliderect(mushroom_boost.rect(camera)):
                    mushroom_boost.got = True
                    player.boost_timer = BOOST_FRAMES
                    score += 2
            for ch in world.chests:
                if not ch.opened and phit.colliderect(ch.rect(camera)):
                    ch.opened = True
                    ch.effect_timer = 70
                    bottles_found += 1
                    score += 3
                    if lives < MAX_LIVES:
                        lives += 1
                        add_popup(popups, "+1 VIDA", ch.x + 10, ch.y - 12, PINK)
                    else:
                        score += 2
                        add_popup(popups, "VIDA MAX", ch.x + 10, ch.y - 12, YELLOW)
                    play_sfx(sounds, "bottle")

            for obstacle in world.obstacles:
                if player.invuln == 0 and phit.colliderect(obstacle.rect(camera)):
                    lives -= 1
                    combo = 0
                    obstacle.scored = True
                    play_sfx(sounds, "hit")
                    player.invuln = 90 if distance < 100 else 75
                    player.boost_timer = 0
                    player.knock_vx = -6.0
                    shake = 13
                    hit_flash = 3
                    if lives <= 0:
                        state = "gameover"
                        save_best_distance(best_distance)
                    break

            # combo: obstaculos ultrapassados sem colidir valem pontos crescentes
            for obstacle in world.obstacles:
                if not obstacle.scored and obstacle.x + obstacle.w < player.x:
                    obstacle.scored = True
                    combo += 1
                    score += combo

        render_camera = camera
        bg(render_camera)
        draw_world_decor(render_camera)
        world.draw(render_camera, frame)
        update_and_draw_particles(particles, render_camera)
        draw_popups(popups, render_camera)

        if not (player.invuln > 0 and frame % 6 < 3):
            squash = 2 if player.land_timer > 3 else 0
            draw_joao_pedro(int(player.x - render_camera), int(player.y), frame, player.ducking, squash)

        if hit_flash > 0:  # flash de dano: borda vermelha por alguns frames
            box(RED, 0, 0, VW, 2)
            box(RED, 0, VH - 2, VW, 2)
            box(RED, 0, 0, 2, VH)
            box(RED, VW - 2, 0, 2, VH)
            hit_flash -= 1

        hud(score, coins, lives, distance, stars_found, bottles_found,
            best_distance, music_on, player.speed, combo)

        if state == "title":
            overlay_title()
        elif state == "gameover":
            overlay_end(score, stars_found, bottles_found, distance, best_distance, distance > start_best)

        scaled = pygame.transform.scale(canvas, DISPLAY_SIZE)
        if shake > 0:
            amp = min(14, shake)
            ox = random.randint(-amp, amp)
            oy = random.randint(-amp, amp)
            screen.fill(BLACK)
            screen.blit(scaled, (ox, oy))
            shake -= 1
        else:
            screen.blit(scaled, (0, 0))
        pygame.display.flip()
        clock.tick(60)
        await asyncio.sleep(0)


if __name__ == "__main__":
    asyncio.run(main())
