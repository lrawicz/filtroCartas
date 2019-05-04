import GeneratePoolFromCSV
import makebooster
import makePDF
code = "03"
csv = "../DB/CSV/DB Yugi - DB_Draft.csv"
CodeFolder =  "../horno/" + code

PoolTest = ["LOB", "LOB"]

Pool02 = "LOB, MRD, SRL, PSV, TP1, TP2, SDY, SDK"
Pool03 = "LON, LOD, PGD, MFC, DCR, TP3, TP4, SDJ, SDP"
PoolCustom = ["LOB", "LOB"]
GeneratePoolFromCSV.main(csv,CodeFolder,PoolTest)


fromDir = CodeFolder + "/pool/"
toDir =  CodeFolder + "/seleccion/"
letter = "A"

makebooster.main(fromDir,toDir, code, letter)

makePDF.main(code,letter)
