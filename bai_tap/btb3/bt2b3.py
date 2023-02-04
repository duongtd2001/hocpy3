''' Dự đoán kết quả của các biểu thức so sánh sau:
'a' > 'b'
3.0 > 3
'' <= ' '
.5 > 1 '''
# trả về False vì a và b có cùng giá trị => 'a' > 'b' False
print('a' > 'b')
# trả về False vì 3.0 = 3
print(3.0 > 3)
# trả về True vì '' và ' ' đề là False và so sánh nhỏ hơn hoặc bằng ở đây 2 giá trị bằng nhau
print('' <= ' ')
# trả về False vì .5 là 0.5 và không thể lớn hơn 1
print(.5 > 1)
