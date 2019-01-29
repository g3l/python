class neryo:
    cust_name = ""
    cust_phone = 0
    where = ""
    date_req = 0
    doors = 0

    def washrequest(self):
        wash_desc = "Name: %s Phone Number: %i Wash Location: %s Date: %s Number of car Doors: %i" % (self.cust_name, self.cust_phone, self.where, self.date_req, self.doors)
        return wash_desc

cust1 = neryo()
cust1.cust_name = "Peter Lemi"
cust1.cust_phone = 12304123456
cust1.where = "Farnworth"
cust1.date_req = "21/01/2019"
cust1.doors = 5

cust2 = neryo()
cust2.cust_name = "Jake Smith"
cust2.cust_phone = 12304133454
cust2.where = "Halliwell"
cust2.date_req = "19/01/2019"
cust2.doors = 3

print (cust1.washrequest())
print (cust2.washrequest())
