# Số đẹp là số nếu vị trí chẵn của nó là số chẵn
# vị trí lẻ của nó là số lẻ => đây là số đẹp

# vd:   
#     1 2 3 4 5 6 7 8 9 10

def is_beautiful_number(number):

  for i in range(1, len(number)):
    if i % 2 == 0:  # Vị trí chẵn
      if int(number[i]) % 2 != 0:  # Số tại vị trí chẵn phải là số chẵn
        return False
    else:  # Vị trí lẻ
      if int(number[i]) % 2 == 0:  # Số tại vị trí lẻ phải là số lẻ
        return False
  return True

# Nhập số từ người dùng
number = input("Nhập số: ")
# Kiểm tra và in kết quả
if is_beautiful_number(number):
  print(number, "là số đẹp")
else:
  print(number, "không phải là số đẹp")

# 6 3
# 1 2 3 4 5 6 7 8 9 10