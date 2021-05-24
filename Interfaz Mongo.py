from Tkinter import *
import tkMessageBox
from pymongo import MongoClient

def SumMul():
    try:
        _e0= int(v0.get())
        _e0=_e0*.50
        _e1 = int(v1.get())
        _e1 = _e1 * 1
        _e2 = int(v2.get())
        _e2 = _e2 * 2
        _e3 = int(v3.get())
        _e3 = _e3 * 5
        _e4 = int(v4.get())
        _e4 = _e4 * 10
        _e5 = int(v5.get())
        _e5 = _e5 * 20
        _e6 = int(v6.get())
        _e6 = _e6 * 50
        _e7 = int(v7.get())
        _e7 = _e7 * 100
        _e8 = int(v8.get())
        _e8 = _e8 * 200
        _e9 = int(v9.get())
        _e9 = _e9 * 500
        _e10= _e0 + _e1 + _e2 + _e3 + _e4 + _e5 + _e6 + _e7 + _e8 + _e9
        tkMessageBox.showinfo("El resultado es", _e10)
        conexion(_e0,_e1,_e2,_e3,_e4,_e5,_e6,_e7,_e8,_e9,_e10)
    except ValueError:
        tkMessageBox.showerror("Introduce un numero entero")


def conexion(_e0,_e1,_e2,_e3,_e4,_e5,_e6,_e7,_e8,_e9,_e10):
    client = MongoClient('localhost', 27017)
    db = client['store']  # me conecto con la bd store

    # collection = db['empleados']
    document = {"Moneda_50":_e0 , "Moneda_1": _e1, "Moneda_5": _e2,
                "Moneda_10": _e4, "Monedo_20":_e5, "Billete_50": _e6,
                "Billete_100":_e7, "Billete_200":_e8, "Billete_500":_e9,
                "Total_dia:":_e10}
    _id = db['corte_dia'].insert(document)
    print_id
    return

v=Tk()
v.title("")
v.geometry("200x450")

vp = Frame(v)
vp.grid(column=0, row=0, padx=(50,50), pady=(10,10))
vp.columnconfigure(0, weight=1)
vp.rowconfigure(0, weight =1)

ET0=Label(vp,text="MONEDAS")
ET0.grid(column=2, row=1)

e0=Label(vp,text="0.50")
e0.grid(column=1, row=3)

e1=Label(vp,text="1.00")
e1.grid(column=1, row=4)

e2=Label(vp,text="2.00")
e2.grid(column=1, row=5)

e3=Label(vp,text="5.00")
e3.grid(column=1, row=6)

e3=Label(vp,text="10.00")
e3.grid(column=1, row=7)

v0 = ""
v0 = Entry(vp, width=5, textvariable=v0)
v0.grid(row=3, column=2)

v1 = ""
v1 = Entry(vp, width=5, textvariable=v1)
v1.grid(row=4, column=2)

v2 = ""
v2 = Entry(vp, width=5, textvariable=v2)
v2.grid(row=5, column=2)

v3 = ""
v3 = Entry(vp, width=5, textvariable=v3)
v3.grid(row=6, column=2)

v4 = ""
v4 = Entry(vp, width=5, textvariable=v4)
v4.grid(row=7, column=2)

ET1=Label(vp,text="BILLETES")
ET1.grid(column=2, row=9)

e4=Label(vp,text="20.00")
e4.grid(column=1, row=11)

e5=Label(vp,text="50.00")
e5.grid(column=1, row=12)

e6=Label(vp,text="100.00")
e6.grid(column=1, row=13)

e7=Label(vp,text="200.00")
e7.grid(column=1, row=14)

e8=Label(vp,text="500.00")
e8.grid(column=1, row=15)

v5 = ""
v5 = Entry(vp, width=5, textvariable=v5)
v5.grid(row=11, column=2)

v6 = ""
v6 = Entry(vp, width=5, textvariable=v6)
v6.grid(row=12, column=2)

v7 = ""
v7 = Entry(vp, width=5, textvariable=v7)
v7.grid(row=13, column=2)

v8 = ""
v8 = Entry(vp, width=5, textvariable=v8)
v8.grid(row=14, column=2)

v9 = ""
v9 = Entry(vp, width=5, textvariable=v9)
v9.grid(row=15, column=2)

b = Button(vp, text="TOTAL", command=SumMul)
b.grid(row=17, column=2, padx=(20, 20), pady=(20, 20))

bc = Button(vp, text="Conectar BD", command=conexion)
bc.grid(row=19, column=2, padx=(20, 20), pady=(20, 20))


v.mainloop()
