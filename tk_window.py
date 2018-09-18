from tkinter import *
import tkinter.messagebox as box

def switch() :
    color='green' if window.cget( 'bg' ) == 'yellow' else 'yellow'
    window.configure( bg = color )

def pr_exit():
    exit

def mess_box():
    var = box.askyesno( 'Message Box' , 'Proceed?' )
    if var == 1 :
        box.showinfo( 'Yes Box', 'Proceeding...' )
    else :
        box.showwarning( 'No Box', 'Cancelling...' )


window = Tk()

window.title( 'Python First Program' )
# window.geometry('400x100')
window.resizable(width=False, height=False)

label = Label( window , text = 'Pileshaka SUPER PUPER' )
# btn_exit = Button( window , text = 'EXIT' , command=pr_exit )
btn_switch = Button( window , text = 'Switch' , command=switch , relief=RAISED, bd=4)
btn_message = Button( window , text = 'Message Box' , command=mess_box , relief=RAISED, bd=4)
# btn_switch.configure()





# btn_exit.place(x=0,y=0)
# btn_switch.place(x=170,y=60)
btn_switch.pack(padx=200, pady=10)
btn_message.pack(padx=200, pady=10)

# label.pack( padx = 200 , pady = 50 )
# label.pack()
# label.place(x=130,y=30)
label.pack(padx=200, pady=10)




window.mainloop()