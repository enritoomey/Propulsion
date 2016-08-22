from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class PoderCalorificoScreen(GridLayout):

    def __init__(self, **kwargs):
        super(PoderCalorificoScreen, self).__init__(**kwargs)
        self.cols = 4
        self.add_widget(Label(text='Carbono'))
        self.carbono = TextInput(multiline=False, height=)
        self.add_widget(self.carbono)
        self.add_widget(Label(text='Oxigeno'))
        self.oxigeno = TextInput(multiline=False)
        self.add_widget(self.oxigeno)
        self.add_widget(Label(text='Hidrogeno'))
        self.hidrogeno = TextInput(multiline=False)
        self.add_widget(self.hidrogeno)
        self.add_widget(Label(text='Azufre[%]'))
        self.azufre = TextInput(multiline=False)
        self.add_widget(self.azufre)
        self.add_widget(Label(text='Fr'))
        self.fr = TextInput(multiline=False)
        self.add_widget(self.fr)

        self.calcular = Button(text='Calcular')
        self.add_widget(self.calcular)
        self.add_widget(Label(text='HVS'))
        self.HVS = TextInput(readonly=True)
        self.add_widget(self.HVS)
        self.add_widget(Label(text='HVI'))
        self.HVI = TextInput(readonly=True)
        self.add_widget(self.HVI)


class MyApp(App):

    def build(self):
        return PoderCalorificoScreen()


if __name__ == '__main__':
    MyApp().run()