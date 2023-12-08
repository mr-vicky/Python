class Cutomer:
    
    def __init__(self, id, name, bdno, bstreet, bcity, bcountry, bpin, sdno, sstreet, scity, scountry, spin):
        self.id = id
        self.name = name
        self.bAddress = self.Address(bdno, bstreet, bcity, bcountry, bpin)
        self.sAddress = self.Address(sdno, sstreet, scity, scountry, spin)

    class Address:

        def __init__(self, dno, street, city, country, pin):
            self.dno = dno
            self.street = street
            self.city = city 
            self.country = country
            self.pin = pin

        def display(self):
            print(self.dno)
            print(self.street)
            print(self.city)
            print(self.country)
            print(self.pin)

if __name__=='__main__':
    c1 = Cutomer(1, "MrVicky", 12, "abc", "Mumbai", "India", 100001, 20, "xyz", "Delhi", "India", 100002)
    print("Billing Address: ")
    c1.bAddress.display()
    print()

    print("Shipping Address: ")
    c1.sAddress.display()