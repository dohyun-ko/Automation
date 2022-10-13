# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import csv
import json

import requests

def get_inputs():
    uuid_list = []

    input_f = open("coupon_list.csv", "r")

    coupon_csv = csv.reader(input_f)


    # for line in coupon_csv:
    #     print("0" + line[0])
    #     uuid_list.append("0" + line[0])


    input_f.close()

    target_list = []

    f = open("user_tb.csv", "r", encoding="utf-8")

    rdr = csv.reader(f)

    line_list = []

    for line in rdr:
        line_list.append(line)

    # for line in uuid_list:
    #     for user_line in line_list:
    #         print(user_line[5], line)
    #         if user_line[5] == line:
    #             target_list.append(user_line[0])

    for line in line_list:
        target_list.append(line[0])


    coupon_uuid = "CO69721c-ADc04814-220923-220923"
    access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbkRhY2hzaHVuZCIsInJvbGUiOiJBRE1JTiIsImlhdCI6MTY2MzkxNjc3NiwiZXhwIjoxNjYzOTE3MDc2fQ.SkPfWblgyZj4msZjWto43L_i7uMu1ZrEPiYzNTVy6NY"

    headers = {'Content-Type': 'application/json; charset=utf-8', 'Authorization': 'Bearer ' + access_token}

    data = {
        'user_list': target_list
    }
    res = requests.post("https://api.doggly.co.kr/v1/admin/coupon/user/"
                      + coupon_uuid, data=json.dumps(data), headers=headers)
    print(res.text)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_inputs()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
