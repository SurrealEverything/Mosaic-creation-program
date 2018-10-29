#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 14:31:02 2018

@author: gabriel

"""
from params import params
from incarcaPieseMozaic import incarcaPieseMozaic
from calculeazaDimensiuniMozaic import calculeazaDimensiuniMozaic
from adaugaPieseMozaicPeCaroiaj import adaugaPieseMozaicPeCaroiaj
from adaugaPieseMozaicModAleator import adaugaPieseMozaicModAleator

def construiesteMozaic():
#functia principala a proiectului
#primeste toate datele necesare in structura params
    
	#incarca toate imaginile mici = piese folosite pentru mozaic
	incarcaPieseMozaic()
	    
	#calculeaza noile dimensiuni ale mozaicului
	calculeazaDimensiuniMozaic()

	#adauga piese mozaic
	if params.modAranjare == 'caroiaj':
		return adaugaPieseMozaicPeCaroiaj()
	elif params.modAranjare == 'aleator':
		return adaugaPieseMozaicModAleator()
	else:
		print('EROARE, optiune necunoscuta \n')
		return None



