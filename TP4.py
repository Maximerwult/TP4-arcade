# Par Maxime Rault
# TP4

# import arcade and random
import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

COLORS = [arcade.color.RED, arcade.color.GREEN, arcade.color.BLUE, arcade.color.YELLOW, arcade.color.ORANGE, arcade.color.PURPLE]

class Balle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.change_x = random.uniform(-5, 5)
        self.change_y = random.uniform(-5, 5)
        self.rayon = random.randint(10, 30)
        self.color = random.choice(COLORS)

    def update(self):
        self.x += self.change_x
        self.y += self.change_y

        # code pour que la balle ne sorte pas de l'écran
        if self.x < 0 + self.rayon:
            self.x = 0 + self.rayon
            self.change_x *= -1
        elif self.x > SCREEN_WIDTH - self.rayon:
            self.x = SCREEN_WIDTH - self.rayon
            self.change_x *= -1
        if self.y < 0 + self.rayon:
            self.y = 0 + self.rayon
            self.change_y *= -1
        elif self.y > SCREEN_HEIGHT - self.rayon:
            self.y = SCREEN_HEIGHT - self.rayon
            self.change_y *= -1

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.rayon, self.color)

class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.change_x = random.uniform(-5, 5)
        self.change_y = random.uniform(-5, 5)
        self.width = random.randint(20, 50)
        self.height = random.randint(20, 50)
        self.color = random.choice(COLORS)
        self.angle = random.uniform(0, 360)

    def update(self):
        self.x += self.change_x
        self.y += self.change_y

        # code pour que le rectangle ne sorte pas de l'écran
        if self.x < 0 + self.width / 2:
            self.x = 0 + self.width / 2
            self.change_x *= -1
        elif self.x > SCREEN_WIDTH - self.width / 2:
            self.x = SCREEN_WIDTH - self.width / 2
            self.change_x *= -1
        if self.y < 0 + self.height / 2:
            self.y = 0 + self.height / 2
            self.change_y *= -1
        elif self.y > SCREEN_HEIGHT - self.height / 2:
            self.y = SCREEN_HEIGHT - self.height / 2
            self.change_y *= -1

    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height, self.color, self.angle)

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice #1")
        self.balles = []
        self.rectangles = []

    def setup(self):
        pass

    def on_draw(self):
        arcade.start_render()

        for balle in self.balles:
            balle.draw()

        for rectangle in self.rectangles:
            rectangle.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.balles.append(Balle(x, y))
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            self.rectangles.append(Rectangle(x, y))

    def update(self, delta_time):
        for balle in self.balles:
            balle.update()

        for rectangle in self.rectangles:
            rectangle.update()

def main():
    my_game = MyGame()
    my_game.setup()
    arcade.run()

main()