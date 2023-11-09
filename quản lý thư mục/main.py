from quanlythumuc import *

gltm = Folder()

while(True):
    print("\tChuong trinh quan ly thu vien")
    print("----------------------------------------------------")
    print(" 1. Them folder:                             ")
    print(" 2. Xuat danh sach folder:                   ")
    print(" 3. Tim kiem folder:                         ")
    print(" 4. Xoa folder:                              ")
    print(" 0. Thoat chuong trinh: Shut Down            ")
    print("----------------------------------------------------")

    key = int(input("Nhap lua chon cua ban: "))

    if(key == 1):
        print("Them folder moi: ")
        gltm.them_folder()
        print("\nThem thanh cong!\n")
    elif(key == 2):
        gltm.xuat_danh_sach()
    elif(key == 3):
        tim_kiem = input("Nhap ten folder ma ban dang tim: ")
        result = gltm.tim_kiem_folder(tim_kiem)
        if( result == None):
            print("Khong co folder ma ban dang tim!")
        else:
            print("{:<8}    {:<8}   {:<8}   {:<8}".format(result.name, result.date, "Folder"," "))
    elif(key == 4):
        xoa_phan_tu = input("Hay nhap ten phan tu ma ban muon xoa: ")
        choice = input("Ban co chac chan se xoa folder nay chu: ")
        dong_y = ['co',"Co","Yes","yes","y","c"]
        if(choice in dong_y):
            remove = gltm.xoa_folder(xoa_phan_tu)
        if(remove == False):
            print("Xoa khong thanh cong!")
        else:
            print("Xoa thanh cong!")
    elif(key == 0):
        print("Ban da thoat thanh cong")
        break
    else:
        print("Nhap lai")
        continue