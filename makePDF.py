from __future__ import division
from fpdf import FPDF
from PIL import Image
import os
import math


ancho = 0
largo = 0
def Dominion(): #Euro Estandar
	return 59, 92
def Magic_Size(): #TCG
	return 63, 88
def YuGiOh_Size(): #TCG
	return 60.5, 87.5
def Mini_Euro():
	return  45, 68
def Mini_American(): #Descent.Items
	return  41, 63
def Square(): #FFG.Blue
	return  70, 70
def DescentHero(): 
	return  128,102
def A4():
	return 210,297

def test():
	files = [f for f in os.listdir('./output/example/') ]
	for f in files:
		print f	 	
def main():
	global largo
	global ancho
	maxPorHoja = max_cartasPorA4()
	SourceFolder = "./output/example/"
	pdf = FPDF('P','mm','A4')
	NumImagen = 1
	files = [f for f in os.listdir('./' + SourceFolder) ]
	pdf.add_page()
	for fileName in files:
		print fileName
		x,y = grilla(NumImagen)	 
		pdf.image(SourceFolder + "/" + fileName,x,y,ancho,largo)
		NumImagen = NumImagen+1
		if NumImagen == (maxPorHoja +1):
			NumImagen =1
			pdf.add_page()		

	pdf.output("yourfile.pdf", "F")



def grilla(Number):
    global largo
    global ancho
    a4Ancho, a4Largo = A4()
    #Max = math.floor((A4ancho)/ancho)
    MaxFila = int(math.floor(a4Ancho/ancho))
    fila = int(math.ceil(Number/MaxFila))
    columna   = Number%MaxFila
    if columna == 0:
        columna = MaxFila
    x = ((columna-1) * int(ancho)) +10
    y = ((fila-1) * int(largo)) + 10
    return x, y 
	
def max_cartasPorA4():
	a4Ancho, a4Largo = A4()
	MaxFila = int(math.floor(a4Ancho/ancho))
	MaxColumn = int(math.floor(a4Largo/largo))
	return MaxFila*MaxColumn

	
ancho, largo = Magic_Size()
main()