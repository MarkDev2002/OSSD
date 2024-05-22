# class CONGTY:
#     def __init__(self, macongty: int, makhuvuc: str):
#         self.macongty = macongty
#         self.makhuvuc = makhuvuc

#     def mota(self):
#         return f"Công ty: {self.macongty}, Mã khu vực: {self.makhuvuc}"

# class NHANVIEN:
#     def __init__(self, tennhanvien: str, tuoinhanvien: float, congty: CONGTY):
#         self.tennhanvien = tennhanvien
#         self.tuoinhanvien = tuoinhanvien
#         self.congty = congty

#     def mota(self):
#         return (f"Nhân viên tên: {self.tennhanvien}, tuổi: {self.tuoinhanvien}, " +
#                 f"công ty: ({self.congty.mota()})")

# # Example usage
# congty = CONGTY(macongty=1, makhuvuc="A")
# nhanvien1 = NHANVIEN(tennhanvien="Nguyen Van A", tuoinhanvien=25, congty=congty)
# print(nhanvien1.mota())


from abc import ABC, abstractmethod

class NhanSu(ABC):
    def __init__(self, ten: str, namsinh: int):
        self.ten = ten
        self.namsinh = namsinh

    @abstractmethod
    def thongtin(self):
        pass

class SinhVien(NhanSu):
    def __init__(self, ten: str, namsinh: int, diem: str):
        super().__init__(ten, namsinh)
        self.diem = diem

    def thongtin(self):
        return f"Sinh viên: {self.ten}, Năm sinh: {self.namsinh}, Điểm: {self.diem}"

class BacSi(NhanSu):
    def __init__(self, ten: str, namsinh: int, chuyenkhoa: str):
        super().__init__(ten, namsinh)
        self.chuyenkhoa = chuyenkhoa

    def thongtin(self):
        return f"Bác sĩ: {self.ten}, Năm sinh: {self.namsinh}, Chuyên khoa: {self.chuyenkhoa}"

class GiangVien(NhanSu):
    def __init__(self, ten: str, namsinh: int, chuyenmon: str):
        super().__init__(ten, namsinh)
        self.chuyenmon = chuyenmon

    def thongtin(self):
        return f"Giảng viên: {self.ten}, Năm sinh: {self.namsinh}, Chuyên môn: {self.chuyenmon}"

class DayNS:
    def __init__(self, ten: str):
        self.ten = ten
        self.danh_sach_nhan_su = []

    def themNhanSu(self, nhansu: NhanSu):
        self.danh_sach_nhan_su.append(nhansu)

    def thongtin(self):
        result = f"Tên dạy NS: {self.ten}\n"
        for nhansu in self.danh_sach_nhan_su:
            result += nhansu.thongtin() + "\n"
        return result

    def demBacSi(self):
        count = sum(1 for nhansu in self.danh_sach_nhan_su if type(nhansu) == BacSi)
        return count

    def sapxepNamSinh(self):
        self.danh_sach_nhan_su.sort(key=lambda nhansu: nhansu.namsinh)

    def trungbinhNamSinh(self):
        giangvien_list = [nhansu.namsinh for nhansu in self.danh_sach_nhan_su if type(nhansu) == GiangVien]
        return sum(giangvien_list) / len(giangvien_list) if giangvien_list else 0

# Example usage
dayns = DayNS(ten="Khoa CNTT")
dayns.themNhanSu(SinhVien(ten="Sinh Vien A", namsinh=2000, diem="A"))
dayns.themNhanSu(GiangVien(ten="Giang Vien B", namsinh=1975, chuyenmon="CNTT"))
dayns.themNhanSu(GiangVien(ten="Giang Vien C", namsinh=1980, chuyenmon="Math"))
dayns.themNhanSu(BacSi(ten="Bac Si D", namsinh=1965, chuyenkhoa="Tim mach"))
dayns.themNhanSu(BacSi(ten="Bac Si E", namsinh=1970, chuyenkhoa="Than kinh"))

print(dayns.thongtin())
print(f"Số lượng bác sĩ: {dayns.demBacSi()}")
dayns.sapxepNamSinh()
print("Sau khi sắp xếp theo năm sinh:")
print(dayns.thongtin())
print(f"Trung bình năm sinh của Giảng Viên: {dayns.trungbinhNamSinh()}")
