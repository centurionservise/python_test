from tkinter import *

def switch() :
    color='green' if window.cget( 'bg' ) == 'yellow' else 'yellow'
    window.configure( bg = color )

def pr_exit():
    exit

window = Tk()

window.title( 'Python First Program' )
window.geometry('400x100')

label = Label( window , text = 'Pileshaka SUPER PUPER' )
# btn_exit = Button( window , text = 'EXIT' , command=pr_exit )
btn_switch = Button( window , text = 'Switch' , command=switch )





# btn_exit.place(x=0,y=0)
btn_switch.place(x=170,y=60)

# label.pack( padx = 200 , pady = 50 )
# label.pack()
label.place(x=130,y=30)




window.mainloop()