import os, random, math, shutil
from PIL import Image, ImageDraw, ImageFont

mydir = "../compra/"
filelist = [ f for f in os.listdir(mydir) if f.endswith(".png") ]
for f in filelist:
	base = Image.open(mydir +'/' +  f ).convert('RGBA')
	fnt1 = ImageFont.truetype('/usr/share/fonts/truetype/freefont/MatrixRegularSmallCaps.ttf', 36) # abajo = 20
	fnt2 = ImageFont.truetype('/usr/share/fonts/truetype/freefont/MatrixRegularSmallCaps.ttf', 35) # abajo = 20
	width, height = base.size
	y = height*9/80 # arriba
	x = 25
	
	rgb_im = base.convert('RGB')
	r, g, b = rgb_im.getpixel((20, 20))
	color = 0
	watermark = Image.new('RGBA', base.size, (255,255,255,0))
	d = ImageDraw.Draw(watermark)
	if (r, g, b) == (5,141,121) or (r, g, b) == (167,27,114):
		print("Spell or Trap")
		print(r, g, b)
		d.text((x,y), "COMPRA" , font=fnt1, fill='white')
		color = 255
	else:
		d.text((x,y), "COMPRA" , font=fnt1, fill='black')

	#d.text((x,y), "COMPRA" , font=fnt2, fill='black')
	out = Image.alpha_composite(base, watermark)
	out.save(mydir + "/output/"+ f )