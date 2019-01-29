class decant:
    tote = ""
    tote1 =  ""
    tote2 = ""
    tote3 = ""

    def scansph(self):
        dec_items = "Tote1: %s Tote2: %s Tote3: %s Tote4: %s" % (self.tote, self.tote1, self.tote2, self.tote3)
        return dec_items

staff1 = decant()
staff1.tote = "150 items per hr"
staff1.tote1 = "93 items per hr"
staff1.tote2 = "100 items per hr"
staff1.tote3 = "47 items per hr"

print (staff1.scansph())

def assocs():
    return "Elena", "Josh", "Muddy", "Zeshan"

def roles(today):
    return "%s is working on decant today!" % today

def assocrole():
    mornin = assocs()
    for x in mornin:
        print (roles(x))

assocrole()

dicso = {    
    "Elena" : 1234,
    "Josh" : 1235,
    "Muddy" : 1236,
    "Zeshan" : 1237
    }

if "Muddy" in dicso:
    print ("Muddy is in the dictionary")
    print ("Number: %d" % dicso["Muddy"])
