# Nhập vào một năm bất kỳ. Kiểm tra xem năm đó có phải là năm nhuận hay không ?
year = int(input('nhập vào năm bất kỳ:'))
if (year % 4 == 0) and (year % 100 != 0):
    print('năm:', year, 'là năm nhuận')
elif (year % 100 == 0) and (year % 400 == 0):
    print('năm:', year, 'là năm nhuận')
else:
    print('năm:', year, 'không phải năm nhuận')
