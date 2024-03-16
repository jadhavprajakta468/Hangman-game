# -*- coding:sss utf-8 -*-
"""
Created on Thu Nov  2 00:09:30 2023

@author: admin
"""

import random
from tkinter import *
from PIL import ImageTk, Image
# list of words
wordlist=["hangman","pythoon","blaah","hoope"]
cat1=["afghanistan","ukaraine","malaysia","singapore","bangladesh","bulgaria","cambodia","ethiopia","indonesia","jamaica","krygyzstan","luxembourg"]
cat2=["tangerine","dragonfruit","pomegranate","jackfruit","strawberry","blueberry","avacado","watermelon","pineapple","grapefruit"]
cat3=["tiger","cheetah","elephant","snake","crocodile","buffalo","donkey","koala","rabbit","panda"]

# list for randomly selected word
#guessed word with underscores for unknown letters.
guessed_letters=[]    
word=""
#letters that have already been guessed.
guessed_word=["_"]*len(word)
attempts=0
attemptext=""
atxt=""

# function to get random word from list
def getword(wlist):
    w=random.choice(wlist)
    return w

   
def animal():
    global word,guessed_letters,guessed_word,attempts,attemptext,hintcount
    hintcount=0
    #getting random word
    wo=getword(cat3)
    word=wo.upper()
    guessed_letters=[]
    guessed_word=["_"]*len(word)
    guess=False
    attempts=10
    atxt=attemptext+str(attempts)
    popup()
   
def fruit():
    global word,guessed_letters,guessed_word,attempts,attemptext,hintcount
    hintcount=0
    wo=getword(cat2)
    word=wo.upper()
    guessed_letters=[]
    guessed_word=["_"]*len(word)
    guess=False
    attempts=10
    atxt=attemptext+str(attempts)
    popup()
   
def country():
    global word,guessed_letters,guessed_word,attempts,attemptext,hintcount
    hintcount=0
    wo=getword(cat1)
    word=wo.upper()
    guessed_letters=[]
    guessed_word=["_"]*len(word)
    guess=False
    attempts=10
    atxt=attemptext+str(attempts)
    popup()
# category window(2nd window)
def choosecategory():
    top=Toplevel(gui)
    top.geometry("1024x650")  
    top.title("Category")
    bg1 = PhotoImage(file ="welcomepage.png")
    # Show image using label -
    label2 = Label(top,image= bg1)
    label2.place(x = 0, y = 0)
   
    category = Label(top,text="C H O O S E C A T E G O R Y",font=("Georgia",17),bg='white')
    category.place(x=360,y=100)
    #Animal category
    category1 = Label(top,text="Animal",font=("Georgia",17),bg='white')
    category1.place(x=160,y=200)
    ani = PhotoImage(file="animal_button1.png")
    animal_label=Label(top,image = ani)
    animal_btn = Button(top,image = ani,command=animal)
    animal_btn.place(x=105,y=250)
    
    #fruit category
    category2 = Label(top,text="Fruit",font=("Georgia",17),bg='white')
    category2.place(x=470,y=200)
    fru = PhotoImage(file="fruit_button1.png")
    fruit_label = Label(top,image =fru)
    fruit_btn = Button(top,image =fru,command=fruit)
    fruit_btn.place(x=405,y=250)
    #country category
    category3 = Label(top,text="Country",font=("Georgia",17),bg='white')
    category3.place(x=760,y=200)
    coun =PhotoImage(file="country_button1.png")
    country_label = Label(top,image = coun)
    country_btn = Button(top,image = coun,command=country)
    country_btn.place(x=705,y=250)
   
    top.mainloop()    

#function for hint button
hintcount=0    
def clickedhint(wig):
    global hintcount
    if(hintcount<2):
        callhint(wig)
        hintcount+=1
    else:
        hidebutton(wig)

