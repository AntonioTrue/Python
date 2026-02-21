#9. Leia uma lista de 10 posições e verifique se existem valores iguais 
# e os escreva. 
def verificador(lista):
    duplicados=[]
    for i in range(len(lista)):
        for k in range(i+1,len(lista)):
            if(lista[i]==lista[k] and lista[i] not in duplicados):
                duplicados.append(lista[i])
    if(duplicados):
        print(f"Valores duplicados encontrados: {duplicados}")
    else:
        print("Não há valores duplicados na lista.")
def main():
    lista=[]
    for i in range(10):
        entrada=int(input(f"Digite o {i+1}º valor: "))
        lista.append(entrada)
    verificador(lista)

main()