import csv
import json
# cách 1 đọc file csv
with open('data.csv', mode='r', encoding='utf8') as file:
    for line in file:  # in ra từng dòng trong file
        # strip: loại bỏ những dấu cách ở đầu và cuối giữa các dòng
        print(line.strip())
# cách 2 đọc file csv
with open('data2.csv', mode='r', encoding='utf8') as file:
    csv_file = csv.DictReader(file)
    lst = list(csv_file)  # trả về list [dict]
    for item in lst:
        print(json.dumps(item, indent=4))
# ghi file csv
header = ['id', 'name', 'age']
stds = ['sv001', 'bob', 24]
with open('text.csv', mode='r', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(header)
    csv_writer.writerow(stds)

    # file json (bắt buộc cặp dấu nháy đôi)
    # đọc file json
with open('test.json', mode='r') as file:
    lst2 = json.load(file)
    print(json.dumps(lst2, indent=4))
'''
dump - ghi dữ liệu vào file json
dumps - chuyển đổi một list[dict] hay dict thành một chuỗi
load - đọc dữ liệu từ file json => list[dict] hay dict 
loads - chuyển đổi một string có dạng dict hay list[dict] thành list[dict] hay dict tương ứng
'''
