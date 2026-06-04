# Danh sách chẩn đoán hiện tại của bệnh nhân Nguyễn Văn A
patient_diagnoses = ["Sốt Xuất Huyết"]

"""
=== PHÂN TÍCH LỖI ===

Câu 1: Tại sao strip() và title() không thay đổi raw_diagnosis?

String trong Python có tính BẤT BIẾN (Immutable).
Khi gọi raw_diagnosis.strip() hay raw_diagnosis.title(),
Python tạo ra một chuỗi MỚI với nội dung đã xử lý,
nhưng KHÔNG ghi đè lên biến gốc raw_diagnosis.
Vì kết quả không được gán vào đâu cả, chuỗi mới bị bỏ đi ngay.

Ví dụ minh họa tính bất biến:
    s = "  hello  "
    s.strip()        # Tạo ra "hello" nhưng không lưu lại
    print(s)         # Vẫn in ra "  hello  " — không đổi gì!
"""

"""
Câu 2: Cần sửa cú pháp gán biến như thế nào?

Phải GÁN LẠI kết quả trả về vào chính biến đó:
    raw_diagnosis = raw_diagnosis.strip()
    raw_diagnosis = raw_diagnosis.title()

Hoặc viết gọn thành một dòng (method chaining):
    raw_diagnosis = raw_diagnosis.strip().title()

Lúc này Python sẽ:
    1. Gọi strip()  → trả về chuỗi đã xóa khoảng trắng 2 đầu
    2. Gọi title()  → trả về chuỗi đã viết hoa chữ đầu mỗi từ
    3. Gán kết quả cuối cùng lại vào raw_diagnosis → lưu được!
"""

"""
Câu 3: extend() hoạt động thế nào khi truyền vào một String?

extend() nhận một ITERABLE (đối tượng có thể duyệt từng phần tử)
và lần lượt thêm TỪNG PHẦN TỬ vào list.

Khi truyền một String vào extend(), Python coi mỗi KÝ TỰ
là một phần tử riêng lẻ — vì String cũng là iterable.

Ví dụ minh họa:
    lst = ["Sốt Xuất Huyết"]
    lst.extend("  viEm  ")
    # Kết quả: ['Sốt Xuất Huyết', ' ', ' ', 'v', 'i', 'E', 'm', ' ', ' ']
    #                               ↑ từng ký tự bị tách rời ↑

Đó là lý do tại sao console in ra 'v', 'i', 'E', 'm' nằm rời rạc.
"""

"""
Câu 4: Thay extend() bằng phương thức nào?

Dùng APPEND() thay thế.
append() thêm NGUYÊN VẸN một đối tượng vào cuối list,
bất kể đó là chuỗi, số, hay list khác.

So sánh trực tiếp:
    lst = ["Sốt Xuất Huyết"]

    lst.extend("Viem Phe Quan")
    # → ['Sốt Xuất Huyết', 'V', 'i', 'e', 'm', ' ', 'P', ...]  ❌ VỠ VỤN

    lst.append("Viem Phe Quan")
    # → ['Sốt Xuất Huyết', 'Viem Phe Quan']                     ✅ ĐÚNG
"""


# ============================================================
# PHẦN SỬA LỖI — SOURCE CODE ĐÚNG CHUẨN
# ============================================================

def add_diagnosis(raw_diagnosis, current_list):

    # SỬA LỖI 1: Gán lại kết quả sau khi chuẩn hóa
    # strip()  → xóa khoảng trắng thừa ở 2 đầu chuỗi
    # title()  → viết hoa chữ cái đầu mỗi từ
    # Dùng method chaining và GÁN LẠI vào raw_diagnosis để lưu kết quả
    raw_diagnosis = raw_diagnosis.strip().title()

    # SỬA LỖI 2: Dùng append() thay vì extend()
    # append() thêm NGUYÊN VẸN chuỗi "Viem Phe Quan" như 1 phần tử
    current_list.append(raw_diagnosis)

    return current_list


# Bác sĩ nhập thêm một chẩn đoán mới bị lỗi định dạng
new_diagnosis = "  viEm phE QUan  "

# Gọi hàm để xử lý và cập nhật hồ sơ
updated_diagnoses = add_diagnosis(new_diagnosis, patient_diagnoses)
print("Hồ sơ bệnh án (Các chẩn đoán):", updated_diagnoses)

# Output mong đợi:
# Hồ sơ bệnh án (Các chẩn đoán): ['Sốt Xuất Huyết', 'Viem Phe Quan']