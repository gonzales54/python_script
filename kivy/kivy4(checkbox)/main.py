import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.gridlayout import GridLayout


class check(GridLayout):
    def __init__(self, **kwargs):
        super(check, self).__init__(**kwargs)
        self.cols = 2

        self.add_widget(Label(text='Male'))
        self.active = CheckBox(active=True)
        self.add_widget(self.active)

        self.add_widget(Label(text='Female'))
        self.active = CheckBox(active=True)
        self.add_widget(self.active)

        self.add_widget(Label(text='other'))
        self.active = CheckBox(active=True)
        self.add_widget(self.active)


class CheckBoxApp(App):
    def build(self):
        return check()


if __name__ == '__main__':
    CheckBoxApp().run()
