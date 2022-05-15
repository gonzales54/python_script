import kivy
from kivy.app import App
from kivy.config import Config
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.floatlayout import FloatLayout

kivy.require('2.1.0')
Config.set('graphics', 'resizable', True)


class SpinnerApp(App):
    def build(self):
        layout = FloatLayout()
        self.spinnerobject = Spinner(text="Python",
                                     values=("Python", "Java", "C++", "C", "C#", "PHP"),
                                     background_color=(0.784, 0.443, 0.216, 1))
        self.spinnerobject.size_hint = (0.3, 0.2)
        self.spinnerobject.pos_hint = {'x': .35, 'y': .75}

        layout.add_widget(self.spinnerobject)
        return layout


if __name__ == '__main__':
    SpinnerApp().run()
