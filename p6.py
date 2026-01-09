class Contact: 
    def __init__(self, n, c):
        self.name = n
        self.contakt = c
    def show(self):
        print(f"ismi:{self.name},numeri:{self.contakt}")
c1 = Contact("ali","+998956585455")
c1.show() 

c2 = Contact("vali","+998955819878")
c2.show() 

c3 = Contact("alish","+998956563212")
c3.show() 