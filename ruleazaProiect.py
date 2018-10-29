#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 14:09:12 2018

@author: gabriel
"""

#proiect REALIZAREA DE MOZAICURI
import cv2
import cv2fixed
from construiesteMozaic import construiesteMozaic
from params import params

#apeleaza functia principala
imgMozaic = construiesteMozaic();

detalii = ''

if params.modAranjare == 'aleator':
	detalii += 'Necaroiat'

if params.criteriu == 'aleator':
	detalii += 'Aleator'

if params.pieseAdiacenteDiferite:
	detalii += 'Dif'
	
if params.imagineColor != 1:
	detalii += 'Grey'

if params.citireCifar10:
	detalii += 'Cifar'
	
numeMozaic = params.numeImgReferinta + detalii + str(params.numarPieseMozaicOrizontala) +'.jpg'
cv2.imwrite(numeMozaic, imgMozaic)
#cv2fixed.imshowfixed(numeMozaic, imgMozaic, 0)