from tkinter import *


class Settings:
    """Classe que gerencia as configuraçoes da classe Calc"""
    def __init__(self, window) -> None:
        """Configuraçoes geral da classe Calc"""
        # Configuraçoes de tela geral
        self.window = window
        self.window.title('Cacl')
        self.window.config(bg='#252e59')
        self.window.resizable(False, False)

        # Desenhando a parte que imprime os valores
        self.screen_numbers = Entry(self.window, font='Ivy 32 bold', bg='#252e59', fg='#fcfcfc', width=15)

        # Dividindo a tela em mais uma parte e posicionando ela na tela
        self.frame_screen = Frame()

        # Configuraçoes do botao
        self.font: str = 'Ivy 13 bold'
        self.comprimento_max: int = 17
        self.comprimento_min: int = 8
        self.altura: int = 4
        self.fg: str = "#fcfcfc"
        self.color_bg: str = "orange"
        self.dates_botton: list[str] = [
                             'C', '%', '/', 
                             '7', '8', '9', '*', 
                             '4', '5', '6', '+', 
                             '1', '2', '3', '-', 
                             '0', '.', '=']