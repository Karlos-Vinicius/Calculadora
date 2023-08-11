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

        self.button_clear = Button(self.frame_screen, font=self.font, fg='#fcfcfc', bg='orange', text='C',
                               width=self.comprimento_max, height=self.altura, command=self.delete)
        self.button_clear.grid(column=0, row=0, columnspan=2)

        self.button_modulo = Button(self.frame_screen, font=self.font, fg='#fcfcfc', bg='orange', text='%',
                               width=self.comprimento_min, height=self.altura, command=lambda: self.insert('%'))
        self.button_modulo.grid(column=2, row=0)

        self.button_division = Button(self.frame_screen, font=self.font, fg='#fcfcfc', bg='orange', text='/',
                               width=self.comprimento_min, height=self.altura, command=lambda: self.insert('/'))
        self.button_division.grid(column=3, row=0)

        self.button_7 = Button(self.frame_screen, font=self.font, fg='#fcfcfc', bg='orange', text='7',
                               width=self.comprimento_min, height=self.altura, command=lambda: self.insert('7'))
        self.button_7.grid(column=0, row=1)

        self.button_8 = Button(self.frame_screen, font=self.font, fg='#fcfcfc', bg='orange', text='8',
                               width=self.comprimento_min, height=self.altura, command=lambda: self.insert('8'))
        self.button_8.grid(column=1, row=1)

        self.button_9 = Button(self.frame_screen, font=self.font, fg='#fcfcfc', bg='orange', text='9',
                               width=self.comprimento_min, height=self.altura, command=lambda: self.insert('9'))
        self.button_9.grid(column=2, row=1)

        self.button_mult = Button(self.frame_screen, font=self.font, fg='#fcfcfc', bg='orange', text='*',
                               width=self.comprimento_min, height=self.altura, command=lambda: self.insert('*'))
        self.button_mult.grid(column=3, row=1)

        self.button_4 = Button(self.frame_screen, font=self.font, fg='#fcfcfc', bg='orange', text='4',
                               width=self.comprimento_min, height=self.altura, command=lambda: self.insert('4'))
        self.button_4.grid(column=0, row=2)

        self.button_5 = Button(self.frame_screen, font=self.font, fg='#fcfcfc', bg='orange', text='5',
                               width=self.comprimento_min, height=self.altura, command=lambda: self.insert('5'))
        self.button_5.grid(column=1, row=2)

        self.button_6 = Button(self.frame_screen, font=self.font, fg='#fcfcfc', bg='orange', text='6',
                               width=self.comprimento_min, height=self.altura, command=lambda: self.insert('6'))
        self.button_6.grid(column=2, row=2)

        self.button_adicao = Button(self.frame_screen, font=self.font, fg='#fcfcfc', bg='orange', text='+',
                               width=self.comprimento_min, height=self.altura, command=lambda: self.insert('+'))
        self.button_adicao.grid(column=3, row=2)

        self.button_1 = Button(self.frame_screen, font=self.font, fg='#fcfcfc', bg='orange', text='1',
                               width=self.comprimento_min, height=self.altura, command=lambda: self.insert('1'))
        self.button_1.grid(column=0, row=3)

        self.button_2 = Button(self.frame_screen, font=self.font, fg='#fcfcfc', bg='orange', text='2',
                               width=self.comprimento_min, height=self.altura, command=lambda: self.insert('2'))
        self.button_2.grid(column=1, row=3)

        self.button_3 = Button(self.frame_screen, font=self.font, fg='#fcfcfc', bg='orange', text='3',
                               width=self.comprimento_min, height=self.altura, command=lambda: self.insert('3'))
        self.button_3.grid(column=2, row=3)

        self.button_subtracao = Button(self.frame_screen, font=self.font, fg='#fcfcfc', bg='orange', text='-',
                               width=self.comprimento_min, height=self.altura, command=lambda: self.insert('-'))
        self.button_subtracao.grid(column=3, row=3)

        self.button_0 = Button(self.frame_screen, font=self.font, fg='#fcfcfc', bg='orange', text='0',
                               width=self.comprimento_max, height=self.altura, command=lambda: self.insert('0'))
        self.button_0.grid(column=0, row=4, columnspan=2)

        self.button_dot = Button(self.frame_screen, font=self.font, fg='#fcfcfc', bg='orange', text='.',
                               width=self.comprimento_min, height=self.altura, command= lambda: self.insert('.'))
        self.button_dot.grid(column=2, row=4)

        self.button_output = Button(self.frame_screen, font=self.font, fg='#fcfcfc', bg='orange', text='=',
                               width=self.comprimento_min, height=self.altura, command=self.calc)
        self.button_output.grid(column=3, row=4)

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

Calc()
