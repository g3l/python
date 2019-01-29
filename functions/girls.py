def  listgirls():
    return "Jessica Lemi", "Joy Lemi", "Janet Lemi", "Judith Lemi"

def defgender(gender):
    return "%s = girl" % gender

def allin():
    girls = listgirls()
    for y in girls:
        print (defgender(y))

allin()
