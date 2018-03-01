from Neuron1 import Neuron1
import math
import random

class RedNeuronal1:

	nodosCapaK= 0
	entCapak= 0
	nodosCapaJ= 0
	entCapaj= 0

	L=0.5

	#Neuron1 [] neuronK, neuronJ
	balance = 1.0

	def __init__(self, nodosCapaK, nodosCapaJ, entCapak, entCapaj):
		self.nodosCapaK=nodosCapaK
		self.nodosCapaJ=nodosCapaJ
		self.entCapak=entCapak
		self.entCapaj=entCapaj

		self.entradas = []
		self.neuronK = []
		self.neuronJ = []
		self.balance = 1.0


	def crearRed(self):
		self.neuronK = []
		for k in range(0,self.nodosCapaK):
			self.neuronK.append(Neuron1(self.entCapak))

		self.neuronJ = []
		for j in range(0,self.nodosCapaJ):
			self.neuronJ.append(Neuron1(self.entCapaj))

	def inicialiaPesos(self):
		for k in range(0,self.nodosCapaK):
			for i in range(0,self.entCapak):
				##print (self.nodosCapaK)
				##print (self.entCapak)
				##print (self.neuronK[0].pesos)
				self.neuronK[k].pesos[i]=random.random()
		for j in range(0,self.nodosCapaJ):
			for i in range(0,self.entCapaj):
				self.neuronJ[j].pesos[i]=random.random()

	def entradasJ(self, capaI):
		for j in range(0,self.nodosCapaJ):
			for i in range(0,len(capaI)):
				self.neuronJ[j].entradas[i]=capaI[i]

	def activacionJ(self ):
		for j in range(0,self.nodosCapaJ):
			self.neuronJ[j].activacion()

	def activacionK(self):
		for k in range(0,self.nodosCapaK):
			self.neuronK[k].activacion()

	def entradasK(self):
		j=0
		for k in range(0,self.nodosCapaK):
			for j in range(0,self.nodosCapaJ):
				self.neuronK[k].entradas[j]= self.neuronJ[j].getActivacion()
			self.neuronK[k].entradas[j]=self.balance

	def errorCapaK (self, apreder, epoca):
		errorl=0.0
		for k in range(0,self.nodosCapaK):
			errorl = (apreder[k][epoca]-self.neuronK[k].getActivacion())*self.neuronK[k].getActivacion()*(1.0-self.neuronK[k].getActivacion())
			self.neuronK[k].setError(errorl)

	def pesos_JK(self):
		for k in range(0,self.nodosCapaK):
			for i in range(0,self.entCapak):
				self.neuronK[k].pesos[i] = self.neuronK[k].pesos[i] + (self.L*self.neuronK[k].getError()*self.neuronK[k].entradas[i])

	def errorCapaJ(self):
		suma=0.0
		errj=0.0
		for j in range(0,self.nodosCapaJ):
			suma=0.0
			for k in range(0,self.nodosCapaK):
				suma+=(self.neuronK[k].getError()*self.neuronK[k].pesos[j])
			errj=(self.neuronJ[j].getActivacion()*(1.0-self.neuronJ[j].getActivacion())*suma)
			self.neuronJ[j].setError(errj)

	def pesos_IJ(self):
		for j in range(0,self.nodosCapaJ):
			for i in range(0,self.entCapaj):
				self.neuronJ[j].pesos[i] = self.neuronJ[j].pesos[i] + self.L*self.neuronJ[j].getError()*self.neuronJ[j].entradas[i]
	def getErrorK(self):
		sumae=0.0
		for j in range(0,self.nodosCapaK):
			sumae= sumae + self.neuronK[j].getError()
		return (math.fabs(sumae))

	def getActivacionk(self,neuron):
		if(self.neuronK[neuron].getActivacion() >= 0.5):
			return 1
		else:
			return 0

	def verPesos_IJ(self):
		print("*******actualiza Pesos_IJ*******")
		for j in range(0,self.nodosCapaJ):
			self.neuronJ[j].verPesos()

	def verPesos_JK(self):
		print("*******actualiza Pesos_JK*******")
		for k in range(0,self.nodosCapaK):
			self.neuronK[k].verPesos()
