#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 14:31:49 2018

@author: gabriel
"""
from params import params
import cv2
import cv2fixed
import numpy as np
import pickle

def incarcaPieseMozaic():
	#citeste toate cele numarPiese piese folosite la mozaic din directorul corespunzator
	#toate cele numarPiese imagini au aceeasi dimensiune dimVertPiesa x dimOrPiesa x C, unde:
	#dimVertPiesa = inaltime, dimOrPiesa = latime, C = nr canale (C=1  gri, C=3 color)
	#functia intoarce pieseMozaic = lista de numarPiese imagini de dimVertPiesa x dimOrPiesa x C in params
	#pieseMoziac[i] reprezinta piesa numarul i 
	
	print('Incarcam piesele pentru mozaic din director \n')
	if params.citireCifar10 == 0:
		for i in range(params.numarPiese):
			img = cv2.imread(params.numeDirector + '/' + str(i+1) + '.' + params.tipImagine, params.imagineColor)
			params.pieseMozaic.append(img)

	else:
		img, lbl = load_batch('data_batch_1')  
		for i in range(10000):
			if lbl[i] == params.clasaCifar:
				params.pieseMozaic.append(img[i])
		params.numarPiese = len(params.pieseMozaic)
	#afiseaza primele 100 de piese ale mozaicului
	if params.afiseazaPieseMozaic:	   
		for i in range(max(100, params.numarPiese)):
			cv2fixed.imshowfixed(str(i+1), params.pieseMozaic[i], 0)
			
	"""
	cv2fixed.imshowfixed('img', params.pieseMozaic[:], 0)	    
	figure,
    title('Primele 100 de piese ale mozaicului sunt:');
    idxImg = 0;
    for i = 1:10
        for j = 1:10
            idxImg = idxImg + 1;
            subplot(10,10,idxImg);
            imshow(pieseMozaic(:,:,:,idxImg));
        end
    end
    drawnow;
    pause(2);
	"""

def load_batch(file):

    f = open(params.numeDirector + file, 'rb')
    dict = pickle.load(f, encoding='bytes')    
    images = dict[b'data']
    images = np.reshape(images, (10000, 3, 32, 32)).transpose(0,2,3,1).astype("uint8")    
    labels = dict[b'labels']
    imagearray = np.array(images)   #   (10000, 3072)
    labelarray = np.array(labels)   #   (10000,)    
    return imagearray, labelarray