from kivy.app import App
from kivy.uix.button import Button
# from kivy.config import Config
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.config import Config
# from kivy.uix.scatter import Scatter

Config.set('graphics','resizable','0')
Config.set('graphics','width',400)
Config.set('graphics','height',500)

class sergApp(App):

    def add_number(self, instance):
        self.formula+=str(instance.text)

    def build(self):
        self.formula='0'
        # scat=Scatter()
        gl=GridLayout(cols=4, spacing=5, size_hint=(1,.6))
        bl=BoxLayout(orientation='vertical', padding=25)
        # scat.add_widget(fl)
        self.lbl=Label(text='012345678', font_size=40, size_hint=(1,.4), halign='right', valign='center', text_size=(400-50, 500*.4-50))
        bl.add_widget(self.lbl)

        gl.add_widget(Button(text='7', on_press=self.add_number))
        gl.add_widget(Button(text='8', on_press=self.add_number))
        gl.add_widget(Button(text='9', on_press=self.add_number))
        gl.add_widget(Button(text='X', on_press=self.add_number))

        gl.add_widget(Button(text='4', on_press=self.add_number))
        gl.add_widget(Button(text='5', on_press=self.add_number))
        gl.add_widget(Button(text='6', on_press=self.add_number))
        gl.add_widget(Button(text='-', on_press=self.add_number))

        gl.add_widget(Button(text='1', on_press=self.add_number))
        gl.add_widget(Button(text='2', on_press=self.add_number))
        gl.add_widget(Button(text='3', on_press=self.add_number))
        gl.add_widget(Button(text='+', on_press=self.add_number))

        gl.add_widget(Widget())
        gl.add_widget(Button(text='0', on_press=self.add_number))
        gl.add_widget(Button(text=',', on_press=self.add_number))
        gl.add_widget(Button(text='=', on_press=self.add_number))

        bl.add_widget(gl)

        return bl

    def btn_click(self, instance):
        print("Button pressed")
        print('The button <%s> is being pressed' % instance.text)
        instance.text='New Text after Click'
        instance.background_color=[1,0,0,1]

if __name__=='__main__':
    sergApp().run()