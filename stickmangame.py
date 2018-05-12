from tkinter import *
import random
import time
import coords_rectangle

class Game:
    def __init__(self):
        self.tk =  Tk()
        self.tk.title("Человечек спешит к выходу")
        self.tk.resizable(0,0) #фиксированный размер окна
        self.tk.wm_attributes("-topmost", 1) #помещаем окно поверх остальных окон
        self.canvas = Canvas(self.tk, width=500, height=500, highlightthickness=0) #создаем холст
        self.canvas.pack()
        self.tk.update()
        self.canvas_height = 500
        self.canvas_width = 500
        self.bg =  PhotoImage(file="background.gif")
        w = self.bg.width()
        h = self.bg.height()
        for x in range (0, 5):
            for y in range (0, 5):
                self.canvas.create_image(x * w, y * h, image=self.bg, anchor='nw')
        self.sprites = []
        self.running = True

    def mainloop(self):
        while 1:
            if self.running == True:
                for sprite in self.sprites:
                    sprite.move()
            self.tk.update_idletasks()
            self.tk.update()
            time.sleep(0.01)

class Sprite:
    def __init__(self, game):
        self.game =  game
        self.endgame = False
        self.coordinates =  None 
    def move(self):
        pass
    def coords(self):
        return self.coordinates

class PlatformSprite(Sprite):
    def __init__(self, game, photo_image, x, y, width, height):
        Sprite.__init__(self, game)
        self.photo_image = photo_image
        self.image = game.canvas.create_image(x, y, image=self.photo_image, anchor='nw')
        self.coordinates = coords_rectangle.Coords(x, y, x + width, y + height)

    
   
g = Game()
platform1 = PlatformSprite(g, PhotoImage(file="platform1.gif"), 0, 480, 100, 10)
g.sprites.append(platform1) # добавляем только что созданный спрайт platform1 в список спрайтов нашего объекта класса Game (g).
g.mainloop()


