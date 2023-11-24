from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import time


root = Tk()
root.title("ВОДА")
def click():
    print("Hello")
root.state('zoomed')



#Холст
canvas = Canvas(bg="#E7F6FE", width=440, height=1000, highlightthickness  = 3,
    highlightbackground = 'blue')
canvas.pack(anchor=CENTER, expand=1)

#Картинки
drop_image = ImageTk.PhotoImage(Image.open("C:\\Users\\mikha\\Desktop\\ProjectsPython\\Practice_main\\venv\\капля.jpg"))
canvas.create_image(30, 30, anchor=NW, image=drop_image)
canvas.create_image(300, 500, anchor=NW, image=drop_image)
money_image = ImageTk.PhotoImage(Image.open("C:\\Users\\mikha\\Desktop\\ProjectsPython\\Practice_main\\venv\\монеты.jpg"))
bottle_image = ImageTk.PhotoImage(Image.open("C:\\Users\\mikha\\Desktop\\ProjectsPython\\Practice_main\\venv\\бутылка.jpg"))



#Дисплей
canvas.create_rectangle(235, 60, 395, 140, fill="white", outline="blue", width = 3)
text_on_display = canvas.create_text(310, 100, text="Внесите деньги", fill="black", font="Arial 12")

#Функция вывода денег на дисплей
sum_of_money = 0
def get_sum(event):
    button_text = event.widget.cget('text')[:-2]
    global sum_of_money
    global text_on_display
    sum_of_money += int(button_text)
    canvas.delete(text_on_display)
    text_on_display = canvas.create_text(310, 100, text=f"{sum_of_money} р", fill="black", font="Arial 12")

#Монетоприемник
def deposit_money_coins():

    one_rubles = Button(text = "1 р")
    one_rubles.bind('<Button-1>', get_sum)
    canvas.create_window(400, 160, window=one_rubles, width=70, height=30)


    two_rubles = Button(text="2 р")
    two_rubles.bind('<Button-1>', get_sum)
    canvas.create_window(400, 195, window=two_rubles, width=70, height=30)

    five_rubles = Button(text="5 р")
    five_rubles.bind('<Button-1>', get_sum)
    canvas.create_window(400, 230, window=five_rubles, width=70, height=30)

    ten_rubles = Button(text="10 р")
    ten_rubles.bind('<Button-1>', get_sum)
    canvas.create_window(400, 265, window=ten_rubles, width=70, height=30)

coins = Button(text="", command = deposit_money_coins, bg="gray")
canvas.create_window(270, 210, window=coins, width=10, height=20)



#Купюроприемник
def deposit_money_papers():
    five_rubles_paper = Button(text = "5 р")
    five_rubles_paper.bind('<Button-1>', get_sum)
    canvas.create_window(400, 160, window=five_rubles_paper, width=70, height=30)

    ten_rubles_paper = Button(text="10 р")
    ten_rubles_paper.bind('<Button-1>', get_sum)
    canvas.create_window(400, 195, window=ten_rubles_paper, width=70, height=30)

    fifty_rubles_paper = Button(text="50 р")
    fifty_rubles_paper.bind('<Button-1>', get_sum)
    canvas.create_window(400, 230, window=fifty_rubles_paper, width=70, height=30)

    hundred_rubles_paper = Button(text="100 р")
    hundred_rubles_paper.bind('<Button-1>', get_sum)
    canvas.create_window(400, 265, window=hundred_rubles_paper, width=70, height=30)
paper_money = Button(text="", command = deposit_money_papers, bg="gray")
canvas.create_window(330, 215, window=paper_money, width=45, height=10)



#Вернуть деньги
give_change = canvas.create_oval(255, 300, 285, 330, fill="blue")
def return_money(event):
    global sum_of_money
    global text_on_display
    def delete_money(event):
        canvas.delete(money_image_object)
        global sum_of_money
        sum_of_money = 0
    if sum_of_money > 0:
        canvas.delete(text_on_display)
        text_on_display = canvas.create_text(310, 100, text="Внесите деньги", fill="black", font="Arial 12")
        money_image_object = canvas.create_image(335, 300, anchor=NW, image=money_image)
        canvas.tag_bind(money_image_object, "<Button-1>", delete_money)
canvas.tag_bind(give_change,"<ButtonPress-1>", return_money)
canvas.create_text(270, 270, text="Вернуть деньги", fill="black", font="Arial 10", width=135)

#python_image = PhotoImage(file="images.png")
#canvas.create_image(10, 10, anchor=NW, image=python_image)


#Забрать сдачу
canvas.create_rectangle(320, 285, 405, 345, fill="white", outline="blue", width = 3)

#Кнопки выбора объема
def pour100(event):
    global text_on_display
    global sum_of_money
    def delete_bottle(event):
        canvas.delete(bottle_image_object)
        global sum_of_money
        sum_of_money = 0
    def delete_money(event):
        canvas.delete(money_image_object)
        global sum_of_money
        sum_of_money = 0
    if sum_of_money < 5:
        canvas.delete(text_on_display)
        text_on_display = canvas.create_text(315, 100, text="Недостаточно денег", fill="black", font="Arial 12")
    else:
        bottle_image_object = canvas.create_image(135, 520, image = bottle_image)
        canvas.delete(text_on_display)
        text_on_display = canvas.create_text(315, 100, text="Внесите деньги", fill="black", font="Arial 12")
        canvas.tag_bind(bottle_image_object, "<Button-1>", delete_bottle)
        if (sum_of_money - 5) > 0:
            money_image_object = canvas.create_image(335, 300, anchor=NW, image=money_image)
            canvas.tag_bind(money_image_object, "<Button-1>", delete_money)
        sum_of_money = 0
