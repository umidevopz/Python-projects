from kivy.app import App
from kivy.uix.widget import Widget 


class myapp(Widget):
    pass

class many(App):
    def build(self):
        return myapp()


if __name__ == '__main__':
    myapp.run()