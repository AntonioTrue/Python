"""7. Leia uma lista de 16 posições e troque os 8 primeiros valores pelos 
8 últimos e vice-e-versa. Escreva ao final a lista obtida. """

def trocador(lista):
    for i in range(8):
        temporario=lista[i]
        lista[i]=lista[i+8]
        lista[i+8]=temporario
    return lista
def main():
    lista=[]
    for i in range(16):
#        n=int(input("Digite o valor de n: "))
        lista.append(i)
    print(f"A lista antiga é {lista}")
    nova_lista=trocador(lista)
    print(f"A nova lista é {nova_lista}")

main()