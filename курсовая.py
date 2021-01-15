Тема связана с датчиком и ГТД двигателем

import Tkinter
from Tkinter import *
root = Tk()
class BinSensor:
  def __init__(self,name,img0,img1,x,y):
    self.name=name
    self.x=x
    self.y=y
    self.img0=PhotoImage(file=img0)
    self.img1=PhotoImage(file=img1)
    self.val=0
    self.label_img=Label(root,image=self.img0)
    self.label_img.place(x=self.x,y=self.y)
  def set(self,state):
    if(self.val==state):
        return
    self.val=state
    if( int(state)==0 ):
      self.label_img.configure(image=self.img0)
    else:
      self.label_img.configure(image=self.img1)
    
class vBarSensor:
  def __init__(self,name,scale,min,max,x,y,w,h):
    self.name=name
    self.scale=scale
    self.x=x
    self.y=y
    self.h=h
    self.val=min
    self.min=min
    self.max=max
    self.delta=max-min
    h1=self.h*(self.val-self.min)/self.delta
    h0=self.h-h1
    self.canv0 = Canvas(root, width = w, height = h0, bg = "lightblue", bd=1, relief='ridge')
    self.canv1 = Canvas(root, width = w, height = h1, bg = "red", bd=1, relief='ridge')
    self.barLabel = Label(root, text = "0")
    self.canv0.place(x=self.x,y=self.y)
    self.canv1.place(x=self.x,y=self.y+h0)
    self.barLabel.place(x=self.x,y=self.y+h+5)
  def set(self,newval):
    val=int(newval,16)
    if(val>0x7fff): val=-val
    val=val/self.scale
    if(self.val==val): return
    self.val=val
    h1=self.h*(self.val-self.min)/self.delta
    h0=self.h-h1
    self.barLabel.configure(text=str(self.val))
    self.canv0.configure(height = h0)
    self.canv1.configure(height = h1)
    self.canv1.place(y=self.y+h0)
	
class GridDisplay:
  def __init__(self,name,scale,min,max,grid_num_x,grid_num_y,x,y,w,h):
    self.name=name
    self.scale=scale
    self.counter=0
    self.x=x
    self.y=y
    self.h=h
    self.w=w
    self.min=min
    self.max=max
    self.val=[]
    self.lines=[]
    self.grid_num_x=grid_num_x
    self.canv = Canvas(root, width = w, height = h, bg = "lightblue", bd=1, relief='ridge')
    self.canv.place(x=self.x,y=self.y)
    i=0
    while (i<grid_num_x+1):
      self.val.append(0)
      i=i+1
    i=0
    while (i<grid_num_x):
      self.canv.create_line((i+1)*(w/grid_num_x),0,(i+1)*(w/grid_num_x),h,width=1)
      x0=i*(w/grid_num_x)
      x1=(i+1)*(w/grid_num_x)
      y0=self.val[i]
      y1=self.val[i+1]
      self.lines.append( self.canv.create_line(x0,y0,x1,y1,width=3,fill="red"))
      i=i+1
      i=1
    while (i<grid_num_y):
      self.canv.create_line(0,i*(h/grid_num_y),w,i*(h/grid_num_y),width=1)
      i=i+1
  def set(self,newval):
    self.counter=self.counter+1
    if(self.counter<200):
      return
    self.counter=0
    val=int(newval,16)
    if(self.min<0):
      if(val>0x7fff): val=-val
    val=val/self.scale
    i=0
    while (i<self.grid_num_x):
      self.val[i]=self.val[i+1]
      i=i+1
    self.val[self.grid_num_x]=val
    i=0
    while (i<self.grid_num_x):
      x0=i*(self.w/self.grid_num_x)
      x1=(i+1)*(self.w/self.grid_num_x)
      y0=self.h-(self.val[i]-self.min)*self.h/(self.max-self.min)
      y1=self.h-(self.val[i+1]-self.min)*self.h/(self.max-self.min)
      c=(x0,y0,x1,y1)
      self.canv.coords(self.lines[i],c)
      i=i+1

class AllSensors:
  def __init__(self):
    self.s=serial.Serial("COM27",115200,timeout=10)
    self.bgnd=PhotoImage(file="bgnd.gif")
    self.label_bgnd=Label(root,image=self.bgnd)
    self.label_bgnd.place(x=0,y=0)
    self.all=[]
    self.all.append(BinSensor("b0","f0.gif","f1.gif",32,32))
    self.all.append(BinSensor("b1","f0.gif","f1.gif",32,128))
    self.all.append(vBarSensor("a0",1,0,255,128,32,32,160))
    self.all.append(GridDisplay("t0",16,-55,125,10,16,180,32,256,160))
  def set(self,name,val):
    for sens in self.all:
      if(sens.name==name):
        sens.set(val)
        return
  def setline(self,line):
    p=line.split("=")
    if(len(p)==2):
      self.set( p[0], p[1])
  def run(self):
    while(1):
      line=self.s.readline()
      line=line.rstrip()
      self.setline(line)
      root.update()

a=AllSensors()
a.run()



