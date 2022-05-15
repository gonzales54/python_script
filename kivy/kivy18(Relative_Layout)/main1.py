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

        btn1 = Button(size_hint=(.2, .2),
                      pos_hint={'x': 0, 'y': 0},
                      text='B1')
        btn2 = Button(size_hint=(.2, .2),
                      pos_hint={'right': 1, 'y': 0},
                      text='B1')
        btn3 = Button(size_hint=(.2, .2),
                      pos_hint={'center_x': .5, 'center_y': .5},
                      text='B3')
        btn4 = Button(size_hint=(.2, .2),
                      pos_hint={'x': 0, 'top': 1},
                      text='B4')
        btn5 = Button(size_hint=(.2, .2),
                      pos_hint={'right': 1, 'top': 1},
                      text='B5')

        rl.add_widget(btn1)
        rl.add_widget(btn2)
        rl.add_widget(btn3)
        rl.add_widget(btn4)
        rl.add_widget(btn5)
        return rl


if __name__ == "__main__":
    MyApp().run()
