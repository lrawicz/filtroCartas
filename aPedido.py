import json 

from scripts import GeneratePoolFromCSV
from scripts import makebooster2
from scripts import makePDF

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
	WaterMark = data["WaterMark"]

	_from = "DB/RAW/"
	_to = "horno/prueba/seleccion/"
	_to2 = "horno/prueba/PDF"
	createFolder(_to)
	createFolder(_to2)

	for x in xrange(0,len(Seleccion)):
		src = _from + Seleccion[x] + ".png"
		dst = _to + Seleccion[x] + ".png"
		makebooster2.Watermark("ASD","UR",1,src,dst)
		
	makePDF.main("prueba","A" )

def  conWaterMark():
	with open('config.json') as json_file:  
	    data = json.load(json_file)



	csv = "DB/CSV/" + data["csv"]
	Seleccion = data["Seleccion"].split(",")
	WaterMark = data["WaterMark"]

	_from = "DB/RAW/"
	_to = "horno/prueba/seleccion/"
	_to2 = "horno/prueba/PDF"
	createFolder(_to)
	createFolder(_to2)

	for x in xrange(0,len(Seleccion)):
		src = _from + Seleccion[x] + ".png"
		dst = _to + Seleccion[x] + ".png"
		copyfile(src, dst)
	makePDF.main("prueba","A" )
	

main()