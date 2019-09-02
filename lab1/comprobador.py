#!/usr/bin/env python
# -*- coding: utf-8 -*-

def promedio(lista):
	pro = sum(lista)/3
	print(pro, "\n")

def cuadrados(lista):
	lista2 = []
	for i in lista:
		lista2.append(i*i)
	print(lista2)

def cuenta_atras(palabras):
	x = 0
	for i in range(0, 3):
		palabra = list(palabras[i])
		letras = len(palabra)
		if letras > x:
			x = i
	print(palabras[x])

#main

lista = [6.0 , 5.0 , 4.0]
palabras = ["hola", "python", "compilador", "nice"]

promedio(lista)
cuadrados(lista)
cuenta_atras(palabras)
