#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 21:01:09 2018

@author: gabriel
"""

import cv2

#seteaza parametri pentru functie
class params:
    
	#puteti inlocui numele imaginii
	numeImgReferinta = 'tomJerry'
	tipImagineRef = 'jpeg'
	#1=imagine color, 0=imagine greyscale
	imagineColor = 1
	#citeste imaginea care va fi transformata in mozaic	
	imgReferinta = cv2.imread('/home/gabriel/Spyder Projects/VA/Tema1/data/imaginiTest/' + numeImgReferinta + '.' + tipImagineRef, imagineColor)
	imgReferintaRedimensionata = None
	#seteaza directorul cu imaginile folosite lfa realizarea mozaicului
	numeDirector = '/home/gabriel/Spyder Projects/VA/Tema1/data/colectie'#cifar-10-batches-py/'
	#1/0
	citireCifar10 = 0
	#0/2/.../9    
	clasaCifar = 8
	
	tipImagine = 'png'
	#seteaza numarul de piese din colectie    
	numarPiese = 500
	#seteaza numarul de piese ale mozaicului pe orizontala
	numarPieseMozaicOrizontala = 100
	#numarul de piese ale mozaicului pe verticala va fi dedus automat
	numarPieseMozaicVerticala = None
	#seteaza optiunea de afisare a pieselor mozaicului dupa citirea lor din director
	afiseazaPieseMozaic = 0
	#seteaza modul de aranjare a pieselor mozaicului
	#optiuni: 'caroiaj','aleator'    
	modAranjare = 'caroiaj'
	nrTotalPiese = 100000
	#seteaza criteriul dupa care sa se realizeze mozaicul
	#optiuni: 'aleator','distantaCuloareMedie'	
	criteriu = 'distantaCuloareMedie'
	
	#1/0
	pieseAdiacenteDiferite = 1
	
	pieseMozaic = []
	mediiPieseMozaic = []
	
	#dimensiuni imagine referinta
	dimVertImg = None
	dimOrImg = None

	#dimensiuni piese	
	dimVertPiesa = None
	dimOrPiesa = None

	#dimensiuni imagine referinta redimensionata
	dimVertRdImg = None
	dimOrRdImg = None
	
