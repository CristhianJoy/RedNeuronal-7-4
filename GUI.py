from tkinter import *
from prueba import RedNeuronal1Prueba

#Propiedades de la ventana
redn = RedNeuronal1Prueba()
ventana = Tk()
ventana.geometry("800x600+0+0")
ventana.title("Red Neuronal")

def base10(strn):
	l = len(strn)-1
	result = 0
	for i in strn:
		p = 2 ** l
		result = result + (int(i) * p)
		l = l - 1
	return result


#Declarar funciones de widgets
#funcion del boton entrenar
def train():
	redn.entrenar()
	print("Completado!")

#funcion del boton leer
def leer():
	num=[input0.get(),input1.get(),input2.get(),input3.get(),input4.get(),input5.get(),input6.get(),1]
	output0.set(redn.procesar(num))	
	outputD.set(base10(output0.get()))
#Variables de Cadena de Entrada
#input
input0=IntVar()
input1=IntVar()
input2=IntVar()
input3=IntVar()
input4=IntVar()
input5=IntVar()
input6=IntVar()

#output
output0=StringVar()
output0.set('0000')
outputD=StringVar()
outputD.set('0')

#Declarar Widgets
#frameInput=Frame(ventana)
#frameInput.grid(row=0, column=9)
#frameInput.place(x=100, y=270, width=160, height=192)

btnTrain=Button(ventana, text="Entrenar", command=train) #boton para entrenar
#btnTrain.grid(row=0, column=0)
btnTrain.place(x=50, y=40, width=211, height=101)

#Labels de la cadena input
labelInput0=Label(ventana, textvariable=input0)
labelInput0.place(x=350, y=80)
#labelInput0.grid(row=0, column=2)

labelInput1=Label(ventana, textvariable=input1)
#labelInput1.grid(row=0, column=3)
labelInput1.place(x=370, y=80)

labelInput2=Label(ventana, textvariable=input2)
#labelInput2.grid(row=0, column=4)
labelInput2.place(x=390, y=80)

labelInput3=Label(ventana, textvariable=input3)
#labelInput3.grid(row=0, column=5)
labelInput3.place(x=410, y=80)

labelInput4=Label(ventana, textvariable=input4)
#labelInput4.grid(row=0, column=6)
labelInput4.place(x=430, y=80)

labelInput5=Label(ventana, textvariable=input5)
#labelInput5.grid(row=0, column=7)
labelInput5.place(x=450, y=80)

labelInput6=Label(ventana, textvariable=input6)
#labelInput6.grid(row=0, column=8)
labelInput6.place(x=470, y=80)

btnLeer=Button(ventana, text="Procesar", command=leer)#boton para procesar
#btnLeer.grid(row=2, column=6)
btnLeer.place(x=310,  y=320, width=141, height=81)

labelOutput0=Label(ventana, textvariable=output0)
#labelOutput0.grid(row=2, column=2)
labelOutput0.place(x=500, y=345)

labelDecimal = Label(ventana, text="Numero: ")
#labelDecimal.grid(row=3, column=0)
labelDecimal.place(x=550, y=345)

labelOutputD=Label(ventana, textvariable=outputD)
#labelOutputD.grid(row=3, column=5)
labelOutputD.place(x=620, y=345)

#Checkbuttons de Input
checkBtnInput0=Checkbutton(ventana, text="Parametro 1", variable=input0)
#checkBtnInput0.grid(row=4, column=1)
checkBtnInput0.place(x=50, y=270)

checkBtnInput1=Checkbutton(ventana, text="Parametro 2", variable=input1)
#checkBtnInput1.grid(row=5, column=1)
checkBtnInput1.place(x=50, y=290)

checkBtnInput2=Checkbutton(ventana, text="Parametro 3", variable=input2)
#checkBtnInput2.grid(row=6, column=1)
checkBtnInput2.place(x=50, y=310)

checkBtnInput3=Checkbutton(ventana, text="Parametro 4", variable=input3)
#checkBtnInput3.grid(row=7, column=1)
checkBtnInput3.place(x=50, y=330)

checkBtnInput4=Checkbutton(ventana, text="Parametro 5", variable=input4)
#checkBtnInput4.grid(row=8, column=1)
checkBtnInput4.place(x=50, y=350)

checkBtnInput5=Checkbutton(ventana, text="Parametro 6", variable=input5)
#checkBtnInput5.grid(row=9, column=1)
checkBtnInput5.place(x=50, y=370)

checkBtnInput6=Checkbutton(ventana, text="Parametro 7", variable=input6)
#checkBtnInput6.grid(row=10, column=1)
checkBtnInput6.place(x=50, y=390)

#btnTrain.pack()
#btnLeer.pack()
#labelInput0.pack()
#labelInput1.pack()
#labelInput2.pack()
#labelInput3.pack()
#labelInput4.pack()
#labelInput5.pack()
#labelInput6.pack()

ventana.mainloop()

