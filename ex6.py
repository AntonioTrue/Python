"""6. Faça um algoritmo que efetua a leitura de cinco elementos para uma 
lista A. No final, apresentar a soma de todos os elementos que sejam 
ímpares, bem como a soma de todos os elementos que sejam pares. """

def somador(lista,soma_par=0,soma_impar=0):
    for i in range(len(lista)):
        if lista[i]%2==0:
            soma_par+=lista[i]
        else:
            soma_impar+=lista[i]
    print(f"A soma dos números ímpares é {soma_impar} e a dos pares é {soma_par}")
def main():
    lista=[]
    for i in range(5):
        n=int(input(f"Digite o {i+1}º valor de n: "))
        lista.append(n)
    somador(lista)

main()
