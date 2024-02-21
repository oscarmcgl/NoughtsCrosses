import time
import random
import turtle 

import json
import score


playing = True 


a = "1"
b = "2"
c = "3"
d = "4"
e = "5"
f = "6"
g = "7"
h = "8"
i = "9"


pick = 0
taken = []




    # 1/a | 2/b | 3/c
    #--------
    # 4/d | 5/e | 6/f
    #--------
    # 7/g | 8/h | 9/i





#score.check_wins("oscar")

def init():

    global s,t,l

    
    s = turtle.getscreen()
    s.title("Noughts and Crosses")
    turtle.hideturtle()
    t = turtle.Turtle()
    t.hideturtle()
    t.shape("blank")
    t.pensize(5)
    

    t.penup()
    t.setpos(-50,150)
    t.rt(90)
    t.pendown()
    t.fd(300)
    t.penup()
    t.setpos(50,-150)
    t.lt(180)
    t.pendown()
    t.fd(300)

    t.penup()
    t.setpos(150,50)
    t.lt(90)
    t.pendown()
    t.fd(300)
    t.penup()
    t.setpos(-150,-50)
    t.lt(180)
    t.pendown()
    t.fd(300)
    from nums import numbers
    numbers()



def x(x,y):

    global s,t

    t.penup()
    t.setpos(x,y)
    t.setheading(225)
    t.pendown()
    t.fd(84.86)
    t.penup()
    t.setpos(x,y-60)
    t.pendown()
    t.setheading(135)
    t.fd(84.86)

def o(x,y):

    global s,t

    t.penup()
    t.setheading(135)
    t.setpos(x,y)
    t.pendown()
    t.circle(35)

def welcome():
    print(f"Welcome Player, let's play a game. \n\n {a} | {b} | {c} \n-----------\n {d} | {e} | {f} \n-----------\n {g} | {h} | {i} ")

def change(): 
    global inp, oup
    inp = 0
    if inp == "1":
        oup = "a"
    elif inp == "2":
        oup = "b"
    elif inp == "3":
        oup ="c"
    elif inp == "4":
        oup = "d"
    elif inp == "5":
        oup = "e"
    elif inp == "6":
        oup = "f"
    elif inp == "7":
        oup = "g"
    elif inp == "8":
        oup = "h"
    elif inp == "9":
        oup = "i"
        

def again():
    global a,b,c,d,e,f,g,h,i,taken,t,wri
    answer = str(turtle.textinput(title = "Would you like to play again?", prompt="y/n"))
    if answer == "y":
        wri.clear()
        wri.write(f"Let's play again!",  
             align = "center", font = ("New Times Roman", 12, "normal"))  
        time.sleep(2)
        taken = []
        a = "1"
        b = "2"
        c = "3"
        d = "4"
        e = "5"
        f = "6"
        g = "7"
        h = "8"
        i = "9"
        t.clear()
        wri.clear()
        play()
    else:
        wri.clear()
        wri.write(f"Thanks for Playing!",  
             align = "center", font = ("New Times Roman", 12, "normal")) 
        time.sleep(3)
        exit()

def randompick():
    global taken,pick
    chosen = False
    
    while chosen == False:
        pick = random.randint(1,9)
        print(pick)
        if str(pick) not in taken:
            return(pick)
            break
                
def randomplay(pick,player):
    
    global a,b,c,d,e,f,g,h,i,taken
    import nums
    if pick == 1:
        a = player
        taken.append("1")
        nums.one(2)
    elif pick == 2:
        b = player
        taken.append("2")
        nums.two(2)
    elif pick == 3:
        c = player
        taken.append("3")
        nums.three(3)
    elif pick == 4:
        d = player
        taken.append("4")
        nums.four(2)
    elif pick == 5:
        e = player
        taken.append("5")
        nums.five(2)
    elif pick == 6:
        f = player
        taken.append("6")
        nums.six(2)
    elif pick == 7:
        g = player
        taken.append("7")
        nums.seven(2)
    elif pick == 8:
        h = player
        taken.append("8")
        nums.eight(2)
    elif pick == 9:
        i = player
        taken.append("9")
        nums.nine(2)

def draw():
    wri.clear()
    wri.write(f"It's a Draw!",  
        align = "center", font = ("New Times Roman", 12, "normal"))  
    again()



