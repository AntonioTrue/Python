"""
13. Com relação ao exercício anterior, calcule e mostre o percentual dos 
apostadores que fizeram de 10 a 13 pontos e o percentual dos apostadores 
que fizeram menos do que 10 pontos. 
"""

def resultado(G,R,dez_a_treze=0,menosDez=0):
    for pessoa in range(len(R)):
        acertos=0
        for numero in range(len(G)):
            if(R[pessoa][numero+1]==G[numero]):
                acertos+=1
        R[pessoa].append(acertos)
        if acertos>=10 and acertos<=13:
            dez_a_treze+=1
        else:
            menosDez+=1
    for ganhadores in range(len(R)):
        print(f"O apostador {R[ganhadores][0]} fez {R[ganhadores][-1]} acertos.")
    print(f"Porcentagem de apostadores que acertaram entre 10 e 13 é {(dez_a_treze/len(R))*100:.2f}")
    print(f"A porcentagem que acertaram menos de 10 é {(menosDez/len(R))*100:.2f}")

def main():
    G=[]
    R=[]
    for i in range(13):#13
        g=int(input(f"Digite o {i+1}º número do gabarito da loteria: "))
        G.append(g)
    for apostador in range(10):#10
        nome=input(f"Digite o nome do {apostador+1}º apostador: ")
        R.append([nome])
        for k in range(13):#13
            r=int(input(f"Digite o {k+1}º número do gabarito da loteria de {nome}: "))
            R[apostador].append(r)
    resultado(G,R)


main()

