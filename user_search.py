# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import csv

def get_inputs():
    uuid_list = []

    input_f = open("input.txt", "r")

    for line in input_f:
        print(line[-1:])
        if line[-1:] == "\n":
            line = line[:-1]
        uuid_list.append(line)

    input_f.close()

    f = open("user_tb.csv", "r", encoding="utf-8")
    rdr = csv.reader(f)

    print(uuid_list)

    line_list = []

    for line in rdr:

        line_list.append(line)

    output = open("output.csv", "w", encoding="utf-8", newline="")
    wr = csv.writer(output)

    # for uuid in uuid_list:
    #     for line in line_list:
    #         if uuid == line[0]:
    #             wr.writerow(line)

    for line in line_list:
        if line[0] in uuid_list:
            print("드글이")
        else:
            wr.writerow(line)

    output.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_inputs()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
