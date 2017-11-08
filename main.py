import Tkinter as tk
import tkFileDialog
import pandas as pd
import xlrd
from random import randint
import sys
import tkinter.messagebox




#repeat = 0
class App(tk.Tk):

    global teamType
    global nPeople
    global entry
    global nTeams
    global firstNames
    global teams
    global nameList
    
    def __init__(self):
        tk.Tk.__init__(self) # create window
        self.filename = "" # variable to store filename
        global teamType
        global nPeople
        global entry
        teamType = tk.IntVar()
        nPeople = 0
        tk.Button(self, text='Choose Name List', command=self.openfile).pack()
        
        tk.Radiobutton(self, text="Different skill levels", variable=teamType, value=1).pack(anchor=tk.W)
        tk.Radiobutton(self, text="The same skill level", variable=teamType, value=2).pack(anchor=tk.W)
        tk.Radiobutton(self, text="Different grades/ages", variable=teamType, value=3).pack(anchor=tk.W)
        tk.Radiobutton(self, text="Same grade/ages", variable=teamType, value=4).pack(anchor=tk.W)
        tk.Radiobutton(self, text="Randomly with no criterion", variable=teamType, value=5).pack(anchor=tk.W)

        # tk.Entry(self, text="Enter number of people per team:", variable=nPeople).pack()
        tk.Label(text='Enter number of people per team: ').pack()
        entry = tk.Entry(self, width=2)
        entry.pack()
        entry.focus_set()


        tk.Button(self, text='Generate Team!', command=self.randomize).pack()

        self.mainloop() 


    def openfile(self):
        self.filename = tkFileDialog.askopenfilename(title="Open file")
       # self.filename = "Users/jacobpashman/Documents/RandomTeamGenerator/names.xlsx"
    def randomize(self):
        global repeat
        global nPeople
        global entry
        global nTeams
        global teamType
        global firstNames
        global teams
        global nameList
        df = pd.read_excel("/Users/jacobpashman/Documents/RandomTeamGenerator/names.xlsx")
        nameList =  df.as_matrix()
        firstNames = []
        for i in range(len(nameList)):
            if i>0 and i<len(nameList):
                print nameList[i][0]
                firstNames.append(nameList[i][0])

        nPeople = int(entry.get())
        nTeams=0
        if len(firstNames) / float(nPeople) == len(firstNames) / int(nPeople):
            nTeams = len(firstNames) / int(nPeople)
        else:
            nTeams = len(firstNames) / int(nPeople) + 1
        print "n teams:", nTeams
        teams = []

        print 'teamtype', teamType.get()
        if teamType.get() == 1:
            randomDifferentSkills()
        if teamType.get() == 5:
            randomNoCriteria()

        print 'teams:', teams
        for i in range(nTeams):
            teamN = 'team #' + (str(i + 1))
            tk.Label(text=teamN).pack()
            for j in range(nPeople):
                tk.Label(text=teams[i][j]).pack()
            


def randomNoCriteria():
    global repeat
    global nPeople
    global entry
    global nTeams
    global teamType
    global firstNames
    global teams

    for i in range(nTeams):
            team = []
            for j in range(nPeople):
                if len(firstNames) > 0:
                    randomPerson = randint(0, len(firstNames) - 1)
                    team.append(firstNames[randomPerson])
                    firstNames.pop(randomPerson)
                print 'random person:', randomPerson
            print 'team:', team
            teams.append(team)

def randomDifferentSkills():
    global repeat
    global nPeople
    global entry
    global nTeams
    global teamType
    global firstNames
    global teams

    skills = []
    for i in range(len(nameList)):
         if i > 0 and i < len(nameList):
            print nameList[i][3]
            skills.append([(nameList[i][0]), (nameList[i][3])])
    print 'skills:', skills

    for i in range(nTeams):
            team = [[u'hfjgvukdfdjdf', 3456789098765]]
            for j in range(nPeople):
                if len(firstNames) > 0: 
                    randomPerson = randint(0, len(firstNames) - 1)
                    print 'random person', randomPerson
                    # print 'skills random', skills[randomPerson][1]
                    # print 'team #1', team[0][1]
                    while skills[randomPerson][1] == team[0][1] and len(firstNames) > (nPeople - 1):
                        randomPerson = randint(0, len(firstNames) - 1)
                    if team == [[u'hfjgvukdfdjdf', 3456789098765]]:
                        team = [skills[randomPerson]]
                    else:
                        team.append(skills[randomPerson])
                    firstNames.pop(randomPerson)
                print 'random person:', randomPerson
            print 'team:', team
            teams.append(team)


if __name__ == '__main__':
    App()
