class fruit:
    def __init__(self,name,color,price,seed):
        self.name=name
        self.color=color
        self.price=price
        self.seed=seed
Apple=fruit ('Apple','Red',45,True)
Banana=fruit('Banana','White',35,False)
Mango=fruit('Mango','Yellow',55,True)
print(Apple.name)
print(Banana.color)
print(Mango.seed)
        
