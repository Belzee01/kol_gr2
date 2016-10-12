#!/usr/bin/python

import math

class Matrix():
	
	matrix = [[]]
	
	def __init__(self, *args):
		size = len(args)
		size = math.sqrt(size)
		for i in range(0, int(size), 1):
			for j in range(0, int(size), 1):
				self.matrix[i][j].append(args[i+j*1])
	
	def add(matrix):
		for i in matrix.matrix:
			for j in matrix.matrix[i]:
				self.matrix[i][j] += j
		
	def mat_product(matrix):
		returnMatrix = Matrix(0, 0, 0, 0)
		for i in range(0,2,1):
			for j in range(0,2,1):
				for k in range(0,2,1):
					returnMatrix.matrix[i][j] += self.matrix[i][k] * matrix[k][j]
		return returnMatrix

	def printMatrix():
		for i in self.matrix:
			for j in self.matrix[i]:
				print j + " "


matrix_1 = Matrix(4,5,6,7)
matrix_2 = Matrix(2,2,2,1)

matrix_3 = matrix_2.add(matrix_1)

matrix_1.printMatrix()

				
