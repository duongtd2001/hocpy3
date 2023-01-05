''' 
1. Tạo một movies list chứa tên các bộ phim đã xem
2. Sử dụng hàm input để nhập vào một bộ phim khác không có trong movies list
3. Thêm bộ phim vừa nhập vào cuối của danh sách movies
4. In ra bộ phim đầu tiên, cuối cùng và ở giữa movies list
5. Tính tổng bộ phim có trong movies
6. Xóa bộ phim đầu và cuối trong movies
7. Lấy ra và xóa bộ phim cuối cùng trong movies
8. Chèn một bộ phim bất kỳ vào đầu danh sách movies
9. Đếm số bộ phim có tiêu đề là "One Piece"
10. Tìm vị trí của bộ phim có tên là "gió"
11. Thêm một danh sách bộ phim khác vào cuối danh sách movies ban đầu
12. Xóa tất cả các bộ phim có trong danh sách 
'''
# 1
movies = ['avengers', 'peak blinder', 'fast furious',
          'iron man', 'spider man', 'avatar']
print(movies)

# 2 # 3
movies.append(input())
print(movies)

# 4
print(movies[0])
print(movies[-1])
