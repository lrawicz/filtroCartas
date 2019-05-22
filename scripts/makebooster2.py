import os, random, math, shutil
from shutil import rmtree
from PIL import Image, ImageDraw, ImageFont

def Watermark(word,rarity,special,imageSrc,destino):
	
	base = Image.open(imageSrc ).convert('RGBA')
	width, height = base.size
	capa2 = Image.new('RGBA', base.size, (255,255,255,0))
	fnt = ImageFont.truetype('/usr/share/fonts/truetype/freefont/MatrixRegularSmallCaps.ttf', 35) # abajo = 20
	y = height*9/80 # arriba
	x = 25
	draw2 = ImageDraw.Draw(capa2)

	#rarity
	diametro = 20
	inicioX = x + 48
	inicioY = y +5

	if(rarity == "C"):
		draw2.ellipse((inicioX, inicioY, inicioX + diametro, inicioY + diametro), fill = 'grey', outline ='black')
	if(rarity == "R"):
		draw2.rectangle((inicioX, inicioY , \
		inicioX +diametro, inicioY + diametro), fill = 'green', outline ='black')
	if(rarity == "SR"):
		distanceX = 20
		distanceY = 40
		draw2.polygon(( \
		inicioX , inicioY + diametro/2, \
		inicioX + distanceX/2, inicioY , \
		inicioX + distanceX, inicioY + diametro/2, \
		inicioX + distanceX/2, inicioY + distanceY/2), \
		fill = 'gold', outline ='black')
	if(rarity == "UR"):
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

			draw2.polygon(( \
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

	#palabra


	rgb_im = base.convert('RGB')
	r, g, b = rgb_im.getpixel((20, 20))
	if (r, g, b) == (5,141,121) or (r, g, b) == (167,27,114):
	#if (words[0] == "Spell" or words[0] == "Trap"):
		C_R = 255
		C_G = 255
		C_B = 255
	else:
		C_R = 0
		C_G = 0
		C_B = 0
	if (special == 1 ):
		#C_R = 0
		#C_G = 153
		#C_B = 0
		C_R = 254
		C_G = 127
		C_B = 156

	draw2.text((x,y), word , font=fnt, fill=(255,255,255,255))

	out = Image.alpha_composite(base, capa2)
	#out.show()
	
	out.save(destino )
	

def main(_from, _to,_code, _letter, _jugadores, _boosterDef, special):
	
	fromDir = _from
	toDir =  _to

	letrasBooster= _letter 
	generacion= "'" + _code


	try:
		os.mkdir(toDir)
	except:
		print("")

	typeCard = []
	watermark = letrasBooster + generacion

	for x in xrange(0,_jugadores):
		typeCard.extend(_boosterDef)


	booster = []

	for TC in typeCard:
		booster.append(random.choice(os.listdir(fromDir + TC)))

	from PIL import Image, ImageDraw, ImageFont

	count  = 0
	for card in booster:
		base = Image.open(fromDir +typeCard[count]+'/' +  str(card) ).convert('RGBA')
		#Watermark(word,rarity,imageSrc,destino)
		watermark= str(card)[:3]
		newFileName = str("00") + str(count+1) + ".png"
		toDir = _to
		destino =  toDir + newFileName[-7:]
		

		print("word:" + str(watermark))
		print("rarity:" + str(typeCard[count]))
		print("special:" + str(special))
		print("src:" + str(fromDir + typeCard[count] + '/' +  str(card)))
		print("destiny:" + str(destino))
		

		Watermark(	watermark \
					,typeCard[count] \
					,special
					,fromDir + typeCard[count] + '/' +  str(card) \
					,destino)
		count  = count +1




#Watermark("ASD","UR","/home/lrawicz/develop/code/yg/DB/RAW/41546.png","/home/lrawicz/develop/code/yg/")