def is_luhn_valid(n):
    arrDigit = []
    i = n
    n_digits = 0
    while i > 0:
        n_digits += 1
        arrDigit.append(i % 10)
        i = int(i / 10)

    arrDigit.reverse()
    
    ans = 0

    if n_digits % 2 == 0:
        for i in range(n_digits):
            if i % 2 == 0:
                t = 2 * arrDigit[i]
                if (t > 9):
                    t -= 9
            else:
                t = arrDigit[i]

            ans += t
    else:
        for i in range(n_digits):
            if i % 2 != 0:
                t = 2 * arrDigit[i]
                if (t > 9):
                    t -= 9
            else:
                t = arrDigit[i]

            ans += t
            
    if ans % 10 == 0:
        return True
    return False

print(is_luhn_valid(int(input())))

