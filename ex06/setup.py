import os


folder_1 = "Face_reg"


now_path = os.path.dirname(os.path.realpath(__file__))


folder_1_path = os.path.join(now_path, folder_1)


if not os.path.exists(folder_1_path):
    os.makedirs(folder_1_path)
    print(f"สร้างโฟลเดอร์ {folder_1} ใน {now_path} เสร็จสิ้น")
else:
    print(f"พบ {folder_1_path} ไม่ทำการสร้างซ้ำ")
