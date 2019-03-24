import sys
import os
import csv
from shutil import copyfile

count = 0
csvFile = "../CSV/DB Yugi - DB'02.csv"
with open(csvFile, 'rb') as f:
    reader = csv.reader(f)
    your_list = list(reader)
for card in your_list:#
	RAWFile = card[0]
	rareza = card[1]
	typeCard = card[9]
	
	subtitulo = "E'02" + rareza 
	Path = "../output/BoosterE-pool/"
	src = "../RAW/"+ RAWFile +".png"

	dst = Path  + rareza+ "/" + typeCard + RAWFile +".png"
	count = count +1
	try:
		if(rareza != "#N/A"):
			#print (subtitulo)
			if not os.path.exists(Path + rareza):
				os.makedirs(Path + rareza)
			copyfile(src, dst)
	except:
  		print("Problem with:" + RAWFile) 
  		print("src:" + src) 
  		print("dst:" + dst) 
  		print(typeCard)
print(count)