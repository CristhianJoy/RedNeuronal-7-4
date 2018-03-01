import math

class Sigmoide:
    e=0.0
    p=0.0
    def __init__(self):
        self.e = math.e
        self.p = 1.0

    def funcion(self,a):
        return (1.0/(1.0 + math.pow(self.e,-a/self.p)))
