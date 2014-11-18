class Baseconv(object):
    def __init__(self, num, base_source, base_target):
        self.num = num
        self.base_source = base_source
        self.base_target = base_target
    def any_to_dec(self):
        self.length = len(self.num)
        self.dec = 0
        for index in range(0, self.length):
            self.reverse = self.num[(self.length - 1) - index]
            if self.reverse == "A":
                self.reverse = 10
            elif self.reverse == "B":
                self.reverse = 11
            elif self.reverse == "C":
                self.reverse = 12
            elif self.reverse == "D":
                self.reverse = 13
            elif self.reverse == "E":
                self.reverse = 14
            elif self.reverse == "F":
                self.reverse = 15
            self.dec += int(self.reverse) * (int(self.base_source) ** index)
            index += 1
        return self.dec
    def dec_to_any(self):
        if type(self.dec) == list:
            self.dec = int("".join(self.dec))
        self.temp = []
        while self.dec > 0:
            self.result = self.dec % self.base_target
            self.dec /= self.base_target
            if self.result == 10:
                self.temp.append("A")
            elif self.result == 11:
                self.temp.append("B")
            elif self.result == 12:
                self.temp.append("C")
            elif self.result == 13:
                self.temp.append("D")
            elif self.result == 14:
                self.temp.append("E")
            elif self.result == 15:
                self.temp.append("F")
            else:
                self.temp.append(str(self.result))
        self.any = "".join(self.temp[::-1])

def cal_base_num():
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
print cal_base_num()
