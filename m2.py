k=0
for i in range (0,3):
 x = int(input('3+5='))
 if x==8:
    print('Правильно!')
    k = k+1
    break
 else :
    if x!=8:
            print('Не правильно!')
            k = k -1
    continue
if k==-3:
 print('Игра окончена!вы проиграли!Правильных ответов : 0')
else:
 print('Игра окончена!вы выиграли!Правильных ответов : 1')
