import random
import turtle as t
# import colorgram


# list_of_colours = []
# colours = colorgram.extract("hirst.jpg", 20)
#
# # for num in range (len(colours)):
# #     list_of_colours.append(colours[Rgb])
#
# for colour in colours:
#     r = colour.rgb.r
#     g = colour.rgb.g
#     b = colour.rgb.b
#
#     new_colour = (r, g, b)
#
#     list_of_colours.append(new_colour)
#
# print(list_of_colours)

colour_list = [(184, 177, 5), (172, 3, 71), (215, 171, 103), (247, 17, 153), (245, 67, 5), (6, 140, 15), (190, 4, 1),
               (40, 196, 238), (5, 132, 208), (89, 2, 95), (6, 168, 130), (237, 10, 133), (248, 72, 11), (246, 226, 39),
               (253, 230, 0), (254, 3, 6)
               ]

#10 x 10 grid. Spot is 20 in size, spaced by 50 paces

t.colormode(255)
timmy = t.Turtle()
timmy.speed("fastest")
timmy.hideturtle()

x = -270
y = -270

for num in range (10):
    timmy.penup()
    timmy.setpos(x, y)

    for num in range (10):
        timmy.dot(20, random.choice(colour_list))
        timmy.penup()
        timmy.forward(50)
        timmy.pendown()


    y += 50






screen = t.Screen()
t.exitonclick()
