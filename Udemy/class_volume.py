class Cylinder:
    
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        p = 3.14
        return p*(self.radius**2)*self.height
    
    def surface_area(self):
        p = 3.14
        xarisxi = 2*(p*self.radius**2)
        return xarisxi + 2*(p*self.radius*self.height)

c = Cylinder(2,3)

print('Volume = ',c.volume())
print('Surface Area = ',c.surface_area())