#!/usr/bin/env python3
"""Generate crisp integer-grid pixel-art SVGs (dark & light themes) for GitHub profile HUSMUS9999."""

import os

# 5x7 crisp bitmap font (integer grid)
FONT_5X7 = {
    'A': ["01110","10001","10001","11111","10001","10001","10001"],
    'B': ["11110","10001","10001","11110","10001","10001","11110"],
    'C': ["01110","10001","10000","10000","10000","10001","01110"],
    'D': ["11110","10001","10001","10001","10001","10001","11110"],
    'E': ["11111","10000","10000","11110","10000","10000","11111"],
    'F': ["11111","10000","10000","11110","10000","10000","10000"],
    'G': ["01110","10001","10000","10111","10001","10001","01110"],
    'H': ["10001","10001","10001","11111","10001","10001","10001"],
    'I': ["11111","00100","00100","00100","00100","00100","11111"],
    'J': ["00111","00010","00010","00010","10010","10010","01100"],
    'K': ["10001","10010","10100","11000","10100","10010","10001"],
    'L': ["10000","10000","10000","10000","10000","10000","11111"],
    'M': ["10001","11011","10101","10101","10001","10001","10001"],
    'N': ["10001","11001","10101","10011","10001","10001","10001"],
    'O': ["01110","10001","10001","10001","10001","10001","01110"],
    'P': ["11110","10001","10001","11110","10000","10000","10000"],
    'Q': ["01110","10001","10001","10001","10101","10010","01101"],
    'R': ["11110","10001","10001","11110","10100","10010","10001"],
    'S': ["01111","10000","10000","01110","00001","00001","11110"],
    'T': ["11111","00100","00100","00100","00100","00100","00100"],
    'U': ["10001","10001","10001","10001","10001","10001","01110"],
    'V': ["10001","10001","10001","10001","10001","01010","00100"],
    'W': ["10001","10001","10001","10101","10101","11011","10001"],
    'X': ["10001","10001","01010","00100","01010","10001","10001"],
    'Y': ["10001","10001","01010","00100","00100","00100","00100"],
    'Z': ["11111","00001","00010","00100","01000","10000","11111"],
    '0': ["01110","10011","10101","10101","11001","10001","01110"],
    '1': ["00100","01100","00100","00100","00100","00100","01110"],
    '2': ["01110","10001","00001","00110","01000","10000","11111"],
    '3': ["11110","00001","00001","01110","00001","00001","11110"],
    '4': ["00010","00110","01010","10010","11111","00010","00010"],
    '5': ["11111","10000","11110","00001","00001","10001","01110"],
    '6': ["01110","10000","11110","10001","10001","10001","01110"],
    '7': ["11111","00001","00010","00100","01000","01000","01000"],
    '8': ["01110","10001","10001","01110","10001","10001","01110"],
    '9': ["01110","10001","10001","01111","00001","00001","01110"],
    ' ': ["000","000","000","000","000","000","000"],
    '.': ["00","00","00","00","00","11","11"],
    ':': ["00","11","11","00","11","11","00"],
    '-': ["0000","0000","0000","1111","0000","0000","0000"],
    '+': ["00000","00100","00100","11111","00100","00100","00000"],
    '/': ["00001","00010","00010","00100","01000","01000","10000"],
    '#': ["01010","01010","11111","01010","11111","01010","01010"],
    '&': ["01100","10010","10100","01000","10101","10010","01101"],
    '|': ["010","010","010","010","010","010","010"],
    '>': ["1000","0100","0010","0001","0010","0100","1000"],
    '~': ["00000","01101","10010","00000","00000","00000","00000"],
    '_': ["00000","00000","00000","00000","00000","00000","11111"],
    '[': ["111","100","100","100","100","100","111"],
    ']': ["111","001","001","001","001","001","111"],
    '\'':["11","11","00","00","00","00","00"],
    '@': ["01110","10001","10111","10101","10110","10000","01110"],
}

