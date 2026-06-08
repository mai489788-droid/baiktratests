players = [
    {
        "ma_ct": "CT001",
        "ho_ten": "Nguyen Quang Hai",
        "so_tran": 10,
        "ban_thang": 5,
        "kien_tao": 4,
        "diem_hieu_suat": 33,
        "phan_loai": "Tru cot doi bong"
    }
]


def tinh_diem(so_tran, ban_thang, kien_tao):
    return so_tran + ban_thang * 3 + kien_tao * 2


def xep_loai(diem):
    if diem < 15:
        return "Can thanh ly/Cho muon"
    elif diem < 30:
        return "Du bi chien luoc"
    elif diem < 50:
        return "Tru cot doi bong"
    else:
        return "Ngoi sao dang cap"


def hien_thi_danh_sach():

    if len(players) == 0:
        print("Danh sach cau thu dang rong")
        return

    print("-" * 120)

    print(
        f"{'Ma CT':<10}"
        f"{'Ho Ten':<25}"
        f"{'So Tran':<10}"
        f"{'Ban Thang':<12}"
        f"{'Kien Tao':<10}"
        f"{'Diem':<10}"
        f"{'Phong Do'}"
    )

    print("-" * 120)

    for player in players:

        print(
            f"{player['ma_ct']:<10}"
            f"{player['ho_ten']:<25}"
            f"{player['so_tran']:<10}"
            f"{player['ban_thang']:<12}"
            f"{player['kien_tao']:<10}"
            f"{player['diem_hieu_suat']:<10}"
            f"{player['phan_loai']}"
        )
        
def them_cau_thu():
    ma_ct = input("Nhap ma cau thu: ")
    for player in players:
        if player["ma_ct"] == ma_ct:
            print("Ma cau thu da ton tai")
            return
    ho_ten = input("Nhap ho ten: ")

    try:

        so_tran = int(input("Nhap so tran: "))

        if so_tran < 0 or so_tran > 50:
            print("So tran phai tu 0 - 50")
            return

        ban_thang = int(input("Nhap ban thang: "))
        kien_tao = int(input("Nhap kien tao: "))

        if ban_thang < 0 or kien_tao < 0:
            print("Du lieu khong hop le")
            return
    except ValueError:
        print("Vui long nhap so")
        return

    diem = tinh_diem(
        so_tran,
        ban_thang,
        kien_tao
    )
    phong_do = xep_loai(diem)

    players.append(
        {
            "ma_ct": ma_ct,
            "ho_ten": ho_ten,
            "so_tran": so_tran,
            "ban_thang": ban_thang,
            "kien_tao": kien_tao,
            "diem_hieu_suat": diem,
            "phan_loai": phong_do
        }
    )

    print("Them thanh cong")
def xoa_cau_thu():

    ma = input("Nhap ma can xoa: ")

    for player in players:

        if player["ma_ct"] == ma:

            xac_nhan = input(
                "Ban co chac chan xoa? (Y/N): "
            )

            if xac_nhan.upper() == "Y":

                players.remove(player)

                print("Xoa thanh cong")

            return

    print("Khong tim thay cau thu")
    
def cap_nhat():

    ma = input("Nhap ma cau thu can sua: ")

    for player in players:

        if player["ma_ct"] == ma:

            try:

                player["so_tran"] = int(
                    input("Nhap so tran moi: ")
                )

                player["ban_thang"] = int(
                    input("Nhap ban thang moi: ")
                )

                player["kien_tao"] = int(
                    input("Nhap kien tao moi: ")
                )

            except ValueError:
                print("Nhap sai dinh dang")
                return

            player["diem_hieu_suat"] = tinh_diem(
                player["so_tran"],
                player["ban_thang"],
                player["kien_tao"]
            )

            player["phan_loai"] = xep_loai(
                player["diem_hieu_suat"]
            )

            print("Cap nhat thanh cong")
            return

    print("Khong tim thay cau thu")
    
def thong_ke():

    ngoi_sao = 0
    tru_cot = 0
    du_bi = 0
    thanh_ly = 0

    for player in players:

        if player["phan_loai"] == "Ngoi sao dang cap":
            ngoi_sao += 1

        elif player["phan_loai"] == "Tru cot doi bong":
            tru_cot += 1

        elif player["phan_loai"] == "Du bi chien luoc":
            du_bi += 1

        else:
            thanh_ly += 1

    print("\n===== THONG KE =====")
    print("Ngoi sao:", ngoi_sao)
    print("Tru cot:", tru_cot)
    print("Du bi:", du_bi)
    print("Can thanh ly:", thanh_ly)
while True:

    print("\n========== QUAN LY CAU THU ==========")
    print("1. Hien thi danh sach")
    print("2. Tiep nhan cau thu moi")
    print("3. Cap nhat thong tin va chi so")
    print("4. Xoa cau thu")
    print("5. Tim kiem cau thu")
    print("6. Thong ke phan loai phong do")
    print("7. Danh gia phong do tu dong")
    print("8. Thoat")

    choice = input("Nhap lua chon: ")

    if choice == "1":
        hien_thi_danh_sach()

    elif choice == "2":
        them_cau_thu()

    elif choice == "3":
        cap_nhat()

    elif choice == "4":
        xoa_cau_thu()

    elif choice == "6":
        thong_ke()


    elif choice == "8":
        print("Tam biet")
        break

    else:
        print("Lua chon khong hop le")