def callhint(wig):
    
    global guessed_word,guessed_letters,word,hintcount
    wo=word.upper()
    #converts the word into a list of its characters 
    tolist=list(word)
    hintlist=[]
    for i in word:
        if i not in guessed_letters:
            #hintlist will contain characters from the word that have not been guessed.
            hintlist.append(i)
    #selects a random character from the hintlist
    h=random.choice(hintlist)
    guessed_letters.append(h)
    a=0
    for char in word:
        if char in guessed_letters:
            guessed_word[a]=wo[a]
        else:
            guessed_word[a]="_"
        a+=1
    display()
  
# function for checking  guess
def checkletter(gu,w):
    global atxt,attemptext,word,guessed_word
    global attempts,guessed_letters
   
    attemptext="A T T E M P T S L E F T: "
    exp=""
    g=gu.upper()
    hidebutton(w)
   
    if g in guessed_letters:
        return
    else:
        guessed_letters.append(g)
    a=0
    for char in word:
        if char in guessed_letters:
            guessed_word[a]=word[a]
        else:
            guessed_word[a]="_"
        a+=1
    if g in word:
        display()
    else:
       
        attempts-=1
        atxt=attemptext+str(attempts)
        for i in guessed_word:
            exp+=i
        display()
       

    if "_" not in guessed_word:
        #call new congo pop up screen
        youwin()
       
    if attempts==0:
        youloose(word)
       
#function for displaying images after guess
def display():
    global my_Label,attempts
    global img0,img1,img2,img3,img4,img5,img6,img7,img8,img9,img10
    exp=""
    for i in guessed_word:
        exp+=i
    text_change_label.config(text=' '.join(str(exp)))
    attempts_label.config(text=' '.join(str(atxt)))
    if attempts==10:
        my_Label.config(image=img0)
    elif attempts==9:
        my_Label.config(image=img1)
    elif attempts==8:
        my_Label.config(image=img2)
    elif attempts==7:
        my_Label.config(image=img3)
    elif attempts==6:
        my_Label.config(image=img4)
    elif attempts==5:
        my_Label.config(image=img5)
    elif attempts==4:
        my_Label.config(image=img6)
    elif attempts==3:
        my_Label.config(image=img7)
    elif attempts==2:
        my_Label.config(image=img8)
    elif attempts==1:
        my_Label.config(image=img9)
    elif attempts==0:
        my_Label.config(image=img10)
   
# function to hide alphabet after clicking it
def hidebutton(let):
    let.destroy()
 
