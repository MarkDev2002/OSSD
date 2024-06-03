class MyMap:
    def __init__(self, number):
        self.list = []
        self.__mapAdd(number)

    def mapAdd(self, number):
        for item in number:
            self.list.append(item)
    __mapAdd = mapAdd

class MapSubClass(MyMap):
    def mapAdd(self, keys, values):
        formatted_values = []
        for num, value in zip(self.list, values):
            if num - 1 < len(keys):
                formatted_values.append(f"{num}-{keys[num - 1]}")
            else:
                formatted_values.append(f"{num}-zero")
        
        return formatted_values

def main():
    number_list = [1, 2, 3, 4, 5]
    map_instance = MapSubClass(number_list)
    keys = ['one', 'two', 'three']
    values = [1, 2, 3, 4, 5]

    print("Before Map list = ", number_list)
    
    formatted_values = map_instance.mapAdd(keys, values)
    
    print("Map list = ", formatted_values)
    
    for formatted_value in formatted_values:
        map_instance.list.append(formatted_value)

    print("After Map list = ", map_instance.list)

if __name__ == "__main__":
    main()
