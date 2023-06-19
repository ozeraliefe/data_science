#ÖZERALİ BURKAZ 21831088
import random

my_city = []
n = 1
for i in range(1, 5445001):
    my_city.append(n)
    n += 1

infected = []
infected.append(random.choice(my_city))

def make_people_infected():
    num = len(infected)
    day = 0
    while day < 20:
        while num != len(my_city)//2:
            x = random.choice(my_city)
            y = random.randint(14,28)
            z = 0
            for j in range(1,len(infected)+1):
                hmp = random.randint(1,10)#How many people will get infected
                for k in range(1,hmp+1):
                    if random.randint(1,5) == 1:#20% possibility to make infected someone
                        if x not in infected:
                            infected.append(x)
                        elif y == day:
                            del infected[0+z]
                            z += 1
                        else:
                            continue
                    else:
                        continue
        day += 1
    while day >= 20:
        while num != len(my_city)//2:
            x = random.choice(my_city)
            y = random.randint(14,28)
            z = 0
            for j in range(1,len(infected)+1):
                possibilities = random.randint(1,100)
                if possibilities <= 25:
                    for k in range(1,2):
                        if random.randint(1,5) == 1:
                            if x not in infected:
                                infected.append(x)
                            elif y == day:
                                del infected[0+z]
                                z += 1
                            else:
                                continue
                        else:
                            continue
                elif possibilities <= 37:
                    for k in range(1,3):
                        if random.randint(1,5) == 1:
                            if x not in infected:
                                infected.append(x)
                            elif y == day:
                                    del infected[0+z]
                                    z += 1
                            else:
                                continue
                        else:
                            continue
                elif possibilities <= 42:
                    for k in range(1,4):
                        if random.randint(1,5) == 1:
                            if x not in infected:
                                infected.append(x)
                            elif y == day:
                                del infected[0+z]
                                z += 1
                            else:
                                continue
                        else:
                            continue
                elif possibilities <= 45:
                    for k in range(1,5):
                        if random.randint(1,5) == 1:
                            if x not in infected:
                                infected.append(x)
                            elif y == day:
                                del infected[0+z]
                                z += 1
                            else:
                                continue
                        else:
                            continue
                elif possibilities <= 47:
                    for k in range(1,6):
                        if random.randint(1,5) == 1:
                            if x not in infected:
                                infected.append(x)
                            elif y == day:
                                del infected[0+z]
                                z += 1
                            else:
                                continue
                        else:
                            continue
                elif possibilities == 48:
                    for k in range(1,7):
                        if random.randint(1,5) == 1:
                            if x not in infected:
                                infected.append(x)
                            elif y == day:
                                del infected[0+z]
                                z += 1
                            else:
                                continue
                        else:
                            continue
                elif possibilities == 49:
                    for k in range(1,8):
                        if random.randint(1,5) == 1:
                            if x not in infected:
                                infected.append(x)
                            elif y == day:
                                del infected[0+z]
                                z += 1
                            else:
                                continue
                        else:
                            continue
                elif possibilities == 50:
                    for k in range(1,9):
                        if random.randint(1,5) == 1:
                            if x not in infected:
                                infected.append(x)
                            elif y == day:
                                del infected[0+z]
                                z += 1
                            else:
                                continue
                        else:
                            continue
                elif possibilities == 51:
                    for k in range(1,10):
                        if random.randint(1,5) == 1:
                            if x not in infected:
                                infected.append(x)
                            elif y == day:
                                del infected[0+z]
                                z += 1
                            else:
                                continue
                        else:
                            continue
                elif possibilities == 52:
                    for k in range(1,11):
                        if random.randint(1,5) == 1:
                            if x not in infected:
                                infected.append(x)
                            elif y == day:
                                del infected[0+z]
                                z += 1
                            else:
                                continue
                        else:
                            continue
                else:
                    continue
    day += 1


    print("How many day requires for to become infected half of the city?")
    print(day)

make_people_infected()



