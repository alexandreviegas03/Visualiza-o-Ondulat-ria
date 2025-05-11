#O PROGRAMA DEVE RECEBER PARAMETROS AJUSTAVEIS TAIS COMO AMPLITUDE A, FREQUÊNCIA F  E FASE P
#E MOSTRAR O COMPORTAMENTO DE TAL ONDA. COM A SUA VISUALIZAÇÃO
#matplotlib - para realizar a apresentação grafica.
#import pyautogui
import matplotlib.pyplot as plt
#plt.plot()
import numpy as np #permite calcular com expressões matematicas.
# from tkinter import*
#root=Tk()

#root.geometry('300x700')
#root.title("MyAPP")
#root.config(bg='lightblue')
#root.mainloop()

t = np.linspace(0,2*np.pi,1000)#Intervalo de tempo
y=np.cos(10*t)#Frequência
plt.plot(t,y)
plt.title("GRAFÍCO DA FUNÇÃO")#Titulo do gráfico.
plt.xlabel("Tempo (S)")
plt.ylabel("Amplitude (V)")
plt.show()