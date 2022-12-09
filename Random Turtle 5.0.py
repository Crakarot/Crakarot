#Random Turtle 5.0


#imports
import turtle
import random
import time

#Title
print("// // // // // // // // // \n= - - - -Turtle!- - - - = \n\\\\ \\\\ \\\\ \\\\ \\\\ \\\\ \\\\ \\\\ \\\\")
time.sleep(1)
print("Please wait...")
time.sleep(2)
print("Welcome")
question = input("Would you like random or scripted? (r, s)")
if question == "r":

    #Choice
    choice = input("Random shape or Random infinite or Random Spirals? (sh, inf, sp)")


    #Code #1
    if choice == "sh":


        ########################################


        #vb
        colors = ("red", "blue", "orange", "green", "yellow", "purple", "white", "magenta", "pink", "snow", "maroon", "peachpuff", "olive", "cyan", "teal", "violet", "navy", "lime")
        t = turtle.Pen()
        t1 = turtle.Pen()
        t2 = turtle.Pen()
        t3 = turtle.Pen()
        
        randommlength = random.randint(1,100)
        randommangle = random.randint(1,359)
        randommcolor = random.choice(colors)
        
        randommlength1 = random.randint(1,100)
        randommangle1 = random.randint(1,359)
        randommcolor1 = random.choice(colors)
        
        randommlength2 = random.randint(1,100)
        randommangle2 = random.randint(1,359)
        randommcolor2 = random.choice(colors)

        randommanglelength = (randommangle, randommlength)
        randommanglelength1 = (randommangle1, randommlength1)
        randommanglelength2 = (randommangle2, randommlength2)


        ##########################


    #Settings / Code
        print("Angle for", randommcolor, "is,", randommangle, "and length for each line is", randommlength, "\nAngle for", randommcolor1, "is,", randommangle1, "and length for each line is", randommlength1, "\nAngle for", randommcolor2, "is,", randommangle2, "and length for each line is", randommlength2)

        turtle.bgcolor("black")
        t.speed(1000)
        t1.speed(1000)
        t2.speed(1000)
        t3.speed(1000)

        #t3

        t3.penup()
        t3.goto(-550, -425)
        t3.pendown()
        t3.color("white")
        style = ('Courier', 15, 'italic')
        t3.write('Made By: Max W', font = style, align='right')
        #color
        t3.penup()
        t3.goto(500, 425)
        t3.pendown()
        t3.write(randommcolor, ",", font = style, align='right')
        #angle and length
        t3.penup()
        t3.goto(590, 425)
        t3.pendown()
        t3.write(randommanglelength, font = style, align='right')
        #color1
        t3.penup()
        t3.goto(500, 410)
        t3.pendown()
        t3.write(randommcolor1, ",", font = style, align='right')
        #angle and length1
        t3.penup()
        t3.goto(590, 410)
        t3.pendown()
        t3.write(randommanglelength1, font = style, align='right')
        #color2
        t3.penup()
        t3.goto(500, 395)
        t3.pendown()
        t3.write(randommcolor2, ",", font = style, align='right')
        #angle and length2
        t3.penup()
        t3.goto(590, 395)
        t3.pendown()
        t3.write(randommanglelength, font = style, align='right')

        t3.penup()
        t3.goto(1000, 1000)
        
        #Shapes    
        
        for x in range(1000):
            t1.color(randommcolor1)
            t1.forward(randommlength1)
            t1.left(randommangle1)
            t.penup()
            t.goto(100,100)
            t.pendown()
            
            t.color(randommcolor)
            t.forward(randommlength)
            t.left(randommangle)
            t2.penup()
            t2.goto(-100,-100)
            t2.pendown()
            
            t2.color(randommcolor2)
            t2.forward(randommlength2)
            t2.left(randommangle2)
                    
            

    #Code #2
    elif choice == "inf":

        
        ########################################


        #vb
        colors = ("red", "blue", "orange", "green", "yellow", "purple", "white", "magenta", "pink", "snow", "maroon", "peachpuff", "olive", "cyan", "teal", "violet", "navy", "lime")
        t = turtle.Pen()
        t1 = turtle.Pen()
        t2 = turtle.Pen()
        t3 = turtle.Pen()
        randommangle = random.randint(1,359)
        randommcolor = random.choice(colors)
        #1
        randommangle1 = random.randint(1,359)
        randommcolor1 = random.choice(colors)
        #2
        randommangle2 = random.randint(1,359)
        randommcolor2 = random.choice(colors)


        ########################################


    #Settings / Code
        print("Angle for", randommcolor, "is,", randommangle, "\nAngle for", randommcolor1, "is,", randommangle1, "\nAngle for", randommcolor2, "is,", randommangle2)

        #speed and background
        turtle.bgcolor("black")
        t.speed(1000)
        t1.speed(1000)
        t2.speed(1000)

        #t3
        t3.penup()
        t3.goto(-550, -425)
        t3.pendown()
        t3.color("white")
        style = ('Courier', 15, 'italic')
        t3.write('Made By: Max W', font = style, align='right')

        t3.penup()
        t3.goto(500, 425)
        t3.pendown()
        t3.write(randommcolor, font = style, align='right')

        t3.penup()
        t3.goto(590, 425)
        t3.pendown()
        t3.write(randommangle, font = style, align='right')

        t3.penup()
        t3.goto(500, 410)
        t3.pendown()
        t3.write(randommcolor1, font = style, align='right')

        t3.penup()
        t3.goto(590, 410)
        t3.pendown()
        t3.write(randommangle1, font = style, align='right')

        t3.penup()
        t3.goto(500, 395)
        t3.pendown()
        t3.write(randommcolor2, font = style, align='right')

        t3.penup()
        t3.goto(590, 395)
        t3.pendown()
        t3.write(randommangle2, font = style, align='right')

        t3.penup()
        t3.goto(1000, 1000)
        
        #Shapes
        for x in range(1000):
        
            t1.color(randommcolor1)
            t1.forward(x)
            t1.left(randommangle1)
            t.penup()
            t.goto(100,100)
            t.pendown()
            
            t.color(randommcolor)
            t.forward(x)
            t.left(randommangle)
            t2.penup()
            t2.goto(-100,-100)
            t2.pendown()
            
            t2.color(randommcolor2)
            t2.forward(x)
            t2.left(randommangle2)




    ######################################


    #Code #3
    elif choice == "sp":

        
        ########################################


        #vb
        colors = ("red", "blue", "orange", "green", "yellow", "purple", "white", "magenta", "pink", "snow", "maroon", "peachpuff", "olive", "cyan", "teal", "violet", "navy", "lime")
        t = turtle.Pen()
        t1 = turtle.Pen()
        t2 = turtle.Pen()
        t3 = turtle.Pen()
        randommangle = random.randint(1,359)
        randommcolor = random.choice(colors)
        #1
        randommangle1 = random.randint(1,359)
        randommcolor1 = random.choice(colors)
        #2
        randommangle2 = random.randint(1,359)
        randommcolor2 = random.choice(colors)


        ########################################


    #Settings / Code
        print("Angle for", randommcolor, "is,", randommangle, "\nAngle for", randommcolor1, "is,", randommangle1, "\nAngle for", randommcolor2, "is,", randommangle2)

        #speed and background
        turtle.bgcolor("black")
        t.speed(1000)
        t1.speed(1000)
        t2.speed(1000)

        #t3
        t3.penup()
        t3.goto(-550, -425)
        t3.pendown()
        t3.color("white")
        style = ('Courier', 15, 'italic')
        t3.write('Made By: Max W', font = style, align='right')

        t3.penup()
        t3.goto(500, 425)
        t3.pendown()
        t3.write(randommcolor, font = style, align='right')

        t3.penup()
        t3.goto(590, 425)
        t3.pendown()
        t3.write(randommangle, font = style, align='right')

        t3.penup()
        t3.goto(500, 410)
        t3.pendown()
        t3.write(randommcolor1, font = style, align='right')

        t3.penup()
        t3.goto(590, 410)
        t3.pendown()
        t3.write(randommangle1, font = style, align='right')

        t3.penup()
        t3.goto(500, 395)
        t3.pendown()
        t3.write(randommcolor2, font = style, align='right')

        t3.penup()
        t3.goto(590, 395)
        t3.pendown()
        t3.write(randommangle2, font = style, align='right')

        t3.penup()
        t3.goto(1000, 1000)
        
        #Shapes
        for x in range(1000):
            
            t1.color(randommcolor1)
            t1.forward(x)
            t1.left(randommangle1)

            
            t.color(randommcolor)
            t.forward(x)
            t.left(randommangle)

            
            t2.color(randommcolor2)
            t2.forward(x)
            t2.left(randommangle2)


    ######################################

