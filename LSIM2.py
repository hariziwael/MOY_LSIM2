# BY WAEL HARIZI
import tkinter as tk
import webbrowser
window=tk.Tk()
window.title('LSIM2')
window.geometry('920x469')
window.configure(background="#708fa2")
def insta():
    webbrowser.open("https://www.instagram.com/haaarizi?igsh=MzRlODBiNWFlZA==")
def myfunction1():
    exit()


def RES2(): 
     try:
         num1 = eval(txtProbads.get())  
         num2 = eval(txtProbaex.get())
         num3 = eval(txtProbatp.get())
         result1 = num1*0.15 + num3*0.15 + num2*0.7

         num4 = eval(txtAutomatesds.get()) 
         num5 = eval(txtAutomatesex.get())
         result2 = num4*0.3 + num5*0.7
         num6 = eval(txtGraphesds.get())  
         num7 = eval(txtGraphesex.get())
         result3 = num6*0.3 + num7*0.7   #You can change the operation as needed


         num8 = eval(txtConceptionds.get())  
         num9 = eval(txtConceptionex.get())
         result4 = num8*0.3+ num9*0.7
         num10 = eval(txtJavads.get())  
         num11 = eval(txtJavaex.get())
         num12 = eval(txtJavatp.get())
         result5 = num10*0.15 + num12*0.15 + num11*0.7

         num13 = eval(txtBSDds.get())  
         num14 = eval(txtBSDex.get())
         num15 = eval(txtBSDtp.get())
         result6 = num13*0.15 + num15*0.15 + num14*0.7
         num16 = eval(txtReseauxds.get())  
         num17 = eval(txtReseauxex.get())
         num18 = eval(txtReseauxtp.get())
         result7 = num16*0.15 + num18*0.15 + num17*0.7

         num19 = eval(txtAnglaisds1.get())  
         num20 = eval(txtAnglaisds2.get())
         num21 = eval(txtAnglaisoral.get())
         result8 = num19*0.4 + num20*0.4 + num21*0.2
         num22 = eval(txtGesDentrepriseds1.get())  
         num23 = eval(txtGesDentrepriseds2.get())
         num24 = eval(txtGesDentrepriseoral.get())
         result9 = num22*0.4 + num23*0.4 + num24*0.2

         num25 = eval(txtWebds.get())  
         num26 = eval(txtWebex.get())
         num27 = eval(txtWebtp.get())
         result10 = num25*0.15 + num27*0.15 + num26*0.7
         num28 = eval(txtAnimationds.get())  
         num29 = eval(txtAnimationex.get())
         num30 = eval(txtAnimationtp.get())
         result11 = num28*0.15 + num30*0.15 + num29*0.7





         result=(result1*2+result2+result3+result4*1.5+result5*2+result6*1.5+result7+result8+result9+result10*1.5+result11*1.5)/15
         #Update the Button with the result
         res=round(result, 2)
         if result>=10:
             btnRES2.config(text=f"{res} MABROUUK")
         else:
             btnRES2.config(text=f"{res} GOOD LUCK\U0001F622")
     except (ValueError, SyntaxError):
         # Handle the case where the input is not a valid number
         btnRES2.config(text='Please enter valid numbers')



 #the new window

lblProbads=tk.Label(window,text='Proba DS:',font=('Arial Bold',10),bg='lightgray')
lblProbads.grid(pady=5,padx=5,row=0, column=0)
txtProbads=tk.Entry(window, width=10)
txtProbads.grid(row=0, column=1,pady=5,padx=5)

lblProbaex=tk.Label(window,text='Proba EX:',font=('Arial Bold',10),bg='lightgray')
lblProbaex.grid(pady=5,padx=5,row=0, column=2)
txtProbaex=tk.Entry(window, width=10)
txtProbaex.grid(row=0, column=3,pady=5,padx=5)

lblProbatp=tk.Label(window,text='Proba TP:',font=('Arial Bold',10),bg='lightgray')
lblProbatp.grid(pady=5,padx=5,row=0, column=4)
txtProbatp=tk.Entry(window, width=10)
txtProbatp.grid(row=0, column=5,pady=5,padx=5)


lblAutomatesds=tk.Label(window,text='Automates DS:',font=('Arial Bold',10),bg='lightgray')
lblAutomatesds.grid(pady=5,padx=5,row=1, column=0)
txtAutomatesds=tk.Entry(window, width=10)
txtAutomatesds.grid(row=1, column=1,pady=5,padx=5)

