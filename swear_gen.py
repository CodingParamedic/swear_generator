import random

desc = ['mealy-mouthed', 'scale-eyed', 'stump-legged', 'sweaty-handed', 'stooped-shouldered']
action = ['turd-licking', 'fart-smelling', 'grass-eating', 'table-licking', 'trout-touching']
final = ['turd-burgler', 'crotch-pheasant', 'deer-sucker', 'wall-licker', 'paint-smeller']

turned_on = True

class Build():

    def __init__(self,desc,action,final):
        self.desc = desc
        self.action = action
        self.final = final

    def __str__(self):
        return self.desc + self.action + self.final

class Insult():

    def __init__(self):
        self.insult = []

        for descs in desc:
            for actions in action:
                for finals in final:
                    self.insult.append(desc,action,final)


    def shuffle(self):
        random.shuffle(self.insult)

    def insults(self):
        single_insult = self.insult.pop()

while True:
    print("What did you just say to me?")

    insults = Insult()
    insults.shuffle()

    
