from PIL import Image
from PIL import ImageDraw

import math

res = 256

img = Image.new("RGBA", (res, res), "#00000000")

PINK = "#ffc0cb"
GOLD = "#ffe600"
RED = "#bf3100"
LIGHT_EARTHY_GREEN = "#aeb999"
DARK_FOREST_GREEN = "#204f00"

draw = ImageDraw.Draw(img)
# FRAME OUTLINE
draw.ellipse(
	[0, 0, res, res],
	DARK_FOREST_GREEN,
	DARK_FOREST_GREEN,
	0)

# MANTLE
draw.ellipse(
	[(res/16, res/16), ((res/16)*15, (res/16)*15)],
	LIGHT_EARTHY_GREEN,
	PINK,
	int(res/32))

# 3
draw.ellipse(
	[(res/2)-(res/4), (res/2)-(res/4), (res/2)+(res/4), (res/2)+(res/4)],
	PINK,
	PINK,
	0)

img.save("icon.png")
