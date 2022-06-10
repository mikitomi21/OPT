class Test:
    __list = []
    def addElement(self, arg):
        self.__list.append(arg)

    def popBack(self):
        if len(self.__list):
            return self.__list.pop(len(self.__list)-1)

obj = Test()

obj.addElement(23)
obj.addElement('a')
obj.addElement("ala")
obj._Test__list.append("elo")
print(obj._Test__list)
obj.popBack()
print(obj._Test__list)