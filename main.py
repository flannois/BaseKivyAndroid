from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class TestAndroid(BoxLayout):
    def __init__(self,**kwargs):
        super(TestAndroid,self).__init__(**kwargs)



class TestAndroidApp(App):
    def build(self):
        Builder.load_file('fichier.kv')
        return TestAndroid()




if __name__ == "__main__":
    
    TestAndroidApp().run()