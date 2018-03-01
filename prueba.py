import math
from RedNeuronal1 import RedNeuronal1


class RedNeuronal1Prueba:
	def __init__(self):
		self.nodosk=4
		self.nodosj=5
		self.prueba=[1]


		self.balance = 1.0
		#self.capaI=[				[1,1,1,0,1,1,1,	self.balance],
		#							[1,0,0,0,0,0,1,	self.balance],
		#							[1,1,0,1,1,1,0,	self.balance],
		#							[1,1,0,1,0,1,1,	self.balance],
		#							[1,0,1,1,0,0,1,	self.balance],
		#							[0,1,1,1,0,1,1,	self.balance],
		#							[0,1,1,1,1,1,1,	self.balance],
		#							[1,1,0,0,0,0,1,	self.balance],
		#							[1,1,1,1,1,1,1,	self.balance],
		#							[1,1,1,1,0,1,1,	self.balance]]

		#self.aprender = [				[0,0,0,0,0,0,0,0,1,1],
		#								[0,0,0,0,1,1,1,1,0,0],
		#								[0,0,1,1,0,0,1,1,0,0],
		#								[0,1,0,1,0,1,0,1,0,1]]

		##self.prueba = [[1,0,0,0,0,0,1, self.balance]]
	#####################################Definir cuantas filas y columnas tiene el archivo
	def leerEntrada(self):
		file=open('Entradas.txt','r')
		numero_filas=10
		numero_columnas=8
		matriz=[]
		for i in range(numero_filas):
			matriz.append([])
			for j in range(numero_columnas):
				matriz[i].append(None)
		i=0
		while i<numero_filas:
			line=file.readline()
			j=0
			while j<numero_columnas:
				if line[j]=='1':
					matriz[i][j]=1
				if line[j]=='0':
					matriz[i][j]=0
				j=j+1
			i=i+1
		file.close()
		return matriz

	def leerSalida(self):
		file=open('Salidas.txt','r')
		numero_filas=4
		numero_columnas=10
		matriz=[]
		for i in range(numero_filas):
			matriz.append([])
			for j in range(numero_columnas):
				matriz[i].append(None)
		i=0
		while i<numero_filas:
			line=file.readline()
			j=0
			while j<numero_columnas:
				if line[j]=='1':
					matriz[i][j]=1
				if line[j]=='0':
					matriz[i][j]=0
				j=j+1
			i=i+1
		file.close()
		return matriz
	#ejecutas esta funcion al momento de presionar entrenar
	def entrenar(self):
		self.capaI=self.leerEntrada()
		self.aprender=self.leerSalida()
		print("datos cargados")
		
		self.redNeuronal = RedNeuronal1(4, 5,6,8)
		self.redNeuronal.crearRed()
		print("red creada")
		self.redNeuronal.inicialiaPesos()
		print("inicialisando pesos")

		n = 10000
		i = 0
		epoca=0
		error=0.0
		k=0
		noigual=False
		while ( i < len(self.capaI) and k<n):
			epoca=i
			#if(i==0):
			#	print("*****epoca " +str(epoca)+" ****** Iteracion "+str(k)+"")
			#strtoprint = ""
			#for c in range(0,7):
			#	strtoprint = strtoprint + ""+str(round(self.capaI[epoca][c]))+", "
			#strtoprint = strtoprint + "Aprender "
			#for c in range(0,self.nodosk):
			#	strtoprint = strtoprint + ""+str(round(self.aprender[c][epoca]))+", "
			#strtoprint = strtoprint + "Salida "


			self.redNeuronal.entradasJ(self.capaI[epoca])
			self.redNeuronal.activacionJ()
			self.redNeuronal.entradasK()
			self.redNeuronal.activacionK()

			self.redNeuronal.errorCapaK(self.aprender,epoca)
			#for c in range(0,self.nodosk):
			#	strtoprint = strtoprint + ""+str(round(self.redNeuronal.getActivacionk(c)))+", "
				# print(""+str(round(self.redNeuronal.getActivacionk(c)))+", ")
			decimal=0.0
			t=0
			#for c in range(self.nodosk-1,-1,-1):
			#	decimal= decimal + self.redNeuronal.getActivacionk(c)*math.pow(2,t)
			#	t=t+1
			#strtoprint = strtoprint + "decimal "+str(decimal)
			#print(strtoprint)

			## print("decimal "+str(decimal))
			noigual=False
			for c in range(0,self.nodosk):
				if(self.redNeuronal.getActivacionk(c)==self.aprender[c][epoca]):
					pass
				else :
					noigual=True

			if(noigual):
				self.redNeuronal.pesos_JK()
				self.redNeuronal.errorCapaJ()
				self.redNeuronal.pesos_IJ()

			i=i+1
			k=k+1
			if(i == 10):
				i = 0

		#self.redNeuronal.verPesos_IJ()
		#self.redNeuronal.verPesos_JK()


		#for c in range(0,8):
		#	print(""+str(round(self.prueba[0][c]))+", ")


		#print("Salida ")
		#ejecutas este al procesar :v

	
	def procesar(self,num):
		print ("Procesando!")
		self.prueba[0]=num
		self.redNeuronal.entradasJ(self.prueba[0])
		self.redNeuronal.activacionJ()
		self.redNeuronal.entradasK()
		self.redNeuronal.activacionK()

		#joven esto te lo imprime :v ves la manera deq te imprima los 4 bits en el label de la interfaz 
		#al ejecutar las 4 siguientes lineas en el printdata se guarda de esta manera x,x,x,x,
		printdata =""
		for c in range(0,self.nodosk):
			printdata = printdata +""+str(round(self.redNeuronal.getActivacionk(c)))
			#print (printdata)
#			enviamos la respuesta a la interfaz
			#
			self.resultado=printdata
		return printdata

#a = RedNeuronal1Prueba()
#a.main()
