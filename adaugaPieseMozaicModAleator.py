#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 14:38:30 2018

@author: gabriel
"""

from params import params
import random
import numpy as np
import cv2

def adaugaPieseMozaicModAleator():
	#caracter necesar afisarii progresului in timp real
	backspace = '\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b' 
	
	h = params.dimVertPiesa
	w = params.dimOrPiesa
	
	if params.imagineColor:
		#3 canale
		imgMozaic = np.empty((params.dimVertRdImg + h - 1, params.dimOrRdImg + w - 1, 3), np.uint8)
	else:
		#1 singur canal
		imgMozaic = np.empty((params.dimVertRdImg + h - 1, params.dimOrRdImg + w - 1), np.uint8)
		
	pixelLiber = np.ones((params.dimVertRdImg, params.dimOrRdImg), np.bool_)
	
	if params.criteriu == 'distantaCuloareMedie':
		#calculeaza media tuturor pieselor
		calculeazaMediiPieseMozaic()
	
	for nrPieseAdaugate in range(params.nrTotalPiese):		
		for incercare in range(round(params.nrTotalPiese/10)):
			iStart = random.randint(0, params.dimVertRdImg - 1)
			jStart = random.randint(0, params.dimOrRdImg - 1)
			if(pixelLiber[iStart, jStart] == 1):
				pixelLiber[iStart, jStart] = 0
				break;
		else:
			break;
		
		if params.criteriu == 'aleator':
			#pune o piese aleatoare in mozaic, nu tine cont de nimic
			indice = random.randint(0, params.numarPiese-1)
		elif params.criteriu == 'distantaCuloareMedie':
			
			if params.imagineColor:
				#selecteaza urmatorul carou(de dimensiunea unei piese si cu 3 canale)
				img = params.imgReferintaRedimensionata[iStart : iStart + h, jStart : jStart + w, :]
				#calculeaza media imaginii pentru fiecare canal
				b, g, r, _ = cv2.mean(img)
				medieCarou = np.array((b , g, r), np.dtype(float))	
			else:
				#selecteaza urmatorul carou(de dimensiunea unei piese si cu 1 canal)
				img = params.imgReferintaRedimensionata[iStart : iStart + h, jStart : jStart + w]
				#calculeaza media imaginii						
				intensitate = cv2.mean(img)
				medieCarou = np.array((intensitate,), np.dtype(float))
			
			#gaseste indicele piesei cu distanta euclidiana minima fata de media caroului
			indice = calculeazaDistantaEuclidiana(medieCarou) 
		
		if params.imagineColor:
			imgMozaic[iStart : iStart + h, jStart : jStart + w, :] = params.pieseMozaic[indice]
		else:
			imgMozaic[iStart : iStart + h, jStart : jStart + w] = params.pieseMozaic[indice]
				  
		print(backspace + 'Construim mozaic ... %.2f' % (100*nrPieseAdaugate/params.nrTotalPiese) + '%', end='\r')				

	return imgMozaic[:params.dimVertRdImg, :params.dimOrRdImg]
 
    
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

		
def calculeazaDistantaEuclidiana(medieCarou):#intoarce primele 3 distante?
	lisDis = []
	for i in range(params.numarPiese):
		#calcueaza distanta euclidiana dintre carou si piesa i
		dist = np.linalg.norm(medieCarou-params.mediiPieseMozaic[i])
		#adauga distanta impreuna cu indicele piesei in lista lisDis
		lisDis.append((i, dist))
		#gaseste distanta minima din lista
	
	minDis = min(lisDis, key = lambda t: t[1])
	#returneaza indicele acesteia
	return minDis[0]