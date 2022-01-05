from tkinter import*
import random
root = Tk()
root.geometry('400x400')
root.title('a rock paper and scizzer game')
root.resizable(0,0)
root.config(bg='yellow')
Label(root,text='lets play a game',font='arial',bg='green').pack()
user_pick = StringVar()
Label(root,text='write your choice',font='arial',bg='purple').place(x=20,y=70)
Entry(root,textvariable= user_pick, font='arial').place(x=90,y=70)
computer_pick= StringVar()
computer_pick=random.randint(1,3)

if computer_pick == 1:
    computer_pick =='rock'
elif computer_pick ==2:
    computer_pick =='paper'
elif computer_pick ==3:
    computer_pick =='scizzer'
result = StringVar()
def play():
    user_chal = user_pick.get()
    if user_chal == computer_pick:
        result.set('the game is tie')
    elif user_chal =='rock' and computer_pick =='paper':
        result.set('computer wins')
    elif user_chal =='paper' and computer_pick =='rock':
        result.set('user wins')
    elif user_chal =='rock' and computer_pick =='scizzor':
        result.set('user wins')
    elif user_chal =='scizzor' and computer_pick =='rock':
        result.set('computer wins')
    elif user_chal =='scizzzor' and computer_pick =='paper':
        result.set('user wins')
    elif user_chal =='paper' and computer_pick =='scizzor':
        result.set('computer wins')
    else:
        result.set('invalid input')
def reset():
    result.set("")
    user_pick("")
def exit():
    root.destroy()
Entry(root,textvariable= result,font='arial').place(x=40,y=100).place(x=,y=)
Button(root,font='arial',text='play',padx=5,command=play,bg='red').place(x=,y=)
Button(root,font='arial',text='exit',padx=5,command=exit,bg='white').place(x=,y=)
Button(root,font='arial',text='reset',padx=5,command=reset)
root.mainloop()
