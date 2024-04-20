from tkinter import *
import random as rd

s= 0


# ==== Functions ==== #
def draw_circle(can,x0,y0,r,color):
    
    can.create_oval(x0-r,y0+r,x0+r,y0-r, outline='red' , fill=color)

def draw_target(can):
    
    for i in range(6,0,-1):
        color = 'yellow'
        if i==2:
            color = 'red'
        draw_circle(can,200,200,30*i, color)   
    for i in range(0,6):
        color1 = 'red'
        if i==1:
            color1 = 'white'
        can.create_text(195,185-30*i,text=f'{6-i}',font=('Times','15','bold'),fill= color1)
    r=180
    can.create_line(200-r, 200,380,200,fill='red')
    can.create_line(200, 200-r,200,200+r,fill='red')
  
def score(x,y):
    score = 0
    for i  in range(7) :
        if (30*(i-1))**2<=(x-200)**2+(y-200)**2 and (x-200)**2+(y-200)**2<=(30*i)**2 :
            score = score + 7 - i
        i += 1
    return score





def draw_shots(can):
    global s
    i = 0
    while i<5:
        i += 1
        x,y = rd.uniform(0,400),rd.uniform(0,400)
        s +=  score(x,y)
        draw_circle(can,x,y,10,'black')
       
    Lab = Label(window, text=f"Your score is {s}!!")
    Lab.grid(row=2,column=1, sticky="SW")
        
def single_shot(can):
    global s
    x,y = rd.uniform(0,400),rd.uniform(0,400)
    draw_circle(can,x,y,10,'black')
    s += score(x,y)
    Lab = Label(window, text=f"Your score is {s}!!")
    Lab.grid(row=2,column=1, sticky="SW")


# ==== Script ==== #

if __name__=='__main__':
    
    #create a window
    window = Tk()
    window.geometry('600x600')
    
    window.grid()
    #create a red canva
    can = Canvas(window, width=400,height=400,background='red')

    
    #put the canva on the window
    can.grid()
    #add buttons
    close = Button(window,text="close", command=window.destroy)
    close.grid(row=1,column=0)
    
    #draw the target
    draw_target(can)
    

    #add 5 shots button
    fire = Button(window,text='5 shots!', command= lambda: draw_shots(can))
    fire.grid()

    #add single shot button
    Label(window, text='Use F to fire a single shot').grid()
    single = Button(window,text='single shot! ', command= lambda: single_shot(can))
    window.bind('<f>',  lambda event: single_shot(can))
    single.grid(row=1,column=1, sticky = 'SE')
    
    #execute the window
    window.mainloop()