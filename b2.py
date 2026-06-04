# Danh sách thuốc ngày hôm qua (Lịch sử bệnh án cần giữ nguyên)
yesterday_prescription = ["Panadol", "Vitamin C", "Amoxicillin"]

# Hàm tạo và cập nhật đơn thuốc cho ngày mới
def update_prescription(old_prescription):
    new_prescription = old_prescription.copy()
    new_prescription[0] = new_prescription[0].replace("Panadol", "Paracetamol")
    new_prescription.append("Oresol")
    return new_prescription

# Hệ thống chạy cấp thuốc cho ngày hôm nay
today_prescription = update_prescription(yesterday_prescription)
print("Đơn thuốc hôm qua:", yesterday_prescription)
print("Đơn thuốc hôm nay:", today_prescription)


"""
Câu 1: Tại sao new_prescription.append("Oresol") làm thay đổi cả yesterday_prescription?

=> Dòng lệnh new_prescription = old_prescription KHÔNG tạo ra một list mới.
   Python chỉ tạo thêm một "nhãn" mới trỏ đến CÙNG MỘT vùng nhớ.
   Lúc này new_prescription và old_prescription (tức yesterday_prescription)
   đều là tên gọi khác nhau của CÙNG MỘT đối tượng trong bộ nhớ.

   Vì vậy khi gọi new_prescription.append("Oresol"),
   thực chất là đang thay đổi trực tiếp vùng nhớ đó
   → yesterday_prescription cũng bị ảnh hưởng theo.


Câu 2: Các cách tạo bản sao độc lập của List?

=> Cách 1 — Dùng phương thức .copy():
       new_prescription = old_prescription.copy()

=> Cách 2 — Dùng slice toàn bộ list:
       new_prescription = old_prescription[:]

=> Cách 3 — Dùng hàm list():
       new_prescription = list(old_prescription)

   Cả 3 cách đều tạo ra một list MỚI ở vùng nhớ khác,
   nên thay đổi list mới sẽ KHÔNG ảnh hưởng đến list gốc.


Câu 3: Tại sao new_prescription[0].replace("Panadol", "Paracetamol") không có tác dụng?

=> String có tính BẤT BIẾN (Immutable).
   replace() trả về một chuỗi MỚI đã được thay thế,
   nhưng không ghi đè lên chuỗi gốc trong list.
   Vì kết quả không được gán vào đâu, chuỗi mới bị bỏ đi ngay,
   và new_prescription[0] vẫn giữ nguyên giá trị "Panadol".


Câu 4: Cần sửa lại cú pháp như thế nào?

=> Phải GÁN KẾT QUẢ trả về của replace() ngược lại vào đúng vị trí index 0:
       new_prescription[0] = new_prescription[0].replace("Panadol", "Paracetamol")

   Lúc này Python sẽ:
       1. Gọi replace()        → tạo ra chuỗi mới "Paracetamol"
       2. Gán chuỗi mới đó     → ghi đè vào new_prescription[0]
       3. Kết quả được lưu lại → list cập nhật thành công!
"""
