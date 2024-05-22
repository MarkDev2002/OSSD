class SubjectMapping:
    def __init__(self, list_A, list_B):
        self.list_A = list_A 
        self.list_B = list_B 
        self.mamonHoc = {
            "Lập trình Python": 1,
            "Hệ thống thông minh": 2,
            "Nguyên lý ngôn ngữ lập trình": 3,
            "Học máy": 4
        }
        self.manganh = {
            1: "CNTT",
            2: "KHDL",
            3: "KTPM",
            4: "TTNT"
        }

    def cauA(self):
        for monHoc, maMon in zip (self.list_A, self.list_B):
            print("Môn học: ", monHoc, "- Mã môn: ", maMon)

    def cauB(self):
        return [(mamonHoc, self.manganh[manganh]) for mamonHoc, manganh in self.mamonHoc.items()]


if __name__ == "__main__":
    list_A = ["Lập trình trực quan", "Cấu trúc dữ liệu Python", "Khai Phá dữ liệu", "Chuyên đề phân tích dữ liệu"]
    list_B = [101, 211, 331, 422]   

    # câu 1 A
    subjects = SubjectMapping(list_A, list_B)
    print("\nMapping list_MonHoc với list_Year:")
    subjects.cauA()
    
    # Câu 1 B
    print("\nMapping mamonHoc với manganh:")
    map = subjects.cauB()
    for mamonHoc, manganh in map:
        print(f"{mamonHoc} : {manganh}")
