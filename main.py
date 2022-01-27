from re import A
from kivy.app import App
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty, Clock
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.graphics.vertex_instructions import Line, Rectangle, Ellipse
from kivy.graphics.context_instructions import Color


class WidgetsExample(GridLayout):
    count = 1
    count_enabled = BooleanProperty(False)
    my_text = StringProperty("1")

    text_input_str = StringProperty("Label Display")

    def on_button_click(self):
        print("Button Clicked")
        if self.count_enabled:
            self.count += 1
            self.my_text = str(self.count)

    def on_toggle_button_state(self, widget):
        print("toggle state "+widget.state)
        if widget.state == "normal":
            widget.text = "OFF"
            self.count_enabled = False
        else:
            widget.text = "ON"
            self.count_enabled = True

    def on_switch_active(self, widget):
        print("Switch " + str(widget.active))

    def on_slider_value(self, widget):
        print("Slider: " + str(int(widget.value)))

    def on_text_validate(self, widget):
        self.text_input_str = widget.text


class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "lr-tb"
        for i in range(0, 100):
            size = dp(100)
            b = Button(text=str(i+1), size_hint=(None, None),
                       size=(size, size))
            self.add_widget(b)


# class GridLayoutExample(GridLayout):
#     pass


class AnchorLayoutExample(AnchorLayout):
    pass


class BoxLayoutExample(BoxLayout):
    '''
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        b1 = Button(text="A")
        b2 = Button(text="B")
        b3 = Button(text="C")
        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)
        '''
    pass


class MainWidget(Widget):
    pass


class TheLabApp(App):
    pass


class CanvasExample1(Widget):
    pass


class CanvasExample2(Widget):
    pass


class CanvasExample3(Widget):
    pass

# good for using a loop to show many shapes


class CanvasExample4(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Line(points=(100, 100, 400, 500), width=2)
            Color(0, 1, 0)
            Line(circle=(400, 200, 80), width=2)
            Line(rectangle=(800, 800, 150, 200), width=5)
            self.rect = Rectangle(pos=(650, 500), size=(150, 200))

    def on_button_a_click(self):
        # print('foo')
        x, y = self.rect.pos
        w, h = self.rect.size
        inc = dp(10)

        diff = self.width - (x+w)
        if diff < inc:
            inc = diff

        x += inc
        self.rect.pos = (x, y)


class CanvasExample5(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ball_size = dp(50)
        self.vx = dp(3)  # velocity x
        self.vy = dp(4)  # velocity y
        with self.canvas:
            self.ball = Ellipse(pos=self.center, size=(
                self.ball_size, self.ball_size))
        Clock.schedule_interval(self.update, 1/120)

    def on_size(self, *args):
        print("on_size : " + str(self.width) + ", " + str(self.height))
        self.ball.pos = (self.center_x-self.ball_size/2,
                         self.center_y-self.ball_size/2)

    def update(self, dt):  # delta time
        # print('update')
        # sets vars x,y to current position of the ball
        x, y = self.ball.pos

        # sets the current position of x,y to vx,vy. And with every instance the ball will move,
        # this is the reason they are named vx=velocityX and vy=velocityY
        x += self.vx
        y += self.vy

        # create a barrier on the top of the window so that the ball will stay inbounds:
        # do this by checking if the vertical position of the ball plus the ball_size
        # is greater than the height of the window
        # if true, then reverse ball in opposite direction
        if y + self.ball_size > self.height:
            # changes the ball poisiton of y to be the height of the window
            y = self.height-self.ball_size
            # minus the size of the ball. this way, the ball is always inbounds
            self.vy = -self.vy  # changes direction of ball vertically

        # create a barrier on the right of the window so that the ball will stay inbounds:
        # check if the ball size + x pos of ball is greater than total width of window,
        # i.e. once the ball reaches the right side of the window
        # when this happnes, set ball position to jsut before the wall and reverse x velocity
        if x + self.ball_size > self.width:
            x = self.width-self.ball_size
            self.vx = -self.vx
        # do this for the left and bottom of the window:
        if y < 0:  # y i the position of the ball and if it's lower then flip velocity direction
            y = 0
            self.vy = -self.vy
        if x < 0:
            x = 0
            self.vx = -self.vx

        self.ball.pos = (x, y)


class CanvasExample6(Widget):
    pass


class CanvasExample7(Widget):
    pass


class CanvasExample8(BoxLayout):
    pass


TheLabApp().run()


# BUGG FIXES:
#
