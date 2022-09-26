class partyan:
    x = 0
    def animal(self):
        self.x = self.x + 1
        print(self.x)
an = partyan()
an.animal()
an.animal()
an.animal()

print("dir", dir(an))
# dir busca capacidades

# cicyle life object

print("/n")
class PartyAnimal:
    x = 0
    name = ''
    def __init__(self, nam):
        self.name = nam
        print(self.name,'constructed')
    def party(self):
        self.x = self.x + 1
        print(self.name,'party count',self.x)

q = PartyAnimal('Quincy') #son 2 intancias independientes
m = PartyAnimal('Miya')

q.party()
m.party()
q.party()
