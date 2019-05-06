#! /usr/bin/python
from __future__ import division
from fpdf import FPDF
from PIL import Image
import os
import math
from shutil import rmtree

ancho = 0
largo = 0
Origen = "../horno/"
Destino = "../PDF/"
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
def toPDF_allIn1(_Origen, _Destino, _letter):
	global largo
	global ancho
	maxPorHoja = max_cartasPorA4()
	SourceFolder = _Origen 
	pdf = FPDF('P','mm','A4')
	NumImagen = 1
	files = [f for f in os.listdir( SourceFolder) ]
	pdf.add_page()
	for fileName in files:
		if NumImagen == (maxPorHoja +1):
			NumImagen =1
			pdf.add_page()
		x,y = grilla(NumImagen)	 
		pdf.image(SourceFolder  + fileName,x,y,ancho,largo)
		NumImagen = NumImagen+1

	pdf.output(_Destino + "booster"+ _letter + ".pdf", "F")

def toPDF_1PerPage(): 
	global largo
	global ancho
	maxPorHoja = max_cartasPorA4()
	SourceFolder = Origen 
	files = [f for f in os.listdir(SourceFolder) ]
	NumImagen = 1
	numHoja = 1
	for fileName in files:
		if NumImagen == (maxPorHoja +1):
			strhoja = ("000" + str(numHoja))[-3:]
			pdf.output( Destino + strhoja + ".pdf", "F")
			NumImagen =1
			numHoja = numHoja +1
		if NumImagen ==1:
			pdf = FPDF('P','mm','A4')
			pdf.add_page()		
		x,y = grilla(NumImagen)	 
		pdf.image(SourceFolder + "/" + fileName,x,y,ancho,largo)
		NumImagen = NumImagen+1

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
	global largo
	global ancho
	a4Ancho, a4Largo = A4()
	MaxFila = int(math.floor(a4Ancho/ancho))
	MaxColumn = int(math.floor(a4Largo/largo))
	return MaxFila*MaxColumn

def main(gen, letter):
	global largo
	global ancho
	ancho, largo = Magic_Size()
	Origen = "horno/" + gen + "/seleccion/"
	Destino = "horno/" + gen + "/PDF/"
	try:
		os.mkdir(Destino)
	except:
		print("")
	toPDF_allIn1(Origen, Destino, letter)
#toZip()
