import tkinter as tk
from random import shuffle


colors = {
    1: 'blue',
    2: 'green',
    3: 'yellow',
}



class myButton(tk.Button):


    def __init__(self, master, x, y, number=0, *args, **kwargs):
        super(myButton, self).__init__(master, width=3, font='Calibri 15 bold', *args, **kwargs)
        self.x = x
        self.y = y
        self.number = number
        self.is_mine = False
        self.count_bomb = 0


    def __repr__(self):
        return f'MyButton{self.x}{self.y}{self.number} {self.is_mine}'


class MineSweeper:


    window = tk.Tk()
    row = 5
    columns = 5
    mines = 5

    def __init__(self):
        self.buttons = []

        for i in range(MineSweeper.row + 2):

            temp = []
            for j in range(MineSweeper.columns + 2):
                btn = myButton(MineSweeper.window, x=i, y=j)
                btn.config(command=lambda button=btn: self.click(button))

                temp.append(btn)
            self.buttons.append(temp)

    def click(self, clicked_button: myButton):
        print(clicked_button)
        if clicked_button.is_mine:
            clicked_button.config(text='*', background='red', disabledforeground='black')
        else:
            clicked_button.config(text=clicked_button.number)
        clicked_button.config(state='disabled')

    def create_widgets(self):
        for i in range(1, MineSweeper.row + 1):
            for j in range(1, MineSweeper.columns + 1):
                btn = self.buttons[i][j]
                btn.grid(row=i, column=j)

    def open_all_buttons(self):
        for i in range(1, MineSweeper.row + 1):
            for j in range(1, MineSweeper.columns + 1):
                btn = self.buttons[i][j]
                if btn.is_mine:
                    btn.config(text='*', background='red', disabledforeground='black')
                elif btn.count_bomb in colors:
                    color = colors.get(btn.count_bomb, 'black')
                    btn.config(text=btn.count_bomb, fg = color)
                btn.grid(row=i, column=j)


    def start(self):
        self.create_widgets()
        self.insert_mines()
        self.count_mines_in_buttons()
        self.print_buttons()
        self.open_all_buttons()


        MineSweeper.window.mainloop()

    def print_buttons(self):
        for i in range(1, MineSweeper.row + 1):
            for j in range(1, MineSweeper.columns + 1):
                btn = self.buttons[i][j]
                if btn.is_mine:
                    print('B', end='')
                else:
                    print(btn.count_bomb, end='')
            print()

    def insert_mines(self):
        index_mines = self.get_mines_places()
        print(index_mines)
        count = 1

        for i in range(1, MineSweeper.row + 1):
            for j in range(1, MineSweeper.columns + 1):
                btn = self.buttons[i][j]
                btn.number = count
                if btn.number in index_mines:
                    btn.is_mine = True
                count += 1

    def count_mines_in_buttons(self):
        for i in range(1, MineSweeper.row + 1):
            for j in range(1, MineSweeper.columns + 1):
                btn = self.buttons[i][j]
                count_bomb = 0
                if not btn.is_mine:
                    for row_dx in [-1, 0, 1]:
                        for col_dx in [-1, 0, 1]:
                            neighbour = self.buttons[i + row_dx][j + col_dx]
                            if neighbour.is_mine:
                                count_bomb += 1
                btn.count_bomb = count_bomb

    @staticmethod
    def get_mines_places():
        indexes = list(range(1, MineSweeper.columns * MineSweeper.row + 1))
        shuffle(indexes)
        return indexes[:MineSweeper.mines]

game = MineSweeper()
game.start()