lblAutomatesex=tk.Label(window,text='Automates EX:',font=('Arial Bold',10),bg='lightgray')
lblAutomatesex.grid(pady=5,padx=5,row=1, column=2)
txtAutomatesex=tk.Entry(window, width=10)
txtAutomatesex.grid(row=1, column=3,pady=5,padx=5)

lblGraphesds=tk.Label(window,text='Graphes DS:',font=('Arial Bold',10),bg='lightgray')
lblGraphesds.grid(pady=5,padx=5,row=2, column=0)
txtGraphesds=tk.Entry(window, width=10)
txtGraphesds.grid(row=2, column=1,pady=5,padx=5)

lblGraphesex=tk.Label(window,text='Graphes EX:',font=('Arial Bold',10),bg='lightgray')
lblGraphesex.grid(pady=5,padx=5,row=2, column=2)
txtGraphesex=tk.Entry(window, width=10)
txtGraphesex.grid(row=2, column=3,pady=5,padx=5)


lblConceptionds=tk.Label(window,text='Conception DS:',font=('Arial Bold',10),bg='lightgray')
lblConceptionds.grid(pady=5,padx=5,row=3, column=0)
txtConceptionds=tk.Entry(window, width=10)
txtConceptionds.grid(row=3, column=1,pady=5,padx=5)

lblConceptionex=tk.Label(window,text='Conception EX:',font=('Arial Bold',10),bg='lightgray')
lblConceptionex.grid(pady=5,padx=5,row=3, column=2)
txtConceptionex=tk.Entry(window, width=10)
txtConceptionex.grid(row=3, column=3,pady=5,padx=5)

lblJavads=tk.Label(window,text='Java DS:',font=('Arial Bold',10),bg='lightgray')
lblJavads.grid(pady=5,padx=5,row=4, column=0)
txtJavads=tk.Entry(window, width=10)
txtJavads.grid(row=4, column=1,pady=5,padx=5)

lblJavaex=tk.Label(window,text='Java EX:',font=('Arial Bold',10),bg='lightgray')
lblJavaex.grid(pady=5,padx=5,row=4, column=2)
txtJavaex=tk.Entry(window, width=10)
txtJavaex.grid(row=4, column=3,pady=5,padx=5)

lblJavatp=tk.Label(window,text='Java TP:',font=('Arial Bold',10),bg='lightgray')
lblJavatp.grid(pady=5,padx=5,row=4, column=4)
txtJavatp=tk.Entry(window, width=10)
txtJavatp.grid(row=4, column=5,pady=5,padx=5)


lblBSDds=tk.Label(window,text='BSD DS:',font=('Arial Bold',10),bg='lightgray')
lblBSDds.grid(pady=5,padx=5,row=5, column=0)
txtBSDds=tk.Entry(window, width=10)
txtBSDds.grid(row=5, column=1,pady=5,padx=5)

lblBSDex=tk.Label(window,text='BSD EX:',font=('Arial Bold',10),bg='lightgray')
lblBSDex.grid(pady=5,padx=5,row=5, column=2)
txtBSDex=tk.Entry(window, width=10)
txtBSDex.grid(row=5, column=3,pady=5,padx=5)

lblBSDtp=tk.Label(window,text='BSD TP:',font=('Arial Bold',10),bg='lightgray')
lblBSDtp.grid(pady=5,padx=5,row=5, column=4)
txtBSDtp=tk.Entry(window, width=10)
txtBSDtp.grid(row=5, column=5,pady=5,padx=5)

lblReseauxds=tk.Label(window,text='Reseaux DS:',font=('Arial Bold',10),bg='lightgray')
lblReseauxds.grid(pady=5,padx=5,row=6, column=0)
txtReseauxds=tk.Entry(window, width=10)
txtReseauxds.grid(row=6, column=1,pady=5,padx=5)

lblReseauxex=tk.Label(window,text='Reseaux EX:',font=('Arial Bold',10),bg='lightgray')
lblReseauxex.grid(pady=5,padx=5,row=6, column=2)
txtReseauxex=tk.Entry(window, width=10)
txtReseauxex.grid(row=6, column=3,pady=5,padx=5)

lblReseauxtp=tk.Label(window,text='Reseaux TP:',font=('Arial Bold',10),bg='lightgray')
lblReseauxtp.grid(pady=5,padx=5,row=6, column=4)
txtReseauxtp=tk.Entry(window, width=10)
txtReseauxtp.grid(row=6, column=5,pady=5,padx=5)


lblAnglaisds1=tk.Label(window,text='Anglais DS1:',font=('Arial Bold',10),bg='lightgray')
lblAnglaisds1.grid(pady=5,padx=5,row=7, column=0)
txtAnglaisds1=tk.Entry(window, width=10)
txtAnglaisds1.grid(row=7, column=1,pady=5,padx=5)

