import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color

kivy.require('2.1.0')


class Canvas(Widget):
    def __init__(self, **kwargs):
        super(Canvas, self).__init__(**kwargs)

        with self.canvas:
            # Color(.234, .456, .678, .8)
            Color(1, 0, 0, 1)
            self.rect = Rectangle(source='main.jpg',
                                  pos=self.pos,
                                  size=self.size
                                  # pos=self.center,
                                  # size=(self.width / 2.,self.height / 2.)
                                  )
            self.bind(pos=self.update_rect,
                      size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size


class CanvasApp(App):
    def build(self):
        return Canvas()


if __name__ == '__main__':
    CanvasApp().run()
