#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 14:38:06 2018

@author: gabriel
"""
from params import params
import random
import numpy as np
import cv2

def adaugaPieseMozaicPeCaroiaj():
	#caracter necesar afisarii progresului in timp real
	backspace = '\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b' 
	
	h = params.dimVertPiesa
	w = params.dimOrPiesa
	
	nrTotalPiese = params.numarPieseMozaicOrizontala * params.numarPieseMozaicVerticala
	nrPieseAdaugate = 0
	
	if params.pieseAdiacenteDiferite:	
		indicePiesaMozaic = np.empty((params.numarPieseMozaicVerticala, params.numarPieseMozaicOrizontala), np.int16)
	
	if params.imagineColor:
		#3 canale
		imgMozaic = np.empty((params.dimVertRdImg, params.dimOrRdImg, 3), np.uint8)
	else:
		#1 singur canal
		imgMozaic = np.empty((params.dimVertRdImg, params.dimOrRdImg), np.uint8)
		
	if params.criteriu == 'distantaCuloareMedie':
		#calculeaza media tuturor pieselor
		calculeazaMediiPieseMozaic()
		
	for i in range(params.numarPieseMozaicVerticala):
		for j in range(params.numarPieseMozaicOrizontala):
				
				if params.criteriu == 'aleator':
					#pune o piese aleatoare in mozaic, nu tine cont de nimic
					indice = random.randint(0, params.numarPiese-1)
				elif params.criteriu == 'distantaCuloareMedie':
				
					if params.imagineColor:
						#selecteaza urmatorul carou(de dimensiunea unei piese si cu 3 canale)
						img = params.imgReferintaRedimensionata[i*h:(i+1)*h, j*w:(j+1)*w, :]
						#calculeaza media imaginii pentru fiecare canal
						b, g, r, _ = cv2.mean(img)
						medieCarou = np.array((b , g, r), np.dtype(float))	
					else:
						#selecteaza urmatorul carou(de dimensiunea unei piese si cu 1 canal)
						img = params.imgReferintaRedimensionata[i*h:(i+1)*h, j*w:(j+1)*w]
						#calculeaza media imaginii						
						intensitate = cv2.mean(img)
						medieCarou = np.array((intensitate,), np.dtype(float))
					
					if params.pieseAdiacenteDiferite:				
						if(i):	
							indiceVecinSus = indicePiesaMozaic[i-1, j] 
						else:
							indiceVecinSus = -1#nu exista vecin sus
						if(j):
							indiceVecinStanga =	indicePiesaMozaic[i, j-1]
						else:
							indiceVecinStanga = -1#nu exista vecin in stanga
						#gaseste 3 indici ale pieselor cu distanta euclidiana minima fata de media caroului
						topIndici = calculeazaDistantaEuclidiana(medieCarou) 
						
						indice = alegeIndice(indiceVecinSus, indiceVecinStanga, topIndici)
						
						indicePiesaMozaic[i, j] = indice
					else:
						#gaseste indicele piesei cu distanta euclidiana minima fata de media caroului
						indice = calculeazaDistantaEuclidiana(medieCarou) 
					
				if params.imagineColor:
					imgMozaic[i*h:(i+1)*h, j*w:(j+1)*w, :] = params.pieseMozaic[indice]
				else:
					imgMozaic[i*h:(i+1)*h, j*w:(j+1)*w] = params.pieseMozaic[indice]
				
				nrPieseAdaugate += 1				  
				print(backspace + 'Construim mozaic ... %.2f' % (100*nrPieseAdaugate/nrTotalPiese) + '%', end='\r')				

	return imgMozaic
 
    
def calculeazaMediiPieseMozaic():
	for i in range(params.numarPiese):
		img = params.pieseMozaic[i]
		if params.imagineColor:
			#calculeaza media imaginii
			b, g, r, _ = cv2.mean(img) 
			mediePiesa = np.array((b, g, r), np.dtype(float))
		else:
			#calculeaza media imaginii
			intensitate = cv2.mean(img) 
			mediePiesa = np.array((intensitate,), np.dtype(float))	
		#adauga media la lista de medii
		params.mediiPieseMozaic.append(mediePiesa)

		
def calculeazaDistantaEuclidiana(medieCarou):
	lisDis = []
	for i in range(params.numarPiese):
		#calcueaza distanta euclidiana dintre carou si piesa i
		dist = np.linalg.norm(medieCarou-params.mediiPieseMozaic[i])
		#adauga distanta impreuna cu indicele piesei in lista lisDis
		lisDis.append((i, dist))
	
	if params.pieseAdiacenteDiferite:
		#returneaza indicii celor mai mici 3 distante din lista
		srtIndici = sorted(lisDis, key = lambda t: t[1])[:3]
		ind1 = srtIndici[0][0]
		ind2 = srtIndici[1][0]
		ind3 = srtIndici[2][0]
		return [ind1, ind2, ind3]
	else:
		#gaseste distanta minima din lista
		minDis = min(lisDis, key = lambda t: t[1])
		#returneaza indicele acesteia
		return minDis[0]

#alege indicele piesei optime care difera de vecini
def alegeIndice(indiceVecinSus, indiceVecinStanga, topIndici):
	if topIndici[0] != indiceVecinSus and topIndici[0] != indiceVecinStanga:
		return topIndici[0]
	elif topIndici[1] != indiceVecinSus and topIndici[1] != indiceVecinStanga:
		return topIndici[1]
	else:
		return topIndici[2]