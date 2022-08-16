var1 = int(input('Primeiro valor: '))
var2 = int(input('Segundo valor: '))

if var1 > var2:
    maior = var1
else:
    maior = var2

for i in range(maior):
    aux = var1 * i
    if (aux % var2) == 0:
        mmc = aux

print('MMC: ',mmc)