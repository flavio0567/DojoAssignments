'''
Draw Star Assignment '''

# Part I

def draw_stars(arr):
    for i in arr:
        k = 0
        str = ''
        while k < i:
            str += '*'
            k += 1
        print(str)

x = draw_stars([4, 6, 1, 3, 5, 7, 25])

# Part II

def draw_stars2(arr):
    for i in arr:
        k = 0
        str_l = ''
        if isinstance(i, str):
            while k < len(i):
              str_l += i[0].lower()
              k += 1
            print(str_l)
        elif isinstance(i, int):
            while k < i:
                str_l += '*'
                k += 1
            print(str_l)

x = draw_stars2([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])
