const VW = 320;
const VH = 180;
const BASE_SPEED = 2.4;
const SPEED_RAMP = 320;
const MAX_SPEED_GAIN = 2.2;
const BOOST_BONUS = 0.7;
const BOOST_FRAMES = 150;
const TOUCH_JUMP_FRAMES = 10;
const JUMP_FORCE = -5.75;
const JUMP_CUT_VY = -2.4;
const APEX_BAND = 1.2;
const APEX_GRAVITY = 0.62;
const GRAVITY = 0.32;
const COYOTE_FRAMES = 6;
const JUMP_BUFFER_FRAMES = 6;
const MAX_LIVES = 5;
const START_LIVES = 3;
const SEGMENT_WIDTH = 320;
const GENERATE_AHEAD = 1100;
const CLEANUP_BEHIND = 260;
const GROUND_Y = 124;
const MUSHROOM_GROUND_Y = 111;
const MUSHROOM_JUMP_Y = 76;
const BIRD_UNLOCK_M = 140;
const BIRD_Y = 92;
const LEVEL_METERS = 250;
const BEST_KEY = "joao-pedro-trail-quest-recorde";

const SKY = "rgb(89,191,255)";
const SKY_DARK = "rgb(52,145,220)";
const CLOUD = "rgb(245,248,231)";
const MOUNTAIN = "rgb(102,130,150)";
const MOUNTAIN_DARK = "rgb(75,100,122)";
const TREE = "rgb(25,117,61)";
const TREE_DARK = "rgb(16,78,48)";
const DIRT = "rgb(154,96,45)";
const DIRT_DARK = "rgb(107,62,32)";
const GRASS = "rgb(61,156,67)";
const GRASS_DARK = "rgb(36,105,45)";
const BLACK = "rgb(17,18,24)";
const WHITE = "rgb(245,245,235)";
const YELLOW = "rgb(255,208,45)";
const GOLD = "rgb(224,152,30)";
const RED = "rgb(230,56,54)";
const BLUE = "rgb(46,164,235)";
const PINK = "rgb(224,78,133)";
const SKIN = "rgb(224,152,98)";
const BROWN = "rgb(84,54,32)";
const WOOD = "rgb(110,66,34)";
const WOOD_LIGHT = "rgb(174,105,47)";
const ORANGE = "rgb(238,129,36)";
const GREEN_LIGHT = "rgb(118,205,85)";
const CYAN = "rgb(67,205,238)";
const ROCK = "rgb(90,83,78)";
const ROCK_LIGHT = "rgb(140,130,118)";
const BIRD_BODY = "rgb(96,96,110)";
const BIRD_WING = "rgb(60,60,78)";
const SUN = "rgb(255,228,94)";
const SUN_EDGE = "rgb(248,177,58)";
const HILL = "rgb(68,145,91)";
const HILL_DARK = "rgb(46,111,75)";
const FLOWER = "rgb(255,105,152)";
const PANEL = "rgb(42,47,55)";

const PIXEL_FONT = {
  A: ["01110", "10001", "10001", "11111", "10001", "10001", "10001"],
  B: ["11110", "10001", "10001", "11110", "10001", "10001", "11110"],
  C: ["01111", "10000", "10000", "10000", "10000", "10000", "01111"],
  D: ["11110", "10001", "10001", "10001", "10001", "10001", "11110"],
  E: ["11111", "10000", "10000", "11110", "10000", "10000", "11111"],
  F: ["11111", "10000", "10000", "11110", "10000", "10000", "10000"],
  G: ["01111", "10000", "10000", "10111", "10001", "10001", "01111"],
  H: ["10001", "10001", "10001", "11111", "10001", "10001", "10001"],
  I: ["111", "010", "010", "010", "010", "010", "111"],
  J: ["00111", "00010", "00010", "00010", "10010", "10010", "01100"],
  K: ["10001", "10010", "10100", "11000", "10100", "10010", "10001"],
  L: ["10000", "10000", "10000", "10000", "10000", "10000", "11111"],
  M: ["10001", "11011", "10101", "10101", "10001", "10001", "10001"],
  N: ["10001", "11001", "10101", "10011", "10001", "10001", "10001"],
  O: ["01110", "10001", "10001", "10001", "10001", "10001", "01110"],
  P: ["11110", "10001", "10001", "11110", "10000", "10000", "10000"],
  Q: ["01110", "10001", "10001", "10001", "10101", "10010", "01101"],
  R: ["11110", "10001", "10001", "11110", "10100", "10010", "10001"],
  S: ["01111", "10000", "10000", "01110", "00001", "00001", "11110"],
  T: ["11111", "00100", "00100", "00100", "00100", "00100", "00100"],
  U: ["10001", "10001", "10001", "10001", "10001", "10001", "01110"],
  V: ["10001", "10001", "10001", "10001", "10001", "01010", "00100"],
  W: ["10001", "10001", "10001", "10101", "10101", "10101", "01010"],
  X: ["10001", "10001", "01010", "00100", "01010", "10001", "10001"],
  Y: ["10001", "10001", "01010", "00100", "00100", "00100", "00100"],
  Z: ["11111", "00001", "00010", "00100", "01000", "10000", "11111"],
  0: ["01110", "10001", "10011", "10101", "11001", "10001", "01110"],
  1: ["010", "110", "010", "010", "010", "010", "111"],
  2: ["01110", "10001", "00001", "00010", "00100", "01000", "11111"],
  3: ["11110", "00001", "00001", "01110", "00001", "00001", "11110"],
  4: ["10010", "10010", "10010", "11111", "00010", "00010", "00010"],
  5: ["11111", "10000", "10000", "11110", "00001", "00001", "11110"],
  6: ["01110", "10000", "10000", "11110", "10001", "10001", "01110"],
  7: ["11111", "00001", "00010", "00100", "01000", "01000", "01000"],
  8: ["01110", "10001", "10001", "01110", "10001", "10001", "01110"],
  9: ["01110", "10001", "10001", "01111", "00001", "00001", "01110"],
  ".": ["0", "0", "0", "0", "0", "0", "1"],
  ",": ["0", "0", "0", "0", "0", "1", "1"],
  ":": ["0", "1", "1", "0", "1", "1", "0"],
  ";": ["0", "1", "1", "0", "1", "1", "1"],
  "!": ["1", "1", "1", "1", "1", "0", "1"],
  "?": ["01110", "10001", "00001", "00010", "00100", "00000", "00100"],
  "+": ["000", "010", "010", "111", "010", "010", "000"],
  "-": ["000", "000", "000", "111", "000", "000", "000"],
  "/": ["00001", "00010", "00010", "00100", "01000", "01000", "10000"],
  "|": ["1", "1", "1", "1", "1", "1", "1"],
  "@": ["01110", "10001", "10111", "10101", "10111", "10000", "01110"],
  "(": ["01", "10", "10", "10", "10", "10", "01"],
  ")": ["10", "01", "01", "01", "01", "01", "10"],
};

