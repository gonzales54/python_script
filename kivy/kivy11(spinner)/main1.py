import kivy
from kivy.config import Config
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.floatlayout import FloatLayout

kivy.require('2.1.0')
Config.set('graphics', 'resizable', True)


class SpinnerExample(App):
    def build(self):
        layout = FloatLayout()

        self.spinnerObject = Spinner(text="Python",
                                     values=("Python", "Java", "C++", "C", "C#", "PHP"),
                                     background_color=(0.784, 0.443, 0.216, 1))

        self.spinnerObject.size_hint = (0.3, 0.2)

        self.spinnerObject.pos_hint = {'x': .35, 'y': .75}

        layout.add_widget(self.spinnerObject)
        self.spinnerObject.bind(text=self.on_spinner_select)

        self.spinnerSelection = Label(text="Selected value in spinner is: %s" % self.spinnerObject.text)

        layout.add_widget(self.spinnerSelection)
        self.spinnerSelection.pos_hint = {'x': .3, 'y': .35}

        return layout

    def on_spinner_select(self, spinner, text):
        self.spinnerSelection.text = ("Selected value in spinner is: %s" % self.spinnerObject.text)

        print('The spinner', spinner, 'have text', text)

        # Run the app


if __name__ == '__main__':
    SpinnerExample().run()
