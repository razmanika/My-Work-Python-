

# product_d = {}

# with open('product.txt') as f:
#     for line in f:
        
#         (key,limit,price) = line.split()
#         product_d[str(key)] = [limit , price]
# ass = product_d[str(key)] = int(limit) - int(limit)/100*10



# print(product_d.values[0])


class Circule():
    pi = 3.14

    def __init__(self,radious = 1):
        self.radious = radious

    def raga(self):
        return self.radious * Circule.pi * 2


class Damp(Circule):
    def __init__(self):
        Circule.__init__(self)
    
    def mamala(self):
        print(Circule.pi * 10)
    def raga(self):
        print(self.radious)


assw = Damp()
print(assw.raga())