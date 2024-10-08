# Python-Function-Arguments-Basic

F1: Ein Parameter ist ein Platzhalter, der in der Funktionsdefinition genutzt wird und ein Argument ist der Wert, mit dem die Funktion aufgerufen wird.

---

F2:

Positionsargument: Wenn eine Funktion mit einem Positionsargument aufgerufen wird, werden die Argumente den Parametern in der Reihenfolge zugeordnet, in der Sie stehen.

```Python
def foo(a, b, c):
    print(a, b, c)

foo(1, 2, 3)
```

Schlüsselargument: Wenn eine Funktion mit einem Schlüsselargument aufgerufen wird, werden die Argumente den Parametern gemäß der Schlüssel zugeordet.

```Python
def foo(a, b, c):
    print(a, b, c)

foo(c=3, a=1, b=2)
```

Die Aussage stimmt. Eine Funktion kann eintweder mit Schlüssel- oder Positionsargumenten aufgerufen werden. Die beiden Typen können auch bedingt mit einander kombiniert werde, solange kein Positionsargument nach einem Schlüsselargument folgt.

```Python
def foo(a, b, c):
    print(a, b, c)

foo(1, 2, c=3)
```

Dieser Aufruf würde grundsätzlich funktionieren, aber folgender nicht.

```Python
def foo(a, b, c):
    print(a, b, c)

foo(a=1, 2, 3)
```

---

F3: In der Funktionsdefinition können für Parameter Standardwerte festgelegt werden. Beim Funktionsaufruf gelten sie eher als Schlüsselwortargument, da sie mit ihrem Schlüsselwort an die Funktion übergeben werden. Außerdem ähnelt die Syntax den Schlüsselwortargumenten.

---

F4:

1:

```Python
def foo(a, b, c):
    return a+b+c
print(foo(1, 2, 3))
```

2:

```Python
def foo(a, b, c):
    return a+b+c
print(foo(1, 2, c=3))
```

3:

```Python
def foo(a, b, c=0):
    return a+b+c
print(foo(a=1, b=2, c=3))
```

---

F5: Positionsargumente sollen vor Schlüsselwortargumenten kommen, damit eindeutig ist, welcher Wert, welchem Parameter zugeordnet werden soll. Außerdem verbessert es die Lesbarkeit.

---

F6:

1: Der / sorgt dafür, dass alle Argumente vor dem / zwangsläufig als Positionsargumente übergeben werden

```Python
def taschenrechner(a, b, op, /)
```

2: Der * sorgt dafür, dass alle Argumente zwangsläufig als Schlüsselwortargumente übergeben werden müssen.

```Python
def taschenrechner(*, a, b, op)
```

3:

```Python
def taschenrechner(a, b, /, *, op)
```

Variante 3. erscheint mir am sinnvollsten, da hier eindeutig ist welcher Operator verwendet wird. Das fördert die Lesbarkeit.

---

F7:

1. Hier würde ich nur Schlüsselwortargumente verwenden um die Eindeutigkeit zu wahren.

2. Hier würde ich den text als Positionsargument angeben und die restlichen Werte als Schlüsselwortargument um auch hier Mehrdeutigkeit zu vermeiden, da mehrere Argumente gleiche Werte annhmen können.

3. Hier reichen Positionsargumente aus, denn wenn die Funktion gut geschrieben ist, ist es egal, in welcher Reihenfolge die Seitenlängen angegeben sind.
