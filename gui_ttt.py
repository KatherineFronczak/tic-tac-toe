from tkinter import*
import random
root = Tk()
game = ['-','-','-','-','-','-','-','-','-']
wins = [[0,0,0,1,1,1,1,1,1],[0,1,1,0,1,1,0,1,1],
[0,1,1,1,0,1,1,1,0],[1,0,1,1,0,1,1,0,1],
[1,1,1,0,0,0,1,1,1],[1,1,0,1,1,0,1,1,0],
[1,1,1,1,1,1,0,0,0],[1,1,0,1,0,1,0,1,1]]
wins_i = [(0,1,2),(0,3,6),(0,4,8),(1,4,7),(3,4,5),(2,5,8),(6,7,8),(2,4,6)]
close_i = [(0,1),(0,2),(1,2),
(0,3),(0,6),(3,6),
(0,4),(0,8),(4,8),
(1,4),(1,7),(7,4),
(3,4),(3,5),(4,5),
(2,5),(2,8),(5,8),
(6,7),(6,8),(7,8),
(2,4),(2,6),(4,6)]

def play(pn,p):
    spot = [p1,p2,p3,p4,p5,p6,p7,p8,p9]
    game[p] = "x"
    pn.config(text= 'x', state=DISABLED)
    print(game)
    #check if x has won
    winner = ["x"]
    w=0
    for s in winner:
        if game[0]== s and game[1]==s and game[2]==s:w,win=2,s
        elif game[0]== s and game[3]==s and game[6]==s:w,win=2,s
        elif game[0]== s and game[4]==s and game[8]==s:w,win=2,s
        elif game[1]== s and game[4]==s and game[7]==s:w,win=2,s
        elif game[3]== s and game[4]==s and game[5]==s:w,win=2,s
        elif game[2]== s and game[5]==s and game[8]==s:w,win=2,s
        elif game[6]== s and game[7]==s and game[8]==s:w,win=2,s
        elif game[2]== s and game[4]==s and game[6]==s:w,win=2,s
    if w==2:
        L2.config(text=win+" is winner")


    #figure out if there is a close win for o
    o_mrkup = []
    for i in range(9):
        if game[i] == 'o':o_mrkup.append('c')
        else:o_mrkup.append(game[i])
    o_close_i = 0
    o_close_w = []
    o_close = []
    win_o = 0
    o_close_s = 0
    for c1,c2 in close_i:
        if o_mrkup[c1]=='c' and o_mrkup[c2]=='c':
            o_c = (c1,c2)
            o_close.append(o_c)
    if o_close!=[]:
        for o_close_t in o_close:
            for i in [0,1,2,3,4,5,6,7,8]:
                o_close_s = (list(o_close_t) + [i])
                o_close_s.sort()
                o_close_w.append(tuple(o_close_s))
        for y in o_close_w:
            for i in wins_i:
                if i==y:
                    win_o=i
        if win_o!=0:
            for i in win_o:
                if game[i]=='-':
                    o_close_i = i
                    break
    #figure out if there is a close win for x
    x_mrkup = []
    for i in range(9):
        if game[i] == 'x':x_mrkup.append('c')
        else:x_mrkup.append(game[i])
    x_close_i = 0
    x_close_w = []
    x_close = []
    win_x = 0
    x_close_s = 0
    for c1,c2 in close_i:
        if x_mrkup[c1]=='c' and x_mrkup[c2]=='c':
            x_c = (c1,c2)
            x_close.append(x_c)
    if x_close!=[]:
        for x_close_t in x_close:
            for i in [0,1,2,3,4,5,6,7,8]:
                x_close_s = (list(x_close_t) + [i])
                x_close_s.sort()
                x_close_w.append(tuple(x_close_s))
        for y in x_close_w:
            for i in wins_i:
                if i==y:
                    win_x=i
        if win_x!=0:
            for i in win_x:
                if game[i]=='-':
                    x_close_i = i
                    break
    #picking which route to take, win, block, or random
    if o_close_i!=0:
        game[o_close_i] = 'o'
        n = spot[o_close_i]
        n.config(text="o", state=DISABLED)

    elif x_close_i!=0:
        game[x_close_i] = 'o'
        n = spot[x_close_i]
        n.config(text="o", state=DISABLED)
    else:
        o_pos = []
        for win_g in wins:
            o_pos_g = []
            for i in range(9):
                if game[i]=='-':g=win_g[i]
                elif game[i]=='o':g=win_g[i]
                else:g=game[i]
                o_pos_g.append(g)
            o_pos.append(o_pos_g)
        o_pos_w = []
        o_pos_wins = []
        for o_pos_ls in o_pos:
            for win in wins_i:
                x = 0
                for u in win:
                    if o_pos_ls[u]==0:
                        x = x+1
                if x==3:
                    o_pos_wins.append(o_pos_ls)
        if o_pos_wins!=[]:
            o_pos_w = (random.choice(o_pos_wins))
            for i in range(9):
                if game[i]=='-' and o_pos_w[i]==0:
                    game[i]='o'
                    n = spot[i]
                    n.config(text="o", state=DISABLED)
                    break
        else:
            for i in range(9):
                if game[i]=='-':
                    game[i]='o'
                    n = spot[i]
                    n.config(text="o", state=DISABLED)
                    break
    #check if o has won
    winner = ["o"]
    if w==0:
        for s in winner:
            if game[0]== s and game[1]==s and game[2]==s:w,win=1,s
            elif game[0]== s and game[3]==s and game[6]==s:w,win=1,s
            elif game[0]== s and game[4]==s and game[8]==s:w,win=1,s
            elif game[1]== s and game[4]==s and game[7]==s:w,win=1,s
            elif game[3]== s and game[4]==s and game[5]==s:w,win=1,s
            elif game[2]== s and game[5]==s and game[8]==s:w,win=1,s
            elif game[6]== s and game[7]==s and game[8]==s:w,win=1,s
            elif game[2]== s and game[4]==s and game[6]==s:w,win=1,s
        if w==1:
            L2.config(text=win+" is winner")

#gui formatting
L1=Label(root,text="click a box")
p1= Button(root, text=' ',padx=10,command=lambda:play(p1,0))
p2= Button(root, text=' ',padx=10,command=lambda:play(p2,1))
p3= Button(root, text=' ',padx=10,command=lambda:play(p3,2))
p4= Button(root, text=' ',padx=10,command=lambda:play(p4,3))
p5= Button(root, text=' ',padx=10,command=lambda:play(p5,4))
p6= Button(root, text=' ',padx=10,command=lambda:play(p6,5))
p7= Button(root, text=' ',padx=10,command=lambda:play(p7,6))
p8= Button(root, text=' ',padx=10,command=lambda:play(p8,7))
p9= Button(root, text=' ',padx=10,command=lambda:play(p9,8))
L2=Label(root, text=" ")

L1.grid(row=0,column=0,columnspan=3)
p1.grid(row=1, column=1)
p2.grid(row=1, column=2)
p3.grid(row=1, column=3)
p4.grid(row=2, column=1)
p5.grid(row=2, column=2)
p6.grid(row=2, column=3)
p7.grid(row=3, column=1)
p8.grid(row=3, column=2)
p9.grid(row=3, column=3)
L2.grid(row=4,column=0,columnspan=3)
root.mainloop()
