import os, random, math, shutil


fromDir = "../output/BoosterE-pool/"
toDir =  "../output/boosterE-seleccion/"

letrasBooster= "X" 
generacion= "'02"


filelist = [ f for f in os.listdir(toDir) if f.endswith(".png") ]

for f in filelist:
    os.remove(os.path.join(toDir, f))
    print("remove")


#try: 
#	shutil.rmtree('../output/example')
#except:
#	print("el folder no existe")
#os.makedirs('../output/example')

watermark = letrasBooster + generacion

typeCard = ["UR","SR","SR","R","R","R","C","C","C",
			"UR","SR","SR","R","R","R","C","C","C",
			"UR","SR","SR","R","R","R","C","C","C",
			"UR","SR","SR","R","R","R","C","C","C",
			"UR","SR","SR","R","R","R","C","C","C"		
			]
booster = []

for TC in typeCard:
	booster.append(random.choice(os.listdir(fromDir + TC)))

#booster = ["Spell Card72302403.png","Flip Effect Monster62121.png",
#			"Spell Card42703248.png","Normal Monster66672569.png",
#			"Spell Card18161786.png","Spell Card19159413.png",
#			"Effect Monster29155212.png","Normal Monster20277860.png",
#			"Normal Monster20277860.png",]

from PIL import Image, ImageDraw, ImageFont

count  = 0
for card in booster:
	base = Image.open('../output/final/'+typeCard[count]+'/' +  str(card) ).convert('RGBA')
	width, height = base.size

	# make a blank image for the tex, initialized to transparent text color
	txt = Image.new('RGBA', base.size, (255,255,255,0))

	# get a font
	fnt = ImageFont.truetype('/usr/share/fonts/truetype/freefont/MatrixRegularSmallCaps.ttf', 35) # abajo = 20
	# get a drawing context
	d = ImageDraw.Draw(txt)
	
	y = height*9/80 # arriba
	x = 25
	# arriba
	#x = width*35/40
	# draw text
	#d.rectangle([(x, y), (x+80, y+20)], fill=(0,0,0,255), outline=None)
	words = card.split(" ")
	words[0]
	if (words[0] == "Spell" or words[0] == "Trap"):
		color = 255
	else:
		color = 0
	d.text((x,y), watermark , font=fnt, fill=(color,color,color,255))
	diametro = 20
	inicioX = x + 48
	inicioY = y +5 
	if typeCard[count] == "C":
		d.ellipse((inicioX, inicioY, inicioX +diametro, inicioY + diametro), fill = 'grey', outline ='black')
	if typeCard[count] == "R":
		d.rectangle((inicioX, inicioY , \
			inicioX +diametro, inicioY + diametro), fill = 'green', outline ='black')
	
	distanceX = 20
	distanceY = 40



	if typeCard[count] == "SR":
		d.polygon(( \
		inicioX , inicioY + diametro/2, \
		 inicioX + distanceX/2, inicioY , \
		 inicioX + distanceX, inicioY + diametro/2, \
		 inicioX + distanceX/2, inicioY + distanceY/2), \
		 	 fill = 'gold', outline ='black')
	#X=distance*cos(angle)
	#Y=distance*sin(angle)
#primera estrella
	angle = 36
	distance = 20
	X1 = inicioX 
	X2 = distance + X1
	X3 = distance*math.cos(math.radians(angle*4)) + X2
	X4 = distance*math.cos(math.radians(angle*8)) + X3
	X5 = distance*math.cos(math.radians(angle*2)) + X4
	X6 = distance*math.cos(math.radians(angle*6)) + X5
	Y1 = inicioY + (distance*1/2)
	Y2 = Y1
	Y3 = distance*math.sin(math.radians(angle*4)) + Y2
	Y4 = distance*math.sin(math.radians(angle*8)) + Y3
	Y5 = distance*math.sin(math.radians(angle*2)) + Y4
	Y6 = distance*math.sin(math.radians(angle*6)) + Y5

#segunda estrella

	if typeCard[count] == "UR":
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


	out = Image.alpha_composite(base, txt)
	#out.show()
	newFileName = str("00") + str(count+1) + ".png"
	print(newFileName[-7:])
	out.save(toDir + newFileName[-7:] )
	count  = count +1
