'''
Cho dict sau:
album_info = {
    "album_name": "The Dark Side of the Moon",
    "band": "Pink Floyd",
    "release_year": 1973,
    "track_list": [
        "Speak to Me",
        "Breathe",
        "On the Run",
        "Time",
        "The Great Gig in the Sky",
        "Money",
        "Us and Them",
        "Any Colour You Like",
        "Brain Damage",
        "Eclipse"
    ]
}
Yêu cầu:
a. Lấy ra giá trị của các key sau: album_name, release_year bằng hai cách
b. Thay đổi giá trị của key: release_year từ 1973 thành 1971
c. Xóa phần tử với key là track_list
d. Thêm một key mới là amount = 2000 bằng hai cách
e. Làm trống dict: album_info
'''
import json
album_info = {
    "album_name": "The Dark Side of the Moon",
    "band": "Pink Floyd",
    "release_year": 1973,
    "track_list": [
        "Speak to Me",
        "Breathe",
        "On the Run",
        "Time",
        "The Great Gig in the Sky",
        "Money",
        "Us and Them",
        "Any Colour You Like",
        "Brain Damage",
        "Eclipse"
    ]
}


# a
val1 = album_info["album_name"]
print(val1)

val2 = album_info["release_year"]
print(val2)

# b
album_info["release_year"] = 1971
print(json.dumps(album_info, indent=4))

# c
remove = album_info.pop('track_list')
print(remove)

# d
album_info['amount'] = 2000
print(json.dumps(album_info, indent=4))

new_val = {
    'amount': 2000
}
album_info.update(new_val)
print(album_info)

# e
album_info.clear()
print(album_info)
