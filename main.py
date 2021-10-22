from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout

class MyApp(App):
    def build(self):
        superBox = BoxLayout(orientation='vertical')
        HBL = BoxLayout(orientation='horizontal')
        VBL = BoxLayout(orientation='vertical')
        btn1 = Button(text="One")
        btn2 = Button(text="Two")
        btn3 = Button(text="Three")
        btn4 = Button(text="Four")
        HBL.add_widget(btn1)
        HBL.add_widget(btn2)
        superBox.add_widget(HBL)
        superBox.add_widget(VBL)
#        fl = FloatLayout(site=(300, 300))
#        TextInput('команда')
        return superBox

    def btn_press(self):
        pass


if __name__ == "__main__":
    root = MyApp()
    root.run()

