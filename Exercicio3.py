#3) Para tratar uma quantidade de 15 dados de avaliações de pessoas usuárias de um serviço da empresa, precisamos verificar se as notas são válidas. Então, escreva um programa que vai receber a nota de 0 a 5 de todos os dados e verificar se é um valor válido. 
#Caso seja inserido uma nota acima de 5 ou abaixo de 0, repita até que a pessoa usuária insira um valor válido.

for i in range(1,16):
    nota = float(input("Digite uma nota: "))
    while (nota > 5 or nota < 0):
        nota = float(input(f'Nota inválida, insira novamente a nota da pessoa usuária {i}: '))
    print(f'Nota dada: {nota}, total de {i} votos de 15')


#Pontos aprendidos:
#Estava no caminho certo porem estava usando | e nao or e por isso nao dava certo o que levou a gastar tempo com if, break e continue mas nao precisou.