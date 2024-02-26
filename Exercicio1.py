#1) Escreva um programa que peça dois números inteiros e imprima todos os números inteiros entre eles.
def sequenciaDosNumeros():
    num1 = int(input("Digite o primeiro numero: "))
    num2 = int(input("Digite o segundo numero: "))

    num1 +=1
    while(num1<num2):
        print(num1)
        num1+=1

sequenciaDosNumeros()

def sequenciaDosNumerosAlternativa():
    num1 = int(input("Digite o primeiro numero: "))
    num2 = int(input("Digite o segundo numero: "))

    if(num1 < num2):
        for i in range(num1+1, num2):
            print(i)
    elif(num1 > num2):
        for i in range(num1-1, num2, -1):
            print(i)
    else:
        print("numeros nao podem ser iguais!")

sequenciaDosNumerosAlternativa()

# Ponto aprendido:
# Neste caso eu nao precisava do while pq eu sabia exatamente inicio e fim da iteração, funcionou mas ficou feio.
# num1 e num2 nao foram melhores nomes poderia ter chamado incio e fim faria mais sentido.