const canvas = document.getElementById("game");
const ctx = canvas.getContext("2d", { alpha: false });
const duckBtn = document.getElementById("duck");
const jumpBtn = document.getElementById("jump");

function trunc(value) {
  return Math.trunc(value);
}

function pymod(value, divisor) {
  return ((value % divisor) + divisor) % divisor;
}

function speedAt(x) {
  return BASE_SPEED + Math.min(x / 10 / SPEED_RAMP, MAX_SPEED_GAIN);
}

function levelAtMeters(distance) {
  return Math.floor(distance / LEVEL_METERS);
}

function makeRng(seed) {
  let state = seed >>> 0;
  return {
    random() {
      state = (Math.imul(state, 1664525) + 1013904223) >>> 0;
      return state / 4294967296;
    },
    randint(min, max) {
      return min + Math.floor(this.random() * (max - min + 1));
    },
  };
}

function randint(min, max) {
  return min + Math.floor(Math.random() * (max - min + 1));
}

function rect(x, y, w, h) {
  return { x: trunc(x), y: trunc(y), w: trunc(w), h: trunc(h) };
}

function overlaps(a, b) {
  return a.x < b.x + b.w && a.x + a.w > b.x && a.y < b.y + b.h && a.y + a.h > b.y;
}

function box(color, x, y, w, h) {
  ctx.fillStyle = color;
  ctx.fillRect(trunc(x), trunc(y), Math.max(1, trunc(w)), Math.max(1, trunc(h)));
}

function polygon(color, points) {
  ctx.fillStyle = color;
  ctx.beginPath();
  ctx.moveTo(trunc(points[0][0]), trunc(points[0][1]));
  for (let i = 1; i < points.length; i += 1) {
    ctx.lineTo(trunc(points[i][0]), trunc(points[i][1]));
  }
  ctx.closePath();
  ctx.fill();
}

function strokePath(color, points, width, closed) {
  ctx.save();
  ctx.translate(0.5, 0.5);
  ctx.strokeStyle = color;
  ctx.lineWidth = Math.max(1, trunc(width));
  ctx.lineCap = "square";
  ctx.lineJoin = "miter";
  ctx.beginPath();
  ctx.moveTo(trunc(points[0][0]), trunc(points[0][1]));
  for (let i = 1; i < points.length; i += 1) {
    ctx.lineTo(trunc(points[i][0]), trunc(points[i][1]));
  }
  if (closed) ctx.closePath();
  ctx.stroke();
  ctx.restore();
}

function line(color, x1, y1, x2, y2, width = 1) {
  strokePath(color, [[x1, y1], [x2, y2]], width, false);
}

function lines(color, closed, points, width = 1) {
  strokePath(color, points, width, closed);
}

function circle(color, center, radius, width = 0) {
  const r = Math.max(1, trunc(radius));
  ctx.beginPath();
  ctx.arc(trunc(center[0]), trunc(center[1]), r, 0, Math.PI * 2);
  ctx.fillStyle = color;
  ctx.strokeStyle = color;
  if (width) {
    ctx.lineWidth = Math.max(1, trunc(width));
    ctx.stroke();
  } else {
    ctx.fill();
  }
}

function bitmapTextWidth(msg, block) {
  let width = 0;
  for (const ch of msg.toUpperCase()) {
    if (ch === " ") width += 3 * block;
    else width += ((PIXEL_FONT[ch] || PIXEL_FONT["?"])[0].length + 1) * block;
  }
  return Math.max(0, width - block);
}

function drawBitmapText(msg, x, y, color, block) {
  let cursor = x;
  for (const ch of msg.toUpperCase()) {
    if (ch === " ") {
      cursor += 3 * block;
      continue;
    }
    const glyph = PIXEL_FONT[ch] || PIXEL_FONT["?"];
    glyph.forEach((row, gy) => {
      for (let gx = 0; gx < row.length; gx += 1) {
        if (row[gx] === "1") box(color, cursor + gx * block, y + gy * block, block, block);
      }
    });
    cursor += (glyph[0].length + 1) * block;
  }
}

function text(msg, x, y, color = WHITE, size = "small", center = false) {
  const block = size === "small" ? 1 : 2;
  let drawX = x;
  if (center) drawX -= Math.floor(bitmapTextWidth(msg, block) / 2);
  drawBitmapText(msg, drawX + 1, y + 1, BLACK, block);
  drawBitmapText(msg, drawX, y, color, block);
}

function heart(x, y) {
  ["0110110", "1111111", "1111111", "0111110", "0011100", "0001000"].forEach((row, py) => {
    for (let px = 0; px < row.length; px += 1) {
      if (row[px] === "1") box(RED, x + px, y + py, 1, 1);
    }
  });
}

function drawCoin(x, y, frame) {
  const wobble = trunc(Math.sin(frame / 6));
  box(GOLD, x + 1 + wobble, y, 6 - Math.abs(wobble), 8);
  box(YELLOW, x + 2 + wobble, y + 1, 3, 6);
  box(WHITE, x + 3 + wobble, y + 2, 1, 2);
}

function starIcon(x, y, frame = 0, color = YELLOW) {
  const shimmer = frame % 30 < 6 ? WHITE : color;
  ["00100", "10101", "01110", "11111", "01010", "10001"].forEach((row, py) => {
    for (let px = 0; px < row.length; px += 1) {
      if (row[px] === "1") box(py === 0 ? shimmer : color, x + px, y + py, 1, 1);
    }
  });
}

function woodPanel(x, y, w, h) {
  box(BLACK, x - 2, y - 2, w + 4, h + 4);
  box(WOOD, x, y, w, h);
  box(WOOD_LIGHT, x + 2, y + 2, w - 4, 2);
  for (let px = x + 6; px < x + w - 4; px += 18) box(DIRT_DARK, px, y + 2, 2, h - 4);
}

function drawChest(x, y, opened) {
  box(BLACK, x - 1, y - 1, 21, 16);
  if (opened) {
    box(WOOD_LIGHT, x + 1, y - 7, 17, 7);
    box(WOOD, x, y + 3, 19, 11);
    box(YELLOW, x + 7, y - 1, 5, 5);
  } else {
    box(WOOD_LIGHT, x, y, 19, 6);
    box(WOOD, x, y + 6, 19, 8);
    box(YELLOW, x + 8, y + 4, 4, 5);
  }
  box(GOLD, x, y + 6, 19, 2);
}

function drawMushroom(x, y) {
  box(WHITE, x + 5, y + 6, 5, 7);
  polygon(RED, [[x, y + 8], [x + 4, y], [x + 12, y], [x + 16, y + 8]]);
  box(WHITE, x + 4, y + 4, 2, 2);
  box(WHITE, x + 10, y + 3, 2, 2);
  box(BLACK, x + 4, y + 13, 8, 1);
}

function drawBottle(x, y, frame) {
  const shine = frame % 18 < 9 ? WHITE : CYAN;
  box(BLACK, x - 1, y - 1, 9, 17);
  box(WHITE, x + 2, y, 4, 3);
  box(CYAN, x + 1, y + 3, 6, 10);
  box(WHITE, x + 2, y + 5, 4, 3);
  box(shine, x + 5, y + 5, 1, 5);
  box(YELLOW, x + 2, y + 13, 4, 2);
}

