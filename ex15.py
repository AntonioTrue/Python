"""15. Faça um algoritmo que leia um lista V[10] e um lista X[10]. A 
seguir, crie um lista Y[20] que conterá os valores dos listas V e X em 
crescente. """

def ordenador(y,menor=None,i=0):
    Y=[]
    while(True):
        while i<len(y):
            if(menor is None or y[i]<menor):
                menor=y[i]
                indice=i
            i+=1
        Y.append(menor)
        y.pop(indice)
        i=0
        menor=None
        if(len(y)==0):
            break
    print(Y)

def main():
    V=[]
    X=[]
    for i in range(10):
        v=int(input(f"Digite o {i+1}º valor da lista v: "))
        V.append(v)
    for i in range(10):
        x=int(input(f"Digite o {i+1}º valor da lista X: "))
        X.append(x)
    y=V+X
    ordenador(y)

main()