elif question == "s":
    tnumber = input("How many turtles? (1, 2, 3)")
    print(tnumber, "Turtles")

    #1 Turtle
    if tnumber == "1":
        colorr = input("Color of turtle?")
        bgcolorr = "black"
        anglee = float(input("Angle of turtle? (1 - 359)"))
        t = turtle.Pen()
        t3 = turtle.Pen()
        t.speed(1000)
        t3.speed(1000)
        turtle.bgcolor(bgcolorr)

        #t3

        t3.penup()
        t3.goto(-550, -425)
        t3.pendown()
        t3.color("white")
        style = ('Courier', 15, 'italic')
        t3.write('Made By: Max W - Crakarot', font = style, align='right')
        t3.penup()
        t3.goto(1000, 1000)

        for x in range(1000):
            
            t.color(colorr)
            t.forward(x)
            t.left(anglee)
 

        
        
    #2 Turtle
    elif tnumber == "2":
        colorr = input("Color of turtle 1?")
        bgcolorr = "black"
        anglee = float(input("Angle of turtle 1? (1 - 359)"))
        colorr1 = input("Color of turtle 2?")
        anglee1 = float(input("Angle of turtle 2? (1 - 359)"))
        t = turtle.Pen()
        t1 = turtle.Pen()
        t3 = turtle.Pen()
        t.speed(1000)
        t1.speed(1000)
        t3.speed(1000)
        turtle.bgcolor(bgcolorr)

            #t3

        t3.penup()
        t3.goto(-550, -425)
        t3.pendown()
        t3.color("white")
        style = ('Courier', 15, 'italic')
        t3.write('Made By: Max W', font = style, align='right')
        t3.penup()
        t3.goto(1000, 1000)

        for x in range(1000):
                
            t.color(colorr)
            t.forward(x)
            t.left(anglee)
            t1.color(colorr1)
            t1.forward(x)
            t1.left(anglee1)

    elif tnumber == "3":

        colorr = input("Color of turtle 1?")
        bgcolorr = "black"
        anglee = float(input("Angle of turtle 1? (1 - 359)"))
        colorr1 = input("Color of turtle 2?")
        anglee1 = float(input("Angle of turtle 2? (1 - 359)"))
        colorr2 = input("Color of turtle 3?")
        anglee2 = float(input("Angle of turtle 3? (1 - 359)"))
        t = turtle.Pen()
        t1 = turtle.Pen()
        t2 = turtle.Pen()
        t3 = turtle.Pen()
        t.speed(1000)
        t1.speed(1000)
        t2.speed(1000)
        t3.speed(1000)
        turtle.bgcolor(bgcolorr)

                #t3

        t3.penup()
        t3.goto(-550, -425)
        t3.pendown()
        t3.color("white")
        style = ('Courier', 15, 'italic')
        t3.write('Made By: Max W', font = style, align='right')
        t3.penup()
        t3.goto(1000, 1000)

        for x in range(1000):
                    
            t.color(colorr)
            t.forward(x)
            t.left(anglee)
            t1.color(colorr1)
            t1.forward(x)
            t1.left(anglee1)
            t2.color(colorr2)
            t2.forward(x)
            t2.left(anglee2)
         


