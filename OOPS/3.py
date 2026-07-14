class Cricket:
    TotalScore:int = 0
    def getScore(self,personalscore): #non static method can be accessed object
        self.personalscore =personalscore
        Cricket.TotalScore += self.personalscore
        print(f'Personal Score : {self.personalscore}')
        print(f'TotalScore : {Cricket.TotalScore}')
print("=================virat===========")
virat = Cricket()
virat.getScore(0)
virat.getScore(50)
print("===============Rothit===========")
Rohit = Cricket()
Rohit.getScore(0)
Rohit.getScore(40)