class CONGTY:
    def __init__(self, maCongTy, makhuVuc):
        self.maCongTy = maCongTy
        self.makhuVuc = makhuVuc

class NHANVIEN:
    def __init__(self, tenNhanVien, tuoiNhanVien, congTy:CONGTY):
        self.tenNhanVien = tenNhanVien
        self.tuoiNhanVien = tuoiNhanVien
        self.congTy = congTy

    
    