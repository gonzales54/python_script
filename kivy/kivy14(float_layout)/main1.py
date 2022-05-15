import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config

kivy.require('2.1.0')
Config.set('graphics', 'resizable', True)


class MyApp(App):
    def build(self):
        fl = FloatLayout()
        btn = Button(text='Hello World',
                     size_hint=(.3, .5),
                     background_color=(.3, .6, .7, 1),
                     pos_hint={'x': .2, 'y': .2})
        fl.add_widget(btn)
        return fl


if __name__ == "__main__":
    MyApp().run()
