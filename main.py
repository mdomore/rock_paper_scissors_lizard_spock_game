"""

RULES :

rock crushes scissors
rock crushes lizard

paper covers rock
paper disproves spock

scissors cuts paper
scissors decapitates lizard

lizard eats paper
lizard poisons spock

spock vaporizes rock
spock smashes scissors

"""

from tkinter import *
import random

choices = ["rock", "paper", "scissors", "lizard", "spock"]

root = Tk()
root.geometry('600x300')
root.resizable(0, 0)
root.title('Rock,Paper,Scissors,Lizard,Spock')
root.config(bg='#db9581')

global user_score
global comp_score
user_score = 0
comp_score = 0

Label(root, text='Rock, Paper, Scissors, Lizard, Spock', font='arial 24 bold', fg='#246A7E', bg='#db9581').pack()
Label(root, text='Choose any one: Rock, Paper, Scissors, Lizard, Spock', font='arial 15 bold', fg='#246A7E',
      bg='#db9581').place(x=20, y=70)

user_take = StringVar()
Result = StringVar()


def Rock():
    user_take.set("rock")


def Paper():
    user_take.set("paper")


def Scissors():
    user_take.set("scissors")


def Lizard():
    user_take.set("lizard")


def Spock():
    user_take.set("spock")


def Reset():
    global user_score
    global comp_score
    Result.set("")
    user_take.set("")
    comp_pick = ""
    user_score = 0
    user_score_label.config(text="User score : " + str(user_score))
    comp_score = 0
    comp_score_label.config(text="Computer score : " + str(comp_score))


def Exit():
    root.destroy()


def play():
    global user_score
    global comp_score
    comp_pick = random.choice(choices)
    user_pick = user_take.get()
    print("user" + user_pick)
    print("comp" + comp_pick)

    if user_pick == comp_pick:
        Result.set('tie,you both select same')

    elif user_pick == 'rock' and comp_pick == 'paper':
        Result.set('you loose,paper covers rock')
        comp_score += 1
        comp_score_label.config(text="User score : " + str(comp_score))
    elif user_pick == 'rock' and comp_pick == 'scissors':
        Result.set('you win,rock crushes scissors')
        user_score += 1
        user_score_label.config(text="User score : " + str(user_score))
    elif user_pick == 'rock' and comp_pick == 'lizard':
        Result.set('you win,rock crushes lizard')
        user_score += 1
        user_score_label.config(text="User score : " + str(user_score))
    elif user_pick == 'rock' and comp_pick == 'spock':
        Result.set('you loose,spock vaporizes rock')
        comp_score += 1
        comp_score_label.config(text="User score : " + str(comp_score))

    elif user_pick == 'paper' and comp_pick == 'rock':
        Result.set('you win,paper covers rock')
        user_score += 1
        user_score_label.config(text="User score : " + str(user_score))
    elif user_pick == 'paper' and comp_pick == 'scissors':
        Result.set('you loose,scissors cuts paper')
        comp_score += 1
        comp_score_label.config(text="User score : " + str(comp_score))
    elif user_pick == 'paper' and comp_pick == 'lizard':
        Result.set('you loose,lizard eats paper')
        comp_score += 1
        comp_score_label.config(text="User score : " + str(comp_score))
    elif user_pick == 'paper' and comp_pick == 'spock':
        Result.set('you win,paper disproves spock')
        user_score += 1
        user_score_label.config(text="User score : " + str(user_score))

    elif user_pick == 'scissors' and comp_pick == 'rock':
        Result.set('you loose,rock crushes scissors')
        comp_score += 1
        comp_score_label.config(text="User score : " + str(comp_score))
    elif user_pick == 'scissors' and comp_pick == 'paper':
        Result.set('you win,scissors cuts paper')
        user_score += 1
        user_score_label.config(text="User score : " + str(user_score))
    elif user_pick == 'scissors' and comp_pick == 'lizard':
        Result.set('you win,scissors decapitates lizard')
        user_score += 1
        user_score_label.config(text="User score : " + str(user_score))
    elif user_pick == 'scissors' and comp_pick == 'spock':
        Result.set('you loose,spock smashes scissors')
        comp_score += 1
        comp_score_label.config(text="User score : " + str(comp_score))

    elif user_pick == 'lizard' and comp_pick == 'rock':
        Result.set('you loose ,rock crushes lizard')
        comp_score += 1
        comp_score_label.config(text="User score : " + str(comp_score))
    elif user_pick == 'lizard' and comp_pick == 'paper':
        Result.set('you win ,lizard eats paper')
        user_score += 1
        user_score_label.config(text="User score : " + str(user_score))
    elif user_pick == 'lizard' and comp_pick == 'scissors':
        Result.set('you loose ,scissors decapitates lizard')
        comp_score += 1
        comp_score_label.config(text="User score : " + str(comp_score))
    elif user_pick == 'lizard' and comp_pick == 'spock':
        Result.set('you win ,lizard poisons spock')
        user_score += 1
        user_score_label.config(text="User score : " + str(user_score))

    elif user_pick == 'spock' and comp_pick == 'rock':
        Result.set('you win ,spock vaporizes rock')
        user_score += 1
        user_score_label.config(text="User score : " + str(user_score))
    elif user_pick == 'spock' and comp_pick == 'paper':
        Result.set('you loose ,paper disproves spock')
        comp_score += 1
        comp_score_label.config(text="User score : " + str(comp_score))
    elif user_pick == 'spock' and comp_pick == 'scissors':
        Result.set('you win ,spock smashes scissors')
        user_score += 1
        user_score_label.config(text="User score : " + str(user_score))
    elif user_pick == 'spock' and comp_pick == 'lizard':
        Result.set('you loose ,lizard poisons spock')
        comp_score += 1
        comp_score_label.config(text="User score : " + str(comp_score))

    else:
        Result.set('Choose any one - rock, paper, scissors, lizard, spock and hit PLAY !')


