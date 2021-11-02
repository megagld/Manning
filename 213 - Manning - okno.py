# mgld
dokx=0.001
def pob():
    global ix,nx,Bx,m1x,m2x,Qsx,dokx
    ix=float(ixE.get())
    nx=float(nxE.get())
    Bx=float(BxE.get())
    m1x=m1xE.get()
    m2x=m2xE.get()
    Qsx=float(QsxE.get())
    # dokx=float(dokxE.get())

def manning(): 
    global ix,nx,Bx,m1x,m2x,Qsx,dokx
    pob()
    out=''
    h=1
    if type(m1x)!=float:
        m1x=float(m1x.split(':')[1])/float(m1x.split(':')[0])
        m2x=float(m2x.split(':')[1])/float(m2x.split(':')[0])

    wynik_Q=[Qsx/2]
    wynik_h=[h]
    while abs(1-(wynik_Q[-1]/Qsx))>dokx:   
        #pole
        S=(Bx+0.5*(m1x+m2x)*h)*h
        #promień hydrauliczny
        d=Bx*h+0.5*(m1x+m2x)*h**2
        e=Bx+h*((1+m1x**2)**0.5+(1+m2x**2)**0.5)
        R=d/e
        #prędkość wody
        v=(1/nx)*R**(2/3)*ix**(0.5)
        #natężenie
        Q=v*S
        #korekta wysokości
        if Qsx>=Q:
            h*=1+dokx
        else:
            h*=1-dokx
        wynik_Q.append(Q)
        wynik_h.append(h)
    wyn.set(str(round(wynik_h[-1],2)))

from tkinter import *
root_window = Tk()
root_window.title("Wypełnienie rowu")
root_window.geometry("450x220")
root_window.resizable(width=False, height=False)
# root_window.configure(background = "blue")

ww=40

Label(root_window, anchor="se",width=ww, height=2, text = "współczynnik szorstkości przekroju [m^-1/3/s]:").grid(row=0)
Label(root_window, anchor="e",width=ww, text = "spadek [%]:").grid(row=1)
Label(root_window, anchor="e",width=ww, text = "szerokość dna [m]:").grid(row=2)
Label(root_window, anchor="e",width=ww, text = "pochylenie rowu lewego:").grid(row=3)
Label(root_window, anchor="e",width=ww, text = "pochylenie rowu prawego:").grid(row=4)
Label(root_window, anchor="e",width=ww, text = "natężenie przepływu [m3/s]:").grid(row=5)
# Label(root_window, anchor="e",width=ww, text = "dokładność iteracji:").grid(row=6)

ixv=IntVar()
nxv=IntVar()
Bxv=IntVar()
m1xv=StringVar()
m2xv=StringVar()
Qsxv=IntVar()
# dokxv=IntVar()

nxv.set(0.01)
ixv.set(0.002)
Bxv.set(0.5)
m1xv.set('1:1.5')
m2xv.set('1:1.5')
Qsxv.set(0.5227)
# dokxv.set(0.001)

nxE = Entry(root_window,text=nxv)
ixE = Entry(root_window,text=ixv)
BxE = Entry(root_window,text=Bxv)
m1xE = Entry(root_window,text=m1xv)
m2xE = Entry(root_window,text=m2xv)
QsxE = Entry(root_window,text=Qsxv)
# dokxE = Entry(root_window,text=dokxv)

nxE.grid(row=0, column=1,sticky='s')
ixE.grid(row=1, column=1)
BxE.grid(row=2, column=1)
m1xE.grid(row=3, column=1)
m2xE.grid(row=4, column=1)
QsxE.grid(row=5, column=1)
# dokxE.grid(row=6, column=1)

funCall = lambda: manning()
Button(root_window, text = "Znajdź wypełnienie", command = funCall).grid(row=7, column=1)
Label(root_window, anchor="e",width=ww, text = "Wypełnienie [m]:").grid(row=8)

wyn = StringVar()
wyn.set('___')

wy=Label(root_window,anchor="e",height=2, textvariable=wyn)
wy.grid(row=8, column=1)

root_window.mainloop()