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
        self.bg1_1 =  PhotoImage(file="background1.1.gif")
        self.bg1_2 = PhotoImage(file="background1.2.gif")
        self.bg2_1 = PhotoImage(file="background2.1.gif")
        self.bg2_2 = PhotoImage(file="background2.2.gif")

        self.bg1 = [self.bg1_1, self.bg1_2]
        self.bg2 = [self.bg2_1, self.bg2_2]


        for x in range (0, 5, 2):
            for y in range (0, 5, 2):
                random.shuffle(self.bg1)
                self.bg1_r = self.bg1[0]
                w1 = self.bg1_r.width()
                h1 = self.bg1_r.height()
                self.canvas.create_image(x * w1, y * h1, image=self.bg1_r, anchor='nw')

        for x in range (1, 5, 2):
            for y in range (1, 5, 2):
                random.shuffle(self.bg1)
                self.bg1_r = self.bg1[0]
                w1 = self.bg1_r.width()
                h1 = self.bg1_r.height()
                self.canvas.create_image(x * w1, y * h1, image=self.bg1_r, anchor='nw')
                
        for x in range (0, 5, 2):
            for y in range (1, 5, 2):
                random.shuffle(self.bg2)
                self.bg2_r = self.bg2[0]
                w2 = self.bg2_r.width()
                h2 = self.bg2_r.height()
                self.canvas.create_image(x * w2, y * h2, image=self.bg2_r, anchor='nw')

        for x in range (1, 5, 2):
            for y in range (0, 5, 2):
                random.shuffle(self.bg2)
                self.bg2_r = self.bg2[0]
                w2 = self.bg2_r.width()
                h2 = self.bg2_r.height()
                self.canvas.create_image(x * w2, y * h2, image=self.bg2_r, anchor='nw')



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

class StickFigureSprite(Sprite):
    def __init__(self, game):
        Sprite.__init__(self, game)

        self.image_left = [PhotoImage(file="figure-L1.gif"), PhotoImage(file="figure-L2.gif"), PhotoImage(file="figure-L3.gif")]
        self.image_right = [PhotoImage(file="figure-R1.gif"), PhotoImage(file="figure-R2.gif"), PhotoImage(file="figure-R3.gif")]

        self.image = game.canvas.create_image(200, 470, image=self.image_left[0], anchor='nw')

        self.x = -2
        self.y =  0
        self.current_image = 0        #   индекс текущего изображения 0, 1 и 2 для трех стадий бега человечка
        self.current_image_add = 1     #  число которое  прибавить к индексу хранящемуся в свойстве current_image, чтобы получить индекс следующего изображения
        self.jump_count = 0           # свойство - счетчик, который понадобится для прыжков человечка.
        self.last_time = time.time()   #  будет хранить время последней смены кадров фигурки. сейчас записано текущее время с помощью функции time из модуля time.
        self.coordinates = coords_rectangle.Coords() 

        game.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        game.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        game.canvas.bind_all('<space>', self.jump)

    def turn_left(self, evt):
        if self.y == 0:
            self.x = -2
    
    def turn_right(self, evt):
        if self.y == 0:
            self.x = 2

    def jump(self, evt):
        if self.y == 0:
            self.y = -4
            self.jump_count = 0

    def animate(self):
        if self.x != 0 and self.y == 0:
            if time.time() - self.last_time > 0.1:    #проверка, сколько времени прошло с пред смены кадра, если нужное время прошло то
                self.last_time = time.time()   #обнуляем счетчик -записывая текущее время
                self.current_image += self.current_image_add
                if self.current_image >=2:
                    self.current_image_add = -1
                if self.current_image <=0:
                    self.current_image_add = 1

        if self.x < 0:       #если фигурка движется в лево
            if self.y != 0:     #прыгает или падает
                self.game.canvas.itemconfig(self.image, image=self.images_left[2]) #с помощью функции itemconfig меняем изображение фигурки на последний кадр в списке изображений, повернутых влево (images_left[2]).
            else:
                self.game.canvas.itemconfig(self.image, image=self.image_left[self.current_image])
            
        elif self.x > 0:
            if self.y != 0:
                self.game.canvas.itemconfig(self.image, image=self.image_right[2])
            else:
                self.game.canvas.itemconfig(self.image, image=self.image_right[self.current_image])

    
    def coords(self):
        xy = self.game.canvas.coords(self.image) #возвращает x- и y-координаты изображения (идентификатор изображения хранится в свойстве image)
        self.coordinates.x1 = xy[0]
        self.coordinates.y1 = xy[1]
        self.coordinates.x2 = xy[0] + 27
        self.coordinates.y2 = xy[1] + 30
        return self.coordinates






g = Game()
platform1 = PlatformSprite(g, PhotoImage(file="platform1.gif"), 0, 480, 100, 10) #первая пара цифр отступы -расположение, вторая - ширина и высота картинки
platform2 = PlatformSprite(g, PhotoImage(file = "platform1.gif"), 150, 440, 110, 10) 
platform3 = PlatformSprite(g, PhotoImage(file="platform1.gif"), 300, 400, 100, 10)
platform4 = PlatformSprite(g, PhotoImage(file="platform1.gif"), 300, 160, 100, 10)
platform5 = PlatformSprite(g, PhotoImage(file="platform2.gif"), 175, 350, 66, 10)
platform6 = PlatformSprite(g, PhotoImage(file="platform2.gif"), 50, 300, 66, 10)
platform7 = PlatformSprite(g, PhotoImage(file="platform2.gif"), 170, 120, 66, 10)
platform8 = PlatformSprite(g, PhotoImage(file="platform2.gif"), 45, 60, 66, 10)
platform9 = PlatformSprite(g, PhotoImage(file="platform3.gif"), 170, 250, 32, 10)
platform10 = PlatformSprite(g, PhotoImage(file="platform3.gif"), 230, 200, 32, 10)

g.sprites.append(platform1) # добавляем только что созданный спрайт platform1 в список спрайтов нашего объекта класса Game (g).
g.sprites.append(platform2)
g.sprites.append(platform3)
g.sprites.append(platform4)
g.sprites.append(platform5)
g.sprites.append(platform6)
g.sprites.append(platform7)
g.sprites.append(platform8)
g.sprites.append(platform9)
g.sprites.append(platform10)


g.mainloop()


