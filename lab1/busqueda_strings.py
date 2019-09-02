#!/usr/bin/env python
# -*- coding: utf-8 -*-

def vocal_consonante(voc, con, letra):
	#la letra se busca en la lista de vocales
	for i in voc:
		if letra == i:
			return True
	#La letra se busca en la lista de consonantes
	for i in con:
		if letra == i:
			return False
	print("No es vocal ni consonante")

def cuenta_vocales_consonantes(voc, con, palabra):
	vocales = 0
	consonantes = 0
	#la palabra se subdivide por cada caracter y se guarda en una lista
	valor1 = list(palabra)
	
	#cada caracter se busca en otra funcion si es vocal o consonante
	for i in valor1:
		x = vocal_consonante(voc, con, i)
		if x == True:
			vocales += 1
		else:
			consonantes += 1
	print("La palabra tiene", vocales, "vocale(s) y", consonantes, "consonante(s)")

#main

vocales = ["AEIOUaeiou"]
consonantes = ["BCDFGHJKLMNÑPQRSTVWXYZbcdfghjklmnñpqrstvwxyz"]
voc = list(vocales[0])
con = list(consonantes[0])

variable = str(input("Ingrese una letra o palabra: "))

valor1 = list(variable)
valor2 = len(valor1)
if valor2 == 1:
	valor = vocal_consonante(voc, con, variable)
	
	if valor == True:
		print("Es vocal")
	if valor == False:
		print("Es consonante")
else:
	cuenta_vocales_consonantes(voc, con, variable)

