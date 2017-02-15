import turtle
def draw_shape():
    window = turtle.Screen()
    window.bgcolor("orange")
    rutu = turtle.Turtle()
    rutu.shape("turtle")
    rutu.color("green")
    rutu.speed(10)
    for j in range(1,38):
        i = 0
        while i < 3:
            rutu.forward(200)
            rutu.right(90)
            i = i+1
        rutu.right(20)
        
    #raj = turtle.Turtle()
    #raj.shape("arrow")
    #raj.color("blue")
    #raj.speed(4)
    #raj.circle(100)

    #bargal = turtle.Turtle()
    #bargal.shape("turtle")
    #bargal.color("red")
    #bargal.speed(1)
    #j = 0
    #while j < 3:
        #bargal.forward(100)
        #bargal.right(120)
        #j = j+1

    window.exitonclick()
    


draw_shape()
