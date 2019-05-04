import sys
import os
import csv
from shutil import rmtree
from shutil import copyfile
def main(_csv, _output, _set):
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
	try:
		os.mkdir(output)
	except:
		print("nah")
	n = 0
	with open(csvFile, 'rb') as f:
	    reader = csv.reader(f)
	    your_list = list(reader)
	for card in your_list:#
		n = n+1
		RAWFile = card[1]
		rareza = card[2]
		typeCard = card[10]
		booster = card[3]
		if _set.count(booster)>0 :
			print(booster)
			
			Path = output
			src = srcDB + RAWFile +".png"
			dst = Path  + rareza+ "/" + RAWFile +"-"  
			try:
				if(rareza != "#N/A"):
					if not os.path.exists(Path + rareza):
						os.makedirs(Path + rareza)
					i=0
					while i < _set.count(booster):
						i=i+1
						copyfile(src, dst + str(i) +".png")
			except:
		  		print("Problem with:" + RAWFile) 
		  		print("src:" + src) 
		  		print("dst:" + dst + str(i) +".png") 
		  		print(typeCard)
