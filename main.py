# coding: utf-8

import time
import tkinter as tk
from tkinter import messagebox
import cv2

get_time = time.ctime()
time_imformation = get_time.split(" ")
hour_imformation = time_imformation[3].split(":")

is_date_permitted_1 = time_imformation[0] != "Sat"
is_date_permitted_2 = time_imformation[0] != "Sun"
is_time_permitted = 8 < int(hour_imformation[0]) < 18

xuan_code = "1"
pin_code = "1"

def verification_passed():
    login_verified_msgbox = messagebox.showinfo("Xuan Final","验证成功")

def coding_xuan_window_start():
    redirection_window.destroy()
    coding_xuan_window = tk.Tk()
    coding_xuan_window.title()
    coding_xuan_window.overrideredirect(True)

    def SaveLastClickPos(event):
        global lastClickX, lastClickY
        lastClickX = event.x
        lastClickY = event.y

    def Dragging(event):
        x, y = event.x - lastClickX + coding_xuan_window.winfo_x(), event.y - lastClickY + coding_xuan_window.winfo_y()
        coding_xuan_window.geometry("+%s+%s" % (x , y))

    coding_xuan_window.bind('<Button-1>', SaveLastClickPos)
    coding_xuan_window.bind('<B1-Motion>', Dragging)

    def blank(row_num:int,column_num:int):
        blank = tk.Label(coding_xuan_window,text="        ")
        blank.grid(row=row_num,column=column_num)

    blank(1,1)

    text = tk.Label(coding_xuan_window,
                    text="\n请输入Xuan码以直接验证：\n\n",
                    font=("微软雅黑",14),
                    justify='left')
    text.grid(row=2,column=2)

    blank(1,5)

    entry = tk.Entry(coding_xuan_window,
                     font=("微软雅黑",14),
                     width=20)
    entry.grid(row=3,column=2)

    blank(4,2)

    def xuan_code_verify():
        xuan_code_get = str(entry.get())
        xuan_code_verify_result = xuan_code_get == xuan_code
        if xuan_code_verify_result:
            verification_passed()
        else:
            coding_xuan_window.destroy()
            raise_error_msgbox = messagebox.showerror("Xuan Final","Xuan验证码错误，验证强制关闭")
            raise Exception

    button_2 = tk.Button(coding_xuan_window,
                         text="验证..",
                         font=("微软雅黑",11),
                         width=30,
                         command=xuan_code_verify)
    button_2.grid(row=6,column=2)

    blank(12,2)
    blank(13,2)
    blank(14,2)

    coding_xuan_window.mainloop()
    
def coding_pin_window_start():
    redirection_window.destroy()
    coding_pin_window = tk.Tk()
    coding_pin_window.title()
    coding_pin_window.overrideredirect(True)

    def SaveLastClickPos(event):
        global lastClickX, lastClickY
        lastClickX = event.x
        lastClickY = event.y

    def Dragging(event):
        x, y = event.x - lastClickX + coding_pin_window.winfo_x(), event.y - lastClickY + coding_pin_window.winfo_y()
        coding_pin_window.geometry("+%s+%s" % (x , y))

    coding_pin_window.bind('<Button-1>', SaveLastClickPos)
    coding_pin_window.bind('<B1-Motion>', Dragging)

    def blank(row_num:int,column_num:int):
        blank = tk.Label(coding_pin_window,text="        ")
        blank.grid(row=row_num,column=column_num)

    blank(1,1)

    text = tk.Label(coding_pin_window,
                    text="\n请输入PIN码以验证：\n\n",
                    font=("微软雅黑",14),
                    justify='left')
    text.grid(row=2,column=2)

    blank(1,5)

    entry = tk.Entry(coding_pin_window,
                     font=("微软雅黑",14),
                     width=20)
    entry.grid(row=3,column=2)

    blank(4,2)

    def pin_code_verify():
        pin_code_get = str(entry.get())
        pin_code_verify_result = pin_code_get == pin_code
        if pin_code_verify_result:
            verification_passed()
        else:
            coding_pin_window.destroy()
            raise_error_msgbox = messagebox.showerror("Xuan Final","PIN验证码错误，验证强制关闭")
            raise Exception

    button_2 = tk.Button(coding_pin_window,
                         text="验证..",
                         font=("微软雅黑",11),
                         width=30,
                         command=pin_code_verify)
    button_2.grid(row=6,column=2)

    blank(12,2)
    blank(13,2)
    blank(14,2)

    coding_pin_window.mainloop()

def redirection_window_start():
    global redirection_window
    redirection_window = tk.Tk()
    redirection_window.title()
    redirection_window.overrideredirect(True)

    def SaveLastClickPos(event):
        global lastClickX, lastClickY
        lastClickX = event.x
        lastClickY = event.y

    def Dragging(event):
        x, y = event.x - lastClickX + redirection_window.winfo_x(), event.y - lastClickY + redirection_window.winfo_y()
        redirection_window.geometry("+%s+%s" % (x , y))

    redirection_window.bind('<Button-1>', SaveLastClickPos)
    redirection_window.bind('<B1-Motion>', Dragging)

    def blank(row_num:int,column_num:int):
        blank = tk.Label(redirection_window,text="        ")
        blank.grid(row=row_num,column=column_num)

    blank(1,1)

    text = tk.Label(redirection_window,
                    text="\nHello码验证已通过。日期/时间验证已\n通过。人脸验证已通过。仍然存在一\n定风险，为确保安全，请继续验证...\n\n您还可以选择以下验证方法：\n\n",
                    font=("微软雅黑",14),
                    justify='left')
    text.grid(row=2,column=2)

    blank(1,5)

    button_1 = tk.Button(redirection_window,
                         text="通过输入Xuan码直接验证..(X)",
                         font=("微软雅黑",11),
                         width=35,
                         command=coding_xuan_window_start)
    button_1.grid(row=4,column=2)

    blank(5,2)

    button_2 = tk.Button(redirection_window,
                         text="通过输入PIN码验证..(P)",
                         font=("微软雅黑",11),
                         width=35,
                         command=coding_pin_window_start)
    button_2.grid(row=6,column=2)

    blank(7,2)

    button_3 = tk.Button(redirection_window,
                         text="通过输入密码验证..(C)",
                         font=("微软雅黑",11),
                         width=35)
    button_3.grid(row=8,column=2)

    blank(9,2)
    blank(10,2)

    def redirection_window_destroy():
        redirection_window.destroy()

    button_e = tk.Button(redirection_window,
                         text="取消访问..",
                         font=("微软雅黑",11),
                         width=35,
                         command=redirection_window_destroy)
    button_e.grid(row=11,column=2)

    blank(12,2)
    blank(13,2)
    blank(14,2)

    redirection_window.mainloop()

def video_verification(verify_time:int):
    video_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    video_capture.read()
    time.sleep(verify_time)
    video_capture.release()
    cv2.destroyAllWindows()

redirection_window_start()

if is_date_permitted_1 and is_date_permitted_2:
    if is_time_permitted:
        video_verification(2)
        redirection_window_start()
    else:
        raise Exception
else:
    raise Exception