# 3x5 crisp micro bitmap font for exact integer scale=2 subtitles
FONT_3X5 = {
    'A': ["010","101","111","101","101"],
    'B': ["110","101","110","101","110"],
    'C': ["011","100","100","100","011"],
    'D': ["110","101","101","101","110"],
    'E': ["111","100","110","100","111"],
    'F': ["111","100","110","100","100"],
    'G': ["011","100","101","101","011"],
    'H': ["101","101","111","101","101"],
    'I': ["111","010","010","010","111"],
    'J': ["001","001","001","101","010"],
    'K': ["101","101","110","101","101"],
    'L': ["100","100","100","100","111"],
    'M': ["10001","11011","10101","10001","10001"],
    'N': ["1001","1101","1011","1001","1001"],
    'O': ["010","101","101","101","010"],
    'P': ["110","101","110","100","100"],
    'Q': ["010","101","101","111","001"],
    'R': ["110","101","110","101","101"],
    'S': ["011","100","010","001","110"],
    'T': ["111","010","010","010","010"],
    'U': ["101","101","101","101","010"],
    'V': ["101","101","101","101","010"],
    'W': ["10001","10001","10101","11011","10001"],
    'X': ["101","101","010","101","101"],
    'Y': ["101","101","010","010","010"],
    'Z': ["111","001","010","100","111"],
    '0': ["111","101","101","101","111"],
    '1': ["010","110","010","010","111"],
    '2': ["110","001","010","100","111"],
    '3': ["110","001","010","001","110"],
    '4': ["101","101","111","001","001"],
    '5': ["111","100","110","001","110"],
    '6': ["011","100","111","101","111"],
    '7': ["111","001","010","010","010"],
    '8': ["111","101","111","101","111"],
    '9': ["111","101","111","001","110"],
    ' ': ["00","00","00","00","00"],
    '.': ["0","0","0","0","1"],
    ',': ["00","00","00","01","10"],
    ':': ["0","1","0","1","0"],
    '-': ["000","000","111","000","000"],
    '+': ["000","010","111","010","000"],
    '/': ["001","001","010","100","100"],
    '#': ["01010","11111","01010","11111","01010"],
    '&': ["010","101","010","101","011"],
    '|': ["1","1","1","1","1"],
    '\'':["1","1","0","0","0"],
    '[': ["11","10","10","10","11"],
    ']': ["11","01","01","01","11"],
}

SHIELD_SPRITE = [
    "......OOOOOO......",
    "....OOLLLLLLOO....",
    "..OOLLGGGGGGLLOO..",
    ".OLGGGGGGGGGGGGLO.",
    ".OLGDDDDDDDDDDGLO.",
    ".OLGDGGGGGGGGDGLO.",
    ".OLGDGGWWWWGGDGLO.",
    ".OLGDGWWGGWWGDGLO.",
    ".OLGDGWWGGWWGDGLO.",
    ".OLGDGGWWWWGGDGLO.",
    ".OLGDGGGWWGGGDGLO.",
    ".OLGDGGGWWGGGDGLO.",
    "..OLGDGWWWWGDGLO..",
    "..OLGDGGGGGGDGLO..",
    "...OLGDDDDDDGLO...",
    "....OLGGGGGGGLO...",
    ".....OOGGGGOO.....",
    ".......OOGOO......",
    "........OO........",
]

CRT_SPRITE = [
    "..OOOOOOOOOOOOOOOO..",
    ".OCCCCCCCCCCCCCCCCO.",
    "OCSSSSSSSSSSSSSSSSCO",
    "OCSBBBBBBBBBBBBBBSCO",
    "OCSBGGGGBBBGBBBBBSCO",
    "OCSBBBBBBBBBBBBBBSCO",
    "OCSBGGBGGGGBGGBBBSCO",
    "OCSBBBBBBBBBBBBBBSCO",
    "OCSBGGGBBGGBGGBBBSCO",
    "OCSBBBBBBBBBWWBBBSCO",
    "OCSBBBBBBBBBBBBBBSCO",
    "OCSSSSSSSSSSSSSSSSCO",
    ".OCCCCCCCCCCCCGGCCO.",
    "..OOOOOOOOOOOOOOOO..",
    "......OCCCCCCOO.....",
    "....OOCCCCCCCCOO....",
]

