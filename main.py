import json 

from scripts import GeneratePoolFromCSV
from scripts import makebooster
from scripts import makePDF


PoolTest = ["LOB", "LOB"]

Pool02 = "LOB,MRD,SRL,PSV,TP1,TP2,SDY,SDK"
Pool03="LON,LOD,PGD,MFC,DCR,TP3,TP4,SDJ,SDP"
PoolCustom="LOB,LOB,LON"

ALLin=Pool02 + Pool03


###### Editar
##with open('config.json') as data_file:    
#    data = json.load(data_file)
#exit()
code = "03"
pool = Pool03
boosterDef = ["UR","SR","SR","R","R","R","C","C","C"]
cantidadJugadores = 5
drafteos = 5
letraInicial = "A"



csv = "DB/CSV/" + "DB Yugi - DB_Draft.csv"
CodeFolder =  "horno/" + code
###### 

pool = pool.replace(" ","")




fromDir = CodeFolder + "/pool/"
toDir =  CodeFolder + "/seleccion/"
letter = letraInicial


print("filtrando cartas")
GeneratePoolFromCSV.main(csv,"DB/RAW/",CodeFolder,pool)

for x in xrange(0,drafteos):
	print("seleccion de cartas:" + letter)
	makebooster.main(fromDir,toDir, code, letter, cantidadJugadores, boosterDef )
	print("Armado de PDF:" + letter)
	makePDF.main(code,letter)
	letter = chr(ord(letter) + 1)
	