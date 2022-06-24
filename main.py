import turtle

t = turtle.Turtle()

# draws a hexagon
for h in ['blue', 'blue', 'blue', 'blue', 'blue', 'blue', ]:
    t.color(h)
    t.forward(100)
    t.right(60)

# draws a square
for sq in ['blue', 'blue', 'blue', 'blue', 'blue', 'blue', ]:
    t.color(sq)
    t.forward(100)
    t.right(90)

# draws a star
for st in ['blue', 'blue', 'blue', 'blue', 'blue', 'blue', ]:
    t.color(st)
    t.forward(110)
    t.right(216)
