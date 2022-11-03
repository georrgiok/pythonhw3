# В файле находятся названия фруктов. Выведите все фрукты, названия которых начинаются на заданную букву.
FILE_NAME = '2_z2_fruits.txt'
try: 
    f = open(FILE_NAME, 'r')
except IOError:
    print('file '+FILE_NAME+' does not exist!')
else:
    letter = raw_input("input: ").lower()
    if 0 < len(letter) < 2:
            fruits_list = f.readlines()
            answer = ''
            for fruit in fruits_list:
                if fruit[0].lower() == letter:
                    answer += fruit
            print(answer)
    else:
        print('u must input just 1 letter')