function drawRock(x, y, w, h) {
  polygon(ROCK, [[x, y + h - 1], [x + 3, y + 2], [x + w - 5, y], [x + w - 1, y + h - 1]]);
  polygon(ROCK_LIGHT, [[x + 3, y + 3], [x + 9, y + 1], [x + 7, y + 6]]);
}

function drawBirdSprite(x, y, frame) {
  const flapUp = frame % 16 < 8;
  box(BIRD_BODY, x + 4, y + 2, 9, 6);
  box(WHITE, x + 5, y + 3, 4, 2);
  box(YELLOW, x + 12, y + 3, 3, 2);
  box(BLACK, x + 11, y + 2, 1, 1);
  if (flapUp) polygon(BIRD_WING, [[x + 5, y + 3], [x + 1, y - 3], [x + 9, y + 3]]);
  else polygon(BIRD_WING, [[x + 5, y + 5], [x + 1, y + 11], [x + 9, y + 5]]);
}

function drawSun(camera) {
  let sunX = 248 - pymod(trunc(camera * 0.025), 420);
  if (sunX < -32) sunX += 420;
  circle(SUN_EDGE, [sunX, 32], 14);
  circle(SUN, [sunX, 32], 11);
  [[-20, 0], [20, 0], [0, -20], [0, 20]].forEach(([dx, dy]) => {
    box(SUN, sunX + dx, 31 + dy, dx ? 5 : 2, dx ? 2 : 5);
  });
}

function drawBackgroundHills(camera) {
  for (let i = -1; i < 6; i += 1) {
    const x = i * 86 - pymod(trunc(camera * 0.2), 86);
    polygon(HILL_DARK, [[x, 122], [x + 42, 82], [x + 88, 122]]);
    polygon(HILL, [[x + 16, 122], [x + 58, 92], [x + 104, 122]]);
  }
}

function drawMidgroundDetails(camera) {
  for (let i = -1; i < 8; i += 1) {
    const x = i * 72 - pymod(trunc(camera * 0.46), 72);
    box(BROWN, x + 10, 116, 4, 14);
    box(WOOD_LIGHT, x + 8, 116, 8, 2);
    box(BROWN, x + 38, 116, 4, 14);
    box(WOOD_LIGHT, x + 36, 116, 8, 2);
    line(WOOD, x + 12, 120, x + 40, 120, 1);
  }
  for (let i = -1; i < 10; i += 1) {
    const x = i * 45 - pymod(trunc(camera * 0.55), 45);
    const y = 133 + pymod(i, 3) * 4;
    box(HILL_DARK, x + 2, y + 3, 14, 3);
    box(HILL, x + 5, y, 9, 5);
  }
}

function drawGroundDetails(camera) {
  for (let i = -1; i < 34; i += 1) {
    const x = i * 18 - pymod(trunc(camera * 0.92), 18);
    const kind = pymod(i, 4);
    if (kind === 0) {
      box(FLOWER, x + 6, 139, 2, 2);
      box(YELLOW, x + 7, 138, 1, 1);
    } else if (kind === 1) {
      box(ROCK_LIGHT, x + 5, 142, 3, 2);
    } else {
      box(GRASS_DARK, x + 3, 136 + pymod(i, 2) * 5, 5, 1);
    }
  }
}

function worldSign(label, x, y, color = YELLOW) {
  if (x < -58 || x > VW + 24) return;
  box(BROWN, x + 22, y - 3, 5, 29);
  woodPanel(x, y - 18, 52, 16);
  text(label, x + 26, y - 14, color, "small", true);
}

function drawBackground(camera) {
  ctx.fillStyle = SKY;
  ctx.fillRect(0, 0, VW, VH);
  box(SKY_DARK, 0, 0, VW, 18);
  drawSun(camera);
  [[35, 32], [82, 22], [210, 30], [272, 22]].forEach(([cx, cy]) => {
    const ox = trunc(pymod(-(camera * 0.06), 120));
    const x = pymod(cx + ox, VW + 50) - 25;
    box(CLOUD, x, cy, 18, 5);
    box(CLOUD, x + 6, cy - 4, 10, 5);
  });
  for (let i = -1; i < 5; i += 1) {
    const mx = i * 90 - pymod(trunc(camera * 0.12), 90);
    polygon(MOUNTAIN_DARK, [[mx, 115], [mx + 45, 45], [mx + 90, 115]]);
    polygon(MOUNTAIN, [[mx + 16, 90], [mx + 45, 45], [mx + 72, 90]]);
    polygon(CLOUD, [[mx + 39, 55], [mx + 45, 45], [mx + 51, 55]]);
  }
  drawBackgroundHills(camera);
  for (let i = -1; i < 8; i += 1) {
    const tx = i * 55 - pymod(trunc(camera * 0.3), 55);
    const ty = 105 + pymod(i, 2) * 10;
    box(BROWN, tx + 15, ty + 8, 5, 28);
    polygon(TREE_DARK, [[tx + 17, ty - 20], [tx, ty + 18], [tx + 34, ty + 18]]);
    polygon(TREE, [[tx + 17, ty - 10], [tx + 3, ty + 25], [tx + 31, ty + 25]]);
  }
  box(GRASS, 0, 122, VW, VH - 122);
  for (let i = 0; i < VW; i += 8) box(GRASS_DARK, i, 126 + pymod(i, 3) * 5, 4, 2);
  drawMidgroundDetails(camera);
  drawGroundDetails(camera);
  const path = [];
  for (let px = 0; px < VW + 20; px += 8) {
    path.push([px, 150 + Math.sin((px + camera * 0.3) / 23) * 7]);
  }
  lines(DIRT_DARK, false, path, 24);
  lines(DIRT, false, path, 18);
}

