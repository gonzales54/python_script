import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

import random

red = [1, 0, 0, 1]
blue = [0, 1, 0, 1]
green = [0, 0, 1, 1]
purple = [1, 0, 1, 1]

kivy.require('2.1.0')


class BoxLayoutApp(App):
    def build(self):
        superbox = BoxLayout(orientation='vertical')

        HB = BoxLayout(orientation='horizontal')

        colors = [red, green, blue, purple]

        btn1 = Button(text='One',
                      background_color=random.choice(colors),
                      font_size=32,
                      size_hint=(0.7, 1)
                      )
        btn2 = Button(text='Two',
                      background_color=random.choice(colors),
                      font_size=32,
                      size_hint=(0.7, 1)
                      )

        HB.add_widget(btn1)
        HB.add_widget(btn2)

        VB = BoxLayout(orientation='vertical')

        btn3 = Button(text='Three',
                      background_color=random.choice(colors),
                      font_size=32,
                      size_hint=(1, 15)
                      )
        btn4 = Button(text='Four',
                      background_color=random.choice(colors),
                      font_size=32,
                      size_hint=(1, 15)
                      )

        VB.add_widget(btn3)
        VB.add_widget(btn4)

        superbox.add_widget(HB)
        superbox.add_widget(VB)

        return superbox


if __name__ == '__main__':
    BoxLayoutApp().run()
