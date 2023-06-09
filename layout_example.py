from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.metrics import dp
from kivy.uix.scrollview import ScrollView

from kivy.lang import Builder

Builder.load_file("layout_example.kv")


# Versions 1
class MainWidget(Widget):
    pass


class BoxLayoutExample(BoxLayout):
    pass

class AnchorLayoutExample(AnchorLayout):
    pass

class GridLayoutExample(GridLayout):
    pass

class StackLayoutExample(StackLayout):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.orientation = "lr-bt"
        for i in range(0, 500):
            b = Button(text=str(i+1), size_hint=(None, None),
                       size=(dp(80), dp(80)))
            self.add_widget(b)
class ScrollViewExample(ScrollView):
    pass