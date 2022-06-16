# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 14:35:40 2022

@author: Usuario
"""

import  tkinter  as  tk
from tkinter.messagebox import showinfo
from tkinter import filedialog 

ventana  =  tk.Tk()
ventana.geometry("700x650")

ventana.config(bg="gray")

##Añadir color al fondo
ventana.title("Calculo de Vuelo")

labelfocal=tk.Label (ventana, text="Distancia Focal (mm)")
labelfocal.grid(row= 0, column=0, padx=10)
caja1=tk.Entry(ventana)
caja1.grid(row= 1, column=0, padx=10)

labelanchosensor=tk.Label (ventana, text="Ancho del sensor (mm)")
labelanchosensor.grid(row= 2, column=0)
caja2=tk.Entry(ventana)
caja2.grid(row= 3, column=0)

labellongitudinal=tk.Label (ventana, text="Solape Longitudinal (%)")
labellongitudinal.grid(row= 4, column=0)
caja3=tk.Entry(ventana)
caja3.grid(row= 5, column=0)

labelanchoparcela=tk.Label (ventana, text="Ancho Parcela")
labelanchoparcela.grid(row= 6, column=0)
caja4=tk.Entry(ventana)
caja4.grid(row= 7, column=0)

labelanchoimg=tk.Label (ventana, text="Ancho de Imagen (pixel)")
labelanchoimg.grid(row= 0, column=1, padx=10)
caja5=tk.Entry(ventana)
caja5.grid(row= 1, column=1, padx=10)

labelanchosensor=tk.Label (ventana, text="Alto del sensor (mm)")
labelanchosensor.grid(row= 2, column=1)
caja6=tk.Entry(ventana)
caja6.grid(row= 3, column=1)

labelsolapetrans=tk.Label (ventana, text="Solape Transversal (%)")
labelsolapetrans.grid(row= 4, column=1)
caja7=tk.Entry(ventana)
caja7.grid(row= 5, column=1)

labelvelvuelo=tk.Label (ventana, text="Velocidad Vuelo (m/s)")
labelvelvuelo.grid(row= 6, column=1)
caja8=tk.Entry(ventana)
caja8.grid(row= 7, column=1)

labelaltoimg=tk.Label (ventana, text="Alto de imagen (pixel)")
labelaltoimg.grid(row= 0, column=2, padx=10)
caja9=tk.Entry(ventana)
caja9.grid(row= 1, column=2, padx=10)

labelalturavuelo=tk.Label (ventana, text="Altura de vuelo(m)")
labelalturavuelo.grid(row= 2, column=2)
caja10=tk.Entry(ventana)
caja10.grid(row= 3, column=2)

labelargoparce=tk.Label (ventana, text="Largo Parcela (m)")
labelargoparce.grid(row=4, column=2)
caja11=tk.Entry(ventana)
caja11.grid(row= 5, column=2)               
               
cajagrande=tk.Text(ventana)
cajagrande.grid(row=10, column=0, columnspan=3, pady=10, padx=20)

def gsd1():
    
    altv=float(caja10.get())
    focal=float(caja1.get())
    rsi=float(caja6.get())
   #GSD = (altv*100 / focal) * rsi
    GSD=f'{(altv*100 / focal) * rsi} = {(altv*100 / focal) * rsi}'
    GSD2=str(GSD)
    cajagrande.insert(tk.END, "GSD = " + GSD2 + " cm/pixel \n ================================================\n")

def escala():
    
    Focalcamara=float(caja1.get())
    Alturadevuelo=float(caja10.get())
    Escalavuelo = 1 / ((Focalcamara/1000) / Alturadevuelo)
    Escalavuelo2=str(Escalavuelo)
    cajagrande.insert(tk.END, "Escala de Vuelo = " + Escalavuelo2 + "\n ================================================\n")
    
def anchoimgterr():
    
    Anchosensor=float(caja2.get())
    Focalcamara=float(caja1.get())
    Alturadevuelo=float(caja10.get())
    escala=1 / ((Focalcamara/1000) / Alturadevuelo)
    Anchoimgterr = (Anchosensor * escala)/1000
    Anchoimgterr2=str(Anchoimgterr)
    cajagrande.insert(tk.END, "Ancho Imagen Terreno = " + Anchoimgterr2 + " m \n ================================================\n")
    
def altoimgterr():
    
    Altosensor=float(caja6.get())
    Focalcamara=float(caja1.get())
    Alturadevuelo=float(caja10.get())
    escala=1 / ((Focalcamara/1000) / Alturadevuelo)
    Altoimgterr = (Altosensor * escala)/1000
    Altoimgterr2=str(Altoimgterr)
    cajagrande.insert(tk.END, "Alto Imagen Terreno "+ Altoimgterr2+ " m \n ================================================\n")   

def basaerea():
    
    Anchoimgterr=float(caja5.get())
    Solapelongitudinal=float(caja3.get())
    Baseaerea= Anchoimgterr* (1-(Solapelongitudinal/100))
    Baseaerea2=str(Baseaerea)
    cajagrande.insert(tk.END, "Base Aerea "+ Baseaerea2+ " m \n ================================================\n")

def distpasadas():
    
    Altoimagenterr=float(caja9.get())
    Solapetransversal=float(caja7.get())
    Distanciaentrepasadas = Altoimagenterr* (1-(Solapetransversal/100))
    Distanciaentrepasadas2=str(Distanciaentrepasadas)
    cajagrande.insert(tk.END, "Distancia Pasada "+ Distanciaentrepasadas2+ " m \n ================================================\n")

def tiempoentrefotos():
    
    Velocidadvuelo=float(caja8.get())
    Anchoimgterr=float(caja5.get())
    Solapelongitudinal=float(caja3.get())
    Basaerea= Anchoimgterr* (1-(Solapelongitudinal/100))
    Intervaloentrefotos = Basaerea/ Velocidadvuelo
    Velocidadvuelo = Basaerea / Intervaloentrefotos
    Intervaloentrefotos2=str(Intervaloentrefotos)
    cajagrande.insert(tk.END, "Tiempo entre fotos "+ Intervaloentrefotos2+ " s \n ================================================\n")

def pasadas():
   
    Anchoparcela=float(caja4.get())
    Altoimagenterr=float(caja9.get())
    Solapetransversal=float(caja7.get())
    distpasadas = Altoimagenterr* (1-(Solapetransversal/100))
    Numeropasadas = Anchoparcela / distpasadas
    Numeropasadas2=str(Numeropasadas)
    cajagrande.insert(tk.END, "Numero Pasadas "+ Numeropasadas2+ "\n ================================================\n")

def fotopasada():
    
    Largodepasada=float(caja11.get())
    Anchoimgterr=float(caja5.get())
    Solapelongitudinal=float(caja3.get())
    basaerea= Anchoimgterr* (1-(Solapelongitudinal/100))
    Nfotosporpasadas = (Largodepasada / basaerea) + 1
    Nfotosporpasadas2=str(Nfotosporpasadas)
    cajagrande.insert(tk.END, "Numero Fotos Pasada "+ Nfotosporpasadas2+ "\n ================================================\n")
    
def fotosporvuelo():
    
    Anchoparcela=float(caja4.get())
    Altoimagenterr=float(caja9.get())
    Solapetransversal=float(caja7.get())
    distpasadas = Altoimagenterr* (1-(Solapetransversal/100))
    Ndepasadas = Anchoparcela / distpasadas
    Anchoimgterr=float(caja5.get())
    Solapelongitudinal=float(caja3.get())
    Largodepasada=float(caja11.get())
    basaerea= Anchoimgterr* (1-(Solapelongitudinal/100))
    fotopasada = (Largodepasada / basaerea) + 1
    Nfotosporvuelo = fotopasada * Ndepasadas
    Nfotosporvuelo2=str(Nfotosporvuelo)
    cajagrande.insert(tk.END, "Numero Fotos vuelo "+ Nfotosporvuelo2+ " \n ================================================\n")

def disvuelo():
    
    Largodeparcela=float(caja11.get())
    Anchodeparcela=float(caja4.get())
    Largodepasada=float(caja11.get())
    Anchoimgterr=float(caja5.get())
    Solapelongitudinal=float(caja3.get())
    basaerea= Anchoimgterr* (1-(Solapelongitudinal/100))
    fotopasada = (Largodepasada / basaerea) + 1
    DV = (fotopasada * Largodeparcela) + Anchodeparcela
    DV2=str(DV)
    cajagrande.insert(tk.END, "Distancia de Vuelo "+ DV2+ " m \n ================================================\n")
    
def durvuelo():
    
   # Largodeparcela=float(caja11.get())
    #Anchodeparcela=float(caja4.get())
    Velocidadvuelo=float(caja8.get())
    Anchoimgterr=float(caja5.get())
    Solapelongitudinal=float(caja3.get())
    baseaerea= Anchoimgterr* (1-(Solapelongitudinal/100))
    Intervaloentrefotos = baseaerea/ Velocidadvuelo
    Anchoparcela=float(caja4.get())
    Altoimagenterr=float(caja9.get())
    Solapetransversal=float(caja7.get())
    distpasadas = Altoimagenterr* (1-(Solapetransversal/100))
    Ndepasadas = Anchoparcela / distpasadas
    Largodepasada=float(caja11.get())
    basaerea= Anchoimgterr* (1-(Solapelongitudinal/100))
    fotopasada = (Largodepasada / basaerea) + 1
    fotosporvuelo = fotopasada * Ndepasadas
    Duracion = (fotosporvuelo * Intervaloentrefotos) / 60
    Duracion2=str(Duracion)
    cajagrande.insert(tk.END, "Duracion de vuelo "+ Duracion2+ " min \n ================================================\n")
  
#def error():
#    if caja1==String:
#       Showinfo ("Usted ingreso un caracter desconocido")
#       boton2=tk.Button(Showinfo, text='SALIR', command=error)
#    else:
def todo():
        cajagrande.delete(1.0, tk.END)
        durvuelo()
        disvuelo()
        fotosporvuelo()
        fotopasada()
        pasadas()
        tiempoentrefotos()
        distpasadas()
        basaerea()
        altoimgterr()
        anchoimgterr()
        escala()
        gsd1()

boton1=tk.Button(ventana, text="CALCULAR", command = todo)
boton1.grid(row=9, column=1, pady=20)

ventana.mainloop()