# popup window for main game
def popup():
        global text_change_label,attempts_label,attempts,my_Label
        global img0,img1,img2,img3,img4,img5,img6,img7,img8,img9,img10
   
        root=Toplevel(gui)
        root.geometry("1024x650")  
        root.title("Hangman")
       
        bgg =PhotoImage(file="welcomepage.png")
       
        label3 = Label(root,image=bgg)
        label3.place(x=0 ,y=0 )
       
       
        attempts_label = Label(root, text=" ",font=("Georgia",12),bg='white')
       
       
        guess_the_word_label = Label(root, text="GUESS THE WORD!!", font=("Georgia",14),bg='white') #guess the word asa lihun yeil
        guess_the_word_label.place(x=630,y=180)
       
       
        text_change_label= Label(root,text=' ',bg='white',font=('Georgia',20))
        text_change_label.place(x=600,y=260)
       
       
        # letter selection buttons
        a =Button(root, text='a', fg= 'black', bg= 'white', height = 2,width=4,command=lambda:checkletter('a',a))    
        a.place(x=460,y = 400)
       
        b =Button(root, text='b', fg= 'black', bg= 'white', height = 2,width=4,command=lambda:checkletter('b',b))
        b.place(x=500,y = 400)
       
        c=Button(root, text='c', fg= 'black', bg= 'white', height = 2,width=4,command=lambda:checkletter('c',c))
        c.place(x=540,y = 400)
       
        d =Button(root, text='d', fg= 'black', bg= 'white', height = 2,width=4,command=lambda:checkletter('d',d))
        d.place(x=580,y= 400)
       
        e =Button(root, text='e', fg= 'black', bg= 'white', height = 2,width=4,command=lambda:checkletter('e',e))
        e.place(x=620,y = 400)
       
        f =Button(root, text='f', fg= 'black', bg= 'white', height = 2,width=4,command=lambda:checkletter('f',f))
        f.place(x=660,y = 400)
       
        g =Button(root, text='g', fg= 'black', bg= 'white', height = 2,width=4,command=lambda:checkletter('g',g))
        g.place(x=700,y = 400)
       
        h =Button(root, text='h', fg= 'black', bg= 'white', height = 2,width=4,command=lambda:checkletter('h',h))
        h.place(x=740,y = 400)
       
        i =Button(root, text='i', fg= 'black', bg= 'white', height = 2,width=4,command=lambda:checkletter('i',i))
        i.place(x=780,y = 400)
       
        j =Button(root,text='j', fg= 'black', bg= 'white', height = 2,width=4,command=lambda:checkletter('j',j))
        j.place(x=820,y = 400)
       
        k =Button(root,text='k', fg= 'black', bg= 'white', height = 2,width=4,command=lambda:checkletter('k',k))
        k.place(x=860,y = 400)
       
        l =Button(root, text='l', fg= 'black', bg= 'white', height = 2,width=4,command=lambda:checkletter('l',l))
        l.place(x=900,y = 400)
       
        m =Button(root, text='m', fg= 'black', bg= 'white', height = 2,width=4,command=lambda:checkletter('m',m))
        m.place(x=940,y = 400)
       
        n =Button(root, text='n', fg= 'black', bg= 'white', height = 2,width=4,command=lambda:checkletter('n',n))
        n.place(x= 460,y = 442)
       
        o =Button(root, text='o', fg= 'black', bg= 'white', height = 2,width=4,command=lambda:checkletter('o',o))
        o.place(x= 500,y = 442)
       
        p =Button(root, text='p', fg= 'black', bg= 'white', height = 2,width=4,command=lambda:checkletter('p',p))
        p.place(x= 540,y = 442)
       
        q =Button(root, text='q', fg= 'black', bg= 'white', height = 2,width=4,command=lambda:checkletter('q',q))
        q.place(x= 580,y = 442)
       
        r =Button(root, text='r', fg= 'black', bg= 'white', height = 2,width=4,command=lambda:checkletter('r',r))
        r.place(x= 620,y = 442)
       
        s =Button(root, text='s', fg= 'black', bg= 'white', height = 2,width=4,command=lambda:checkletter('s',s))
        s.place(x= 660,y = 442)
       
        t =Button(root, text='t', fg= 'black', bg= 'white', height = 2,width=4,command=lambda:checkletter('t',t))
        t.place(x= 700,y = 442)
       
        u =Button(root, text='u', fg= 'black', bg= 'white', height = 2,width=4,command=lambda:checkletter('u',u))
        u.place(x= 740,y = 442)
       
        v=Button(root, text='v', fg= 'black', bg= 'white', height = 2,width=4,command=lambda:checkletter('v',v))
        v.place(x= 780,y = 442)
       
        w =Button(root, text='w', fg= 'black', bg= 'white', height = 2,width=4,command=lambda:checkletter('w',w))
        w.place(x= 820,y = 442)
       
        x =Button(root, text='x', fg= 'black', bg= 'white', height = 2,width=4,command=lambda:checkletter('x',x))
        x.place(x= 860,y = 442)
       
        y=Button(root, text='y', fg= 'black', bg= 'white', height = 2,width=4,command=lambda:checkletter('y',y))
        y.place(x= 900,y = 442)
       
        z =Button(root, text='z', fg= 'black', bg= 'white', height = 2,width=4,command=lambda:checkletter('z',z))
        z.place(x= 940,y = 442)
       
        hint = Button(root, text=' Hint ', fg='black', bg='salmon3', height=1, width=7,command=lambda:clickedhint(hint))
        hint.place(x=730,y=490)
        
        # import images in code
        img0 = PhotoImage(file="s .png")
        img1 = PhotoImage(file="h0.png")
        img2 = PhotoImage(file="h1.png")
        img3 = PhotoImage(file="h2.png")
        img4 = PhotoImage(file="h3.png")
        img5 = PhotoImage(file="h4.png")
        img6 = PhotoImage(file="h5.png")
        img7 = PhotoImage(file="h6.png")
        img8 = PhotoImage(file="h7.png")
        img9 = PhotoImage(file="h8.png")
        img10 = PhotoImage(file="h9.png")
       
        my_Label = Label(root,image=img0)
        my_Label.place(x=40,y=20)
 
        root.mainloop()
       
