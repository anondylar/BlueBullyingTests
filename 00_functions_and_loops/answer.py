def fizz_buzz(n):
    s = ""
    for i in range(1, n + 1):
        isdiv3 = (i % 3) == 0
        isdiv5 = (i % 5) == 0

        if isdiv3:
            s += "Fizz"
        
        if isdiv5:
            s += "Buzz"

        if not (isdiv3 or isdiv5):
            s += str(i)

        s += '\n'

    return s

def cirno_mult(x, y):
    x = str(x)
    return int(x * y)

def calc_best_dpm(guns):
    best_gun = ''
    best_dpm = -1

    for gun in guns:
        name, damage, shots_per_min = gun
        current_gun_dpm = damage * shots_per_min
        if current_gun_dpm > best_dpm:
            best_dpm = current_gun_dpm
            best_gun = name

    return best_gun