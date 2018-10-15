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

    formula='0'
    
    def upd_label (self):
        self.lbl.text=self.formula

    def add_number(self, instance):
        if instance.text=='.' and self.formula.find(instance.text)==-1:
            self.formula+=instance.text
            self.upd_label()
        elif instance.text=='.' and self.formula.find(instance.text)!=-1:
            self.formula+=instance.text
            self.upd_label()
        elif self.formula=='0' and instance.text.isdigit()==True:
            print('***** IsDigit *****')
            self.formula=str(int(self.formula)+int(instance.text))
            self.upd_label()
        elif self.formula=='0' and instance.text in ['(',')']:
            self.formula=instance.text
            self.upd_label()
        else:
            self.formula+=instance.text
            self.upd_label()
    
    def add_operator (self, instance):
        if instance.text=='x':
            self.formula+='*'
        else:
            self.formula+=instance.text
        self.upd_label()
    
    def get_result (self, instance):
        try:
            self.formula=str(eval(self.lbl.text))
        # print('Eval= ',eval(self.lbl.text))
            self.upd_label()
            self.formula='0'
        except:
            print('Was an error')
            self.formula='0'
            self.lbl.text="Error"

    def clear (self, instance):
        self.formula='0'
        self.lbl.text='0'

    def backspace (self, instance):
        # print(type(self.lbl.text))
        self.lbl.text=self.lbl.text[:len(self.lbl.text)-1]
        # self.upd_label()
        if len(self.lbl.text) is 0:
            self.formula=self.lbl.text='0'
        else:
            self.formula=self.lbl.text
        
        # pass
    def add_simbol(self):
        pass

    def build(self):
        # self.formula='0'
        # scat=Scatter()
        gl=GridLayout(cols=5, spacing=5, size_hint=(1,.6))
        bl=BoxLayout(orientation='vertical', padding=5)
        # scat.add_widget(fl)
        self.lbl=Label(text='0', font_size=40, size_hint=(1,.2), halign='right', 
        valign='center', text_size=(400-50, 500*.4-50))
       
        bl.add_widget(self.lbl)

        gl.add_widget(Button(text='7', on_press=self.add_number))
        gl.add_widget(Button(text='8', on_press=self.add_number))
        gl.add_widget(Button(text='9', on_press=self.add_number))
        gl.add_widget(Button(text='+', on_press=self.add_operator))
        # gl.add_widget(Button(text='<--', on_press=self.clear))
        gl.add_widget(Button(text='<--', on_press=self.backspace))

        

        gl.add_widget(Button(text='4', on_press=self.add_number))
        gl.add_widget(Button(text='5', on_press=self.add_number))
        gl.add_widget(Button(text='6', on_press=self.add_number))
        gl.add_widget(Button(text='-', on_press=self.add_operator))
        gl.add_widget(Button(text='(', on_press=self.add_number))

        gl.add_widget(Button(text='1', on_press=self.add_number))
        gl.add_widget(Button(text='2', on_press=self.add_number))
        gl.add_widget(Button(text='3', on_press=self.add_number))
        gl.add_widget(Button(text='x', on_press=self.add_operator))
        gl.add_widget(Button(text=')', on_press=self.add_number))



        # gl.add_widget(Button(text='C', on_press=self.sett_zerro))
        # gl.add_widget(Widget())
        gl.add_widget(Button(text='0', on_press=self.add_number))
        gl.add_widget(Button(text='.', on_press=self.add_number))
        gl.add_widget(Button(text='=', on_press=self.get_result))
        gl.add_widget(Button(text='/', on_press=self.add_operator))
        gl.add_widget(Button(text='C', on_press=self.clear))

        

        bl.add_widget(gl)

        return bl

    def btn_click(self, instance):
        print("Button pressed")
        print('The button <%s> is being pressed' % instance.text)
        instance.text='New Text after Click'
        instance.background_color=[1,0,0,1]

if __name__=='__main__':
    sergApp().run()