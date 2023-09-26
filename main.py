from tkinter import *


from settings import Settings


class Calc:
    """Classe responsável por cirar e gerenciar uma calculadora, somando,
    subtraindo, multiplicando, entre outros, valores"""
    def __init__(self):
        """Defini os atributos da classe Calc"""
        self.window = Tk()
        self.settings = Settings(self.window)
        self.screen_numbers = self.settings.screen_numbers
        self.frame_screen = self.settings.frame_screen

        # Posicionando a tela de números e o frame na janela
        self.screen_numbers.pack()
        self.frame_screen.pack()

        row: int = 0
        column: int = 0
        for button_char in self.settings.dates_botton:
            # Itera sobre cada botão
            if button_char == 'C':
                Button(self.frame_screen, font=self.settings.font, fg=self.settings.fg, bg=self.settings.color_bg, text=button_char, width=self.settings.comprimento_max, height=self.settings.altura, command=self.delete).grid(column=column, row=row, columnspan=2)
                column += 2
                
            elif button_char == '=':
                Button(self.frame_screen, font=self.settings.font, fg=self.settings.fg, bg=self.settings.color_bg, text=button_char, width=self.settings.comprimento_max, height=self.settings.altura, command=self.calc).grid(column=column, row=row, columnspan=2)
                column += 2

            else:
                Button(self.frame_screen, font=self.settings.font, fg=self.settings.fg, bg=self.settings.color_bg, text=button_char, width=self.settings.comprimento_min, height=self.settings.altura, command=lambda: self.insert(button_char)).grid(column=column, row=row) 
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

if '__main__' == __name__:
    Calc()
