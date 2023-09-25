from tkinter import *


class Calc:

    def __init__(self):

        self.window = Tk()
        self.window.title('Cacl')
        self.window.config(bg='#252e59')
        self.window.resizable(False, False) # Eu não posso movimentar a tela no eixo x e y

        self.screen_numbers = Entry(self.window, font='Ivy 32 bold', bg='#252e59', fg='#fcfcfc', width=15)
        self.screen_numbers.pack()

        self.frame_screen = Frame()
        self.frame_screen.pack()

        self.font = 'Ivy 13 bold'
        self.comprimento_max = 17
        self.comprimento_min = 8
        self.altura = 4
        self.fg = "#fcfcfc"
        self.color_bg = "orange"
        self.dates_botton: list[str] = [
                             'C', '%', '/', 
                             '7', '8', '9', '*', 
                             '4', '5', '6', '+', 
                             '1', '2', '3', '-', 
                             '0', '.', '=']

        row: int = 0
        column: int = 0
        for button_char in self.dates_botton:
            # Itera sobre cada botão
            if button_char == 'C':
                Button(self.frame_screen, font=self.font, fg=self.fg, bg=self.color_bg, text=button_char, width=self.comprimento_max, height=self.altura, command=lambda: self.delete).grid(column=column, row=row, columnspan=2)
                column += 2
                
            elif button_char == '=':
                Button(self.frame_screen, font=self.font, fg=self.fg, bg=self.color_bg, text=button_char, width=self.comprimento_max, height=self.altura, command=lambda: self.calc).grid(column=column, row=row, columnspan=2)
                column += 2

            else:
                Button(self.frame_screen, font=self.font, fg=self.fg, bg=self.color_bg, text=button_char, width=self.comprimento_min, height=self.altura, command=lambda: self.insert(button_char)).grid(column=column, row=row) 
                column += 1

            if  column > 3:
                column = 0
                row += 1

        self.window.mainloop()

    def insert(self, num):
        self.screen_numbers.insert(END, num)

    def delete(self):
        self.screen_numbers.delete(0, END) # Deletar do início até o fim

    def calc(self):
        try:
            valor = eval(self.screen_numbers.get())
        except:
            valor = 0

        self.screen_numbers.delete(0, END)
        self.screen_numbers.insert(0, str(valor))

if 'main' == __name__:
    Calc()
