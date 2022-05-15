import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout
from kivy.config import Config

kivy.require('2.1.0')
Config.set('graphics', 'resizable', True)


class MyApp(App):
    def build(self):
        rl = RelativeLayout()
        btn = Button(text='Hello World',
                     size_hint=(.2, .2),
                     pos=(396.0, 298.0))
        btn1 = Button(text='Hello World',
                      size_hint=(.2, .2),
                      pos=(-137.33, 298.0))

        rl.add_widget(btn)
        rl.add_widget(btn1)
        return rl


if __name__ == "__main__":
    MyApp().run()