ICON_SHIELD = [
    "...OOOOOO...",
    ".OOGGGGGGOO.",
    "OGGDDDDDDGGO",
    "OGDGGWWGGDGO",
    "OGDGGWWGGDGO",
    "OGDGWWWWGDGO",
    "OGDGGWWGGDGO",
    ".OGDDDDDDGO.",
    "..OGGGGGGO..",
    "...OOGGOO...",
    ".....OO.....",
]

ICON_BINARY = [
    "OOOOOOOOOOOO",
    "ODDDDDDDDDDO",
    "ODGGDGDGGDDO",
    "ODGDGGDGDDDO",
    "ODDDDDDDDDDO",
    "ODGDDGGDGDDO",
    "ODGGDGDDGGDO",
    "ODDDDDDDDDDO",
    "ODGGWWGGDDDO",
    "ODDDDDDDDDDO",
    "OOOOOOOOOOOO",
]

ICON_GEAR = [
    "....OOOO....",
    ".OO.OGGO.OO.",
    ".OGGOGGOGGO.",
    "..OGGGGGGO..",
    "OOGGDDDDGGOO",
    "OGGGDWWDDGGO",
    "OGGGDWWDDGGO",
    "OOGGDDDDGGOO",
    "..OGGGGGGO..",
    ".OGGOGGOGGO.",
    ".OO.OGGO.OO.",
    "....OOOO....",
]

ICON_TROPHY = [
    "OOOOOOOOOOOO",
    "OYYYYYYYYYYO",
    "OYOOYYYYOOYO",
    "OYOYYYYYYOYO",
    ".OOYYYYYYOO.",
    "..OYYYYYYO..",
    "...OYYYYO...",
    "....OYYO....",
    "....OYYO....",
    "..OOYYYYOO..",
    ".OYYYYYYYYO.",
    ".OOOOOOOOOO.",
]


def measure_text(text, scale, font=FONT_5X7, tracking=1):
    total = 0
    chars = text.upper()
    for idx, ch in enumerate(chars):
        glyph = font.get(ch, font[' '])
        total += len(glyph[0]) * scale
        if idx < len(chars) - 1:
            total += tracking * scale
    return total


def draw_text(rects, text, x, y, scale, color, font=FONT_5X7, tracking=1):
    cx = x
    for ch in text.upper():
        glyph = font.get(ch, font[' '])
        w = len(glyph[0])
        for ry, row in enumerate(glyph):
            for rx, bit in enumerate(row):
                if bit == '1':
                    rects.append(f'<rect x="{cx + rx*scale}" y="{y + ry*scale}" width="{scale}" height="{scale}" fill="{color}"/>')
        cx += (w + tracking) * scale
    return cx


def draw_sprite(rects, sprite, x, y, scale, palette):
    for ry, row in enumerate(sprite):
        for rx, ch in enumerate(row):
            if ch != '.' and ch in palette:
                rects.append(f'<rect x="{x + rx*scale}" y="{y + ry*scale}" width="{scale}" height="{scale}" fill="{palette[ch]}"/>')


def draw_pixel_box(rects, x, y, w, h, px, fill, border, corner_cut=True):
    rects.append(f'<rect x="{x+px}" y="{y+px}" width="{w-2*px}" height="{h-2*px}" fill="{fill}"/>')
    cut = px if corner_cut else 0
    rects.append(f'<rect x="{x+cut}" y="{y}" width="{w-2*cut}" height="{px}" fill="{border}"/>')
    rects.append(f'<rect x="{x+cut}" y="{y+h-px}" width="{w-2*cut}" height="{px}" fill="{border}"/>')
    rects.append(f'<rect x="{x}" y="{y+cut}" width="{px}" height="{h-2*cut}" fill="{border}"/>')
    rects.append(f'<rect x="{x+w-px}" y="{y+cut}" width="{px}" height="{h-2*cut}" fill="{border}"/>')
    if corner_cut:
        for cx, cy in [(x+px, y+px), (x+w-2*px, y+px), (x+px, y+h-2*px), (x+w-2*px, y+h-2*px)]:
            rects.append(f'<rect x="{cx}" y="{cy}" width="{px}" height="{px}" fill="{border}"/>')