function drawJoaoPedro(x, y, frame, ducking, squash) {
  circle(BLACK, [x + 5, y - 5], 5, 1);
  circle(BLACK, [x + 19, y - 5], 5, 1);
  const spoke = pymod(frame, 12);
  line(BLACK, x + 5, y - 10, x + 5, y, 1);
  line(BLACK, x + 19, y - 10, x + 19, y, 1);
  line(BLACK, x + 1 + Math.floor(spoke / 3), y - 5, x + 9 - Math.floor(spoke / 3), y - 5, 1);
  line(BLACK, x + 15 + Math.floor(spoke / 3), y - 5, x + 23 - Math.floor(spoke / 3), y - 5, 1);
  line(CYAN, x + 5, y - 5, x + 11, y - 12, 2);
  line(BLUE, x + 19, y - 5, x + 11, y - 12, 2);
  line(CYAN, x + 8, y - 13, x + 16, y - 13, 2);
  line(BLUE, x + 16, y - 13, x + 20, y - 16, 1);
  line(BLUE, x + 8, y - 13, x + 9, y - 17, 1);
  box(BLACK, x + 8, y - 18, 4, 2);
  line(BLACK, x + 20, y - 16, x + 23, y - 17, 1);
  if (ducking) {
    box(SKIN, x + 8, y - 16, 8, 6);
    box(BROWN, x + 9, y - 17, 6, 2);
    box(WHITE, x + 6, y - 13, 12, 7);
    box(YELLOW, x + 11, y - 11, 3, 3);
    box(SKIN, x + 16, y - 12, 3, 2);
    box(BLACK, x + 10, y - 14, 1, 1);
    box(BLACK, x + 13, y - 14, 1, 1);
    box(RED, x + 11, y - 12, 2, 1);
    box(BLUE, x + 7, y - 7, 4, 2);
    box(BLUE, x + 14, y - 7, 4, 2);
    return;
  }
  const top = y - 31 + squash;
  box(SKIN, x + 8, top, 8, 8);
  box(BROWN, x + 9, top - 2, 6, 2);
  box(WHITE, x + 7, top + 7, 10, 10 - squash);
  box(YELLOW, x + 10, top + 10, 3, 3);
  box(SKIN, x + 5, top + 9, 2, 6);
  box(SKIN, x + 17, top + 9, 2, 6);
  if (pymod(frame, 12) < 6) {
    line(SKIN, x + 10, y - 14, x + 8, y - 8, 2);
    line(SKIN, x + 14, y - 14, x + 17, y - 8, 2);
  } else {
    line(SKIN, x + 10, y - 14, x + 13, y - 8, 2);
    line(SKIN, x + 14, y - 14, x + 10, y - 8, 2);
  }
  box(BLUE, x + 7, y - 8, 4, 2);
  box(BLUE, x + 15, y - 8, 4, 2);
  box(BLACK, x + 10, top + 3, 1, 1);
  box(BLACK, x + 13, top + 3, 1, 1);
  box(RED, x + 11, top + 6, 2, 1);
}

function drawRafaelAmanda(x, y) {
  box(BLACK, x + 4, y - 34, 12, 20);
  box(SKIN, x + 6, y - 46, 9, 9);
  box(BROWN, x + 5, y - 48, 11, 3);
  box(BLACK, x + 8, y - 42, 1, 1);
  box(BLACK, x + 12, y - 42, 1, 1);
  box(WHITE, x + 9, y - 39, 3, 1);
  box(WHITE, x + 8, y - 28, 4, 2);
  text("Rafael", x + 2, y - 58, BLUE);
  box(PINK, x + 22, y - 34, 12, 20);
  box(SKIN, x + 24, y - 46, 9, 9);
  box(BROWN, x + 23, y - 48, 11, 4);
  box(BROWN, x + 31, y - 43, 3, 12);
  box(BLACK, x + 26, y - 42, 1, 1);
  box(BLACK, x + 30, y - 42, 1, 1);
  box(WHITE, x + 27, y - 39, 3, 1);
  heart(x + 26, y - 28);
  text("Amanda", x + 18, y - 58, PINK);
}

function drawHud(game) {
  for (let i = 0; i < game.lives; i += 1) heart(8 + i * 11, 8);
  drawCoin(8, 23, 0);
  text(`x ${game.coins}`, 21, 23);
  starIcon(9, 39);
  text(`x ${game.starsFound}`, 21, 37);
  drawBottle(8, 52, 0);
  text(`x ${game.bottlesFound}`, 21, 55);
  const pct = Math.max(0, Math.min(1, (game.player.speed - BASE_SPEED) / (MAX_SPEED_GAIN + BOOST_BONUS)));
  box(BLACK, 72, 23, 42, 6);
  box(CYAN, 73, 24, trunc(40 * pct), 4);
  text(`${game.player.speed.toFixed(1)}x`, 72, 31, CYAN);
  text("PULO/AGACHA", 72, 43, WHITE);
  if (game.combo >= 3) text(`COMBO x${game.combo}`, 72, 55, ORANGE);
  text(`PTS ${game.score}`, VW / 2, 18, YELLOW, "small", true);
  text("JOAO PEDRO: TRAIL QUEST", VW / 2, 7, YELLOW, "small", true);
  box(BLACK, 218, 18, 98, 55);
  box(PANEL, 221, 21, 92, 49);
  text("TRILHA", 267, 24, WHITE, "small", true);
  box(SKY, 226, 37, 34, 20);
  polygon(TREE_DARK, [[227, 57], [239, 41], [251, 57]]);
  polygon(GREEN_LIGHT, [[236, 57], [251, 45], [260, 57]]);
  lines(DIRT, false, [[228, 57], [238, 51], [247, 51], [258, 45]], 3);
  text(`LVL ${1 + levelAtMeters(game.distance)}`, 265, 37, YELLOW);
  text(`${game.distance}m`, 265, 47, WHITE);
  box(BLACK, 265, 57, 44, 4);
  box(YELLOW, 266, 58, trunc(42 * (pymod(game.distance, LEVEL_METERS) / LEVEL_METERS)), 2);
  text(`REC ${game.bestDistance}m`, 222, 63, CYAN);
  text("M", 304, 63, game.musicOn ? YELLOW : RED);
}

function drawTitle() {
  box(BLACK, 23, 24, 274, 136);
  woodPanel(27, 28, 266, 128);
  text("JOAO PEDRO", VW / 2, 40, YELLOW, "big", true);
  text("TRAIL QUEST", VW / 2, 60, WHITE, "big", true);
  text("PULAR: TOQUE/ESPACO", VW / 2, 84, WHITE, "mid", true);
  text("AGACHAR: BAIXO/S", VW / 2, 104, CYAN, "mid", true);
  text("TOQUE PARA COMECAR", VW / 2, 124, YELLOW, "mid", true);
  text("M: MUSICA", VW / 2, 144, WHITE, "small", true);
  text("desenvolvido por @rafaelcotote", VW / 2, 166, CYAN, "small", true);
}

function drawEnd(game) {
  const beaten = game.distance > game.startBest;
  box(BLACK, 36, 32, 248, 124);
  woodPanel(40, 36, 240, 116);
  text(beaten ? "NOVO RECORDE!" : "FIM DA CORRIDA", VW / 2, 50, beaten ? GOLD : RED, "big", true);
  text(`DISTANCIA ${game.distance}M`, VW / 2, 78, YELLOW, "mid", true);
  text(`RECORDE ${game.bestDistance}M`, VW / 2, 98, CYAN, "mid", true);
  text(`PTS ${game.score}  ESTRELAS ${game.starsFound}`, VW / 2, 118, WHITE, "small", true);
  text(`MAMADEIRAS ${game.bottlesFound}`, VW / 2, 130, PINK, "small", true);
  text("TOQUE OU R: REINICIAR", VW / 2, 144, WHITE, "small", true);
}

