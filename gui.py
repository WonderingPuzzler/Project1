from tkinter import *
from csv import *

class GUI:
    def __init__(self, window: Tk) -> None:
        """
        Initalizes kiosk variables and creates beginning intro screen

        :param window: connects GUI actions to main Tk window
        """

        self.burger: int = 0
        self.chicken_sandwich: int = 0
        self.nuggets: int = 0
        self.drink: int = 0
        self.fries: int = 0
        self.apple: int = 0
        self.new_canvas(window)

        self.canvas.create_rectangle(115, 25, 285, 125, fill="RED", outline='RED')
        self.canvas.create_text(200, 75, text="W", fill="YELLOW", font=("Arial Bold", 70), anchor="center")
        self.canvas.create_text(195, 180, text="Welcome!", fill="BLACK", font=("Arial", 50), anchor="center")
        self.canvas.create_text(200, 330, text="Press the button below to\n      begin your order!", fill="BLACK", font=("Arial", 25), anchor="center")

        self.button_begin = Button(window, text='Begin?', font=('Arial Bold', 12), bg='RED', command=lambda: self.menu1(window))
        self.button_begin.place(x=130, y=500, width=120, height=70)



    def menu1(self, window: Tk) -> None:
        """
        Creates the first menu screen and necessary actions to buy different foods

        :param window: connects GUI actions to main Tk window
        """

        self.next_screen(window)
        self.new_canvas(window)

        self.canvas.create_rectangle(40, 50, 165, 175, fill="WHITE", outline='WHITE')
        self.canvas.create_rectangle(60, 65, 146, 90, fill="#DBAD26", outline='#DBAD26')
        self.canvas.create_rectangle(60, 90, 146, 95, fill="YELLOW", outline='YELLOW')
        self.canvas.create_rectangle(60, 95, 146, 110, fill="#695313", outline='#695313')
        self.canvas.create_rectangle(60, 110, 146, 140, fill="#DBAD26", outline='#DBAD26')
        self.button_submit: Button = Button(window, text='+', font=('Arial Bold', 40), bg='WHITE', command=lambda: self.add_burger(self))
        self.button_submit.place(x=75, y=190, width=50, height=50)

        self.canvas.create_rectangle(240, 50, 365, 175, fill="WHITE", outline='WHITE')
        self.button_submit: Button = Button(window, text='+', font=('Arial Bold', 40), bg='WHITE', command=lambda: self.add_nuggets(self))
        self.canvas.create_oval(270, 80, 305, 150, fill="#DBAD26")
        self.canvas.create_oval(305, 80, 335, 150, fill="#DBAD26")
        self.canvas.create_rectangle(265, 100, 340, 165, fill="RED", outline='RED')
        self.button_submit.place(x=275, y=190, width=50, height=50)
        self.canvas.create_text(302, 140, text="W", fill="YELLOW", font=("Arial Bold", 50), anchor="center")


        self.canvas.create_rectangle(40, 300, 165, 425, fill="WHITE", outline='WHITE')
        self.canvas.create_rectangle(65, 330, 140, 355, fill="#DBAD26", outline='#DBAD26')
        self.canvas.create_rectangle(55, 355, 150, 385, fill="ORANGE", outline='ORANGE')
        self.canvas.create_rectangle(65, 385, 140, 410, fill="#DBAD26", outline='#DBAD26')
        self.button_submit: Button = Button(window, text='+', font=('Arial Bold', 40), bg='WHITE', command=lambda: self.add_chicken_sandwich(self))
        self.button_submit.place(x=75, y=440, width=50, height=50)


        self.canvas.create_rectangle(240, 300, 365, 425, fill="WHITE", outline='WHITE')
        self.canvas.create_rectangle(270, 330, 340, 410, fill="RED", outline='RED')
        self.canvas.create_rectangle(265, 320, 345, 330, fill="GREY", outline='GREY')
        self.canvas.create_rectangle(300, 310, 310, 320, fill="#FFDF57", outline='#FFDF57')
        self.canvas.create_rectangle(300, 305, 340, 310, fill="#FFDF57", outline='#FFDF57')
        self.button_submit: Button = Button(window, text='+', font=('Arial Bold', 40), bg='WHITE', command=lambda: self.add_drink(self))
        self.button_submit.place(x=275, y=440, width=50, height=50)
        self.canvas.create_text(305, 373, text="W", fill="YELLOW", font=("Arial Bold", 50), anchor="center")


        self.button_continue: Button = Button(window, text='Continue?', font=('Arial Bold', 12), bg='RED', command=lambda: self.menu2(window))
        self.button_continue.place(x=200, y=510, width=190, height=70)

    def menu2(self, window: Tk) -> None:
        """
        Creates the second menu screen with more food options and tip buttons

        :param window: connects GUI actions to main Tk window
        """
        self.next_screen(window)
        self.new_canvas(window)

        self.canvas.create_rectangle(40, 50, 165, 175, fill="WHITE", outline='WHITE')
        self.canvas.create_rectangle(95, 55, 105, 150, fill="BROWN", outline='BROWN')
        self.canvas.create_oval(60, 80, 140, 165, fill="RED", outline="RED")
        self.canvas.create_oval(90, 70, 145, 90, fill = "GREEN", outline="GREEN")
        self.button_submit: Button = Button(window, text='+', font=('Arial Bold', 40), bg='WHITE', command=lambda: self.add_apple(self))
        self.button_submit.place(x=75, y=190, width=50, height=50)


        self.canvas.create_rectangle(240, 50, 365, 175, fill="WHITE", outline='WHITE')
        self.button_submit: Button = Button(window, text='+', font=('Arial Bold', 40), bg='WHITE', command=lambda: self.add_fries(self))
        self.button_submit.place(x=275, y=190, width=50, height=50)
        self.canvas.create_rectangle(265, 70, 275, 165, fill="#FFDF57", outline='#FFDF57')
        self.canvas.create_rectangle(285, 70, 295, 165, fill="#FFDF57", outline='#FFDF57')
        self.canvas.create_rectangle(305, 70, 315, 165, fill="#FFDF57", outline='#FFDF57')
        self.canvas.create_rectangle(325, 70, 335, 165, fill="#FFDF57", outline='#FFDF57')
        self.canvas.create_rectangle(265, 100, 340, 165, fill="RED", outline='RED')
        self.canvas.create_text(302, 140, text="W", fill="YELLOW", font=("Arial Bold", 50), anchor="center")



        self.tip_var: StringVar = StringVar(value='10%')
        self.radio_button = Radiobutton(window, text='10%', font=('Arial Bold', 25), variable=self.tip_var, value='10%')
        self.radio_button.place(x=20, y=275)
        self.radio_button = Radiobutton(window, text='15%', font=('Arial Bold', 25), variable=self.tip_var, value='15%')
        self.radio_button.place(x=145, y=275)
        self.radio_button = Radiobutton(window, text='20%', font=('Arial Bold', 25), variable=self.tip_var, value='20%')
        self.radio_button.place(x=275, y=275)


        self.button_continue: Button = Button(window, text='Continue?', font=('Arial Bold', 12), bg='RED', command=lambda: self.summary(window))
        self.button_continue.place(x=200, y=510, width=190, height=70)

        self.button_back: Button = Button(window, text='Back?', font=('Arial Bold', 12), bg='RED',command=lambda: self.menu1(window))
        self.button_back.place(x=10, y=510, width=190, height=70)

    def summary(self, window: Tk) -> None:
        """
        Creates the summary screen which shows monetary value of food bought.

        :param window: connects GUI actions to main Tk window
        """

        self.next_screen(window)
        self.new_canvas(window)

        self.burger_price: float = self.burger * 2.25
        self.chicken_sandwich_price: float = self.chicken_sandwich * 2
        self.nuggets_price: float = self.nuggets * 1.75
        self.drink_price: float = self.drink * 1.50
        self.fries_price: float = self.fries * 1.25
        self.apple_price: float = self.apple * 0.5

        if self.tip_var.get() == '10%':
            self.tip = .1
        elif self.tip_var.get() == '15%':
            self.tip = .15
        else:
            self.tip = .2

        self.food_total: float = (self.burger_price + self.chicken_sandwich_price + self.nuggets_price + self.fries_price + self.apple_price)
        self.tax_total: float = (self.burger_price + self.chicken_sandwich_price + self.nuggets_price + self.drink_price + self.fries_price + self.apple_price) * .1
        self.tip_total: float = (self.burger_price + self.chicken_sandwich_price + self.nuggets_price + self.fries_price + self.apple_price + self.drink_price) * self.tip
        self.total: float = self.food_total + self.drink_price + self.tax_total + self.tip_total

        dollar_sign: str = "$"
        self.label: Label = Label(window, text=f' SUMMARY\n\nFood: {dollar_sign:>21}{self.food_total:.2f}\nDrink:{dollar_sign:>20}{self.drink_price:.2f}\nTax:{dollar_sign:>23}{self.tax_total:.2f}\nTip:{dollar_sign:>24}{self.tip_total:.2f}\n\nTOTAL:{dollar_sign:>18}{self.total:.2f}', font=('Arial Bold', 15), bg='#FFDF57')
        self.label.place(x=0, y=-40, width=400, height=600)

        self.button_continue: Button = Button(window, text='Continue?', font=('Arial Bold', 12), bg='RED', command=lambda: self.order(window))
        self.button_continue.place(x=200, y=510, width=190, height=70)

        self.button_back: Button = Button(window, text='Back?', font=('Arial Bold', 12), bg='RED', command=lambda: self.menu2(window))
        self.button_back.place(x=10, y=510, width=190, height=70)

        self.tip_total: str = f'{self.tip_total:.2f}'
        self.total: str = f'{self.total:.2f}'

    def order(self, window: Tk) -> None:
        """
        Creates GUI to have user put in financial information

        :param window: connects GUI actions to main Tk window
        """
        self.next_screen(window)
        self.new_canvas(window)

        self.label_name: Label = Label(window, text='Name', font=('Arial Bold', 20), bg='#FFDF57')
        self.label_name.place(x=155, y=5)
        self.input_name: Entry = Entry(window)
        self.input_name.place(x=20, y=40, width=360)


        self.label_credit: Label = Label(window, text='Credit Card #', font=('Arial Bold', 20), bg='#FFDF57')
        self.label_credit.place(x=110, y=75)
        self.input_credit: Entry = Entry(window)
        self.input_credit.place(x=20, y=110, width=360)

        self.label_cvv: Label = Label(window, text='CVV', font=('Arial Bold', 20), bg='#FFDF57')
        self.label_cvv.place(x=160, y=145)
        self.input_cvv: Entry = Entry(window)
        self.input_cvv.place(x=20, y=180, width=360)

        self.label_address: Label = Label(window, text='Address', font=('Arial Bold', 20), bg='#FFDF57')
        self.label_address.place(x=140, y=215)
        self.input_address: Entry = Entry(window)
        self.input_address.place(x=20, y=250, width=360)

        self.button_continue: Button = Button(window, text='Sumbit?', font=('Arial Bold', 12), bg='RED', command=lambda: self.finance_file(window))
        self.button_continue.place(x=200, y=510, width=190, height=70)

        self.button_back: Button = Button(window, text='Back?', font=('Arial Bold', 12), bg='RED', command=lambda: self.menu1(window))
        self.button_back.place(x=10, y=510, width=190, height=70)



    def check_order(self, window: Tk) -> bool:
        """
        Checks to make sure the finanicial information was put in correctly, and doesn't move forward/add to CSV file if there is any mistakes

        :param window: Connects GUI actions to main Tkinter Window
        """
        self.error: bool = False
        try:
            self.name: str = self.input_name.get()
            self.credit: str = self.input_credit.get()
            self.cvv: str = self.input_cvv.get()
            self.address: str = self.input_address.get()

            if self.name.replace(' ','').isalpha() == False or len(self.credit) > 19 or len(self.credit) < 19 or self.credit.replace(' ', '').isnumeric() == False or len(self.cvv) < 3 or len(self.cvv) > 3 or self.cvv.isnumeric() == False or self.address.replace(" ", "").replace(".","").isalnum() == False:
                raise ValueError
            else:
                self.error: bool = False


        except ValueError as e:
            self.input_name.delete(0, END)
            self.input_credit.delete(0, END)
            self.input_cvv.delete(0, END)
            self.input_address.delete(0, END)
            self.error = True

        return self.error

    def finance_file(self, window: Tk) -> None:
        """
        If check_order caught mistake, tells user what input is needed. If it didn't, then it writes financial information to output.csv file

        :param window: connects GUI actions to main Tk window
        """


        if self.check_order(window) == True:
            self.label_submit: Label = Label(window,text=f'Names should only be letters and spaces\n\nCredit Card # needs spaces and numbers only\n\nCVV should be three numbers\n\nAddress is alphanumerics, spaces can be included',font=('Arial Bold', 11), bg='#FFDF57')
            self.label_submit.place(x=10, y=300, width=370, height=175)

        else:
            with open('output.csv', 'a', newline='') as csv_file:
                fieldnames = ['Name', 'Credit Card #', 'CVV', 'Address', 'Tip Total', 'Order Total']
                row = {'Name': self.name, 'Credit Card #': self.credit, 'CVV': self.cvv, 'Address': self.address, 'Tip Total': self.tip_total, 'Order Total': self.total}
                csv_writer: DictWriter = DictWriter(csv_file, fieldnames=fieldnames, delimiter=',')
                csv_writer.writerow(row)
                self.label_submit: Label = Label(window, text=f'Your order will be done soon!\nThank you for ordering!\nOrder reset!\nGo back to start!', font=('Arial Bold', 13), bg='#FFDF57')
                self.label_submit.place(x=10, y=300, width=370, height=175)

                self.burger: int = 0
                self.chicken_sandwich: int = 0
                self.nuggets: int = 0
                self.drink: int = 0
                self.fries: int = 0
                self.apple: int = 0

    def next_screen(self, window: Tk) -> None:
        """
        Deletes canvas and elements so new GUI screen can be created
        :param window: connects GUI actions to main Tk window
        """

        self.canvas.destroy()
        [widget.destroy() for widget in window.winfo_children()]

    def new_canvas(self, window: Tk) -> None:
        """
        Creates a new canvas so new GUI screen can be created

        :param window: connects GUI actions to main Tk window
        """

        self.canvas = Canvas(window, width=400, height=600, bg='#FFDF57')
        self.canvas.pack()

    def add_burger(self, window: Tk) -> None:
        """
        Adds one burger to order
        :param window: connects GUI actions to main Tk window
        """

        self.burger += 1


    def add_fries(self, window: Tk) -> None:
        """
        Adds one order of fries to things bought
        :param window: connects GUI actions to main Tk window
        """

        self.fries += 1

    def add_drink(self, window: Tk) -> None:
        """
        Adds one drink to order
        :param window: connects GUI actions to main Tk window
        """

        self.drink += 1

    def add_nuggets(self, window: Tk) -> None:
        """
        Adds one chicken_nugget order to things bought
        :param window: connects GUI actions to main Tk window
        """

        self.nuggets += 1

    def add_chicken_sandwich(self, window: Tk) -> None:
        """
        Adds a chicken_sandwich to order
        :param window: connects GUI actions to main Tk window
        """
        self.chicken_sandwich += 1

    def add_apple(self, window: Tk) -> None:
        """
        Adds an apple to order
        :param window: connects GUI actions to main Tk window
        """
        self.apple += 1
