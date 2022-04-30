case = int(input())
const = ""
#Вот и всё





if(case == 1):
    case = input()
    result = list(map(int, case.split()))
    i = 0
    const = 0
    while(i != len(result)):
        if(const < result[i]):
            const = result[i]
        i += 1
if(case == 2):
    case = input()
    result = list(map(int, case.split()))
    print(result)
    i = 0
    const = 0
    while (i != len(result)):
        if (0 < result[i]):
            const += 1
        i += 1
if(case == 3):
    case = input()
    result = ". , : ; ! _  *  - + ( ) / # ¤ % &".split()
    numbers = "0 1 2 3 4 5 6 7 8 9".split()
    letter = "q w e r t y u i o p a s d f g h j k l z x c v b n m".split()
    i = 0
    while(i < len(result)):
        if(case == result[i]):
            const = "знак припинания"
        i += 1
        if (const != ""):
            break
    i = 0
    while(i < len(numbers)):
        if (case == numbers[i]):
            const = "цифра"
        i += 1
        if (const != ""):
            break
    i = 0
    while (i < len(letter)):
        if (case == letter[i]):
            const = "буква"
        i += 1
        if (const != ""):
            break
if(case == 4):
    case = input().split('.')
    if(len(case) <= 1 ):
        const = "Натуральное число"
    else: const = "Вас обманули"


# Дано: три целых числа.
# Требуется: определить, существует ли треугольник с заданными длинами сторон.
if(case == 5):
    case = input().split()
    i = 0
    while(i < 3):
        if(int(case[i%3])<(int(case[(i+1)%3])+int(case[(i+2)%3]))):
            const = "Треугольник существует"
        else:
            const = "Треугольника не существует"
            break
        i += 1

# Дано: шестизначное целое число.
# Требуется: определить, является ли это число "счастливым билетиком"
if(case == 6):
    case = input().split()
    if((int(case[0]) + int(case[1]) + int(case[2])) - (int(case[3]) + int(case[4]) + int(case[5])) == 0):
        const = "Счастливый белет"
    else: const = "Жаль"


#  Дано: действительные положительные числа а, b, с, х, у.
# Требуется: определить, пройдет ли кирпич с ребрами а, b, с в прямоугольное отверстие со сторонами х и у. Просовывать кирпич в отверстие разрешается только так, чтобы каждое из его ребер было параллельно или перпендикулярно каждой из сторон отверстия
if(case == 7):
    case = input().split()
    gold = []
    if(int(case[0]) < int(case[3]) or int(case[1]) < int(case[3]) or int(case[2]) < int(case[3])):
        i = 0
        while(i < 3):
            if(int(case[i]) <= int(case[3])):
                gold.append(i)
            i += 1
    silver = []
    if (int(case[0]) < int(case[4]) or int(case[1]) < int(case[4]) or int(case[2]) < int(case[4])):
        i = 0
        while (i < 3):
            if (int(case[i]) <= int(case[4])):
                silver.append(i)
            i += 1
    print(gold)
    print(silver)
    if(len(gold) == len(silver)):
        if((len(gold) >= 2 and len(silver) >= 1) or (len(gold)>= 1 and len(silver) >= 2)):
            const = "кирпич пройдёт"
        elif(len(gold) == 1 and len(silver)  == 1):
                if(gold[0] != silver[0]):
                    const = "кирпич пройдёт"
                else: const = "кирпич не пройдёт"
        else:
             const = "кирпич не пройдёт"
    elif(len(gold) != 0 and len(silver) != 0):
        const = "кирпич пройдёт"
    else:
        const = "кирпич не пройдёт"
print(const)