ml100 = canvas.create_oval(50, 200, 65, 215, fill="blue", )
canvas.create_text(115, 207, text="100 мл (5 р) ", fill="black", font="Arial 12")
canvas.tag_bind(ml100, "<Button-1>", pour100)

def pour500(event):
    global text_on_display
    global sum_of_money
    def delete_bottle(event):
        global sum_of_money
        canvas.delete(bottle_image_object)
        sum_of_money = 0
    def delete_money(event):
        canvas.delete(money_image_object)
        global sum_of_money
        sum_of_money = 0
    if sum_of_money < 25:
        canvas.delete(text_on_display)
        text_on_display = canvas.create_text(315, 100, text="Недостаточно денег", fill="black", font="Arial 12")
    else:
        bottle_image_object = canvas.create_image(135, 520, image = bottle_image)
        canvas.delete(text_on_display)
        text_on_display = canvas.create_text(315, 100, text="Внесите деньги", fill="black", font="Arial 12")
        canvas.tag_bind(bottle_image_object, "<Button-1>", delete_bottle)
        if (sum_of_money - 25) > 0:
            money_image_object = canvas.create_image(335, 300, anchor=NW, image=money_image)
            canvas.tag_bind(money_image_object, "<Button-1>", delete_money)
        sum_of_money = 0
ml500 = canvas.create_oval(50, 230, 65, 245, fill="blue")
canvas.create_text(115, 237, text="500 мл (25 р)", fill="black", font="Arial 12")
canvas.tag_bind(ml500, "<Button-1>", pour500)

def pour1000(event):
    global text_on_display
    global sum_of_money
    def delete_bottle(event):
        global sum_of_money
        canvas.delete(bottle_image_object)
        sum_of_money = 0
    def delete_money(event):
        canvas.delete(money_image_object)
        global sum_of_money
        sum_of_money = 0
    if sum_of_money < 50:
        canvas.delete(text_on_display)
        text_on_display = canvas.create_text(315, 100, text="Недостаточно денег", fill="black", font="Arial 12")
    else:
        bottle_image_object = canvas.create_image(135, 520, image = bottle_image)
        canvas.delete(text_on_display)
        text_on_display = canvas.create_text(315, 100, text="Внесите деньги", fill="black", font="Arial 12")
        canvas.tag_bind(bottle_image_object, "<Button-1>", delete_bottle)
        if (sum_of_money - 50) > 0:
            money_image_object = canvas.create_image(335, 300, anchor=NW, image=money_image)
            canvas.tag_bind(money_image_object, "<Button-1>", delete_money)
        sum_of_money = 0
ml1000 = canvas.create_oval(50, 260, 65, 275, fill="blue")
canvas.create_text(115, 267, text="1 л (50 р)", fill="black", font="Arial 12")
canvas.tag_bind(ml1000, "<Button-1>", pour1000)

def pour5000(event):
    global text_on_display
    global sum_of_money
    def delete_bottle(event):
        canvas.delete(bottle_image_object)
        sum_of_money = 0
    def delete_money(event):
        canvas.delete(money_image_object)
        global sum_of_money
        sum_of_money = 0
    if sum_of_money < 250:
        canvas.delete(text_on_display)
        text_on_display = canvas.create_text(315, 100, text="Недостаточно денег", fill="black", font="Arial 12")
    else:
        bottle_image_object = canvas.create_image(135, 520, image = bottle_image)
        canvas.delete(text_on_display)
        text_on_display = canvas.create_text(315, 100, text="Внесите деньги", fill="black", font="Arial 12")
        canvas.tag_bind(bottle_image_object, "<Button-1>", delete_bottle)
        if (sum_of_money - 250) > 0:
            money_image_object = canvas.create_image(335, 300, anchor=NW, image=money_image)
            canvas.tag_bind(money_image_object, "<Button-1>", delete_money)
        sum_of_money = 0
ml5000 = canvas.create_oval(50, 290, 65, 305, fill="blue")
canvas.create_text(115, 297, text="5 л (250 р)", fill="black", font="Arial 12")
canvas.tag_bind(ml5000, "<Button-1>", pour5000)

def pour19000(event):
    global text_on_display
    global sum_of_money
    def delete_bottle(event):
        global sum_of_money
        canvas.delete(bottle_image_object)
        sum_of_money = 0
    def delete_money(event):
        canvas.delete(money_image_object)
        global sum_of_money
        sum_of_money = 0
    if sum_of_money < 950:
        canvas.delete(text_on_display)
        text_on_display = canvas.create_text(315, 100, text="Недостаточно денег", fill="black", font="Arial 12")
    else:
        bottle_image_object = canvas.create_image(135, 520, image = bottle_image)
        canvas.delete(text_on_display)
        text_on_display = canvas.create_text(315, 100, text="Внесите деньги", fill="black", font="Arial 12")
        canvas.tag_bind(bottle_image_object, "<Button-1>", delete_bottle)
        if (sum_of_money - 950) > 0:
            money_image_object = canvas.create_image(335, 300, anchor=NW, image=money_image)
            canvas.tag_bind(money_image_object, "<Button-1>", delete_money)
        sum_of_money = 0
ml19000 = canvas.create_oval(50, 320, 65, 335, fill="blue")
canvas.create_text(115, 327, text="19 л (950 р)", fill="black", font="Arial 12")
canvas.tag_bind(ml19000, "<Button-1>", pour19000)

#Емкость для тары
canvas.create_rectangle(50, 400, 225, 600, fill="white", outline="blue", width = 3)


root.mainloop()