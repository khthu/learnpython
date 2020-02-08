import turtle
import math

def arc(t,r,angle):
    arc_length=2*math.pi*r*angle/360
    n=int(arc_length/3)+1
    step_length=arc_length/n
    step_angle=angle/n

    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)


def petal(t,r,angle):
    for i in range(2):
        arc(t,r,angle)
        t.lt(180-angle)



def flower(t, r, angle):
    for i in range(20):
        petal(t,r,angle)
        t.lt(18)
    

bob=turtle.Turtle()    
flower(bob,100,30)
turtle.mainloop()
