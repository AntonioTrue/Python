"""8. Leia uma lista de 25 posições e em seguida um valor X qualquer. Seu 
programa deverá fazer uma busca do valor de X na lista lido e informar a 
posição em que foi encontrada a primeira ocorrência ou se não foi 
encontrado. Pensando na possibilidade de repetição, também deve ser 
retornada quantas ocorrências do valor X foram identificadas. """

def buscador(lista,x,o=0,primeiro=False):
    for i in range(len(lista)):
        if(lista[i]==x):
            o+=1
            if(primeiro==False):
                print(f"Foi encontrado {x} no índice {i}")
                primeiro=True
    if(o>0):
        print(f"Total de ocorrências {o}")
    else:
        print(f"Não foi encontrado o valor de {x} na lista")

def main():
    lista=[]
    x=int(input("Digite um número que deseja buscar: "))
    for i in range(25):
        n=int(input(f"Digite o {i+1}º valor de n: "))
        lista.append(n)
    buscador(lista,x)

main()
