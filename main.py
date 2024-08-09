from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.label import Label


class MainScreen(Screen):
    def getValue(value): 
        print(value)
        

class BtnNumber(Button):
    def on_release(self):
        MainScreen.getValue(self.text)
        LabelShow().text += self.text


class LabelShow(Label):
    def insertText(text):
        pass


class CalculatorApp(App):
    def build(self):
        return MainScreen()
    

if __name__ == '__main__':
    CalculatorApp().run()