function drawWorldDecor(camera) {
  const labels = [["TRAIL", YELLOW], ["AVENTURA", WHITE], ["DIVERSAO", CYAN], ["FAMILIA", PINK]];
  const firstMarker = Math.floor(camera / 520) * 520;
  for (let marker = firstMarker; marker < firstMarker + 1560; marker += 520) {
    const [label, color] = labels[Math.floor(marker / 520) % labels.length];
    const y = Math.floor(marker / 520) % 2 === 0 ? 119 : 115;
    worldSign(label, trunc(marker + 165 - camera), y, color);
  }
  const firstFamily = Math.floor(camera / 1800) * 1800;
  for (let fx = firstFamily + 1420; fx < firstFamily + 3600; fx += 1800) {
    const x = trunc(fx - camera);
    if (x > -80 && x < VW + 80) drawRafaelAmanda(x, 124);
  }
}

class Player {
  constructor() {
    this.x = 22;
    this.y = GROUND_Y;
    this.vy = 0;
    this.onGround = true;
    this.ducking = false;
    this.invuln = 0;
    this.baseSpeed = BASE_SPEED;
    this.speed = BASE_SPEED;
    this.boostTimer = 0;
    this.jumpHeldPrev = false;
    this.coyote = COYOTE_FRAMES;
    this.jumpBuffer = 0;
    this.landTimer = 0;
    this.knockVx = 0;
  }

  hitbox() {
    if (this.ducking) return rect(trunc(this.x) + 6, trunc(this.y) - 18, 18, 18);
    return rect(trunc(this.x) + 6, trunc(this.y) - 34, 18, 34);
  }

  update(jumpKey, duckKey) {
    let jumped = false;
    let landed = false;
    this.baseSpeed = speedAt(this.x);
    this.speed = this.baseSpeed + (this.boostTimer ? BOOST_BONUS : 0);
    this.x += this.speed + this.knockVx;
    if (this.knockVx) {
      this.knockVx *= 0.7;
      if (Math.abs(this.knockVx) < 0.4) this.knockVx = 0;
    }
    this.ducking = this.onGround && duckKey;
    if (this.onGround) this.coyote = COYOTE_FRAMES;
    else if (this.coyote) this.coyote -= 1;
    if (jumpKey && !this.jumpHeldPrev) this.jumpBuffer = JUMP_BUFFER_FRAMES;
    else if (this.jumpBuffer) this.jumpBuffer -= 1;
    if (this.jumpBuffer && (this.onGround || this.coyote)) {
      this.vy = JUMP_FORCE;
      this.onGround = false;
      this.ducking = false;
      this.jumpBuffer = 0;
      this.coyote = 0;
      jumped = true;
    }
    if (!jumpKey && this.vy < JUMP_CUT_VY) this.vy = JUMP_CUT_VY;
    const gravity = GRAVITY * (Math.abs(this.vy) < APEX_BAND ? APEX_GRAVITY : 1);
    this.vy += gravity;
    this.y += this.vy;
    if (this.y >= GROUND_Y) {
      if (!this.onGround) {
        landed = true;
        this.landTimer = 6;
      }
      this.y = GROUND_Y;
      this.vy = 0;
      this.onGround = true;
    }
    this.x = Math.max(8, this.x);
    if (this.invuln) this.invuln -= 1;
    if (this.boostTimer) this.boostTimer -= 1;
    if (this.landTimer) this.landTimer -= 1;
    this.jumpHeldPrev = jumpKey;
    return { jumped, landed };
  }
}

class Coin {
  constructor(x, y) {
    this.x = x;
    this.y = y;
    this.got = false;
  }
  bounds(camera) { return rect(this.x - camera, this.y, 8, 9); }
  draw(camera, frame) { if (!this.got) drawCoin(trunc(this.x - camera), trunc(this.y), frame); }
}

class RockObstacle {
  constructor(x, tall = false) {
    this.x = x;
    this.tall = tall;
    this.w = tall ? 16 : 14;
    this.h = tall ? 25 : 12;
    this.y = 130 - this.h;
    this.scored = false;
  }
  bounds(camera) { return rect(this.x - camera, this.y, this.w, this.h); }
  draw(camera) { drawRock(trunc(this.x - camera), this.y, this.w, this.h); }
}

class LogObstacle {
  constructor(x) {
    this.x = x;
    this.y = 118;
    this.w = 25;
    this.scored = false;
  }
  bounds(camera) { return rect(this.x - camera, this.y + 2, 25, 9); }
  draw(camera) {
    const x = trunc(this.x - camera);
    box(BLACK, x - 1, this.y + 1, 27, 11);
    box(WOOD, x, this.y + 3, 25, 7);
    box(WOOD_LIGHT, x + 2, this.y + 4, 18, 2);
    box(DIRT_DARK, x + 20, this.y + 3, 3, 7);
  }
}

class Bird {
  constructor(x) {
    this.x = x;
    this.y = BIRD_Y;
    this.w = 16;
    this.scored = false;
  }
  bounds(camera) { return rect(this.x - camera + 2, this.y + 1, 12, 8); }
  draw(camera, frame) { drawBirdSprite(trunc(this.x - camera), this.y, frame); }
}

class BranchObstacle {
  constructor(x, length) {
    this.x = x;
    this.y = 92;
    this.w = length;
    this.h = 13;
    this.scored = false;
  }
  bounds(camera) { return rect(this.x - camera, this.y, this.w, this.h); }
  draw(camera, frame) {
    const x = trunc(this.x - camera);
    const leaf = pymod(frame, 20) < 10 ? TREE : TREE_DARK;
    box(BROWN, x + 8, 74, 3, 18);
    box(BROWN, x + this.w - 12, 70, 3, 22);
    box(BLACK, x, 90, this.w, 15);
    box(WOOD, x + 1, 92, this.w - 2, 9);
    box(WOOD_LIGHT, x + 2, 93, this.w - 4, 2);
    for (let i = 4; i < this.w - 4; i += 12) {
      box(leaf, x + i, 99, 7, 4);
      box(GREEN_LIGHT, x + i + 1, 97, 3, 2);
    }
  }
}

class MushroomBoost {
  constructor(x, y) {
    this.x = x;
    this.y = y;
    this.got = false;
  }
  bounds(camera) { return rect(this.x - camera - 1, this.y - 1, 18, 17); }
  draw(camera) { if (!this.got) drawMushroom(trunc(this.x - camera), this.y); }
}

class StarPickup {
  constructor(x, y) {
    this.x = x;
    this.y = y;
    this.got = false;
  }
  bounds(camera) { return rect(this.x - camera, this.y, 10, 10); }
  draw(camera, frame) { if (!this.got) starIcon(trunc(this.x - camera), trunc(this.y), frame); }
}

class ChestPickup {
  constructor(x) {
    this.x = x;
    this.y = 108;
    this.opened = false;
    this.effectTimer = 0;
  }
  bounds(camera) { return rect(this.x - camera, this.y - 7, 20, 22); }
  draw(camera, frame) {
    drawChest(trunc(this.x - camera), this.y, this.opened);
    if (this.effectTimer) {
      const lift = trunc((70 - this.effectTimer) / 5);
      drawBottle(trunc(this.x - camera) + 6, this.y - 22 - lift, frame);
      this.effectTimer -= 1;
    }
  }
}

