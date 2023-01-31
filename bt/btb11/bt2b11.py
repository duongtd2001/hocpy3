'''Định nghĩa một hàm được gọi là print_show_info nhận vào một tham số duy nhất đó là một dict, lúc gọi thì sử dụng dict như sau:
tv_show = {
    "title": "Breaking Bad",
    "seasons": 5,
    "initial_release": 2008
}
Hàm nên in ra một chuỗi có định dạng như sau:
Breaking Bad (2008) - 5 seasons
'''


def print_show_info(tv_show):
    print(
        f"{tv_show['title']} ({tv_show['initial_release']}) - {tv_show['seasons']} seasons")


info = {
    'title': 'Breaking Bad',
    'seasons': 5,
    'initial_release': 2008
}
print_show_info(info)
