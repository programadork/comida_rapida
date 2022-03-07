
from tkinter import *

root = Tk()
root.title("Servicio de comida rapida")
root.geometry("1300x775")
root.config(bg="#109DFA")

titulo = Label(root, text="Servicio de comida rapida con Python",
bd=10, relief=GROOVE,font=("arial black",20),bg="#109DFA",fg="white").pack(fill=X)

lado_izquierdo = Frame(root,width=800,height=700,relief=GROOVE)
lado_izquierdo.place(x=10,y=80)

calculadora = Frame(root,width=400,height=700,relief=GROOVE)
calculadora.place(x=870,y=80)

frame = Frame(root, bd=10,relief=GROOVE, bg="#109DFA")
frame.place(x=10,y=370,width=400,height=275)

factura = Label(frame,text="Factura",font=("arial black",14),
bd=2,relief=GROOVE,bg="#109DFA",fg="white").pack(fill=X)

scroll = Scrollbar(frame,orient=VERTICAL)
texarea = Text(frame,yscrollcommand=scroll.set)
scroll.pack(side=RIGHT,fill=Y)
scroll.config(command=texarea.yview)
texarea.pack(fill=BOTH,expand=1)

resumen_total = LabelFrame(root, text="Resumen Total",font=("arial black",12),
    bg="#109DFA", fg="white", relief=GROOVE, bd=10)
resumen_total.place(x=0,y=640,width=1300,height=125)   

boton_frame = Frame(resumen_total,bd=7,relief=GROOVE,bg="#109DFA")
boton_frame.place(x=420, width=850,height=100)

sadas = Label(lado_izquierdo,font=("arial",16,"bold"),text="Refrescos",bd=10,anchor=W,)
sadas.grid(row=0,column=0)
textsodas = Entry(lado_izquierdo,font=("arial",16,"bold"),bd=10,insertborderwidth=4,bg="#109DFA")
textsodas.grid(row=0,column=1)

Frito = Label(lado_izquierdo,font=("arial", 16, "bold"), text="Papas fritas", bd=10, anchor="w")
Frito.grid(row=1,column=0)
txtFrito=Entry(lado_izquierdo,font=("arial", 16, "bold"), bd=10, insertwidth=4,bg="#109DFA", justify="left")
txtFrito.grid(row=1,column=1)

Burger = Label(lado_izquierdo,font=("arial", 16, "bold"), text="hamburguesa",  bd=10, anchor="w")
Burger.grid(row=2,column=0)
txtBurger=Entry(lado_izquierdo,font=("arial", 16, "bold"), bd=10, insertwidth=4,bg="#109DFA", justify="left")
txtBurger.grid(row=2,column=1)

Filete = Label(lado_izquierdo,font=("arial", 16, "bold"), text="Filete de tiburon",  bd=10, anchor="w")
Filete.grid(row=3,column=0)
txtFilete=Entry(lado_izquierdo,font=("arial", 16, "bold"), bd=10, insertwidth=4,bg="#109DFA", justify="left")
txtFilete.grid(row=3,column=1)

Pollo = Label(lado_izquierdo,font=("arial", 16, "bold"), text="Pollo frito",  bd=10, anchor="w")
Pollo.grid(row=4,column=0)
txtPollo=Entry(lado_izquierdo,font=("arial", 16, "bold"),bd=10, insertwidth=4,bg="#109DFA", justify="left")
txtPollo.grid(row=4,column=1)

Queso = Label(lado_izquierdo,font=("arial", 16, "bold"), text="Queso frito", bd=10, anchor="w")
Queso.grid(row=5,column=0)
texQueso=Entry(lado_izquierdo,font=("arial", 16, "bold"), bd=10, insertwidth=4,bg="#109DFA", justify="left")
texQueso.grid(row=5,column=1)

empanadas = Label(lado_izquierdo,font=("arial", 16, "bold"), text="Empanadas", bd=10, anchor="w")
empanadas.grid(row=0,column=2)
txtempanadas=Entry(lado_izquierdo,font=("arial", 16, "bold"), bd=10, insertwidth=4,bg="#109DFA", justify="left")
txtempanadas.grid(row=0,column=3)

pezcado = Label(lado_izquierdo,font=("arial", 16, "bold"), text="Pezcado", bd=10, anchor="w")
pezcado.grid(row=1,column=2)
pezcado=Entry(lado_izquierdo,font=("arial", 16, "bold"), bd=10, insertwidth=4,bg="#109DFA", justify="left")
pezcado.grid(row=1,column=3)

hot_dog= Label(lado_izquierdo,font=("arial", 16, "bold"), text="Hot dog", bd=10, anchor="w")
hot_dog.grid(row=2,column=2)
texhot_dog=Entry(lado_izquierdo,font=("arial", 16, "bold"), bd=10, insertwidth=4,bg="#109DFA", justify="left")
texhot_dog.grid(row=2,column=3)

pizza = Label(lado_izquierdo,font=("arial", 16, "bold"), text="Pizza", bd=10, anchor="w")
pizza.grid(row=3,column=2)
txtpizza=Entry(lado_izquierdo,font=("arial", 16, "bold"), bd=10, insertwidth=4,bg="#109DFA", justify="left")
txtpizza.grid(row=3,column=3)

