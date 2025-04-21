# Функция проверки, что последовательность состоит из одинаковых цифр
def isSameDigits(digits):
    for i in range(1, len(digits)):
        if digits[i] != digits[0]:
            return False
    return True

# Функция проверки, что номер «эксклюзивный»
def checkExclusive(number):
    return isSameDigits(str(number))

# Функция проверки, что номер «бриллиантовый»
def checkDiamond(number):
    string = str(number)
    if (isSameDigits(string[1:]) or
        isSameDigits(string[: len(string)-1])):
        return True
    else:
        return False

# Функция проверки, что номер «сапфировый»
def checkSapphire(number):
    string = str(number)
    length = len(string)
    middle = length // 2

    if (isSameDigits(string[0 : middle]) and
        isSameDigits(string[middle : length]) and
        string[0] != string[length - 1]
       ) or \
       (length % 2 == 1 and
        isSameDigits(string[0 : middle + 1]) and
        isSameDigits(string[middle + 1: length]) and
        string[0] != string[length - 1]
       ):
        return True
    else:
        return False

# Функция для проверки ВАШЕГО «красивого» номера
def checkBeautiful(number):
    string = str(number)
    length = len(string)
    if length < 5:
        return False
    count = 1
    maximum = 0
    for j in range(length - 1):
        if int(string[j]) - int(string[j + 1]) == 1:
            count += 1
            maximum = max(count, maximum)
        else:
            count = 1
    if maximum >= 5:
        return True
    return False

