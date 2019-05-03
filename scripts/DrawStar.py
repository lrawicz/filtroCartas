import os, random, math, shutil

from PIL import Image, ImageDraw, ImageFont


mydir = "../FIM/"
letrasBooster= "X" 
generacion= "'02"
watermark = letrasBooster + generacion

filelist = [ f for f in os.listdir(mydir) if f.endswith(".png") ]

for card in filelist:

	base = Image.open(mydir +  card ).convert('RGBA')
	width, height = base.size
	y = height*9/80 # arriba
	x = 25
	inicioX = x + 46
	inicioY = y +5 
	inicioX = x + 48
	inicioY = y +5

	txt = Image.new('RGBA', base.size, (255,255,255,0))
	fnt = ImageFont.truetype('/usr/share/fonts/truetype/freefont/MatrixRegularSmallCaps.ttf', 35) # abajo = 20
	d = ImageDraw.Draw(txt)

	angle = 36
	distance = 10
	X1 = inicioX 
	X2 = distance + X1
	X3 = distance*math.cos(math.radians(angle*8)) + X2
	X4 = distance*math.cos(math.radians(angle*2)) + X3
	X5 = distance*math.cos(math.radians(angle*0)) + X4
	X6 = distance*math.cos(math.radians(angle*4)) + X5
	X7 = distance*math.cos(math.radians(angle*2)) + X6
	X8 = distance*math.cos(math.radians(angle*6)) + X7
	X9 = distance*math.cos(math.radians(angle*4)) + X8
	X10 = distance*math.cos(math.radians(angle*8)) + X9
	X11 = distance*math.cos(math.radians(angle*6)) + X10
	Y1 = inicioY + (distance*1/2)
	Y2 = Y1
	Y3 = distance*math.sin(math.radians(angle*8)) + Y2
	Y4 = distance*math.sin(math.radians(angle*2)) + Y3
	Y5 = distance*math.sin(math.radians(angle*0)) + Y4
	Y6 = distance*math.sin(math.radians(angle*4)) + Y5
	Y7 = distance*math.sin(math.radians(angle*2)) + Y6
	Y8 = distance*math.sin(math.radians(angle*6)) + Y7
	Y9 = distance*math.sin(math.radians(angle*4)) + Y8
	Y10 = distance*math.sin(math.radians(angle*8)) + Y9
	Y11 = distance*math.sin(math.radians(angle*6)) + Y10

	if (True == True):
		d.polygon(( \
		X1 , Y1, \
		X2 , Y2, \
		X3 , Y3,  \
		X4, Y4, \
		X5, Y5, \
		X6, Y6, \
		X7, Y7, \
		X8, Y8, \
		X9, Y9, \
		X10, Y10, \
		X11, Y11 \
		), \
		fill = 'red', outline ='black')
	#txt = txt.rotate(45)


	d.text((x,y), watermark , font=fnt, fill='white')
	out = Image.alpha_composite(base, txt)
	#out.show()
	newFileName = str("000") + "01" + ".png"
	print(card)
	out.save("../output/FIM/" + card )



	#X=distance*cos(angle)
	#Y=distance*sin(angle)
#primera estrella
