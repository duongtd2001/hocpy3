''' Dự đoán kết quả của các biểu thức logic sau:
0 and 1
'' or None
3 and 4 or 0
'a' or '1'
not None
not 0 '''
# dự đoán kết quả 0, vì and trả về giá trị True khi 2 vế bằng True, và trả về False khi 1 trong 2 về bằng False hoặc cả 2 về bằng False
print(0 and 1)
# trả về None vì '' là False trong toán tử or chỉ trả về False  khi 2 vế bằng False
print('' or None)
# trả về 4 vì 3 and 4 trong and sẽ trả về giá trị thứ nhất nếu nó sai, và ngược lại sẽ trả về giá trị thứ 2 vì vậy 3 and 4 sẽ trả về 4
# 4 or 0 sẽ trả về 4 vì 0 là False và or chỉ trả về False khi 2 vế bằng False
print(3 and 4 or 0)
####
print(not None)
# not 0 trả về True vì 0 là False, not 0 là True
print(not 0)
