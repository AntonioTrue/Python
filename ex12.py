"""
12. Faça um algoritmo que leia um lista G[13] que é o gabarito de um 
teste da loteria esportiva, contendo os valores 1 quando for coluna 1, 0 
quando for coluna do meio e 2 quando for coluna 2.  Ler a seguir, para 10 
apostadores, o número do cartão de cada apostador e um lista R[13] que 
seriam as respostas dos apostadores. Para cada apostador, mostre o número 
de acertos. 
"""

def resultado(G,R):
    for pessoa in range(len(R)):
        acertos=0
        for numero in range(len(G)):
            if(R[pessoa][numero+1]==G[numero]):
                acertos+=1
        R[pessoa].append(acertos)

    for ganhadores in range(len(R)):
        print(f"O apostador {R[ganhadores][0]} fez {R[ganhadores][-1]} acertos.")
def main():
    G=[]
    R=[]
    for i in range(3):#13
        g=int(input(f"Digite o {i+1}º número do gabarito da loteria: "))
        G.append(g)
    for apostador in range(3):#10
        nome=input(f"Digite o nome do {apostador+1}º apostador: ")
        R.append([nome])
        for k in range(3):#13
            r=int(input(f"Digite o {k+1}º número do gabarito da loteria de {nome}: "))
            R[apostador].append(r)
    resultado(G,R)

main()

