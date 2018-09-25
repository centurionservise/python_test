from kivy.app import App
from kivy.uix.button import Button
from kivy.config import Config
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter

Config.set('graphics','resizable','0')
Config.set('graphics','width','640')
Config.set('graphics','height','480')

class sergApp(App):

    def build(self):

        scat=Scatter()
        fl=FloatLayout(size=(300,300))
        scat.add_widget(fl)

        fl.add_widget(Button(
            text='Serg First Button on Kivy',
            font_size=20,
            on_press=self.btn_click,
            background_color=[.55,.86,.85,1],
            background_normal='',
            size_hint=(.5,.25),
            pos=(640/2-(640/2/2),480/2-(480*.25/2))
                      ))
        return scat

    def btn_click(self, instance):
        print("Button pressed")
        print('The button <%s> is being pressed' % instance.text)
        instance.text='New Text after Click'
        instance.background_color=[1,0,0,1]

if __name__=='__main__':
    sergApp().run()