class World {
  constructor() {
    this.coins = [];
    this.obstacles = [];
    this.mushrooms = [];
    this.stars = [];
    this.chests = [];
    this.nextSegment = 0;
    this.lastObstacleX = -999;
    this.lastChestSegment = -999;
    this.generateUntil(GENERATE_AHEAD);
  }

  generateUntil(targetX) {
    while (this.nextSegment * SEGMENT_WIDTH < targetX) {
      this.generateSegment(this.nextSegment);
      this.nextSegment += 1;
    }
  }

  generateSegment(segment) {
    const base = segment * SEGMENT_WIDTH;
    const rng = makeRng(segment * 9173 + 41);
    const segSpeed = speedAt(base);
    const level = levelAtMeters(base / 10);
    let minGap = trunc(segSpeed * Math.max(24, 52 - level * 3));
    if (segment === 0) minGap = Math.max(minGap, 150);
    [70, 125, 185, 245].forEach((offset, index) => {
      const x = base + offset + rng.randint(-8, 8);
      const arc = (segment + index) % 3 ? 88 : 76;
      const y = arc + trunc(Math.sin((segment + index) * 1.7) * 7);
      this.coins.push(new Coin(x, y));
    });
    let slots;
    if (segment === 0) slots = [base + 235];
    else {
      slots = [base + 70, base + 200];
      if (level >= 2) slots.push(base + 135);
      if (level >= 4) slots.push(base + 285);
    }
    slots.sort((a, b) => a - b).forEach((slot) => {
      this.addObstacle(slot + rng.randint(-6, 6), segment, level, rng, minGap);
    });
    if (rng.random() < Math.max(0.2, 0.42 - level * 0.03)) {
      const y = rng.random() < 0.5 ? MUSHROOM_GROUND_Y : MUSHROOM_JUMP_Y;
      this.mushrooms.push(new MushroomBoost(base + 55 + rng.randint(-8, 8), y));
    }
    if (rng.random() < 0.38) this.stars.push(new StarPickup(base + 145 + rng.randint(-10, 10), 74));
    const chestChance = Math.max(0.05, 0.16 - level * 0.012);
    if (segment >= 4 && segment - this.lastChestSegment >= 6 && rng.random() < chestChance) {
      this.chests.push(new ChestPickup(base + 178 + rng.randint(-8, 8)));
      this.lastChestSegment = segment;
    }
  }

  addObstacle(x, segment, level, rng, minGap) {
    const typeRoll = rng.random();
    const clusterRoll = rng.random();
    const tallRoll = rng.random();
    const kindRoll = rng.random();
    const pairRoll = rng.random();
    if (x - this.lastObstacleX < minGap) return;
    const baseMeters = (segment * SEGMENT_WIDTH) / 10;
    if (baseMeters >= BIRD_UNLOCK_M) {
      const branchChance = Math.min(0.4, 0.32 + level * 0.015);
      const birdChance = branchChance + Math.min(0.46, 0.36 + level * 0.02);
      if (kindRoll < branchChance) {
        const length = Math.min(176, Math.max(108, trunc(speedAt(x) * 26 + 50)));
        this.obstacles.push(new BranchObstacle(x, length));
        this.lastObstacleX = x + length;
        return;
      }
      if (kindRoll < birdChance) {
        this.obstacles.push(new Bird(x));
        let end = x;
        const flock = level >= 3 && pairRoll < 0.42 ? 3 : pairRoll < 0.62 ? 2 : 1;
        for (let i = 1; i < flock; i += 1) {
          const pairX = x + i * 30;
          this.obstacles.push(new Bird(pairX));
          end = pairX;
        }
        this.lastObstacleX = end;
        return;
      }
    }
    let cluster = 1;
    if (level >= 2 && clusterRoll < 0.3) cluster = 2;
    if (level >= 5 && clusterRoll < 0.12) cluster = 3;
    if (cluster > 1) {
      for (let i = 0; i < cluster; i += 1) this.obstacles.push(new RockObstacle(x + i * 18));
      this.lastObstacleX = x + (cluster - 1) * 18;
      return;
    }
    if (segment > 5 && typeRoll < 0.32) this.obstacles.push(new LogObstacle(x));
    else this.obstacles.push(new RockObstacle(x, level >= 1 && tallRoll < (level >= 4 ? 0.4 : 0.26)));
    this.lastObstacleX = x;
  }

  cleanup(camera) {
    const cutoff = camera - CLEANUP_BEHIND;
    this.coins = this.coins.filter((item) => item.x > cutoff && !item.got);
    this.mushrooms = this.mushrooms.filter((item) => item.x > cutoff && !item.got);
    this.stars = this.stars.filter((item) => item.x > cutoff && !item.got);
    this.chests = this.chests.filter((item) => item.x > cutoff);
    this.obstacles = this.obstacles.filter((item) => item.x > cutoff);
  }

  draw(camera, frame) {
    this.coins.forEach((item) => item.draw(camera, frame));
    this.stars.forEach((item) => item.draw(camera, frame));
    this.mushrooms.forEach((item) => item.draw(camera));
    this.chests.forEach((item) => item.draw(camera, frame));
    this.obstacles.forEach((item) => item.draw(camera, frame));
  }
}

function loadBest() {
  try {
    const value = Number.parseInt(localStorage.getItem(BEST_KEY) || "0", 10);
    return Number.isFinite(value) ? Math.max(0, value) : 0;
  } catch (error) {
    return 0;
  }
}

function saveBest(distance) {
  try {
    localStorage.setItem(BEST_KEY, String(Math.max(0, trunc(distance))));
  } catch (error) {
    // O navegador pode recusar o armazenamento local.
  }
}

const SAMPLE_RATE = 22050;
let audioCtx = null;
let musicGain = null;
let musicSource = null;
let buffers = null;

function voice(freq, time, duty = 0.5, triMix = 0.6) {
  if (freq <= 0) return 0;
  const phase = pymod(time * freq, 1);
  const tri = 4 * Math.abs(phase - 0.5) - 1;
  const pulse = phase < duty ? 1 : -1;
  return tri * triMix + pulse * (1 - triMix);
}

function makeToneBuffer(context, freq, duration, volume, slide, triMix) {
  const total = Math.floor(SAMPLE_RATE * duration);
  const buffer = context.createBuffer(1, total, SAMPLE_RATE);
  const data = buffer.getChannelData(0);
  for (let i = 0; i < total; i += 1) {
    const time = i / SAMPLE_RATE;
    const current = freq + slide * (i / Math.max(1, total));
    let fade = Math.min(1, i / Math.max(1, SAMPLE_RATE * 0.006));
    fade *= Math.min(1, (total - i) / Math.max(1, SAMPLE_RATE * 0.02));
    fade *= Math.exp((-3 * i) / total);
    data[i] = voice(current, time, 0.5, triMix) * volume * fade;
  }
  return buffer;
}

