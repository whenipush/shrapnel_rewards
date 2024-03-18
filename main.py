from random import uniform, randint

bet = int(input("Ставка: "))
proccent = int(input("Процент: "))





CONST = 999999
kek = randint(0, CONST)

win = bet * 100 / proccent

minn = int(uniform(0, CONST / 100 * proccent))
maxx = int(uniform(CONST - (CONST / 100 * proccent), CONST))

# print(zone_minn, zone_maxx)
choice = int(input("0 - минимум, 1- максимум:  "))
if choice == 1:
    if kek >= CONST-(CONST/100*proccent):
        print(f'Ты выиграл: {win}')
    else:
        print('Проигрыш')


