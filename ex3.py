"""3. Faça um algoritmo que leia um lista de números A[10]. No final, 
mostre todas as posições da lista que armazenam um valor menor ou igual a 
10 e o valor armazenado na posição em questão. """

def verificador(lista):
    for i in range(len(lista)):
        if(lista[i]<=10):
            print(f"Posição {i} = {lista[i]}")

def main():
    lista=[]
    for i in range(10):
        n=int(input(f"Digite o {i+1}º valor de n: "))
        lista.append(n)
    verificador(lista)

main()
