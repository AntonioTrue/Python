"""4. Faça um algoritmo que leia um lista numérico N[20]. A seguir, 
encontre o menor elemento do lista N e a sua posição dentro do lista, 
mostrando: “O menor elemento de N é ”, M, “ e sua posição dentro do lista 
é: ”,P. """

def verificador(N,menor=None):
    for i in range(len(N)):
        if menor is None or N[i]<menor:
            menor,indice=N[i],i
    print(f"O menor elemento de N é {menor} e sua posição dentro da lista é {indice}")
def main():
    N=[]
    for i in range(20):
        n=int(input("Digite um valor: "))
        N.append(n)
    verificador(N)

main()
