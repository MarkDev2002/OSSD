# from abc import ABC, abstractmethod
# class NhanSu(ABC):
#     def __init__(self, ten: str, namsinh: int):
#         self.ten = ten
#         self.namsinh = namsinh
#     @abstractmethod
#     def thongtin(self):
#         pass
#     @abstractmethod
#     def get_role(self):
#         pass
# class SinhVien(NhanSu):
#     def __init__(self, ten: str, namsinh: int, diem: str):
#         super().__init__(ten, namsinh)
#         self.diem = diem

#     def thongtin(self):
#         return f"Sinh viên: {self.ten}, Năm sinh: {self.namsinh}, Điểm: {self.diem}"

#     def get_role(self):
#         return "sinhvien"
# class BacSi(NhanSu):
#     def __init__(self, ten: str, namsinh: int, chuyenkhoa: str):
#         super().__init__(ten, namsinh)
#         self.chuyenkhoa = chuyenkhoa

#     def thongtin(self):
#         return f"Bác sĩ: {self.ten}, Năm sinh: {self.namsinh}, Chuyên khoa: {self.chuyenkhoa}"

#     def get_role(self):
#         return "bacsi"

# class GiangVien(NhanSu):
#     def __init__(self, ten: str, namsinh: int, chuyenmon: str):
#         super().__init__(ten, namsinh)
#         self.chuyenmon = chuyenmon

#     def thongtin(self):
#         return f"Giảng viên: {self.ten}, Năm sinh: {self.namsinh}, Chuyên môn: {self.chuyenmon}"

#     def get_role(self):
#         return "giangvien"

# class DayNS:
#     def __init__(self, ten: str):
#         self.ten = ten
#         self.danh_sach_nhan_su = []

#     def themNhanSu(self, nhansu: NhanSu):
#         self.danh_sach_nhan_su.append(nhansu)

#     def thongtin(self):
#         result = f"Tên dãy NS: {self.ten}\n"
#         for nhansu in self.danh_sach_nhan_su:
#             result += nhansu.thongtin() + "\n"
#         return result

#     def demBacSi(self):
#         return sum(1 for nhansu in self.danh_sach_nhan_su if nhansu.get_role() == "bacsi")

#     def sapxepNamSinh(self):
#         self.danh_sach_nhan_su.sort(key=lambda nhansu: nhansu.namsinh)

#     def trungbinhNamSinh(self):
#         giangvien_list = [nhansu.namsinh for nhansu in self.danh_sach_nhan_su if nhansu.get_role() == "giangvien"]
#         return sum(giangvien_list) / len(giangvien_list) if giangvien_list else 0

# # Example usage
# dayns = DayNS(ten="Khoa Dược")
# dayns.themNhanSu(SinhVien(ten="Sinh Vien A", namsinh=2000, diem="A"))
# dayns.themNhanSu(GiangVien(ten="Giang Vien B", namsinh=1975, chuyenmon="CNTT"))
# dayns.themNhanSu(GiangVien(ten="Giang Vien C", namsinh=1980, chuyenmon="Math"))
# dayns.themNhanSu(BacSi(ten="Bac Si D", namsinh=1965, chuyenkhoa="Tim mach"))
# dayns.themNhanSu(BacSi(ten="Bac Si E", namsinh=1970, chuyenkhoa="Than kinh"))

# print(dayns.thongtin())
# print(f"Số lượng bác sĩ: {dayns.demBacSi()}")
# dayns.sapxepNamSinh()
# print("Sau khi sắp xếp theo năm sinh:")
# print(dayns.thongtin())
# print(f"Trung bình năm sinh của Giảng Viên: {dayns.trungbinhNamSinh()}")


# class Manufacturer:
#     def __init__(self, name, location):
#         self.name = name
#         self.location = location

#     def mota(self):
#         return f"{self.name}, Location  : {self.location}"

# class Device:
#     def __init__(self, name, price, manufacturer):
#         self.name = name
#         self.price = price
#         self.manufacturer = manufacturer    

#     def mota(self):
#         return (f"Phone Name : {self.name}, Price: {self.price}, " +
#                 f"From: {self.manufacturer.mota()}")

# # Example usage
# device1 = Device("Apple", 32000, Manufacturer("Apple","USA"))
# print(device1.mota())

class CONGTY:
    def __init__(self, macongty, makhuvuc):
        self.macongty = macongty
        self.makhuvuc = makhuvuc

    def mota(self):
        return f"{self.macongty}, Mã khu vực: {self.makhuvuc}"

class NHANVIEN:
    def __init__(self, tennhanvien, tuoinhanvien, congty):
        self.tennhanvien = tennhanvien
        self.tuoinhanvien = tuoinhanvien
        self.congty = congty

    def mota(self):
        return (f"Nhân viên tên: {self.tennhanvien}, tuổi: {self.tuoinhanvien}, " +
                f"công ty: {self.congty.mota()}")

# Example usage
nhanvien1 = NHANVIEN("Nguyen Van A", 25, CONGTY(1, "A"))
print(nhanvien1.mota())

