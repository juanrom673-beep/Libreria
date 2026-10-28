valores = [True,False]

print ("P\ t Q \ AND Q")
print ("-" * 25)

for P in valores:
    for Q in valores:
        resultado = P and Q
        print (P, "\t ", Q, "\t ", resultado)


n = int(input("Cuantas proposiciones: "))

print ("P\t Q\t NOT P\t P OR Q\t P -> Q\t P <-> Q")
print ("-" * 60)

for P in valores:
    for Q in valores:
        negacion = not P
        disyuncion = P or Q
        condicional = (not P) or Q
        bicondicional = P == Q
        print (P, "\t ", Q, "\t ", negacion, "\t ", disyuncion, "\t ", condicional, "\t ", bicondicional)
