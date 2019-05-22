import json 

from scripts import GeneratePoolFromCSV
from scripts import makebooster2
from scripts import makePDF

import re 
import sys
import os
from shutil import rmtree
from shutil import copyfile
def createFolder(_dir2):
	try:
		rmtree(_dir2)
	except:
		print("")
	os.mkdir(_dir2)
def CleanFolder(_dir):



	createFolder(_dir);
	createFolder(_dir+ "/pool/");
def main():

	with open('config.json') as json_file:  
	    data = json.load(json_file)



	csv = "DB/CSV/" + data["csv"]
	Seleccion = data["Seleccion"].split(",")
	waterMark = data["WaterMark"].split(",")
	rarity = data["Rarity"].split(",")

	proyect = "prueba"
	_from = "DB/RAW/"
	_to = "horno/"+ proyect + "/seleccion/"
	_to2 = "horno/"+ proyect + "/PDF"
	createFolder("horno/"+ proyect)
	createFolder(_to)
	createFolder(_to2)

	for x in xrange(0,len(Seleccion)):
		src = _from + Seleccion[x] + ".png"
		dst = _to + Seleccion[x] + ".png"
	
		if (waterMark[x] == "[DB]"):
			textfile = open(csv, 'r')
			filetext = textfile.read()
			palabra = re.findall(Seleccion[x] + ".*\\n", filetext) [0]
			palabra = palabra.split(",")[1]
		else:
			palabra = waterMark[x]
		makebooster2.Watermark(palabra,rarity[x],1,src,dst)
		
	makePDF.main(proyect,"A" )


main()