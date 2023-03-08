import turtle
turtle.color('blue')
turtle.pendown()
turtle.speed(10)
turtle.left(180)
#  转弯第一下
turtle.forward(20)
turtle.right(90)
#  转弯第二下
turtle.forward(10)
turtle.right(90)
#  转弯第三下
turtle.forward(20)
turtle.right(90)
#  转弯第四下
turtle.forward(60)
turtle.left(90)
#  转弯第五下
turtle.forward(70)
turtle.right(90)
#  转弯第六下
turtle.forward(60)
#  返回
#  返回
#  返回
turtle.penup()
turtle.left(180)
#  调头
turtle.forward(60)
turtle.left(90)
#  返回转弯第一下
turtle.forward(70)
#  开始画第二条
turtle.left(45)
turtle.color('red')
turtle.pendown()
turtle.forward(60)
turtle.right(90)
turtle.forward(10)
#  左端绘制完成 掉头
turtle.backward(10)
turtle.right(90)
turtle.forward(60)
turtle.right(45)
#  转弯
turtle.forward(100)
turtle.left(90)
turtle.forward(50)
turtle.right(45)
turtle.forward(10)