lblAnglaisds2=tk.Label(window,text='Anglais DS2:',font=('Arial Bold',10),bg='lightgray')
lblAnglaisds2.grid(pady=5,padx=5,row=7, column=2)
txtAnglaisds2=tk.Entry(window, width=10)
txtAnglaisds2.grid(row=7, column=3,pady=5,padx=5)

lblAnglaisoral=tk.Label(window,text='Anglais ORAL:',font=('Arial Bold',10),bg='lightgray')
lblAnglaisoral.grid(pady=5,padx=5,row=7, column=4)
txtAnglaisoral=tk.Entry(window, width=10)
txtAnglaisoral.grid(row=7, column=5,pady=5,padx=5)

lblGesDentrepriseds1=tk.Label(window,text='Ges Dentreprise DS1:',font=('Arial Bold',10),bg='lightgray')
lblGesDentrepriseds1.grid(pady=5,padx=5,row=8, column=0)
txtGesDentrepriseds1=tk.Entry(window, width=10)
txtGesDentrepriseds1.grid(row=8, column=1,pady=5,padx=5)

lblGesDentrepriseds2=tk.Label(window,text='Ges Dentreprise DS2:',font=('Arial Bold',10),bg='lightgray')
lblGesDentrepriseds2.grid(pady=5,padx=5,row=8, column=2)
txtGesDentrepriseds2=tk.Entry(window, width=10)
txtGesDentrepriseds2.grid(row=8, column=3,pady=5,padx=5)

lblGesDentrepriseoral=tk.Label(window,text='Ges Dentreprise ORAL:',font=('Arial Bold',10),bg='lightgray')
lblGesDentrepriseoral.grid(pady=5,padx=5,row=8, column=4)
txtGesDentrepriseoral=tk.Entry(window, width=10)
txtGesDentrepriseoral.grid(row=8, column=5,pady=5,padx=5)


lblWebds=tk.Label(window,text='Web DS:',font=('Arial Bold',10),bg='lightgray')
lblWebds.grid(pady=5,padx=5,row=9, column=0)
txtWebds=tk.Entry(window, width=10)
txtWebds.grid(row=9, column=1,pady=5,padx=5)

lblWebex=tk.Label(window,text='Web EX:',font=('Arial Bold',10),bg='lightgray')
lblWebex.grid(pady=5,padx=5,row=9, column=2)
txtWebex=tk.Entry(window, width=10)
txtWebex.grid(row=9, column=3,pady=5,padx=5)

lblWebtp=tk.Label(window,text='Web TP:',font=('Arial Bold',10),bg='lightgray')
lblWebtp.grid(pady=5,padx=5,row=9, column=4)
txtWebtp=tk.Entry(window, width=10)
txtWebtp.grid(row=9, column=5,pady=5,padx=5)

lblAnimationds=tk.Label(window,text='Animation DS:',font=('Arial Bold',10),bg='lightgray')
lblAnimationds.grid(pady=5,padx=5,row=10, column=0)
txtAnimationds=tk.Entry(window, width=10)
txtAnimationds.grid(row=10, column=1,pady=5,padx=5)

lblAnimationex=tk.Label(window,text='Animation EX:',font=('Arial Bold',10),bg='lightgray')
lblAnimationex.grid(pady=5,padx=5,row=10, column=2)
txtAnimationex=tk.Entry(window, width=10)
txtAnimationex.grid(row=10, column=3,pady=5,padx=5)

lblAnimationtp=tk.Label(window,text='Animation TP:',font=('Arial Bold',10),bg='lightgray')
lblAnimationtp.grid(pady=5,padx=5,row=10, column=4)
txtAnimationtp=tk.Entry(window, width=10)
txtAnimationtp.grid(row=10, column=5,pady=5,padx=5)



btn1=tk.Button(window,text='exit',  fg="black",bg="lightblue", command=myfunction1 , padx=10 , pady=3,font=('Arial Bold',15),relief=tk.FLAT)
btn1.grid(row=11, column=0,pady=5,padx=5)

btnRES2=tk.Button(window,text='MOY SEM1',command=RES2,font=('Arial Bold',20),bg='#1a4f76',relief=tk.FLAT)
btnRES2.grid(row=12, column=2,pady=5,padx=5)

btninsta=tk.Button(text="follow me", command=insta , padx=5, pady=3,font=('Arial Bold',15),bg="lightblue",relief=tk.FLAT)
btninsta.grid(row=11, column=5,pady=5,padx=5)
window.mainloop()