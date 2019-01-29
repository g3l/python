def grades():
    return range(4,11)

def result(passedw):
    return "You passed with: %i0 percent" % passedw

def everything():
    igot = grades()
    for x in igot:
        print (result(x))

everything()

