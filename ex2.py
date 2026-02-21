"""2. Faça um algoritmo que leia 10 valores inteiros armazenando-os em uma 
lista teste1. Construa uma lista adicional (teste2) de 10 posições, 
formado a partir da seguinte regra: se o valor do índice for par, o valor 
do elemento deve ser igual ao elemento equivalente de teste1 multiplicado
por 5; se for ímpar, deverá ser somado com 5. Ao final, mostrar o conteúdo
das duas listas. """
def verificador(teste1):
    teste2=[]
    for i in range(len(teste1)):
        if(i%2==0):
            teste2.append(teste1[i]*5)
        else:
            teste2.append(teste1[i]+5)
    print(f"O conteúdo do teste1 é {teste1}")
    print(f"O conteúdo do teste2 é {teste2}")

def main(i=0):
    teste1=[]
    #while(len(teste1)<10):
    for i in range(10):
        n=int(input(f"Informe o {i+1}º valor de n: "))
        teste1.append(n)
    verificador(teste1)

main()
