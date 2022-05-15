from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class AnchorLayoutApp(App):
    def build(self):
        layout = AnchorLayout(
            anchor_x='right',
            anchor_y='bottom'
        )
        btn = Button(
            text="Hello World",
            size_hint=(.3, .3),
            background_color=(1.0, 0.0, 0.0, 1.0)
        )
        layout.add_widget(btn)
        return layout


if __name__ == '__main__':
    AnchorLayoutApp().run()