function makeMusicBuffer(context, notes) {
  const step = 0.16;
  const volume = 0.16;
  const totalPerStep = Math.floor(SAMPLE_RATE * step);
  const attack = Math.max(140, Math.floor(SAMPLE_RATE * 0.008));
  const decay = Math.floor(SAMPLE_RATE * 0.05);
  const sustain = 0.6;
  const release = Math.floor(SAMPLE_RATE * 0.045);
  const raw = [];
  notes.forEach((note, index) => {
    const bass = index % 8 === 0 ? 98 : 0;
    const duty = index % 2 === 0 ? 0.5 : 0.42;
    for (let i = 0; i < totalPerStep; i += 1) {
      const time = i / SAMPLE_RATE;
      let env;
      if (i < attack) env = i / attack;
      else if (i < attack + decay) env = 1 - (1 - sustain) * ((i - attack) / decay);
      else env = sustain;
      const remaining = totalPerStep - i;
      if (remaining < release) env *= remaining / release;
      let value = voice(note, time, duty, 0.6) * 0.82;
      if (bass) value += voice(bass, time, 0.5, 1) * 0.22;
      raw.push(value * env);
    }
  });
  const buffer = context.createBuffer(1, raw.length, SAMPLE_RATE);
  const data = buffer.getChannelData(0);
  for (let i = 0; i < raw.length; i += 1) {
    const prev = i > 0 ? raw[i - 1] : raw[i];
    const next = i < raw.length - 1 ? raw[i + 1] : raw[i];
    data[i] = Math.max(-1, Math.min(1, (0.25 * prev + 0.5 * raw[i] + 0.25 * next) * volume));
  }
  return buffer;
}

function ensureAudio() {
  try {
    ensureAudioContext();
  } catch (error) {
    audioCtx = null;
  }
}

function ensureAudioContext() {
  if (!audioCtx) {
    audioCtx = new AudioContext();
    musicGain = audioCtx.createGain();
    musicGain.gain.value = 0;
    musicGain.connect(audioCtx.destination);
    const notes = [
      220, 0, 220, 247, 262, 330, 294, 262,
      220, 0, 330, 370, 440, 370, 330, 294,
      247, 0, 247, 262, 294, 370, 330, 294,
      247, 0, 370, 392, 494, 440, 392, 330,
      262, 0, 262, 294, 330, 392, 370, 330,
      262, 0, 392, 440, 523, 494, 440, 392,
      330, 0, 370, 440, 392, 330, 294, 262,
      220, 0, 220, 247, 262, 330, 294, 220,
    ];
    buffers = {
      music: makeMusicBuffer(audioCtx, notes),
      jump: makeToneBuffer(audioCtx, 520, 0.09, 0.16, 150, 0.55),
      coin: makeToneBuffer(audioCtx, 1046, 0.07, 0.14, 120, 0.8),
      hit: makeToneBuffer(audioCtx, 150, 0.16, 0.22, -70, 0.3),
      star: makeToneBuffer(audioCtx, 1320, 0.13, 0.18, 240, 0.8),
      bottle: makeToneBuffer(audioCtx, 900, 0.18, 0.18, 150, 0.7),
      level: makeToneBuffer(audioCtx, 880, 0.2, 0.18, 320, 0.75),
    };
  }
  if (audioCtx.state === "suspended") audioCtx.resume();
}

function playSfx(name) {
  if (!audioCtx || !buffers || !buffers[name]) return;
  const source = audioCtx.createBufferSource();
  source.buffer = buffers[name];
  source.connect(audioCtx.destination);
  source.start();
}

function startMusic() {
  if (!buffers || !buffers.music) return;
  if (!musicSource) {
    musicSource = audioCtx.createBufferSource();
    musicSource.buffer = buffers.music;
    musicSource.loop = true;
    musicSource.connect(musicGain);
    musicSource.start();
  }
  musicGain.gain.value = 0.22;
}

function toggleMusic(game) {
  ensureAudio();
  if (!musicGain) return;
  if (!game.musicOn) {
    startMusic();
    game.musicOn = true;
    return;
  }
  game.musicOn = false;
  musicGain.gain.value = 0;
}

function fitCanvas() {
  const controls = document.getElementById("controls");
  const controlsH = controls && getComputedStyle(controls).display !== "none" ? controls.offsetHeight : 0;
  let scale = Math.min(window.innerWidth / VW, (window.innerHeight - controlsH) / VH);
  if (scale >= 2) scale = Math.floor(scale);
  canvas.style.width = `${Math.max(1, VW * scale)}px`;
  canvas.style.height = `${Math.max(1, VH * scale)}px`;
}

function createGame() {
  return {
    player: new Player(),
    world: new World(),
    lives: START_LIVES,
    score: 0,
    coins: 0,
    starsFound: 0,
    bottlesFound: 0,
    combo: 0,
    state: "title",
    frame: 0,
    bestDistance: loadBest(),
    startBest: loadBest(),
    distance: 0,
    prevLevel: 0,
    popups: [],
    particles: [],
    shake: 0,
    hitFlash: 0,
    musicOn: false,
    touchJumpFrames: 0,
    jumpPointer: false,
    duckPointer: false,
  };
}

const keys = new Set();
const pointers = new Map();
let game = createGame();

function jumpHeld() {
  return keys.has("Space") || keys.has("ArrowUp") || keys.has("KeyW") || game.jumpPointer || game.touchJumpFrames > 0;
}

function duckHeld() {
  return keys.has("ArrowDown") || keys.has("KeyS") || game.duckPointer;
}

function syncPointers() {
  game.jumpPointer = false;
  game.duckPointer = false;
  pointers.forEach((kind) => {
    if (kind === "duck") game.duckPointer = true;
    else game.jumpPointer = true;
  });
}

function addPopup(msg, x, y, color) {
  game.popups.push({ msg, x, y, color, ttl: 50 });
}

function spawnDust(x, count) {
  for (let i = 0; i < count; i += 1) {
    game.particles.push({
      x: x + 4 + Math.random() * 14,
      y: GROUND_Y - 1,
      vx: -1.1 + Math.random() * 1.3,
      vy: -1.4 + Math.random() * 1.1,
      ttl: 16,
      color: Math.random() < 0.5 ? DIRT : DIRT_DARK,
    });
  }
  if (game.particles.length > 60) game.particles.splice(0, game.particles.length - 60);
}

function restartRun() {
  const best = game.bestDistance;
  const musicOn = game.musicOn;
  game = createGame();
  game.bestDistance = best;
  game.startBest = best;
  game.musicOn = musicOn;
  game.state = "play";
  syncPointers();
}

function drawPopups(camera) {
  game.popups = game.popups.filter((popup) => {
    const lift = trunc((50 - popup.ttl) * 0.4);
    text(popup.msg, trunc(popup.x - camera), trunc(popup.y - lift), popup.color, "small", true);
    popup.ttl -= 1;
    return popup.ttl > 0;
  });
}

function drawParticles(camera) {
  game.particles = game.particles.filter((particle) => {
    particle.x += particle.vx;
    particle.y += particle.vy;
    particle.vy += 0.18;
    particle.ttl -= 1;
    if (particle.ttl <= 0) return false;
    box(particle.color, trunc(particle.x - camera), trunc(particle.y), 1, 1);
    return true;
  });
}