def draw_badge(rects, text, x, y, scale, pad_x, pad_y, border_px, bg, border, fg, font=FONT_3X5):
    tw = measure_text(text, scale, font=font, tracking=1)
    th = (5 if font is FONT_3X5 else 7) * scale
    bw = tw + 2 * pad_x + 2 * border_px
    bh = th + 2 * pad_y + 2 * border_px
    draw_pixel_box(rects, x, y, bw, bh, border_px, bg, border, corner_cut=False)
    draw_text(rects, text, x + border_px + pad_x, y + border_px + pad_y, scale, fg, font=font, tracking=1)
    return bw, bh


def build_banner(theme):
    if theme == "dark":
        c = {
            "panel": "#111A23",
            "panel_inner": "#0D151D",
            "border": "#23634B",
            "border_hi": "#34D399",
            "grid": "#16222D",
            "title": "#E6F4EE",
            "accent": "#34D399",
            "accent_dim": "#1F7A5A",
            "muted": "#8FA6B8",
            "gold": "#F5B841",
            "gold_bg": "#241E11",
            "badge_bg": "#122922",
            "crt_case": "#2B3A49",
            "crt_bezel": "#18232E",
            "crt_screen": "#091311",
            "outline": "#050A0E",
        }
    else:
        c = {
            "panel": "#FFFFFF",
            "panel_inner": "#F4F9F6",
            "border": "#23634B",
            "border_hi": "#1B7A57",
            "grid": "#E5EFEA",
            "title": "#18242E",
            "accent": "#1E6B4F",
            "accent_dim": "#358A6A",
            "muted": "#516170",
            "gold": "#A86E05",
            "gold_bg": "#FDF5E4",
            "badge_bg": "#E7F4EE",
            "crt_case": "#536779",
            "crt_bezel": "#2C3B48",
            "crt_screen": "#0D1C17",
            "outline": "#1C2933",
        }

    W, H = 880, 232
    px = 4
    rects = []

    draw_pixel_box(rects, 0, 0, W, H, px, c["panel"], c["border"], corner_cut=True)

    # Pixel matrix background
    for gx in range(20, W - 20, 24):
        for gy in range(44, H - 28, 20):
            rects.append(f'<rect x="{gx}" y="{gy}" width="2" height="2" fill="{c["grid"]}"/>')

    # Window title bar
    rects.append(f'<rect x="{px}" y="{px}" width="{W-2*px}" height="28" fill="{c["panel_inner"]}"/>')
    rects.append(f'<rect x="{px}" y="32" width="{W-2*px}" height="{px}" fill="{c["border"]}"/>')
    for idx, col in enumerate(["#E05A5A", "#E5B44B", c["border_hi"]]):
        rects.append(f'<rect x="{16 + idx*16}" y="12" width="8" height="8" fill="{col}"/>')

    draw_text(rects, "HUSMUS9999@ALGIERS:~/SECURITY", 76, 11, 2, c["muted"])
    right_lbl = "APPSEC // APK // ELF64"
    rw = measure_text(right_lbl, 2)
    draw_text(rects, right_lbl, W - 20 - rw, 11, 2, c["accent"])

    # Left Shield Card
    draw_pixel_box(rects, 24, 52, 116, 136, 4, c["panel_inner"], c["border"], corner_cut=True)
    shield_pal = {
        'O': c["outline"], 'L': c["border_hi"], 'G': c["accent"],
        'D': c["accent_dim"], 'W': "#E6FFF5" if theme == "dark" else "#FFFFFF",
    }
    draw_sprite(rects, SHIELD_SPRITE, 46, 70, 4, shield_pal)
    sl_w = measure_text("SEC.ENG", 2)
    draw_text(rects, "SEC.ENG", 24 + (116 - sl_w) // 2, 162, 2, c["accent"])

    # Center Name & Subtitle
    name_txt = "HOUSSEM EDDINE BENAZZI"
    name_w = measure_text(name_txt, 4)
    assert 162 + name_w < 714, f"Name overflows: {162 + name_w}"
    draw_text(rects, name_txt, 162, 56, 4, c["title"])

    rects.append(f'<rect x="162" y="92" width="420" height="4" fill="{c["border_hi"]}"/>')
    rects.append(f'<rect x="586" y="92" width="12" height="4" fill="{c["gold"]}"/>')
    rects.append(f'<rect x="602" y="92" width="8" height="4" fill="{c["accent_dim"]}"/>')

    draw_text(rects, "> CYBERSECURITY ENGINEER", 162, 108, 2, c["accent"])
    sub_txt = "APPSEC | PENTESTING | MOBILE & BINARY ANALYSIS"
    assert 162 + measure_text(sub_txt, 2) < 714
    draw_text(rects, sub_txt, 162, 130, 2, c["muted"])

    # Auto-sized crisp badges (scale=2, FONT_3X5 -> 10px tall, razor sharp integer grid!)
    b1_w, _ = draw_badge(rects, "CTF PEAK: #1 DZ / #14 GLOBAL", 162, 158, 2, 10, 8, 2, c["gold_bg"], c["gold"], c["gold"], font=FONT_3X5)
    b2_x = 162 + b1_w + 12
    b2_w, _ = draw_badge(rects, "PYTHON | C/C++ | GO | RUST", b2_x, 158, 2, 10, 8, 2, c["badge_bg"], c["border"], c["accent"], font=FONT_3X5)
    assert b2_x + b2_w < 716, f"Badges overflow right card: {b2_x + b2_w}"

    # Right Retro CRT Card
    draw_pixel_box(rects, 728, 52, 128, 136, 4, c["panel_inner"], c["border"], corner_cut=True)
    crt_pal = {
        'O': c["outline"], 'C': c["crt_case"], 'S': c["crt_bezel"],
        'B': c["crt_screen"], 'G': "#34D399", 'W': "#F5B841",
    }
    draw_sprite(rects, CRT_SPRITE, 752, 74, 4, crt_pal)
    tl_w = measure_text("TEMP.0", 2)
    draw_text(rects, "TEMP.0", 728 + (128 - tl_w) // 2, 162, 2, c["gold"])

    # Bottom status bar (exact integer scale=2 FONT_3X5)
    rects.append(f'<rect x="{px}" y="{H-26}" width="{W-2*px}" height="22" fill="{c["panel_inner"]}"/>')
    rects.append(f'<rect x="{px}" y="{H-28}" width="{W-2*px}" height="2" fill="{c["grid"]}"/>')
    draw_text(rects, "ALGIERS, DZ // SECURITY ENGINEERING & VULNERABILITY RESEARCH", 20, H - 20, 2, c["muted"], font=FONT_3X5)
    rects.append(f'<rect x="{W-26}" y="{H-21}" width="8" height="12" fill="{c["border_hi"]}"><animate attributeName="opacity" values="1;1;0;0" dur="1.2s" repeatCount="indefinite"/></rect>')

    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" shape-rendering="crispEdges">\n'
        + "\n".join(rects)
        + "\n</svg>\n"
    )


def build_loadout(theme):
    if theme == "dark":
        c = {
            "panel": "#111A23",
            "card": "#0D151D",
            "border": "#23634B",
            "border_hi": "#34D399",
            "title": "#E6F4EE",
            "accent": "#34D399",
            "accent_dim": "#1D5E46",
            "muted": "#8FA6B8",
            "gold": "#F5B841",
            "gold_bg": "#241E11",
            "badge_bg": "#122922",
            "outline": "#050A0E",
        }
    else:
        c = {
            "panel": "#FFFFFF",
            "card": "#F4F9F6",
            "border": "#23634B",
            "border_hi": "#1B7A57",
            "title": "#18242E",
            "accent": "#1E6B4F",
            "accent_dim": "#70B59A",
            "muted": "#516170",
            "gold": "#A86E05",
            "gold_bg": "#FDF5E4",
            "badge_bg": "#E7F4EE",
            "outline": "#1C2933",
        }

    W, H = 880, 198
    px = 4
    rects = []

    draw_pixel_box(rects, 0, 0, W, H, px, c["panel"], c["border"], corner_cut=True)
    draw_text(rects, "[ OPERATOR LOADOUT // CORE FOCUS AREAS ]", 22, 16, 2, c["accent"])
    rects.append(f'<rect x="22" y="36" width="{W-44}" height="2" fill="{c["border"]}"/>')

    # 4 crisp pixel cards (2x2), zero arbitrary skill bars — verified tag chips instead!
    cards = [
        (22, 48, ICON_SHIELD, "APPSEC & PENTEST", "200+ VALIDATED VULNS | WEB API ANDROID", "2+ YOE", c["badge_bg"], c["border"], c["accent"]),
        (450, 48, ICON_BINARY, "MOBILE & BINARY RE", "APK/JNI | ELF64 | FRIDA | GHIDRA | GDB", "RE/BIN", c["badge_bg"], c["border"], c["accent"]),
        (22, 120, ICON_GEAR, "SECURITY TOOLING", "RUST/C99 SEALING | ANTI-STEALTH | MCP", "0-DEPS", c["badge_bg"], c["border"], c["accent"]),
        (450, 120, ICON_TROPHY, "COMPETITIVE CTF", "TEMPERATURE0 | MIDNIGHT FLAG '26 FINAL", "#14 GLB", c["gold_bg"], c["gold"], c["gold"]),
    ]

    icon_pal = {
        'O': c["outline"], 'G': c["accent"], 'D': c["accent_dim"],
        'W': "#E6FFF5" if theme == "dark" else "#FFFFFF", 'Y': c["gold"],
    }

    for cx, cy, icon, heading, sub, tag, tbg, tbd, tfg in cards:
        cw, ch = 408, 62
        draw_pixel_box(rects, cx, cy, cw, ch, 3, c["card"], c["border"], corner_cut=False)
        draw_sprite(rects, icon, cx + 10, cy + 12, 3, icon_pal)
        draw_text(rects, heading, cx + 56, cy + 12, 2, c["title"])
        # Right-aligned pixel tag chip
        tag_tw = measure_text(tag, 2, font=FONT_3X5)
        tag_bw = tag_tw + 12 + 4
        tag_x = cx + cw - 10 - tag_bw
        assert cx + 56 + measure_text(heading, 2) + 8 < tag_x, f"Heading collides tag: {heading}"
        draw_badge(rects, tag, tag_x, cy + 9, 2, 6, 4, 2, tbg, tbd, tfg, font=FONT_3X5)
        # Integer scale=2 FONT_3X5 subtitle (10px tall, crisp!)
        assert cx + 56 + measure_text(sub, 2, font=FONT_3X5) < cx + cw - 8, f"Sub overflows: {sub}"
        draw_text(rects, sub, cx + 56, cy + 38, 2, c["muted"], font=FONT_3X5)

    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" shape-rendering="crispEdges">\n'
        + "\n".join(rects)
        + "\n</svg>\n"
    )


if __name__ == "__main__":
    os.makedirs("/tmp/gh-profile/assets", exist_ok=True)
    for theme in ("dark", "light"):
        with open(f"/tmp/gh-profile/assets/pixel-banner-{theme}.svg", "w") as f:
            f.write(build_banner(theme))
        with open(f"/tmp/gh-profile/assets/pixel-loadout-{theme}.svg", "w") as f:
            f.write(build_loadout(theme))
    print("Generated 4 integer-grid pixel-art SVGs with overflow assertions passing.")
