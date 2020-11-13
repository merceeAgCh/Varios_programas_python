# for iterator in sequence :
#    Bloque

# range(de A. hasta B, decuantao en cuanto C)
# 100 E(Sigma) i=3 | 2 * i =

s = 0
rango = range(3, 101)  # 101 por que el ultimo valor no lo toca
valo = 0;

for s in rango:  # acumulador !!!!
    valo = valo + (2 * s)

print('Sumatoria de los elementos de un rango de (3,101) su sumatoria es : ' + str(valo))
i = 0
num = 0;
acum = 0;
for i in range(1, 21):
    if i % 3 == 0:
        acum = acum + i
print('\nLa sumatoria de los primeros 20 multiplos de 3 : ' + str(acum))

acum = 0

i = 0
num = 0;
acum = 0;
for i in range(1, 21):
    if i % 4 == 0:
        acum = acum + i
print('La sumatoria de los primeros 20 multiplos de 4 : ' + str(acum))

i = 0
num = 0;
acum = 0;
for i in range(1, 21):
    if i % 5 == 0:
        acum = acum + i
print('La sumatoria de los primeros 20 multiplos de 5 : ' + str(acum))