# button
Button(root, font='arial 13 bold', text='ROCK', padx=5, fg='#c9e19d', bg='#4273BE', command=Rock).place(x=50, y=120)
Button(root, font='arial 13 bold', text='PAPER', padx=5, fg='#c9e19d', bg='#4273BE', command=Paper).place(x=150, y=120)
Button(root, font='arial 13 bold', text='SCISSORS', padx=5, fg='#c9e19d', bg='#4273BE', command=Scissors).place(x=250,
                                                                                                                y=120)
Button(root, font='arial 13 bold', text='LIZARD', padx=5, fg='#c9e19d', bg='#4273BE', command=Lizard).place(x=380,
                                                                                                            y=120)
Button(root, font='arial 13 bold', text='SPOCK', padx=5, fg='#c9e19d', bg='#4273BE', command=Spock).place(x=480, y=120)

Entry(root, font='arial 10 bold', textvariable=Result, bg='seashell4', width=60, ).place(x=120, y=185)

Button(root, font='arial 13 bold', text='PLAY', padx=5, fg='#c9e19d', bg='#4273BE', command=play).place(x=50, y=180)

Button(root, font='arial 13 bold', text='RESET', padx=5, fg='#c9e19d', bg='#4273BE', command=Reset).place(x=50, y=240)

Button(root, font='arial 13 bold', text='EXIT', padx=5, fg='#c9e19d', bg='#4273BE', command=Exit).place(x=150, y=240)

# Score label
user_score_label = Label(root, text="User score : " + str(user_score), fg='#c9e19d', bg='#4273BE')
user_score_label.place(x=300, y=250)
comp_score_label = Label(root, text="Computer score : " + str(comp_score), fg='#c9e19d', bg='#4273BE')
comp_score_label.place(x=400, y=250)

root.mainloop()
