# 2) Escreva um programa para calcular quantos dias levará para a colônia de uma bactéria A ultrapassar ou igualar a colônia de uma bactéria B, 
# com base nas taxas de crescimento de 3% e 1,5% respectivamente. Considere que a colônia A inicia com 4 elementos e a B com 10.

coloniaA = 4
coloniaB = 10

taxaColoniaA = 0.03
taxaColoniaB = 0.015
dias = 0

while(coloniaA<coloniaB):
    coloniaA = coloniaA * (1+taxaColoniaA)
    coloniaB = coloniaB * (1+taxaColoniaB)
    dias += 1

print(dias)

# Pontos aprendidos:
# tentei colocar um if aqui para so printar quando terminasse o while mas nao deu certo e nao precisava