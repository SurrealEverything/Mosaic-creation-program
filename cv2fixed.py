#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 22:58:13 2018

@author: gabriel
"""
import cv2

#din pacate, pe setupul meu, afisarea de imagini merge doar asa
def imshowfixed(name, img, waitTime):
	cv2.namedWindow(name, cv2.WINDOW_NORMAL)
	cv2.resizeWindow(name, 200, 200)
	cv2.imshow(name, img)
	cv2.waitKey(waitTime)
	cv2.destroyAllWindows()
	cv2.waitKey(1)
	cv2.destroyAllWindows()
	cv2.waitKey(1)
	cv2.destroyAllWindows()
	cv2.waitKey(1)
	cv2.destroyAllWindows()
	cv2.waitKey(1)
	cv2.destroyAllWindows()