import random

#A2
random.seed('propra')

#A3
random_float = random.uniform(-10, 10)
print("[-10,10]:", random_float)

#A4
list_rand = []
for i in range(4):
    list_rand.append(random.randint(-1000,1000))
print("-1000 .. 1000:", list_rand)

#A5
list_normal_verteilugn = []
for i in range(5):
    list_normal_verteilugn.append(random.gauss(10, 3))
print("normalverteilt:" ,list_normal_verteilugn) 

#A6
def permute(list):
    list_permutiert = []
    for i in range(len(list)):
        x = random.choice(list)
        if x not in list_permutiert:
            list_permutiert.append(x)
        else: 
            permute(list)
    return list_permutiert
permut_list = permute(list_rand)
print("permutiert:", permut_list)

#A7
print("davon 2:", random.choices(permut_list, k = 2))

#A8
def throw_dice (k, n):
    return random.choices(range (1, n + 1), k=k)
result = throw_dice(3, 6)
print(result)

#A9
def throw_dice_ntimes (n):
    array2 = []
    for i in range(n):
        array = throw_dice(3, 6)
        array2.append(array)
    return array2

print ("Würfeln:" , throw_dice_ntimes(10))