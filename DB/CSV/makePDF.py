from __future__ import division
from fpdf import FPDF
from PIL import Image
import os
import math


ancho = 63
largo = 88

def test():
	files = [f for f in os.listdir('/home/lrawicz/develop/code/yg/') if os.path.isfile(f)]
	for f in files:
		print f	 

def main():

	pdf = FPDF('P','mm','A4')

	pdf.add_page()
	x,y = grilla(4)
	pdf.image("RAW/10000001.png",x,y,ancho,largo)
	x,y = grilla(5)
	pdf.image("RAW/10000001.png",x,y,ancho,largo)
	x,y = grilla(6)
	pdf.image("RAW/10000001.png",x,y,ancho,largo)
	fila= 1
	columna = 2

	pdf.output("yourfile.pdf", "F")



def grilla(Number):
    d = dict();
    d['fila'] = int(math.ceil(Number/3))
    d['columna']   = Number%3
    if d['columna'] == 0:
        d['columna'] = 3
    d['x'] = ((d['columna']-1) * int(ancho)) +10
    d['y'] = ((d['fila']-1) * int(largo)) + 10
    return d['x'], d['y'] 
	


test()