import GeneratePoolFromCSV
import makebooster
import makePDF
code = "03"
csv = "../DB/CSV/DB Yugi - DB'" + code + ".csv"
CodeFolder =  "../horno/" + code
GeneratePoolFromCSV.main(csv,CodeFolder)


fromDir = CodeFolder + "/pool/"
toDir =  CodeFolder + "/seleccion/"
letter = "A"

makebooster.main(fromDir,toDir, code, letter)

makePDF.main(code,letter)
