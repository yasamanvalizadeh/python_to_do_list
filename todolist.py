"""
author: 'Yasaman Valizadeh'

-------------------------
To do list App

-------------------------
Python GUI app using tkinter.
program needs to be run from command line/ terminal.
"""


from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from PIL import Image , ImageTk
import tksheet
import datetime
import winsound
import calendar
from datetime import date
import tkinter.messagebox
from threading import *

class ToDoList:
    def __init__(self , window):

        self.root = window

        self.christmas_image=Image.open('img/annie.jpg')
        self.christmas_image=self.christmas_image.resize((400 , 600))
        self.christmas_image=ImageTk.PhotoImage(image=self.christmas_image)

        self.raspopova_image=Image.open('img/raspopova.jpg')
        self.raspopova_image=self.raspopova_image.resize((400 , 600))
        self.raspopova_image=ImageTk.PhotoImage(image=self.raspopova_image)

        self.mourad_image=Image.open('img/mourad.jpg')
        self.mourad_image=self.mourad_image.resize((400 , 600))
        self.mourad_image=ImageTk.PhotoImage(image=self.mourad_image)

        self.taisiia_image=Image.open('img/taisiia.jpg')
        self.taisiia_image=self.taisiia_image.resize((400 , 600))
        self.taisiia_image=ImageTk.PhotoImage(image=self.taisiia_image)

        self.didi_image=Image.open('img/did.jpg')
        self.didi_image=self.didi_image.resize((400 , 600))
        self.didi_image=ImageTk.PhotoImage(image=self.didi_image)

        self.cake_image=Image.open('img/cake.jpg')
        self.cake_image=self.cake_image.resize((400 , 600))
        self.cake_image=ImageTk.PhotoImage(image=self.cake_image)

        self.bg_canvas=Canvas(self.root ,width=400 , height=600)
        self.bg_canvas.pack(fill=BOTH, expand = True)
        self.bg_canvas.create_image(0 , 0 , image=self.christmas_image , anchor=NW)

        self.daily_task_image=Image.open('img/gift.png')
        self.daily_task_image=self.daily_task_image.resize((80 , 80))
        self.daily_task_image=ImageTk.PhotoImage(image=self.daily_task_image)

        self.all_task_image=Image.open('img/christmas-tree.png')
        self.all_task_image=self.all_task_image.resize((80 , 80))
        self.all_task_image=ImageTk.PhotoImage(image=self.all_task_image)

        self.calender_image=Image.open('img/santa_claus.png')
        self.calender_image=self.calender_image.resize((80 , 80))
        self.calender_image=ImageTk.PhotoImage(image=self.calender_image)

        self.reminder_image=Image.open('img/candle.png')
        self.reminder_image=self.reminder_image.resize((80 , 80))
        self.reminder_image=ImageTk.PhotoImage(image=self.reminder_image)

        self.digital_clock_image=Image.open('img/Gingerman.png')
        self.digital_clock_image=self.digital_clock_image.resize((80 , 80))
        self.digital_clock_image=ImageTk.PhotoImage(image=self.digital_clock_image)

        self.subject_image=Image.open('img/christmas-ball.png')
        self.subject_image=self.subject_image.resize((40 , 40))
        self.subject_image=ImageTk.PhotoImage(image=self.subject_image)

        self.priority_image=Image.open('img/christmas.png')
        self.priority_image=self.priority_image.resize((40 , 40))
        self.priority_image=ImageTk.PhotoImage(image=self.priority_image)

        self.date_image=Image.open('img/candy-cane.png')
        self.date_image=self.date_image.resize((40 , 40))
        self.date_image=ImageTk.PhotoImage(image=self.date_image)

        self.month_image=Image.open('img/deer.png')
        self.month_image=self.month_image.resize((40 , 40))
        self.month_image=ImageTk.PhotoImage(image=self.month_image)

        self.year_image=Image.open('img/christmas2.png')
        self.year_image=self.year_image.resize((40 , 40))
        self.year_image=ImageTk.PhotoImage(image=self.year_image)

        self.min_image=Image.open('img/gift (1).png')
        self.min_image=self.min_image.resize((40 , 40))
        self.min_image=ImageTk.PhotoImage(image=self.min_image)

        self.hour_image=Image.open('img/snowflake.png')
        self.hour_image=self.hour_image.resize((40 , 40))
        self.hour_image=ImageTk.PhotoImage(image=self.hour_image)

        self.sec_image=Image.open('img/sleigh.png')
        self.sec_image=self.sec_image.resize((40 , 40))
        self.sec_image=ImageTk.PhotoImage(image=self.sec_image)

        self.ampm_image=Image.open('img/bow.png')
        self.ampm_image=self.ampm_image.resize((40 , 40))
        self.ampm_image=ImageTk.PhotoImage(image=self.ampm_image)

        self.note_image=Image.open('img/hat.png')
        self.note_image=self.note_image.resize((40 , 40))
        self.note_image=ImageTk.PhotoImage(image=self.note_image)

        self.time_image=Image.open('img/candy.png')
        self.time_image=self.time_image.resize((40 , 40))
        self.time_image=ImageTk.PhotoImage(image=self.time_image)

        self.date2_image=Image.open('img/snowman.png')
        self.date2_image=self.date2_image.resize((40 , 40))
        self.date2_image=ImageTk.PhotoImage(image=self.date2_image)

        self.daily_task_label=Button(self.root,bg='white' , image=self.daily_task_image , anchor=CENTER , text='Create New Task', compound=LEFT , font=('times new roman' , 25) , command=self.new_task , fg='#7e0f12')
        self.d_c=self.bg_canvas.create_window(30 , 30 , anchor=NW , window=self.daily_task_label, width= 340 , height= 100)

        self.all_task_label=Button(self.root,bg='white' , image=self.all_task_image , anchor=CENTER , text='All Tasks', compound=LEFT , font=('times new roman' , 25), command=self.create_sheet , fg='#313c33')
        self.a_c=self.bg_canvas.create_window(30 , 140 , anchor=NW , window=self.all_task_label, width= 340 , height= 100)

        self.calender_label=Button(self.root,bg='white', image=self.calender_image , anchor=CENTER , text='See Calender', compound=LEFT , font=('times new roman' , 25) , command=self.calender , fg='#bc6d4c')
        self.c_c=self.bg_canvas.create_window(30 , 250 , anchor=NW , window=self.calender_label, width= 340 , height= 100)

        self.reminder_label=Button(self.root,bg='white', image=self.reminder_image , anchor=CENTER , text='Set A Reminder', compound=LEFT , font=('times new roman' , 25) , command=self.set_reminder , fg='#b71a3b')
        self.r_c=self.bg_canvas.create_window(30 , 360 , anchor=NW , window=self.reminder_label, width= 340 , height= 100)

        self.digital_clock_label=Button(self.root,bg='white', image=self.digital_clock_image , anchor=CENTER , text='See Time & Date', compound=LEFT , font=('times new roman' , 25), command=self.clock , fg='#6a7045')
        self.d_c=self.bg_canvas.create_window(30 , 470 , anchor=NW , window=self.digital_clock_label, width= 340 , height= 100)

        self.new_task_mode=False
        self.all_task_mode=False
        self.tasks=[]
        self.detail_mode=False
        self.delete_row_task_mode=False

    def new_task(self):
        if not self.new_task_mode:
            self.bg_canvas.pack_forget()

            self.daily_task_canvas=Canvas(self.root ,width=400 , height=600)
            self.daily_task_canvas.pack(fill=BOTH, expand = True)
            self.daily_task_canvas.create_image(0 , 0 , image=self.raspopova_image , anchor=NW)

            self.task_list=['' , '' , '']

            self.subject_task=Label(self.root , text='Subject',font=('times new roman' , 25) , compound=LEFT , image=self.subject_image , bg='white')
            self.s_c=self.daily_task_canvas.create_window(20 ,30 , anchor=NW , window=self.subject_task)
            
            self.subject_text=Text(self.root , width=40, font= ('times new roman', 14),height= 2 , bg='white')
            self.st_c=self.daily_task_canvas.create_window(20 ,90 , anchor=NW , window=self.subject_text)

            self.priority_task=ttk.Menubutton(self.root, text='Priority', style='my.TMenubutton')
            self.pt_c=self.daily_task_canvas.create_window(20 ,140 , anchor=NW , window=self.priority_task)
            self.someStyle=ttk.Style()
            self.someStyle.configure('my.TMenubutton',font=('times new roman' , 25), compound=LEFT , image=self.priority_image)

            self.priority_menu=Menu(self.priority_task , tearoff=0 )
            self.priority_task['menu']=self.priority_menu

            self.priority_menu.add_radiobutton(label='high' , command=lambda :self.save_change ('high') ,font=('times new roman' , 15))
            self.priority_menu.add_radiobutton(label='normal' ,  command=lambda :self.save_change ('normal') ,font=('times new roman' , 15))
            self.priority_menu.add_radiobutton(label='low' ,  command=lambda :self.save_change ('low') ,font=('times new roman' , 15))

            self.date=Label(self.root , text='Date', font= ('times new roman', 25), compound=LEFT , image=self.date_image , bg='white')
            self.dt_c=self.daily_task_canvas.create_window(20 ,200 , anchor=NW , window=self.date)

            self.date_entry=DateEntry(self.root ,selectmode='day',font=('times new roman' , 15))
            self.dtentry_c=self.daily_task_canvas.create_window(20 ,250 , anchor=NW , window=self.date_entry)

            self.save=Button(self.root, text='Save' ,font=('times new roman', 24) , command=lambda :self.save_change ('i') , bg='#fac57d')
            self.sbt_c=self.daily_task_canvas.create_window(20 ,300 , anchor=NW , window=self.save)

            self.close_daily_task=Button(self.root, text='Close' ,font=('times new roman', 23) , command=self.close_dailytask  , bg='#fac57d')
            self.cdt_c=self.daily_task_canvas.create_window(130 ,300 , anchor=NW , window=self.close_daily_task)

            self.reminder_mode=False
            self.new_task_mode=True
        else:
            self.new_task_mode = False
            self.new_task()

    def save_change(self, a):

        if a =='high' or a=='normal' or a == 'low':
            self.task_list[1]= a

        if a == 'i':
            self.task_list[0] = self.subject_text.get(1.0, END)
            self.task_list[2] = self.date_entry.get()
            
            self.tasks.append( self.task_list)
            print(len(self.tasks))
            print(self.tasks)
            self.daily_task_canvas.pack_forget()
            self.bg_canvas.pack(fill=BOTH, expand = True)
            
    def close_dailytask(self):
        self.daily_task_canvas.pack_forget()
        self.bg_canvas.pack(fill=BOTH, expand = True)

    def create_sheet(self):
        if not self.all_task_mode:
            self.bg_canvas.pack_forget()

            self.create_sheet_canvas=Canvas(self.root ,width=400 , height=600)
            self.create_sheet_canvas.pack(fill=BOTH, expand = True)
            self.create_sheet_canvas.create_image(0 , 0 , image=self.mourad_image , anchor=NW)

            self.sheet = tksheet.Sheet(self.root , width=380 , height= 400)
            self.sh_c=self.create_sheet_canvas.create_window(10 ,80, anchor=NW , window=self.sheet)
            self.sheet.headers(["task","priority","due date"])
            
            self.sheet.set_sheet_data(data=[[f"" for ci in range(3)]for ri in range(100)])
            for item in range(len(self.tasks)):
                self.sheet.set_row_data(r=item , values=self.tasks[item])

            self.sheet.font(newfont = ("times new roman", 12, "normal"))
            self.sheet.header_font(newfont = ("times new roman", 16, "bold"))
            
            self.sheet.enable_bindings('all',"single_select", "row_select")
            self.sheet.extra_bindings("row_select", func =self.show_detail)
            self.sheet.align_columns(columns = [1 ,2 ,3 ], align = "center")
            self.sheet.column_width(column = 0 , width = 300)
            self.sheet.set_all_row_heights(height = 50)

            self.close_sheet_butten=Button(self.root , text='Close Table' , command=self.close_sheet ,font=('times new roman' , 20),bg='#fac57d')
            self.cbt_c=self.create_sheet_canvas.create_window(130 ,500, anchor=NW , window=self.close_sheet_butten)
            self.all_task_mode =True
        else:
            self.all_task_mode = False
            self.create_sheet()

    def close_sheet(self):
        self.create_sheet_canvas.pack_forget()
        self.bg_canvas.pack(fill=BOTH, expand = True)

    def show_detail(self,a):
        if not self.delete_row_task_mode:
            self.delete_row_task_mode = True
            pass
        else:
            self.delete_row_task_mode= False
            if not self.detail_mode:
                self.x = self.sheet.get_selected_rows()

                self.sheet.pack_forget()
                self.close_sheet_butten.pack_forget()

                self.create_sheet_canvas.pack_forget()
                
                self.detail_task_canvas=Canvas(self.root ,width=400 , height=600 , bg='#bc6d4c')
                self.detail_task_canvas.pack(fill=BOTH, expand = True)

                self.subject_label=Label(self.root , text='Subject ', font= ('times new roman', 15) , height=4,bg='white',)
                self.slabel_c=self.detail_task_canvas.create_window(20 ,30, anchor=NW , window=self.subject_label)

                self.subject_text_label=Label(self.root,anchor=W ,bg='white', text=self.sheet.get_cell_data(r=list(self.x)[0],c=0), font= ('times new roman', 15), width=25 , height=4)
                self.stext_c=self.detail_task_canvas.create_window(100 ,30, anchor=NW , window=self.subject_text_label)

                self.priority_label=Label(self.root ,bg='white', text='Priority ', font= ('times new roman', 15) , height=4)
                self.plabel_c=self.detail_task_canvas.create_window(20 ,130, anchor=NW , window=self.priority_label)

                self.priorty_text_label=Label(self.root ,anchor=W ,bg='white', text=self.sheet.get_cell_data(r=list(self.x)[0],c=1), font= ('times new roman', 15), width=25 , height=4)
                self.ptext_c=self.detail_task_canvas.create_window(100 ,130, anchor=NW , window=self.priorty_text_label)

                self.due_date_label=Label(self.root ,bg='white', text='due date', font= ('times new roman', 15) , height=4)
                self.duelabel_c=self.detail_task_canvas.create_window(20 ,230, anchor=NW , window=self.due_date_label)
                

                self.due_date_text=Label(self.root ,bg='white',anchor=W , text=self.sheet.get_cell_data(r=list(self.x)[0],c=2), font= ('times new roman', 15), width=25 , height=4)
                self.duetext_c=self.detail_task_canvas.create_window(100 ,230, anchor=NW , window=self.due_date_text)

                self.close_detail_frame_button=Button(self.root , text='CLOSE' , command=self.closedetail_frame ,  font= ('times new roman', 15) , bg='#fac57d' )
                self.closebutton_c=self.detail_task_canvas.create_window(160 ,335, anchor=NW , window=self.close_detail_frame_button)

                self.done_button=Button(self.root , text='DONE ' , command=self.done, font= ('times new roman', 15) , bg='#77a047')
                self.donebutton_c=self.detail_task_canvas.create_window(160 ,380, anchor=NW , window=self.done_button)

                self.detail_mode=True

    def closedetail_frame(self):
        self.detail_task_canvas.pack_forget()
        self.create_sheet_canvas.pack(fill=BOTH, expand = True)
        self.detail_mode = False

    def done(self):
        self.sheet.highlight_rows(rows =list(self.x)[0], bg = 'light green')
        self.closedetail_frame()

    def calender(self):
        self.bg_canvas.pack_forget()

        self.calender_canvas=Canvas(self.root ,width=400 , height=600)
        self.calender_canvas.pack(fill=BOTH, expand = True)
        self.calender_canvas.create_image(0 , 0 , image=self.taisiia_image , anchor=NW)

        self.month_label=Label(self.root , text='Month' ,font= ('times new roman', 20) , compound=LEFT , image=self.month_image , bg='white')
        self.mlabel_c=self.calender_canvas.create_window(20 ,30, anchor=NW , window=self.month_label)

        self.year_label=Label(self.root, text='Year   ' ,font= ('times new roman', 20) , compound=LEFT , image=self.year_image , bg='white')
        self.ylabel_c=self.calender_canvas.create_window(20 ,80, anchor=NW , window=self.year_label)

        self.month_var=IntVar()
        self.year_var=IntVar()

        self.current_month=date.today().month
        self.current_year=date.today().year

        self.month_var.set(self.current_month)
        self.year_var.set(self.current_year)

        self.month_spinbox=Spinbox(self.root, from_=1  , to=12 , width= 5 , textvariable=self.month_var , font= ('times new roman', 20))
        self.ms_c=self.calender_canvas.create_window(180 ,35, anchor=NW , window=self.month_spinbox)

        self.year_spinbox=Spinbox(self.root, from_=0000 , to=3000 , width= 5 , textvariable=self.year_var, font= ('times new roman', 20))
        self.ys_c=self.calender_canvas.create_window(180 ,85, anchor=NW , window=self.year_spinbox)

        self.calender_field=Text(self.root, width =20,height= 8, font= ('times new roman', 20), relief = RIDGE,borderwidth = 2  ,padx= 10,pady= 30)
        self.cf_c=self.calender_canvas.create_window(20 ,140, anchor=NW , window=self.calender_field)

        self.display_button=Button(self.root, text='Display' , command=self.display_calender , font= ('times new roman', 20), bg='#fac57d')
        self.db_c=self.calender_canvas.create_window(20 ,460, anchor=NW , window=self.display_button)

        self.reset_button=Button(self.root , text='Reset' , command=self.reset , font= ('times new roman', 20), bg='#fac57d')
        self.rb_c=self.calender_canvas.create_window(130 ,460, anchor=NW , window=self.reset_button)
        
        self.close_button=Button(self.root , text='Close' , command=self.close, font= ('times new roman', 20), bg='#fac57d')
        self.cbutton_c=self.calender_canvas.create_window(217 ,460, anchor=NW , window=self.close_button)

    def display_calender(self):
        month=int(self.month_spinbox.get())
        year=int(self.year_spinbox.get())

        finalcalender=calendar.month(year, month)
        self.calender_field.delete(1.0 , END)
        self.calender_field.insert(END ,finalcalender)

    def reset(self):
        self.calender_field.delete(1.0 , END)

        self.month_var.set(self.current_month)
        self.year_var.set(self.current_year)

        self.month_spinbox.config(textvariable=self.month_var)
        self.year_spinbox.config(textvariable=self.year_var)

    def close(self):
        self.calender_canvas.pack_forget()
        self.bg_canvas.pack(fill=BOTH, expand = True)

    def set_reminder(self):
        self.bg_canvas.pack_forget()

        self.reminder_canvas=Canvas(self.root ,width=400 , height=600)
        self.reminder_canvas.pack(fill=BOTH, expand = True)
        self.reminder_canvas.create_image(0 , 0 , image=self.didi_image , anchor=NW)

        self.hour_entry=Entry(self.root, width= 15,  font= ('times new roman', 20))
        self.he_c=self.reminder_canvas.create_window(170 ,35, anchor=NW , window=self.hour_entry)

        self.hour_label=Label(self.root, text=' Hour' ,  font= ('times new roman', 20) , image=self.hour_image , compound=LEFT , bg='white')
        self.hl_c=self.reminder_canvas.create_window(20 ,30, anchor=NW , window=self.hour_label)

        self.min_entry=Entry(self.root , width= 15,  font= ('times new roman', 20))
        self.me_c=self.reminder_canvas.create_window(170 ,95, anchor=NW , window=self.min_entry)
        
        self.min_label=Label(self.root , text=' Minout',  font= ('times new roman', 20) , image=self.min_image , compound=LEFT , bg='white')
        self.ml_c=self.reminder_canvas.create_window(20,90, anchor=NW , window=self.min_label)
        
        self.sec_entry=Entry(self.root, width= 15,  font= ('times new roman', 20))
        self.se_c=self.reminder_canvas.create_window(170,155, anchor=NW , window=self.sec_entry)

        self.sec_label=Label(self.root, text=' Seconde' , font=('times new roman',20), image=self.sec_image , compound=LEFT , bg='white')
        self.sl_c=self.reminder_canvas.create_window(20,150, anchor=NW , window=self.sec_label)

        self.note_label=Label(self.root, text=' Note', font=('times new roman',20), image=self.note_image, compound=LEFT , bg='white')
        self.nl_c=self.reminder_canvas.create_window(20,220, anchor=NW , window=self.note_label)

        self.note_entry=Entry(self.root, width= 15, font=('times new roman',15))
        self.ne_c=self.reminder_canvas.create_window(170,225, anchor=NW , window=self.note_entry)

        self.set_button=Button(self.root , text='set' , command=self.set , width= 10, font=('times new roman',20) , bg='#fac57d')
        self.setb_c=self.reminder_canvas.create_window(20,290, anchor=NW , window=self.set_button)

        self.closewimdow_button=Button(self.root , text='Close' , command=self.close_reminder , width= 10, font=('times new roman',20) , bg='#fac57d')
        self.cw_c=self.reminder_canvas.create_window(200,290, anchor=NW , window=self.closewimdow_button)

    def close_reminder(self):
        self.reminder_canvas.pack_forget()
        self.bg_canvas.pack(fill=BOTH , expand=True)

    def set(self):
        t1=Thread(target=self.alarm)
        t1.start()
    
    def alarm(self):
        hour = self.hour_entry.get()
        mini = self.min_entry.get()
        sec = self.sec_entry.get()

        while True:
            set_alarm_time = f"{hour}:{mini}:{sec}"
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            
            if current_time == set_alarm_time:
                tkinter.messagebox.showinfo(title="alarm", message=self.note_entry.get())
                winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
                break

    def clock(self):
        self.bg_canvas.pack_forget()

        self.clock_canvas=Canvas(self.root ,width=400 , height=600)
        self.clock_canvas.pack(fill=BOTH, expand = True)
        self.clock_canvas.create_image(0 , 0 , image=self.cake_image , anchor=NW)

        self.time_label=Label(self.root, font=('times new roman',20) , image=self.time_image , compound=LEFT , bg='white')
        self.tl_c=self.clock_canvas.create_window(100,30, anchor=NW , window=self.time_label)

        self.date_label=Label(self.root , font=('times new roman',20), image=self.date2_image , compound=LEFT , bg='white')
        self.dl_c=self.clock_canvas.create_window(75,90, anchor=NW , window=self.date_label)

        self.closee_button=Button(self.root , text='Close' , command=self.close_clock, font= ('times new roman', 15) , bg='#fac57d')
        self.ceb_c=self.clock_canvas.create_window(170 ,150, anchor=NW , window=self.closee_button)

        self.show_time()

    def show_time(self):
        time=datetime.datetime.now()
        time=time.strftime(' %H:%M:%S %p ')
        self.time_label.config(text=time)
        self.time_label.after(1000 , self.show_time)

        date=datetime.datetime.today()
        date=date.strftime('%a, %b %d, %Y ')
        self.date_label['text'] = date

    def close_clock(self):
        self.clock_canvas.pack_forget()
        self.bg_canvas.pack(fill=BOTH, expand = True)


if __name__ == '__main__':

    window = Tk()
    window.geometry('400x600')
    window.title('To Do List')
    window.wm_iconbitmap('img/Gingerman.ico')

    x = ToDoList(window)
    window.mainloop()
