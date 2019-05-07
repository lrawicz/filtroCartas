import json 

from scripts import GeneratePoolFromCSV
from scripts import makebooster
from scripts import makePDF


PoolTest = ["LOB", "LOB"]

Pool02 = "LOB,MRD,SRL,PSV,TP1,TP2,SDY,SDK"
Pool03="LON,LOD,PGD,MFC,DCR,TP3,TP4,SDJ,SDP"
PoolCustom="LOB,LOB,LON"

ALLin=Pool02 + Pool03


with open('config.json') as json_file:  
    data = json.load(json_file)
#    for p in data['config']:
#		code = p['code']
 #       print('code: ' + code)
 #       csv = "DB/CSV/" + p['csv']
 #       print("csv: " +  csv)
 #       jugadores =  p['jugadores']
 ##       letraInicial = p['letraInicial']
 #       drafteos = p['drafteos']
 #       print('boosters: ' + p['boosters'])
 #       print('')
poolUsado = data["pools"][data["poolUsado"]]
poolUsado = poolUsado.replace(" ","")

csv = "DB/CSV/" + data["csv"]
code = data["code"]
letter = data["letraInicial"]
cantidadJugadores = data["jugadores"]
boosterDef = data["boosterDef"]
drafteos = data["drafteos"]



###### Editar
##with open('config.json') as data_file:    
#    data = json.load(data_file)
#exit()




csv = "DB/CSV/" + "DB Yugi - DB_Draft.csv"
CodeFolder =  "horno/" + code
###### 






fromDir = CodeFolder + "/pool/"
toDir =  CodeFolder + "/seleccion/"

print(poolUsado)
print("filtrando cartas")
GeneratePoolFromCSV.main(csv,"DB/RAW/",CodeFolder,poolUsado)

for x in xrange(0,drafteos):
	print("seleccion de cartas:" + letter)
	makebooster.main(fromDir,toDir, code, letter, cantidadJugadores, boosterDef )
	print("Armado de PDF:" + letter)
	makePDF.main(code,letter)
	letter = chr(ord(letter) + 1)
	