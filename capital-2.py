print("---------------------------------------------------")
print("----------------Capital----------------------------")
print("---------------------------------------------------")


C= int(input("DIgite el valor del Capital: "))

M = 2*C
N=0

while(C<M):
    C=C + 0.05 * C
    N=N+1
    print(" Mes " + str(N))
    print("Capital " + str (C))




print("El numero de meses en que se duplica el capital es: " + str(N))