from kivy.lang import Builder

from kivy.uix.gridlayout import GridLayout
from kivy.properties import  StringProperty

Builder.load_file('widget_example.kv')

class WidgetsExample(GridLayout):
    mon_text = StringProperty('1')

    def on_button_click(self):
        print("Button clicker")
        
        self.mon_text = "hello"
        