# popup window for win
def youwin():
    chicken = Toplevel(gui)
    chicken.title('wohoo!')
    chicken.geometry('600x600')
    you_won_label = Label(chicken,text = "CONGOO!!\nYOU WON!",font=("Georgia",16))
    you_won_label.pack()

    replay = PhotoImage(file="Replay_button.png")
    replay_label = Label(chicken,image=replay)
    replay_btn = Button(chicken,image = replay,command=choosecategory)
    replay_btn.pack()

    exit2 = PhotoImage(file="exit_button.png")
    exit_label2 = Label(chicken, image = exit2)
    exit_btn2 = Button(chicken, image= exit2)
    exit_btn2.pack()

    chicken.mainloop()
# popup window for loose
def youloose(word):
    rat = Toplevel(gui)
    rat.title('oh no :(')
    rat.geometry('600x600')
    you_lost_label = Label(rat,text = "YOU LOST :(",font=("Georgia",16),bg='white')
    you_lost_label.pack()
    label=Label(rat,text="Word was:",font=("Georgia",16),bg="white")
    label.pack()
    label1=Label(rat,text=word,font=("Georgia",16),bg="white")
    label1.pack()
    replay1 = PhotoImage(file="Replay_button.png")
    replay1_label = Label(rat,image=replay1)
    replay_btn1 = Button(rat,image = replay1,command=choosecategory)
    replay_btn1.pack()
    exit3 = PhotoImage(file="exit_button.png")
    exit_label3 = Label(rat, image = exit3)
    exit_btn3 = Button(rat, image= exit3,command=exit_screen)
    exit_btn3.pack()

    rat.mainloop()
   
 
# function for quit
def exit_screen():
    gui.destroy()
gui = Tk()
 
# Adjust size  
gui.geometry("1024x650")
 
# Add image file
bg = PhotoImage(file = "welcomepage.png")
 
# Show image using label
label1 = Label(image = bg)
label1.place(x = 0, y = 0)
 
l = Label(gui, text="W E L C O M E T O H A N G M A N :)",bg='white')
l.config(font=("Georgia",25))
l.pack(pady=80)
 
# Add buttons
start = PhotoImage(file="start_button.png")
start_label = Label(gui,image = start)
button1 = Button(gui,image=start,command=choosecategory)
button1.pack(pady=15)

#Rules window
def rules():
    R=Toplevel(gui)
    label=Label(R,text="HANGMAN RULES",relief=RAISED,font=("Georgia",16))
    label.pack()
    text=StringVar()
    msg=Message(R,textvariable=text,relief=RAISED,font=("Georgia",16))
    text.set("HOW TO PLAY\nIntro:\nHangman is a classic word game.\nIn this game, you must guess the secret word one letter at a time.\nEach incorrect guess adds another part to the hangman. Hints:\nIf you need help finding a word, click the Hint button \nEach hint will give you 1 letter.\nYou are only allowed two hints per word\nHOPE YOU ENJOY GAMING :)")
    msg.pack()
    R.geometry("600x500")
    R.mainloop()
rule =PhotoImage(file="rules_button.png")
rules_label = Label(gui,image = rule)
rules_btn = Button(gui,image = rule,command=rules)
rules_btn.pack(pady=30)

# exit button
exit1 = PhotoImage(file="exit_button.png")
exit_label = Label(gui,image=exit1)
exit_btn = Button(gui,image=exit1,command=exit_screen)
exit_btn.pack(pady=28)
 
# Execute tkinter
gui.mainloop()


