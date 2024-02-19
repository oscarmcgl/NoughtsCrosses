import turtle


on = turtle.Turtle()
on.hideturtle()
tw = turtle.Turtle()
tw.hideturtle()
th = turtle.Turtle()
th.hideturtle()
fo = turtle.Turtle()
fo.hideturtle()
fi = turtle.Turtle()
fi.hideturtle()
si = turtle.Turtle()
si.hideturtle()
se = turtle.Turtle()
se.hideturtle()
ei = turtle.Turtle()
ei.hideturtle()
ni = turtle.Turtle()
ni.hideturtle()

def one(p):
    if p == 1: #placement
        on.hideturtle()
        on.penup()
        on.setpos(-100,75)
        on.write(f"1",  
            align = "center", font = ("New Times Roman", 30, "normal")) 
        print("placed 1")
    if p == 2:
        on.clear()
        print("cleared 1")

def two(p):
    if p == 1:
        tw.hideturtle()
        tw.penup()
        tw.setpos(0,75)
        tw.write(f"2",  
             align = "center", font = ("New Times Roman", 30, "normal"))  
        print("placed 2")
    if p == 2:
        tw.clear()
        print("cleared 2")
    
def three(p):

    if p == 1:
        th.hideturtle()
        th.penup()
        th.setpos(100,75)
        th.write(f"3",  
             align = "center", font = ("New Times Roman", 30, "normal"))  
        print("placed 3") 
    if p == 2:
        th.clear()
        print("cleared 3")

def four(p):
    if p == 1:
        fo.hideturtle()
        fo.penup()
        fo.setpos(-100,-25)
        fo.write(f"4",  
             align = "center", font = ("New Times Roman", 30, "normal"))  
        print("placed 4")
    if p == 2:
        fo.clear()
        print("cleared 4")

def five(p):
    if p == 1:
        fi.hideturtle()
        fi.penup()
        fi.setpos(0,-25)
        fi.write(f"5",  
             align = "center", font = ("New Times Roman", 30, "normal"))  
        print("placed 5")
    if p == 2:
        fi.clear()
        print("cleared 2")

def six(p):
    if p == 1:
        si.hideturtle()
        si.penup()
        si.setpos(100,-25)
        si.write(f"6",  
             align = "center", font = ("New Times Roman", 30, "normal"))  
        print("placed 6")
    if p == 2:
        si.clear()
        print("cleared 2")
    
def seven(p):
    if p == 1:
        se.hideturtle()
        se.penup()
        se.setpos(-100,-125)
        se.write(f"7",  
            align = "center", font = ("New Times Roman", 30, "normal"))  
        print("placed 7")
    if p == 2:
        se.clear()
        print("placed 7")
    
def eight(p):
    if p == 1:
        ei.hideturtle()
        ei.penup()
        ei.setpos(0,-125)
        ei.write(f"8",  
             align = "center", font = ("New Times Roman", 30, "normal"))  
        print("placed 8")
    if p == 2:
        ei.clear()
        print("cleared 8")

def nine(p):
    if p == 1:
        ni.hideturtle()
        ni.penup()
        ni.setpos(100,-125)
        ni.write(f"9",  
             align = "center", font = ("New Times Roman", 30, "normal"))  
        print("placed 9")
    if p == 2:
        ni.clear()
        print("cleared 9")


def numbers():
    one(1)
    two(1)
    three(1)
    four(1)
    five(1)
    six(1)
    seven(1)
    eight(1)
    nine(1)
