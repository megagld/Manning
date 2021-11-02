# oblicznenia dla rowów trapezowych
# dane:
    # współczynnik szorstkości przekroj[m^-1/3/s]
n=0.01
    #spadek[%]
i=0.002
    # szerokość dna [m]
B=0.5
    #spadki skarp rowów
m1=1.5
m2=1.5
    #natężenie przepływu [m3/s]
Qs=0.5227

# wyznaczenie napełnienie dla zadanego Qs
    # dokładność iteracji
dok=0.001
    # wstępna głębokośc rowu [m]
h=1

wynik_Q=[Qs/2]
wynik_h=[h]

while abs(1-(wynik_Q[-1]/Qs))>dok:   
    #pole
    S=(B+0.5*(m1+m2)*h)*h
    #promień hydrauliczny
    d=B*h+0.5*(m1+m2)*h**2
    e=B+h*((1+m1**2)**0.5+(1+m2**2)**0.5)
    R=d/e
    #prędkość wody
    v=(1/n)*R**(2/3)*i**(0.5)
    #natężenie
    Q=v*S
    #korekta wysokości
    if Qs>=Q:
        h*=1+dok
    else:
        h*=1-dok
    wynik_Q.append(Q)
    wynik_h.append(h)

# print(wynik_Q,wynik_h)
print('****')
print('h=',round(wynik_h[-1],3),'[m3]')
print('Q=',round(wynik_Q[-1],3),'[m3/s]')
print('****')


