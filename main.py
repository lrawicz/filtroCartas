import json 

from scripts import GeneratePoolFromCSV
from scripts import makebooster2
from scripts import makePDF

import sys
import os
from shutil import rmtree
from shutil import copyfile

def CleanFolder(_dir):
	def createFolder(_dir2):
		try:
			rmtree(_dir2)
		except:
			print("")
		os.mkdir(_dir2)


	createFolder(_dir);
	createFolder(_dir+ "/pool/");




with open('config.json') as json_file:  
    data = json.load(json_file)
poolUsado = data["pools"][data["poolUsado"]]
poolUsado = poolUsado.replace(" ","")
csv = "DB/CSV/" + data["csv"]
code = data["code"]
letter = data["letraInicial"]
cantidadJugadores = data["jugadores"]
boosterDef = data["boosterDef"]
drafteos = data["drafteos"]

CodeFolder =  "horno/" + code

fromDir = CodeFolder + "/pool/"
toDir =  CodeFolder + "/seleccion/"

print(poolUsado)
print("filtrando cartas")



#Normal
#Special
print(data["poolUsado"])

CleanFolder(CodeFolder)


if(data["poolUsado"] == "Custom"):
	sets = poolUsado.split(",")
	for x in xrange(0,cantidadJugadores):


		rmtree(CodeFolder + "/pool/")
		os.mkdir(CodeFolder + "/pool/")

		print("cantidad jugadores" + str(cantidadJugadores))
		GeneratePoolFromCSV.main(csv,"DB/RAW/",CodeFolder,sets[x])
	#2
		print("seleccion de cartas:" + letter)
		oficialSet = []
		oficialSet.append(sets[x])
		makebooster2.main(fromDir,toDir, code, letter + str(x), 1, boosterDef,1 )
	#3
		print("Armado de PDF:" + letter)
		makePDF.main(code,letter + str(x))
	#change letter
		letter = chr(ord(letter) + 1)
		
else:
	GeneratePoolFromCSV.main(csv,"DB/RAW/",CodeFolder,poolUsado)

	for x in xrange(0,drafteos):
	#2
		print("seleccion de cartas:" + letter)
		makebooster2.main(fromDir,toDir, code, letter, cantidadJugadores, boosterDef,0 )
	#3
		print("Armado de PDF:" + letter)
		makePDF.main(code,letter)
	#change letter
		letter = chr(ord(letter) + 1)
		
