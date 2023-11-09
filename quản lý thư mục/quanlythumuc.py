from init import *

class Folder:
    # tạo mảng
    folders = []
    # hàm thêm folder
    def them_folder(self):
        # mở một tệp và trả về đối tượng tệp tương ứng, Mở file chế độ đọc và ghi tiếp.
        f = open('info_folder.txt',"a+")
        name = input("Nhap ten folder: ")
        date = input("Nhap ngay/thang/nam tao folder: ")
        
        new_folder = init_folder(name,date)
        self.folders.append(new_folder)
        info = name + "\t\t" + date + "\t\t" + "Folder" + "\t\t" + " " + "\n"
        f.write(info)
        f.close()
        
    # đếm số lượng folder
    def so_luong_folder(self):
        return self.folders.__len__()

    # xuất ra danh sách các folder đã được tạo
    def xuat_danh_sach(self):
        print("\t\tDanh sach folder cua ban: ")
        print("{:<8}    {:<8}   {:<8}   {:<8}".format("Ten","Ngay","Loai","Kich thuoc"))
        for folder in self.folders:
            print("{:<8}    {:<8}   {:<8}   {:<8}".format(folder.name, folder.date, "Folder"," "))

    # tìm kiếm một folder và in ra thông tin
    def tim_kiem_folder(self, tim_kiem):
        result = None
        if( self.so_luong_folder() > 0):
            for folder in self.folders:
                if( folder.name == tim_kiem):
                    result = folder
        return result

    # xóa một folder khỏi danh sách
    def xoa_folder(self, xoa_phan_tu):
        remove = False
        folder  = self.tim_kiem_folder(xoa_phan_tu)
        if( folder != None):
            self.folders.remove(folder)
            remove = True
        f = open('info_folder.txt',"w")
        if(self.so_luong_folder() > 0):
            for folder in self.folders:
                info = folder.name + "\t" + folder.date + "\t" + "Folder" + "\t" + " " + "\n"
                f.write(info)
        f.close()
        return remove

    