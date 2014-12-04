"""Program : Number Base Converter
Author : Natthawee Chutianusornchai
         Peeraphon Kunthamyothin
Language : Python 2.7.8
"""

class Baseconv(object):
    """Convert number base by convert input number base to decimal first,
    and then convert decimal to require number base
    Input : num(int) > input number or alphabet A-F
            base_source > input number base
            base_target > require number base
    Output : return converted number base
    """
    def __init__(self, num, base_source, base_target):
        """set variable section"""
        self.num = num
        self.base_source = base_source
        self.base_target = base_target
    def any_to_dec(self):
        """convert from any base to decimal section"""
        self.length = len(self.num)
        self.dec = 0
        num_format = "0123456789ABCDEF"
        for index in range(0, self.length):
            self.reverse = self.num[(self.length - 1) - index]
            self.reverse = num_format.index(self.reverse)
            self.dec += int(self.reverse) * (int(self.base_source) ** index)
            index += 1
        return self.dec
    def dec_to_any(self):
        """Convert decimal to any base section"""
        if type(self.dec) == list:
            self.dec = int("".join(self.dec))
        self.temp = []
        while self.dec > 0:
            num_format = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, \
                      "A", "B", "C", "D", "E", "F"]
            self.result = self.dec % self.base_target
            self.dec /= self.base_target
            self.temp.append(str(num_format.pop(self.result)))
        self.any = "".join(self.temp[::-1])

def ctrl():
    """control "Baseconv" class section"""
    cls = Baseconv(map(str, raw_input()), input(), input())
    if cls.base_source == cls.base_target:
        return "".join(cls.num)
    elif cls.base_source == 10:
        cls.dec = cls.num
        cls.dec_to_any()
        return cls.any
    elif cls.base_target == 10:
        cls.any_to_dec()
        return cls.dec
    else:
        cls.any_to_dec()
        cls.dec_to_any()
        return cls.any
def tk_ctrl():
    """Control Tkinter section"""
    root = Tk()
    #base dictionary
    base = {2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, \
            10:10, 11:11, 12:12, 13:13, 14:14, 15:15, 16:16}
    #title
    root.title("Base Number Converter")
    #Convert from
    frame_1 = Frame(root)
    frame_1.pack()
    box_1 = LabelFrame(frame_1, text="Convert from", padx=3, pady=3)
    box_1.pack(side=LEFT)
    box_1_pack = Entry(box_1)
    box_1_pack.pack()
    label_1 = Label(frame_1, text="base")
    label_1.pack(side=LEFT)
    var_1 = IntVar(frame_1)
    base_1 = OptionMenu(frame_1, var_1, *base)
    var_1.set(10)
    base_1.pack(side=LEFT)
    #to
    frame_2 = Frame(root)
    frame_2.pack()
    box_3 = LabelFrame(frame_2, text="to", padx=3, pady=3)
    box_3.pack(side=LEFT)
    box_3_pack = Entry(box_3)
    box_3_pack.pack()
    label_2 = Label(frame_2, text="base")
    label_2.pack(side=LEFT)
    var_2 = IntVar(frame_2)
    base_2 = OptionMenu(frame_2, var_2, *base)
    var_2.set(10)
    base_2.pack(side=LEFT)
    #calculate
    frame_3 = Frame(root, bd=5)
    frame_3.pack()
    cal = Button(frame_3, text="Calculate")
    cal.pack()
    #mainloop
    root.mainloop()
from Tkinter import *
tk_ctrl()
#print ctrl()
