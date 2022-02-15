#!/usr/bin/env python3
import pathlib, fontforge

FONT_NAME = "jsrf"
FONT_NAME_TITLE = FONT_NAME.title()
FONT_STYLE = "regular"
FONT_FULL = f"{FONT_NAME_TITLE}-{FONT_STYLE.title()}"

font = fontforge.font()

font.ascent     = 96
font.descent    = 32
font.em         = 128
font.encoding   = "UnicodeFull"
font.familyname = FONT_NAME_TITLE
font.fontname   = FONT_FULL
font.fullname   = FONT_FULL

glyph_data = {
  32:  { "width": 80 },  # <space>
  33:  { "width": 20 },  # !
  34:  { "width": 20 },  # "
  35:  { "width": 20 },  # #
  36:  { "width": 20 },  # $
  37:  { "width": 20 },  # %
  38:  { "width": 20 },  # &
  39:  { "width": 20 },  # '
  40:  { "width": 20 },  # (
  41:  { "width": 20 },  # )
  42:  { "width": 20 },  # *
  43:  { "width": 20 },  # +
  44:  { "width": 20 },  # ,
  45:  { "width": 20 },  # -
  46:  { "width": 30 },  # .
  47:  { "width": 20 },  # /
  48:  { "width": 20 },  # 0
  49:  { "width": 20 },  # 1
  50:  { "width": 20 },  # 2
  51:  { "width": 20 },  # 3
  52:  { "width": 20 },  # 4
  53:  { "width": 20 },  # 5
  54:  { "width": 20 },  # 6
  55:  { "width": 20 },  # 7
  56:  { "width": 20 },  # 8
  57:  { "width": 20 },  # 9
  58:  { "width": 20 },  # :
  59:  { "width": 20 },  # ;
  60:  { "width": 20 },  # <
  61:  { "width": 20 },  # =
  62:  { "width": 20 },  # >
  63:  { "width": 40 },  # ?
  64:  { "width": 20 },  # @
  65:  { "width": 20, "right": -10, "left": 15 },  # A
  66:  { "width": 20, "right": -10 },  # B
  67:  { "width": 20, "right": -10 },  # C
  68:  { "width": 20, "right": -10 },  # D
  69:  { "width": 20, "right": -10 },  # E
  70:  { "width": 20, "right": -10 },  # F
  71:  { "width": 20, "right": -10 },  # G
  72:  { "width": 20, "right": -10 },  # H
  73:  { "width": 20, "right": -5  },  # I
  74:  { "width": 20, "right": -10 },  # J
  75:  { "width": 20, "right": -10 },  # K
  76:  { "width": 20, "right": 0 },  # L
  77:  { "width": 20, "right": -10 },  # M
  78:  { "width": 20, "right": -10 },  # N
  79:  { "width": 20, "right": -15 },  # O
  80:  { "width": 20, "right": -10 },  # P
  81:  { "width": 20, "right": -10 },  # Q
  82:  { "width": 20, "right": -10 },  # R
  83:  { "width": 20, "right": -10 },  # S
  84:  { "width": 20, "right": -10 },  # T
  85:  { "width": 20, "right": -10 },  # U
  86:  { "width": 20, "right": -10, "left": 25 },  # V
  87:  { "width": 20, "right": -10 },  # W
  88:  { "width": 20, "right": -10 },  # X
  89:  { "width": 20, "right": -10, "left": 15 },  # Y
  90:  { "width": 20, "right": -10 },  # Z
  91:  { "width": 20 },  # [
  93:  { "width": 20 },  # ]
  94:  { "width": 20 },  # ^
  95:  { "width": 20 },  # _
  96:  { "width": 20 },  # `
  97:  { "width": 20 },  # a
  98:  { "width": 20 },  # b
  99:  { "width": 20, "right": -5 },  # c
  100: { "width": 20, "right": -10 },  # d
  101: { "width": 20 },  # e
  102: { "width": 20, "right": -15 },  # f
  103: { "width": 20 },  # g
  104: { "width": 20 },  # h
  105: { "width": 20 },  # i
  106: { "width": 20 },  # j
  107: { "width": 20 },  # k
  108: { "width": 20 },  # l
  109: { "width": 20 },  # m
  110: { "width": 20 },  # n
  111: { "width": 20 },  # o
  112: { "width": 20 },  # p
  113: { "width": 20 },  # q
  114: { "width": 20 },  # r
  115: { "width": 20 },  # s
  116: { "width": 20 },  # t
  117: { "width": 20 },  # u
  118: { "width": 20 },  # v
  119: { "width": 20 },  # w
  120: { "width": 20, "left": 0 },  # x
  121: { "width": 20 },  # y
  122: { "width": 20 },  # z
}

for svg in pathlib.Path('svg').iterdir():
  codepoint = int(svg.name.partition('.')[0])
  char_literal = chr(codepoint)
  glyph = font.createChar(codepoint, char_literal)
  glyph.importOutlines(str(svg))
  glyph.removeOverlap()
  # glyph.transform((1,0,0,1,0,20))
  this_glyph_data = glyph_data[codepoint]
  glyph.width              = this_glyph_data.pop('width', 80)
  glyph.left_side_bearing  = this_glyph_data.pop('left',  glyph.width // 2)
  glyph.right_side_bearing = this_glyph_data.pop('right', glyph.width // 2)

  for k,v in this_glyph_data.items():
    if hasattr(glyph, k):
      setattr(glyph, k, v)

    glyph.simplify(
      0.1,
      (
        # "ignoreslopes",        # Allow slopes to change
        # "ignoreextrema",       # Allow removal of extrema
        # "smoothcurves",
        # "choosehv",              # Snap to horizontal or vertical
        "forcelines",            # flatten bumps on lines
        # "nearlyhvlines",         # Make nearly horizontal/vertical lines be so
        # "mergelines",            # Merge adjacent lines into one
        "setstarttoextremum",    # Rotate the point list so that the start point is on an extremum
        "removesingletonpoints", # If the contour contains just one point then remove it
      )
    )


for ext in [ "woff2", "woff", "ttf" ]:
  font_file = f"{FONT_NAME}.{ext}"
  font.generate(font_file)
  print(f"Generated {font_file}")