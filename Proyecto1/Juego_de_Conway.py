#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Funcion que determina si la celula vive, muere
# o renace segun las siguientes condiciones.
def vive_muere(variante, vecinos):

	if variante == "X":
		if vecinos >= 4:
			return " "
		if vecinos >= 2:
			return "X"
		if vecinos <= 1:
			return " "
	if variante == " ":
		if vecinos == 3:
			return "X"
		else:
			return " "


# Funcion que contabiliza las 8 celulas vecinas
# de cada celula dentra de la matriz.
def celulas_vecinas(matriz, y, x, tamaño):

	vecinos = 0
	if matriz[y][x] == "X":
		vecinos -= 1		# Se resta 1 si la celula central esta viva

	for Y in range(y-1, y+2):
		if Y>=0 and Y<tamaño:
			for X in range(x-1, x+2):
				if X>=0 and X<tamaño:
					if matriz[Y][X] == "X":
						vecinos += 1
	
	return vecinos


# Funcion que imprime la matriz actual y modifica
# para la siguiente generacion
def funcion_principal(tamaño, matriz, generacion):

	os.system("clear")		# Se mantiene limpia la terminal
	matriz_2 = []
	viva = 0
	nace = 0
	muere = 0
	
	print("Generacion", generacion)
	generacion += 1
	
	# Ciclo que imprime la matriz
	for i in range(tamaño):
	
		print("|", end = "")
		for j in range(tamaño):
			print(matriz[i][j], "|", end = "")
		print("")
	
	# Ciclo que guarda la siguiente generacion
	for i in range(tamaño):
	
		fila = []
		for j in range(tamaño):
			vecinos = celulas_vecinas(matriz, i, j, tamaño)
			
			# Condiciones para contar la celulas que nacen,
			# siguen vivas o mueren
			if matriz[i][j] == "X":
				if vive_muere(matriz[i][j], vecinos) == "X":
					viva += 1
				else:
					muere += 1
			if matriz[i][j] == " ":
				if vive_muere(matriz[i][j], vecinos) != " ":
					nace += 1
			
			fila.append(vive_muere(matriz[i][j], vecinos))
		matriz_2.append(fila)
	
	print("Vivas:", viva)
	print("Nacen:", nace)
	print("Mueren:", muere)

	# Un lapso de tiempo para poder visualizar mejor 
	# las generaciones en la terminal
	time.sleep(0.5)
	
	if viva != 0:
		# Se vuelve a autollamar la funcion infinitamente
		funcion_principal(tamaño, matriz_2, generacion)
	else:
		print("\nLa vida se extinguió")


#main

import random
import time
import os

try:
	print("	Bienvenido al juego de la vida de Conway")
	time.sleep(1)
	
	tamaño = int(input("Ingrese tamaño de la matriz: "))

	matriz = []
	for i in range(tamaño):		# Se crea la primera generacion random
		fila = []
		for i in range(tamaño):
			fila.append(random.choice([" ", "X"]))
		matriz.append(fila)

	funcion_principal(tamaño, matriz, generacion=0)
	# Se ingresa los datos en la funcion infinita
	
except ValueError:
	print("El valor no es valido")
except TypeError:
	print("El tipo ingresado no es valido")
except:
	print("Virus trollano")
