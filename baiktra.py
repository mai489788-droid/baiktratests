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
        return "Cần thanh lý cho mượn"
    elif diem < 30:
        return "Dự bị chiến lược"
    elif diem < 50:
        return "Trụ cột đội bóng"
    else:
        return "Ngôi sao đẳng cấp"


def hien_thi_danh_sach():

    if len(players) == 0:
        print("Danh sách cầu thủ đang trống")
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
    ma_ct = input("Nhập mã cầu thủ: ")
    for player in players:
        if player["ma_ct"] == ma_ct:
            print("Mã cầu thủ đã tồn tại")
            return
    ho_ten = input("Nhập họ tên: ")

    try:

        so_tran = int(input("Nhập số trận: "))

        if so_tran < 0 or so_tran > 50:
            print("Số trận phải từ 0 - 50")
            return

        ban_thang = int(input("Nhập bàn thắng "))
        kien_tao = int(input("NHập kiến tạo: "))

        if ban_thang < 0 or kien_tao < 0:
            print("Dữ liệu hợp lệ")
            return
    except ValueError:
        print("Vui lòng nhận só")
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

    print("Thêm thành công")
def xoa_cau_thu():

    ma = input("Nhập mã cầu thủ cần xóa: ")

    for player in players:

        if player["ma_ct"] == ma:

            xac_nhan = input(
                "Bạn có chắc chắn? (Y/N): "
            )

            if xac_nhan.upper() == "Y":

                players.remove(player)

                print("Xóa thành công")

            return

    print("Không tìm thấy cầu thủ")
    
def cap_nhat():

    ma = input("Nhập mã cầu thủ cần sửa: ")

    for player in players:

        if player["ma_ct"] == ma:

            try:

                player["so_tran"] = int(
                    input("Nhập số trận mới: ")
                )

                player["ban_thang"] = int(
                    input("Nhập số bàn thắng mới: ")
                )

                player["kien_tao"] = int(
                    input("Nhập kiến tạo mới: ")
                )

            except ValueError:
                print("Nhập sai định dạng ")
                return

            player["diem_hieu_suat"] = tinh_diem(
                player["so_tran"],
                player["ban_thang"],
                player["kien_tao"]
            )

            player["phan_loai"] = xep_loai(
                player["diem_hieu_suat"]
            )

            print("Cập nhật thành công")
            return

    print("Không tìm thấy cầu thủ")
    
def thong_ke():

    ngoi_sao = 0
    tru_cot = 0
    du_bi = 0
    thanh_ly = 0

    for player in players:

        if player["phan_loai"] == "Ngôi sao đẳng cấp":
            ngoi_sao += 1

        elif player["phan_loai"] == "Trụ cột đội bóng":
            tru_cot += 1

        elif player["phan_loai"] == "Dự bị chiến lược":
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
    print("1. Hiển thị danh sách cầu thủ")
    print("2. Tiếp nhận cầu thủ mới")
    print("3. Cập nhật thông tin và số")
    print("4. Xóa cầu thủ(Thanh lý hợp đồng)")
    print("5. Tìm kiếm cầu thủ")
    print("6. Thống kê loại phong độ")
    print("7. đánh giá tự động")
    print("8. Thoát chương trình")

    choice = input("Nhập lựa chọn: ")

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