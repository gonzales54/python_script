import kivy
from kivy.app import App
from kivy.uix.button import Button

kivy.require('2.1.0')


class ButtonApp(App):
    def build(self):
        # btn = Button(text="Push me")
        btn = Button(text='Push me',
                     font_size="20sp",
                     background_color=(1, 1, 1, 1),
                     color=(1, 1, 1, 1),
                     size=(32, 32),
                     size_hint=(.2, .2),
                     pos=(300, 250))
        return btn


if __name__ == '__main__':
    ButtonApp().run()
