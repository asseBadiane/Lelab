from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.graphics.vertex_instructions import Line, Rectangle, Ellipse
from kivy.graphics.context_instructions import Color

from kivy.metrics import dp
from kivy.properties import Clock


Builder.load_file("canvas_example.kv")

class CanvasExample1(Widget):
    pass

class CanvasExample2(Widget):
    pass

class CanvasExample3(Widget):
    pass

class CanvasExample4(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Line(points=(100, 50, 40, 50), width=2)
            Color(0, 1, 0)
            Line(circle=(400, 100, 80), width=2)
            self.elip = Ellipse(pos=(100, 200), size=(80, 80))
            Line(rectangle=(100, 400, 100, 60), width=1)
            self.rec = Rectangle(pos=(100, 400), size=(100, 60))

    def on_button_a_click_rectangle(self):
        x, y = self.rec.pos
        w, h = self.rec.size
        diff = self.width - (x+w)
        inc = dp(10)
        if diff < dp(10):
            inc = diff
        x += inc
        self.rec.pos = (x, y)

    def on_button_a_click_cercle(self):
        x, y = self.elip.pos
        w, h = self.elip.size
        inc = dp(50)

        diff = self.width - (x+w)
        if diff < inc:
            inc = diff
        x += inc
        self.elip.pos = (x, y)


class CanvasExample5(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ball_size = dp(50)
        self.vx = dp(3)
        self.vy = dp(4)
        self.value_y = dp(4)
        self.value_x = dp(5)
        self.value_3_y = dp(5)
        self.value_3_x = dp(6)
        with self.canvas:
            Color(0, 1, 0, 1)
            self.ball = Ellipse(pos=self.center, size=(
                self.ball_size, self.ball_size))
            Color(1, 0, 0, 1)
            self.ball_2 = Ellipse(pos=self.center, size=(
                self.ball_size, self.ball_size))
            Color(0, 0, 1, 1)
            self.ball_3 = Ellipse(pos=self.center, size=(
                self.ball_size, self.ball_size))

        Clock.schedule_interval(self.update, 0.01)
        Clock.schedule_interval(self.update_2, 0.01)
        Clock.schedule_interval(self.update_3, 0.01)

    def on_size(self, *args):
        print(f"width: {self.width}, height: {self.height}")
        self.ball.pos = (self.center_x - self.ball_size/2,
                         self.center_y - self.ball_size/2)
        self.ball_2.pos = (self.center_x - self.ball_size/2,
                           self.center_y - self.ball_size*8/2)
        self.ball_3.pos = (self.center_x - self.ball_size/2,
                           self.center_y + self.ball_size*6/2)

    def update(self, dt):
        print("Update")
        x, y = self.ball.pos
        x += self.vx
        y += self.vy
        if y+self.ball_size > self.height:
            y = self.height - self.ball_size
            self.vy = -self.vy
        if x+self.ball_size > self.width:
            x = self.width - self.ball_size
            self.vx = -self.vx
        if y < 0:
            y = 0
            self.vy = -self.vy
        if x < 0:
            x = 0
            self.vx = -self.vx
        self.ball.pos = (x, y)

    def update_2(self, dt):
        print("Update")
        x, y = self.ball_2.pos
        x -= self.value_x
        y -= self.value_y
        if y+self.ball_size > self.height:
            y = self.height - self.ball_size
            self.value_y = -self.value_y
        if x+self.ball_size > self.width:
            x = self.width - self.ball_size
            self.value_x = -self.value_x
        if y < 0:
            y = 0
            self.value_y = -self.value_y
        if x < 0:
            x = 0
            self.value_x = -self.value_x
        self.ball_2.pos = (x, y)

    def update_3(self, dt):
        print("Update")
        x, y = self.ball_3.pos
        x -= self.value_3_x
        y -= self.value_3_y
        if y+self.ball_size > self.height:
            y = self.height - self.ball_size
            self.value_3_y = -self.value_3_y
        if x+self.ball_size > self.width:
            x = self.width - self.ball_size
            self.value_3_x = -self.value_3_x
        if y < 0:
            y = 0
            self.value_3_y = -self.value_3_y
        if x < 0:
            x = 0
            self.value_3_x = -self.value_3_x
        self.ball_3.pos = (x, y)

