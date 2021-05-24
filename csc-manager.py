import tkinter

from app import App
import pygame


def main():
    tk = tkinter.Tk()
    pygame.mixer.init()
    App("CSC Manager 1.0.4", tk)
    tk.mainloop()


if __name__ == '__main__':
    main()
