def bisiesto():
    anyo = int(input("Indica un año: "))

    if anyo % 4 == 0:
        if anyo % 100 == 0:
            if anyo % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

res = bisiesto()
print(res)