from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button


class MainScreen(Screen):
    def getValue(value): 
        pass


class BtnNumber(Button):
    def on_release(self):
        MainScreen.getValue(self.text)
        

class CalculatorApp(App):
    def build(self):
        return MainScreen()
    

if __name__ == '__main__':
    CalculatorApp().run()
