class Football:
    team = "ABC"
    def __init__(self,name, age, height, weight):
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight

    def  get_age(self):
        print(f"Age of {self.name} is {self.age} and Team is {self.team}")

    def get_height(self):
        print(f"Height of {self.name} is {self.height}cms")

    def  get_weight(self):
        print(f"Weight of {self.name} is {self.weight}kg")

football = Football("David",25,175,45)
football.get_age()
football.get_height()
football.get_weight()
        
# print("\n*******************")

# player2 = Football("Disha",22,150,42)
# player2.get_age()
# player2.get_height()
# player2.get_weight()