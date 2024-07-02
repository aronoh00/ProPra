import operator

what = "Tupel von Alter, Gewicht, Körpergröße"
data = [
    (22, 69, 177,), 
    (22, 71, 172,), 
    (48, 72, 174,), 
    (38, 89, 179,), 
    (71, 59, 170,), 
]

#A2
data1 = sorted(data)

#A3
def hight(mytuple: tuple[int, int, int]) -> int:
    return mytuple[2]
datah = sorted(data, key=hight)

#A4
data3 = sorted(data, key=operator.itemgetter(2))

#A5
def excess_weight(mytuple: tuple[int, int, int]) -> int:
    age, weight, height = mytuple
    normal_weight = height - 100
    return weight - normal_weight
data4 = sorted(data, key=excess_weight)

#A6
class MyTuple(tuple):
    def __lt__(self, other) -> bool:
        g = 172
        if self[2] <= g and other[2] > g:
            return True
        else:
            return tuple(self) < tuple(other)

data2 = [MyTuple(t) for t in data]
data2.sort()

print(what)
print(data)
print("Sortiert:")
print(data1)  # Schritt 1
print("Sortiert nach Körpergröße 1:")
print(datah)  # Schritt 2
print("Sortiert nach Körpergröße 2:")
print(data3)  # Schritt 3
print("Sortiert nach Übergewicht:")
print(data4)  # Schritt 4
print("Sortiert in Gewichtsgruppen:")
print(data2)  # Schritt 5
