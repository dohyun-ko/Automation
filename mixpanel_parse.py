import json
import urllib.request
import ssl


def read_mixpanel_file(filename):
    f = open(filename, "r", encoding="utf-8")

    events = []

    for line in f:
        events.append(json.loads(line))

    f.close()

    user_list_file = open("mixpanel_users/mixpanel_user_list.csv", "w", encoding="utf-8")

    user_list = []

    for event in events:
        distinct_id = event["properties"]["distinct_id"]
        if distinct_id not in user_list:
            user_list.append(distinct_id)

    for user in user_list:
        user_list_file.write(user + "\n")

    user_list_file.close()

    return events

def write_user_events(events):
    for event in events:
        user = event["properties"]["distinct_id"]
        f = open("mixpanel_users/" + user + ".csv", "a", encoding="utf-8")
        f.write(json.dumps(event) + "\n")
        f.close()

def parse_json_csv(path):
    f = open(path, "r", encoding="utf-8")
    list = []
    for line in f:
        list.append(json.loads(line))
    f.close()
    return list


def parse_csv(path):
    f = open(path, "r", encoding="utf-8")
    list = []
    for line in f:
        list.append(line.strip())
    f.close()
    return list


def count_stages():
    events = parse_json_csv("mixpanel.csv")

    user_list = parse_csv("mixpanel_users/mixpanel_user_list.csv")

    print(user_list[0])

    print(events[0]["properties"]["distinct_id"])

    print(user_list[0] == events[0]["properties"]["distinct_id"])

    print(len(events))

    hasStage = 0

    stage_0 = 0

    stage_1 = 0

    stage_2 = 0

    stage_3 = 0

    stage_4 = 0

    stage_minus = 0

    image_file = open("mixpanel_users/mixpanel_image_list.csv", "w", encoding="utf-8")

    for user in user_list:
        user_events = parse_json_csv("mixpanel_users/" + user + ".csv")
        stage_bool = [False, False, False, False, False, False]  # 0, 1, 2, 3, 4, -1

        size_img = ""

        for user_event in user_events:
            try:
                stage = int(user_event["properties"]["stage"])
                if stage != -1:
                    stage_bool[stage] = True
                else:
                    stage_bool[5] = True
                if user_event["properties"]["dog"]["dog_size_img"]:
                    size_img = user_event["properties"]["dog"]["dog_size_img"] + "\n"

            except KeyError:
                continue

        if any(i is True for i in stage_bool):
            hasStage += 1

        if stage_bool[0]:
            stage_0 += 1
        if stage_bool[1]:
            stage_1 += 1
        if stage_bool[2]:
            stage_2 += 1
        if stage_bool[3]:
            stage_3 += 1
        if stage_bool[4]:
            stage_4 += 1
        if stage_bool[5]:
            stage_minus += 1

        if size_img:
            image_file.write(size_img)

    image_file.close()

    print("hasStage: " + str(hasStage))
    print("stage_0: " + str(stage_0))
    print("stage_1: " + str(stage_1))
    print("stage_2: " + str(stage_2))
    print("stage_3: " + str(stage_3))
    print("stage_4: " + str(stage_4))
    print("stage_minus: " + str(stage_minus))

    print("done")


def download_images():
    ssl._create_default_https_context = ssl._create_unverified_context
    image_list = parse_csv("mixpanel_users/mixpanel_image_list.csv")

    for image in image_list:
        urllib.request.urlretrieve(image, "mixpanel_users/images/" + image.split("/")[-1])


if __name__ == "__main__":

    # read_mixpanel_file("mixpanel.csv")

    write_user_events(read_mixpanel_file("mixpanel.csv"))

    # download_images()

    count_stages()
