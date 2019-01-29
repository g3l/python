def girls():
    return "Meling", "Recho", "Faith", "Sophie", "Lucy"

def gender(x):
    return "%s is a girl" % x

def everything():
    x = girls()
    for y in x:
        print(gender (y))

everything()