def wincheck():
    global t,wri

    if a == b == c:
        wri.clear()
        wri.write(f"{a} Wins!",  
             align = "center", font = ("New Times Roman", 12, "normal"))  
        t.penup()
        t.color("Red")
        t.setpos(-125,100)
        t.setheading(0)
        t.pendown()
        t.fd(250)
        again()
    elif d == e == f:
        wri.clear()
        wri.write(f"{d} Wins!",  
             align = "center", font = ("New Times Roman", 12, "normal"))  
        t.penup()
        t.color("Red")
        t.setpos(-125,0)
        t.setheading(0)
        t.pendown()
        t.fd(250)
        again()
    elif g == h == i:
        wri.clear()
        wri.write(f"{g} Wins!",  
             align = "center", font = ("New Times Roman", 12, "normal"))  
        t.penup()
        t.color("Red")
        t.setpos(-125,-100)
        t.setheading(0)
        t.pendown()
        t.fd(250)
        again()
    elif a == d == g:
        wri.clear()
        wri.write(f"{a} Wins!",  
             align = "center", font = ("New Times Roman", 12, "normal"))  
        t.penup()
        t.color("Red")
        t.setpos(-100,125)
        t.setheading(270)
        t.pendown()
        t.fd(250)
        again()
    elif b == e == h:
        wri.clear()
        wri.write(f"{b} Wins!",  
             align = "center", font = ("New Times Roman", 12, "normal"))  
        t.penup()
        t.color("Red")
        t.setpos(0,125)
        t.setheading(270)
        t.pendown()
        t.fd(250)
        again()
    elif c == f == i:
        wri.clear()
        wri.write(f"{c} Wins!",  
             align = "center", font = ("New Times Roman", 12, "normal"))  
        t.penup()
        t.color("Red")
        t.setpos(100,125)
        t.setheading(270)
        t.pendown()
        t.fd(250)
        again()
        
    elif a == e == i:
        wri.clear()
        wri.write(f"{a} Wins!",  
             align = "center", font = ("New Times Roman", 12, "normal"))  
        t.penup()
        t.color("Red")
        t.setpos(-130,130)
        t.setheading(315)
        t.pendown()
        t.fd(367.5)
        again()
    elif c == e == g:
        wri.clear()
        wri.write(f"{c} Wins!",  
             align = "center", font = ("New Times Roman", 12, "normal"))  
        t.penup()
        t.color("Red")
        t.setpos(130,130)
        t.setheading(225)
        t.pendown()
        t.fd(367.5)
        again()
    


def player1():

    global a,b,c,d,e,f,g,h,i,pick,taken
    import nums
    try:
        y = str(int(turtle.numinput("Place Your X", "Choose a Number",minval=1,maxval=9)))
        print(y)
        if y in taken:
            randompick()
            player = "X"
            randomplay(pick, player)
            print(f"That doesn't work! I've placed your X at {pick}")
        elif y == "1": 
            a = "X" 
            taken.append("1") 
            x(-70,130)
            nums.one(2)
        elif y == "2":
            b = "X"
            taken.append("2")
            x(30,130)
            nums.two(2)
        elif y == "3":
            c = "X"
            taken.append("3")
            x(130,130)
            nums.three(2)
        elif y == "4":
            d = "X"
            taken.append("4")
            x(-70,30)
            nums.four(2)
        elif y == "5":
            e = "X"
            taken.append("5")
            x(30,30)
            nums.five(2)
        elif y == "6":
            f = "X"
            taken.append("6")
            x(130,30)
            nums.six(2)
        elif y == "7":
            g = "X"
            taken.append("7")
            x(-70,-70)
            nums.seven(2)
        elif y == "8":
            h = "X"
            taken.append("8")
            x(30,-70)
            nums.eight(2)
        elif y == "9":
            i = "X"
            taken.append("9")
            x(130,-70)
            nums.nine(2)

        print(f"\n\n {a} | {b} | {c} \n-----------\n {d} | {e} | {f} \n-----------\n {g} | {h} | {i} ")
    except:
        player1()

def player2():

    global a,b,c,d,e,f,g,h,i,pick,taken
    import nums
    try:
        y = str(int(turtle.numinput("Place Your O", "Choose a Number",minval=1,maxval=9)))
        if y in taken:
            randompick()
            player = "O"
            randomplay(pick, player)
            print(f"That doesn't work! I've placed your O at {pick}")
        elif y == "1":
            a = "O"
            taken.append("1")
            o(-75,125)
            nums.one(2)
        elif y == "2":
            b = "O"
            taken.append("2")
            o(25,125)
            nums.two(2)
        elif y == "3":
            c = "O"
            taken.append("3")
            o(125,125)
            nums.three(2)
        elif y == "4":
            d = "O"
            taken.append("4")
            o(-75,25)
            nums.four(2)
        elif y == "5":
            e = "O"
            taken.append("5")
            o(25,25)
            nums.five(2)
        elif y == "6":
            f = "O"
            taken.append("6")
            o(125,25)
            nums.six(2)
        elif y == "7":
            g = "O"
            taken.append("7")
            o(-75,-75)
            nums.seven(2)
        elif y == "8":
            h = "O"
            taken.append("8")
            o(25,-75)
            nums.eight(2)    
        elif y == "9":
            i = "O"
            taken.append("9")
            o(125,-75)
            nums.nine(2)

        print(f"\n\n {a} | {b} | {c} \n-----------\n {d} | {e} | {f} \n-----------\n {g} | {h} | {i} ")
    except:
        player2()


def play():

    global t,s,wri,l
    
    init()
    #x(-70,130)
    #o(25,125)
    #t.dot(10,"blue")

    wri = turtle.Turtle()  
    wri.hideturtle()
    wri.speed(0)  
    wri.color("black")  
    wri.penup()  
    wri.hideturtle()  
    wri.goto(0, 240)  
    wri.write("Let's Play a Game!",  
             align = "center", font = ("New Times Roman", 12, "normal"))  

    
    welcome()
    player1()
    player2()

    player1()
    player2()

    player1()
    wincheck()
    player2()
    wincheck()

    player1()
    wincheck()
    player2()
    wincheck()

    player1()
    draw()



play()
    
