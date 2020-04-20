from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

import sys

class Fenetre(BoxLayout):

        container = ObjectProperty(None)

class AppliApp(App):
    def build(self):
        self.root = Builder.load_file('kv/menu.kv')
    
    def menu(self,fenetreActuelle):
        self.changementFenetre(fenetreActuelle,'menu.kv')

    def jouer(self,fenetreActuelle):
        self.changementFenetre(fenetreActuelle,'jouer.kv')

    def option(self,fenetreActuelle):
        self.changementFenetre(fenetreActuelle,'option.kv')
    
    def changementFenetre(self,fenetreActuelle,fenetreSuivante):
        Builder.unload_file('kv/'+fenetreActuelle)
        self.root.container.clear_widgets()
        screen = Builder.load_file('kv/'+fenetreSuivante)
        self.root.container.add_widget(screen)

    def quitter(self):
        sys.exit()

if __name__ == "__main__":
    
    AppliApp().run()