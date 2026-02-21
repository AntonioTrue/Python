"""10. Faça um algoritmo que leia um lista G[5] que contém a letra certa 
da resposta de uma prova que constou de 5 questões objetivas.  A seguir 
leia 15 nomes de alunos e de listas R[5], que seriam as respostas de cada
aluno para as questões, da letra A até a letra E, sendo que deve ser lido 
um nome de aluno e um lista de respostas por vez. Para cada aluno, mostre 
o seu nome, número de acertos e a sua nota, sendo que todas as questões 
têm o mesmo valor (2 pt). """

"""def pauta(G,R,pontos=0):
    for aluno in range(len(R)):
        pontos=0
        for nota in range(len(G)):
            if(R[aluno][nota+1]==G[nota]):
                pontos+=2
        print(f"O/A aluno(a) {R[aluno][0]} obteve {pontos} pontos com {int(pontos/2)} acertos")

def main():
    G=[] #gabarito
    R=[] #alunos e suas respostas
    for i in range(5):
        g=input(f"Digite a {i+1}º letra correta das respostas: ")
        G.append(g)
    for a in range(1): #range(15)
        aluno=input(f"Digite o nome do {a+1}º aluno: ")
        R.append([aluno])
        for b in range(5):
            respostas=input(f"Agora digite a {b+1}º resposta de {aluno}: ")
            R[a].append(respostas)
    pauta(G,R)
main()"""







def pauta(G,R,pontos=0):
    for aluno in range(len(R)):
        pontos=0
        for nota in range(len(G)):
            if(R[aluno][nota+1]==G[nota]):
                pontos+=2
        R[aluno].append(pontos)
    for i in range(len(R)):
        print(f"O/A aluno(a) {R[i][0]} obteve {R[i][-1]} pontos com {int(R[i][-1]/2)} acertos")

def main():
    G=[] #gabarito
    R=[] #alunos e suas respostas
    for i in range(5):
        g=input(f"Digite a {i+1}º letra correta das respostas: ")
        G.append(g)
    for a in range(1): #range(15)
        aluno=input(f"Digite o nome do {a+1}º aluno: ")
        R.append([aluno])
        for b in range(5):
            respostas=input(f"Agora digite a {b+1}º resposta de {aluno}: ")
            R[a].append(respostas)
    pauta(G,R)
main()
