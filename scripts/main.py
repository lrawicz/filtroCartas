from   scripts import GeneratePoolFromCSV
from scripts import makebooster
from  scripts import makePDF
code = "03"
csv = "../DB/CSV/DB Yugi - DB_Draft.csv"
CodeFolder =  "../horno/" + code

PoolTest = ["LOB", "LOB"]

Pool02 = "LOB,MRD,SRL,PSV,TP1,TP2,SDY,SDK"
Pool03="LON,LOD,PGD,MFC,DCR,TP3,TP4,SDJ,SDP"
PoolCustom="LOB,LOB,LON"
ALLin=Pool02 + Pool03


###### Editar

pool = "DCR"
drafteos = 5
letraInicial = "A"

###### 

pool = pool.replace(" ","")



GeneratePoolFromCSV.main(csv,CodeFolder,pool	)


fromDir = CodeFolder + "/pool/"
toDir =  CodeFolder + "/seleccion/"
letter = letraInicial


for x in xrange(0,drafteos):
	print("seleccion de cartas:" + letter)
	makebooster.main(fromDir,toDir, code, letter)
	print("Armado de PDF:" + letter)
	makePDF.main(code,letter)
	letter = chr(ord(letter) + 1)
	