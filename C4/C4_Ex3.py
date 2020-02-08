import turtle
import math

def polypie(t, n, r):
    """Draws a pie divided into radial segments.

    t: Turtle
    n: number of segments
    r: length of the radial spokes
    """
    angle = 360.0 / n
    for i in range(n):
        isosceles(t, r, angle/2)
        t.lt(angle)
        
bob=turtle.Turtle()
polygon(bob,5)
turtle.mainloop()
    
