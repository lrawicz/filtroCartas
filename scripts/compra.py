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
	txt = Image.new('RGBA', base.size, (255,255,255,0))
	d = ImageDraw.Draw(txt)
	#d.text((x,y), "COMPRA" , font=fnt1, fill='black')
	d.text((x,y), "COMPRA" , font=fnt2, fill='black')
	out = Image.alpha_composite(base, txt)
	out.save(mydir + "test.png" )