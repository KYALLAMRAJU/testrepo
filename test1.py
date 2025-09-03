class EA:
    def __init__(self):
        self.__accno = 1234
        self.accname = "kalyan"
        self.__pin = 1234
        self.branch = "sbi"
        self.state = "tg"
    def __output(self):
        for k,v in self.__dict__.items():
           # if k.startswith("_EA__"):
               # continue
            print(v)
    def show(self):
        self.__output()
E=EA()
E.show()