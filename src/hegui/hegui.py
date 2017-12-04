import kivy
#kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label


class HEguiApp(App):

    #icon = 'custom-kivy-icon.png'
    title = 'Home Economy'

    def __init__(self, my_string, **kwargs):
        super(HEguiApp, self).__init__(**kwargs)
        self.my_string = my_string

    def build(self):
        return Label(text=self.my_string)


if __name__ == '__main__':
    HEguiApp().run()