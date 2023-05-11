from kivy.lang import Builder

from kivy.uix.gridlayout import GridLayout
from kivy.properties import  StringProperty

Builder.load_file('widget_example.kv')

class WidgetsExample(GridLayout):
    mon_text = StringProperty('1')
    compteur = 1

    def on_button_click(self):
        print("Button clicker")
        self.compteur += 1
        self.mon_text = str(self.compteur)
        print(f"Compteur: {self.compteur}")

