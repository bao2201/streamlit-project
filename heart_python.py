import turtle
import tkinter as TK
import streamlit as st
st.title('Chúc mừng 20/10')
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
def curve():
    for i in range(200):
        pen.right(1)
        pen.forward(1)
def heart():
    pen.fillcolor('red')
    pen.begin_fill()
    pen.left(140)
    pen.forward(113)
    curve()
    pen.left(120)
    curve()
    pen.forward(112)
    pen.end_fill()
def txt():
    pen.up()
  
    pen.setpos(-70, 100)

    pen.down()

    pen.color('lightpink')

    pen.write("Chúc mừng 20/10", font=(
      "Verdana", 12, "bold"))
heart()
txt()
turtle.done()
