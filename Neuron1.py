from Sigmoide import Sigmoide

class Neuron1:
	activacionu=0.0


	errorNodo=0.0;

	sigmoide= Sigmoide;

	def __init__(self, nentradas):

		self.entradas= [];

		self.pesos= [];
		for k in range(0,nentradas):
			self.pesos.append(0.0)
			self.entradas.append(0.0)
		self.sigmoide	= Sigmoide();
		self.errorNodo	=0.0;

	def activacion(self):
		suma = 0.0
		for i in range(0,len(self.entradas)):
			suma= suma + self.entradas[i]*self.pesos[i];
		self.activacionu = self.sigmoide.funcion(suma);

	def verEntradas(self):
		print("*******Entradas*******")
		for i in range(0,len(self.entradas)):
			print(self.entradas[i])

	def verPesos(self):
		print("*******Pesos*******")
		for i in range(0,len(self.pesos)):
			print(self.pesos[i]);

	def getActivacion(self):
		return (self.activacionu);

	def verActivacion(self):
		print("*******Activacion*******")
		print(self.activacionu)

	def getError(self):
		return(self.errorNodo);

	def setError(self, error):
		self.errorNodo=error;
