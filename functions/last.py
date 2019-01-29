def jobroles():
    return "decant", "Each Recieve", "Prep", "Docks", "Reactives"

def addwords(ican):
    return "At amazon i can work in the %s area" % ican

def buildjobs():
    jobs = jobroles()
    for x in jobs:
        print (addwords(x))

buildjobs()
