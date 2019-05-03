import sys
import os
import csv
from shutil import rmtree
from shutil import copyfile
def main(_csv, _output):
	srcDB = "../DB/RAW/"
	count = 0
	csvFile = _csv
	output = _output
	try:
		rmtree(output)
	except:
		print("nah")
	os.mkdir(output)
	output = output + "/pool/"

	with open(csvFile, 'rb') as f:
	    reader = csv.reader(f)
	    your_list = list(reader)
	for card in your_list:#
		RAWFile = card[1]
		rareza = card[2]
		typeCard = card[10]
		booster = card[19]
		subtitulo = "'03" + rareza 
		Path = output
		src = srcDB + RAWFile +".png"
		filtrarBoosters= ["PGD", "DCR"]
		dst = Path  + rareza+ "/" + RAWFile +".png"
		try:
			if(rareza != "#N/A" and booster in filtrarBoosters):
				#print (subtitulo)
				if not os.path.exists(Path + rareza):
					os.makedirs(Path + rareza)

				copyfile(src, dst)
				count = count +1
		except:
	  		print("Problem with:" + RAWFile) 
	  		print("src:" + src) 
	  		print("dst:" + dst) 
	  		print(typeCard)
