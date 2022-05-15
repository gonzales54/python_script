import kivy
from kivy.app import App
from kivy.core.window import Window

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

kivy.require('2.1.0')
Window.size = (1000, 600)


class TopWidget(BoxLayout):
    pass


class TopApp(App):
    def build(self):
        return TopWidget()


if __name__ == '__main__':
    TopApp().run()
