

f = open("CSV/boostersNico.csv", "r")
for line in f:
	card = line.split(",")
	RAWFile = card[5]
	subtitulo = card[6]

	from PIL import Image, ImageDraw, ImageFont
	base = Image.open('RAW/' +  str(int(RAWFile)) + '.png').convert('RGBA')
	width, height = base.size

	# make a blank image for the text, initialized to transparent text color
	txt = Image.new('RGBA', base.size, (255,255,255,0))

	# get a font
	fnt = ImageFont.truetype('/usr/share/fonts/truetype/freefont/MatrixRegularSmallCaps.ttf', 30) # abajo = 20
	# get a drawing context
	d = ImageDraw.Draw(txt)

	y = height*9/80 # arriba
	x = 25
	# arriba
	#x = width*35/40
	# draw text
	#d.rectangle([(x, y), (x+80, y+20)], fill=(0,0,0,255), outline=None)
	d.text((x,y), subtitulo.rstrip(), font=fnt, fill=(255,255,255,255))
	#txt = txt.rotate(45)


	out = Image.alpha_composite(base, txt)
	#out.show()
	out.save("boosterNico/"+ RAWFile.rstrip() + ".png")
	
	