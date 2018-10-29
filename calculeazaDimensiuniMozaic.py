#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 14:32:09 2018

@author: gabriel
"""
import cv2
from params import params

def calculeazaDimensiuniMozaic():
	#calculeaza dimensiunile mozaicului
	#obtine si imaginea de referinta redimensionata avand aceleasi dimensiuni ca mozaicul
	
	#calculam dimensiunile imaginii de referinta 
	params.dimVertImg, params.dimOrImg = params.imgReferinta.shape[:2]
	#calculam dimensiunile pieselor
	params.dimVertPiesa, params.dimOrPiesa = params.pieseMozaic[0].shape[:2]

	#calculeaza automat numarul de piese pe verticala
	scaling = (params.dimOrPiesa * params.numarPieseMozaicOrizontala)/params.dimOrImg
	params.numarPieseMozaicVerticala = round((scaling * params.dimVertImg)/params.dimVertPiesa)
	
	#calculeaza dimensiunile mozaicului/imaginii viitoare redimensionate
	params.dimVertRdImg = params.numarPieseMozaicVerticala * params.dimVertPiesa
	params.dimOrRdImg = params.numarPieseMozaicOrizontala * params.dimOrPiesa
	#redimensioneaza imaginea  
	params.imgReferintaRedimensionata = cv2.resize(params.imgReferinta, (params.dimOrRdImg, params.dimVertRdImg), cv2.INTER_CUBIC) 

	#afiseaza detalii mozaic	
	print('numar piese: ' + str(params.numarPieseMozaicVerticala) + 'x' + str(params.numarPieseMozaicOrizontala))
	print('piesa:       ' + str(params.dimVertPiesa) + 'x' + str(params.dimOrPiesa))
	print('img red:     ' + str(params.dimVertRdImg) + 'x' + str(params.dimOrRdImg))
	print('img ref:     ' + str(params.dimVertImg) + 'x' + str(params.dimOrImg))
	print('scaling:     ' + str(scaling) + '\n')

