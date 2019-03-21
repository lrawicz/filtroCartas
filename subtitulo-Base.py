

jugadores = ["Ger","Lean","Eze","Nico","Sansa"]

for jugador in jugadores:
	f = open("CSV/base25.csv", "r")
	cardID = 0	
	for line in f:
		cardID=cardID+1
		card = line.split(",")
		RAWFile = card[2]
		tipoCarta = card[4]
		cardDSHOW = ("00" + str(cardID))
		subtitulo = jugador + "-"+ cardDSHOW[-2:]
		print(tipoCarta)
		from PIL import Image, ImageDraw, ImageFont
		base = Image.open('RAW/' +  str(int(RAWFile)) + '.png').convert('RGBA')
		width, height = base.size

		# make a blank image for the text, initialized to transparent text color
		txt = Image.new('RGBA', base.size, (255,255,255,0))

		# get a font
		fnt = ImageFont.truetype('/usr/share/fonts/truetype/freefont/MatrixRegularSmallCaps.ttf', 35) # abajo = 20
		# get a drawing context
		d = ImageDraw.Draw(txt)

		y = height*19/20 # abajo 
		y = height*9/80 # arriba

		x = 0
		if jugador == "NICO" or jugador == "LEAN":
			x = width*34/40
		if jugador == "SANSA":
			x = width*32/40
		if jugador == "GER" or jugador == "EZE":
			x = width*35/40

		if (tipoCarta.find("Spell") >= 0 or tipoCarta.find("Trap") >= 0):
			color = 255
		else:
			color = 0	
		x = 25
		# arriba
		#x = width*35/40
		# draw text
		#d.rectangle([(x, y), (x+80, y+20)], fill=(0,0,0,255), outline=None)
		d.text((x,y), subtitulo, font=fnt, fill=(color,color,color,255))
		#txt = txt.rotate(45)


		out = Image.alpha_composite(base, txt)
		#out.show()
		out.save("output/base25/"+ subtitulo.rstrip() + ".png")
		
		