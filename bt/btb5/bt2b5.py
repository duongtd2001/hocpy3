'''
Cho danh sách các sinh viên chứa thông tin của mỗi sinh viên [id, tên, tuổi] như sau:
students = [["SV001", "Bob", 23], ["SV002", "Kenny", 34], ["SV003", "Henry", 45]]
Yêu cầu:
a. Lấy ra thông tin của sinh viên thứ nhất và in ra định dạng "ID: {id}, name: {name} - age: {age}"
b. Lấy ra tuổi của sinh viên thứ hai
c. Lấy ra thông tin hai sinh viên cuối cùng
d. Lấy ra id của sinh viên thứ ba
'''

students = [["SV001", "Bob", 23],
            ["SV002", "Kenny", 34],
            ["SV003", "Henry", 45]]

# a
sv1 = students[0]
print('thông tin sv 1:', sv1)
sv1_id = sv1[0]
sv1_name = sv1[1]
sv1_ege = sv1[2]
print(f'ID: {sv1_id}, name: {sv1_name}, age: {sv1_ege}')

# b
sv2 = students[1]
age_sv2 = sv2[-1]
print('tuổi sv 2:', age_sv2)

# c
sv_last = students[-1]
print(' thông tin sv cuối cùng:', sv_last)

# d
sv3 = students[2]
sv3_id = id(sv3)
print('id sv 3:', sv3_id)
