import kivy
from kivy.app import App
from kivy.uix.progressbar import ProgressBar
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

kivy.require('2.1.0')


class MyWidget(Widget):
    progress_bar = ObjectProperty()

    def __init__(self, **kwargs):
        super(MyWidget, self).__init__(**kwargs)
        self.progress_bar = ProgressBar()
        self.popup = Popup(
            title='Download',
            content=self.progress_bar
        )
        self.popup.bind(on_open=self.puopen)
        self.add_widget(Button(text='Download', on_release=self.pop))

    def pop(self, instance):
        self.progress_bar.value = 1
        self.popup.open()

    def next(self, dt):
        if self.progress_bar.value >= 100:
            return False
        self.progress_bar.value += 1

    def puopen(self, instance):
        Clock.schedule_interval(self.next, 1 / 25)


class MyApp(App):
    def build(self):
        return MyWidget()


if __name__ == "__main__":
    MyApp().run()
