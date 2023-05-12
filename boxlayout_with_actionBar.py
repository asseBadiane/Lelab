from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout

Builder.load_file("boxlayout_with_actionBar.kv")


class BoxLayoutWithActionBar(BoxLayout):
    title = StringProperty()
