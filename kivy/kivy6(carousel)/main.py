import kivy
from kivy.app import App
from kivy.uix.image import AsyncImage
from kivy.uix.carousel import Carousel

kivy.require('2.1.0')


class CarouselApp(App):
    def build(self):
        carousel = Carousel(direction='right')

        for i in range(10):
            src = 'https://placehold.jp/837c7c/ffffff/480x270.png?text=slide-{}'.format(i)
            image = AsyncImage(source=src, allow_stretch=True)
            carousel.add_widget(image)
        return carousel


if __name__ == '__main__':
    CarouselApp().run()
