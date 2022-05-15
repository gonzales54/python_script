import kivy
from kivy.app import App
from kivy.uix.label import Label

kivy.require('2.1.0')


class MyFirstApp(App):
    def build(self):
        return Label(text='Hello World')


if __name__ == '__main__':
    MyFirstApp().run()
