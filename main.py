def Recurs(n):
    StrNumber = str(n)
    if len(StrNumber) > 1:
        first = int(StrNumber[0])
        return first * Recurs(int(StrNumber[1:]))
    else:
        return int(StrNumber)
Fin = Recurs(401)
print(Fin)