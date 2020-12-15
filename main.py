from kivy.app import App
from kivy.config import Config
Config.set('graphics', 'width',  720)
Config.set('graphics', 'height', 720)

        

class ScrabbleApp(App):
    def build(self):
        pass



if __name__ == "__main__":
    
    ScrabbleApp().run()






