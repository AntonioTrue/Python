"""5.Faça um algoritmo que leia um lista numérico D[60]. A seguir, troque 
o 1o elemento com o 31o , o 2o com o 32o , etc. Mostre no final a lista 
modificada. 5. Faça um algoritmo que leia um lista numérico D[60]. A 
seguir, troque o 1o elemento com o 31o , o 2o com o 32o , etc. Mostre no 
final a lista modificada. """

def trocador(D):
    for i in range(30):
        #print(f"D[{i}]={D[i]}\nD[{i-30}]={D[i-30]}\n")
        mutavel=D[i]
        D[i]=D[i+30]
        D[i+30]=mutavel
    print(D)

def main():
    D=[]
    for i in range(60):
        D.append(i)
    print(D)
    trocador(D)
main()

