import turtle
import random

#images
image1 = "./dvd_1.gif"
image2 = "./dvd_2.gif"
image3 = "./dvd_3.gif"
image4 = "./dvd_4.gif"
image5 = "./dvd_5.gif"
image6 = "./dvd_6.gif"
image7 = "./dvd_7.gif"
dvds = image1, image2, image3, image4, image5, image6, image7
def rdvd(dvds):
    return random.choice(dvds)

#screen
scrn = turtle.Screen()
scrn.bgcolor("black")
scrn.setup(width=1280, height=720)
scrn.addshape(image1)
scrn.addshape(image2)
scrn.addshape(image3)
scrn.addshape(image4)
scrn.addshape(image5)
scrn.addshape(image6)
scrn.addshape(image7)

#dvd
dvd = turtle.Turtle()
dvd.shape(image1)
dvd.speed(40)
dvd.penup()
dvd.goto(0, 0)
dvd.dx = 6
dvd.dy = -5

#collision
while True:
    try:
        scrn.update()
    
        dvd.setx(dvd.xcor()+dvd.dx)
        dvd.sety(dvd.ycor()+dvd.dy)

        if dvd.ycor() > 270:
            dvd.shape(rdvd(dvds))
            dvd.sety(270)
            dvd.dy *= -1

        if dvd.ycor() < -270:
            dvd.shape(rdvd(dvds))
            dvd.sety(-270)
            dvd.dy *= -1
        
        if dvd.xcor() > 530:
            dvd.shape(rdvd(dvds))
            dvd.setx(530)
            dvd.dx *= -1

        if dvd.xcor() < -530:
            dvd.shape(rdvd(dvds))
            dvd.setx(-530)
            dvd.dx *= -1

    except:
        break
