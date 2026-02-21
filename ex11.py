"""
11. Faça um algoritmo que leia 2 listas A[10] e B[10]. A seguir, crie uma 
lista C que seja a intersecção de A com B e mostre esta lista C. Obs.: 
Intersecção é quando um valor estiver nas duas listas.  Considere que 
não há elementos duplicados em cada uma das listas. 
"""

def interseccao(A,B):
    C=[]
    for l in range(10):
        for k in range(10):
            if A[l]==B[k]:
                C.append(B[k])
    return C
def main():
    A=[]
    B=[]
    for i in range(10):
        a=int(input(f"Digite o {i+1}º valor da lista A: "))
        b=int(input(f"Digite o {i+1}º valor da lista B: "))
        A.append(a)
        B.append(b)
    C=interseccao(A,B)
    print(f"A lista A={A} e a lista B={B}\n possui a seguinte intersecção: {C}")

main()
