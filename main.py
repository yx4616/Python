# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    r = 5
    # s = 3.14 * r * r
    # print(s)
# name = input("")
# print(name)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import turtle as t

t.pencolor("red")
t.fillcolor("yellow")
t.begin_fill()
while True:
    t.forward(200)
    t.right(144)
    if abs(t.pos()) < 1:
        break
    t.end_fill()
