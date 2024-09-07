from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

class TelaLogin(Screen):
    pass

class TelaPrincipal(Screen):
    pass

class TelaVenda(Screen):
    pass

class TelaNovaVenda(Screen):
    pass

class TelaEstoque(Screen):
    pass

class TelaFuncionarios(Screen):
    pass

class GerenciadorTelas(ScreenManager):
    pass

kv = Builder.load_file('loja.kv')

class LojaApp(App):
    def build(self):
        return kv
    
if __name__ == "__main__":
    LojaApp().run()