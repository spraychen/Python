x = 20
print('anfangs ist x = ',x)
if x < 50: # wird ausgefuehrt wenn wahr true
    print("x ist kleiner 50")
    x = 0
    
elif x > 50:
    print("x ist groesser 50")
    x=2
else:
    print(" x ist geleich 50 ")
    x =10
print("es wird die jeweilige Bedingung ausgefuehrt\nund hier geht das Programm weiter\nund x wird ausgegeben\naber es wurde jeweils ueberschrieben mit Null\ndeshalb Ausgabe 0")
print('x = ',x)