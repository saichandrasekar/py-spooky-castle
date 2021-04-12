from shapes import Paper, Triangle, Rectangle, Oval

paper =  Paper()

rectangle = Rectangle()
rectangle.set_width(500)
rectangle.set_height(200)
rectangle.set_color('green')
rectangle.draw()


rectangle_2 = Rectangle()

rectangle_2.set_color('red')
rectangle_2.set_width(300)
rectangle_2.set_height(50)
rectangle_2.set_x(55)
rectangle_2.set_y(145)
rectangle_2.draw()


oval = Oval()
oval.randomize()
oval.draw()

paper.display()