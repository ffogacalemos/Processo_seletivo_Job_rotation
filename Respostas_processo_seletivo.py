#exercicio 1
#resposta = 91

#exercicio 2
def chk_fib(n):
    i = 0
    j = 1

    while 1:
        if j == n or i == n:
            return 1
        if j > n:
            return 0
        i = j+i
        j = i+j
#exercicios 3
#a) 9
#b) 128
#c) 49
#d) 100
#e) 13
#f) 200

#exercicios 4
#Todos os dados na pergunta são irrelevantes, se você tem dois pontos A e B, e tem duas incôgnitas atravessando ela, na momento que ambas se
#encontram, elas estão tão próximas de A quanto de B, pois estão no mesmo local na mesma distância



#exercicio  5
def revstring():
    s = "abcdefghijklmnopqrstuvwxyz"

    for i in range(len(s)-1, -1, -1):
        print(f"{s[i]}", end='')