frituras= Label(lado_izquierdo,font=("arial", 16, "bold"), text="Frituras", bd=10, anchor="w")
frituras.grid(row=4,column=2)
txtfrituras=Entry(lado_izquierdo,font=("arial", 16, "bold"), bd=10, insertwidth=4,bg="#109DFA", justify="left")
txtfrituras.grid(row=4,column=3)

chimi = Label(lado_izquierdo,font=("arial", 16, "bold"), text="Chimi", bd=10, anchor="w")
chimi.grid(row=5,column=2)
txtchimi=Entry(lado_izquierdo,font=("arial", 16, "bold"), bd=10, insertwidth=4,bg="#109DFA", justify="left")
txtchimi.grid(row=5,column=3)

display = Entry(calculadora,font=("arial", 20, "bold"),bd=20,insertborderwidth=4,fg="white",
bg="#109DFA",justify="left")
display.grid(columnspan=4)

btn7=Button(calculadora,padx=16,pady=16,fg="black",bd=8, font=("arial", 20, "bold"),
text="7",bg="#109DFA").grid(row=2,column=0)

btn8=Button(calculadora,padx=16,pady=16,fg="black",bd=8, font=("arial", 20, "bold"),
text="8",bg="#109DFA").grid(row=2,column=1)

btn9=Button(calculadora,padx=16,pady=16,fg="black",bd=8, font=("arial", 20, "bold"),
text="9",bg="#109DFA").grid(row=2,column=2)

Addition=Button(calculadora,padx=16,pady=16,bd=8, fg="black", font=("arial", 19, "bold"), text="+", bg="#109DFA").grid(row=2,column=3)

btn4=Button(calculadora,padx=16,pady=16,bd=8, fg="black", font=("arial", 20, "bold"), text="4", bg="#109DFA").grid(row=3,column=0) 

btn5=Button(calculadora,padx=16,pady=16,bd=8, fg="black", font=("arial", 20, "bold"), text="5", bg="#109DFA").grid(row=3,column=1)

btn6=Button(calculadora,padx=16,pady=16,bd=8, fg="black", font=("arial", 20, "bold"), text="6", bg="#109DFA").grid(row=3,column=2)

subtraccion=Button(calculadora,padx=16,pady=16,bd=8, fg="black", font=("arial", 20, "bold"), text="-", bg="#109DFA").grid(row=3,column=3)

btn1=Button(calculadora,padx=16,pady=16,bd=8, fg="black", font=("arial", 20, "bold"), text="1", bg="#109DFA").grid(row=4,column=0) 

btn2=Button(calculadora,padx=16,pady=16,bd=8, fg="black", font=("arial", 20, "bold"), text="2", bg="#109DFA").grid(row=4,column=1)

btn3=Button(calculadora,padx=16,pady=16,bd=8, fg="black", font=("arial", 20, "bold"), text="3", bg="#109DFA").grid(row=4,column=2)

multiply=Button(calculadora,padx=16,pady=16,bd=8, fg="black", font=("arial", 20, "bold"), text="*", bg="#109DFA").grid(row=4,column=3)

btn0=Button(calculadora,padx=16,pady=16,bd=8, fg="black", font=("arial", 20, "bold"), text="0", bg="#109DFA").grid(row=5,column=0) 

btnClear=Button(calculadora,padx=16,pady=16,bd=8, fg="black", font=("arial", 20, "bold"), text="C", bg="#109DFA").grid(row=5,column=1)

btnEquals=Button(calculadora,padx=16,pady=16,bd=8, fg="black", font=("arial", 20, "bold"), text="=", bg="#109DFA").grid(row=5,column=2)

Division=Button(calculadora,padx=16,pady=16,bd=8, fg="black", font=("arial", 20, "bold"), text="/", bg="#109DFA").grid(row=5,column=3)

precio_total = Label(resumen_total,font=("arial", 16, "bold"), text="Precio Total", bd=10, anchor="w")
precio_total.grid(row=0,column=0)
txtprecio_total=Entry(resumen_total,font=("arial", 16, "bold"), bd=10, insertwidth=4,bg="#109DFA", justify="left")
txtprecio_total.grid(row=0,column=1)

impuestos = Label(resumen_total,font=("arial", 16, "bold"), text="Impuestos", bd=10, anchor="w")
impuestos.grid(row=1,column=0)
txtimpuestos=Entry(resumen_total,font=("arial", 16, "bold"), bd=10, insertwidth=4,bg="#109DFA", justify="left")
txtimpuestos.grid(row=1,column=1)

btnTotal = Button(boton_frame,padx=30,pady=5, bd=16, fg="black",font=("arial", 16, "bold"), 
width=10, text="Total", bg="#109DFA").grid(row=0, column=1,padx=25,pady=5) 

btnReset = Button(boton_frame,padx=30,pady=5, bd=16, fg="black",font=("arial", 16, "bold"), 
width=10, text="Reset", bg="#109DFA").grid(row=0, column=2,padx=25,pady=5)

btnExit = Button(boton_frame,padx=30,pady=5, bd=16, fg="black",font=("arial", 16, "bold"), 
width=10, text="Exit", bg="#109DFA").grid(row=0, column=3,padx=25,pady=5)

root.mainloop()