function simulate() {
  game.frame += 1;
  if (game.state === "play") {
    const { jumped, landed } = game.player.update(jumpHeld(), duckHeld());
    if (jumped) {
      playSfx("jump");
      spawnDust(game.player.x, 3);
    }
    if (landed) spawnDust(game.player.x, 5);
  }
  if (game.touchJumpFrames) game.touchJumpFrames -= 1;

  const camera = game.state === "title"
    ? 0
    : Math.max(0, game.player.x - (74 + trunc(Math.min(game.player.baseSpeed - BASE_SPEED, 1.6) * 12)));

  if (game.state === "play") {
    game.world.generateUntil(game.player.x + GENERATE_AHEAD);
    game.world.cleanup(camera);
    game.distance = Math.max(game.distance, trunc(game.player.x / 10));
    game.bestDistance = Math.max(game.bestDistance, game.distance);
    const level = levelAtMeters(game.distance);
    if (level > game.prevLevel) {
      game.prevLevel = level;
      addPopup("LEVEL UP!", game.player.x + 60, 64, YELLOW);
      playSfx("level");
    }
    const hitbox = game.player.hitbox();
    hitbox.x = trunc(hitbox.x - camera);
    game.world.coins.forEach((coin) => {
      if (!coin.got && overlaps(hitbox, coin.bounds(camera))) {
        coin.got = true;
        game.coins += 1;
        game.score += 1;
        playSfx("coin");
      }
    });
    game.world.stars.forEach((star) => {
      if (!star.got && overlaps(hitbox, star.bounds(camera))) {
        star.got = true;
        game.starsFound += 1;
        game.score += 5;
        addPopup("+5", star.x + 4, star.y - 8, YELLOW);
        playSfx("star");
      }
    });
    game.world.mushrooms.forEach((mushroom) => {
      if (!mushroom.got && overlaps(hitbox, mushroom.bounds(camera))) {
        mushroom.got = true;
        game.player.boostTimer = BOOST_FRAMES;
        game.score += 2;
      }
    });
    game.world.chests.forEach((chest) => {
      if (!chest.opened && overlaps(hitbox, chest.bounds(camera))) {
        chest.opened = true;
        chest.effectTimer = 70;
        game.bottlesFound += 1;
        game.score += 3;
        if (game.lives < MAX_LIVES) {
          game.lives += 1;
          addPopup("+1 VIDA", chest.x + 10, chest.y - 12, PINK);
        } else {
          game.score += 2;
          addPopup("VIDA MAX", chest.x + 10, chest.y - 12, YELLOW);
        }
        playSfx("bottle");
      }
    });
    for (const obstacle of game.world.obstacles) {
      if (game.player.invuln === 0 && overlaps(hitbox, obstacle.bounds(camera))) {
        game.lives -= 1;
        game.combo = 0;
        obstacle.scored = true;
        playSfx("hit");
        game.player.invuln = game.distance < 100 ? 90 : 75;
        game.player.boostTimer = 0;
        game.player.knockVx = -6;
        game.shake = 13;
        game.hitFlash = 3;
        if (game.lives <= 0) {
          game.state = "gameover";
          saveBest(game.bestDistance);
        }
        break;
      }
    }
    game.world.obstacles.forEach((obstacle) => {
      if (!obstacle.scored && obstacle.x + obstacle.w < game.player.x) {
        obstacle.scored = true;
        game.combo += 1;
        game.score += game.combo;
      }
    });
  }
  return camera;
}

function render(camera) {
  const amp = game.shake > 0 ? Math.max(1, Math.round(game.shake / 4)) : 0;
  const ox = amp ? randint(-amp, amp) : 0;
  const oy = amp ? randint(-amp, amp) : 0;
  ctx.setTransform(1, 0, 0, 1, 0, 0);
  ctx.fillStyle = BLACK;
  ctx.fillRect(0, 0, VW, VH);
  ctx.setTransform(1, 0, 0, 1, ox, oy);
  drawBackground(camera);
  drawWorldDecor(camera);
  game.world.draw(camera, game.frame);
  drawParticles(camera);
  drawPopups(camera);
  if (!(game.player.invuln > 0 && pymod(game.frame, 6) < 3)) {
    const squash = game.player.landTimer > 3 ? 2 : 0;
    drawJoaoPedro(trunc(game.player.x - camera), trunc(game.player.y), game.frame, game.player.ducking, squash);
  }
  if (game.hitFlash > 0) {
    box(RED, 0, 0, VW, 2);
    box(RED, 0, VH - 2, VW, 2);
    box(RED, 0, 0, 2, VH);
    box(RED, VW - 2, 0, 2, VH);
    game.hitFlash -= 1;
  }
  drawHud(game);
  if (game.state === "title") drawTitle();
  else if (game.state === "gameover") drawEnd(game);
  if (game.shake > 0) game.shake -= 1;
}

function tick() {
  render(simulate());
}

function beginFromPointer(kind) {
  ensureAudio();
  if (kind === "jump") game.touchJumpFrames = TOUCH_JUMP_FRAMES;
  syncPointers();
  if (game.state === "title" && kind === "jump") game.state = "play";
  else if (game.state === "gameover") restartRun();
}

window.addEventListener("pointerdown", (event) => {
  const kind = event.target === duckBtn ? "duck" : "jump";
  pointers.set(event.pointerId, kind);
  beginFromPointer(kind);
  event.preventDefault();
}, { passive: false });

window.addEventListener("pointerup", (event) => {
  pointers.delete(event.pointerId);
  syncPointers();
});
window.addEventListener("pointercancel", (event) => {
  pointers.delete(event.pointerId);
  syncPointers();
});
window.addEventListener("contextmenu", (event) => event.preventDefault());

window.addEventListener("keydown", (event) => {
  keys.add(event.code);
  if (event.code === "Space" || event.code.startsWith("Arrow")) event.preventDefault();
  if (event.repeat) return;
  ensureAudio();
  if (event.code === "KeyM") toggleMusic(game);
  if (event.code === "Space" && game.state === "title") game.state = "play";
  if ((event.code === "KeyR" || event.code === "Space") && game.state === "gameover") restartRun();
  if ((event.code === "Space" || event.code === "ArrowUp" || event.code === "KeyW") && game.state === "play") {
    game.touchJumpFrames = TOUCH_JUMP_FRAMES;
  }
});
window.addEventListener("keyup", (event) => keys.delete(event.code));
window.addEventListener("pagehide", () => saveBest(game.bestDistance));
window.addEventListener("resize", fitCanvas);

fitCanvas();
canvas.focus();

let lastTime = performance.now();
let accumulator = 0;
function loop(now) {
  let delta = now - lastTime;
  lastTime = now;
  if (delta > 100) delta = 100;
  accumulator += delta;
  const step = 1000 / 60;
  let steps = 0;
  while (accumulator >= step && steps < 5) {
    tick();
    accumulator -= step;
    steps += 1;
  }
  requestAnimationFrame(loop);
}
requestAnimationFrame(loop);
