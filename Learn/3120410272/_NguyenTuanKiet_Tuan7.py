class MyMap:

    def __init__(self, number):
        self.list = []
        self.__mappAdd(number)

    def mapAdd(self, number):
        for item in number:
            self.list.append(item)
    __mapAdd = mapAdd

class MapSubClass(MyMap):
    def mapAdd (self,keys,values):
        for i in zip(keys,values):
            self.list.append(i)

def main ():
    number_list = [1,2,3,4,5]
    map_instance = MyMap(number_list)
    print("Map list = ", map_instance.list)
    keys = ['one','two','three']
    