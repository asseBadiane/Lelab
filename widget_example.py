from kivy.lang import Builder

from kivy.uix.gridlayout import GridLayout
from kivy.properties import  StringProperty, BooleanProperty

Builder.load_file('widget_example.kv')

class WidgetsExample(GridLayout):
    mon_text = StringProperty('1')
    compteur = 1
    compteur_actif = BooleanProperty(False)

    def on_button_click(self):
        print("Button clicker")
        if self.compteur_actif:
           self.compteur += 1
           self.mon_text = str(self.compteur)
        
    def on_toggle_button_state(self, widget):
        print("toggle state: " + widget.state)
        if widget.state == 'down':
            widget.text = "On"
            self.compteur_actif = True
        elif widget.state == 'normal':
            widget.text = "Off"
            self.compteur_actif = False

    def on_switch_active(self, widget):
        print(f"widget {widget.active}")