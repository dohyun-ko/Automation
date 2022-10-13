import glob
from PIL import Image
import requests
import json
from shutil import copyfile
import os

if __name__ == "__main__":
    # download_images()
    os.mkdir("mixpanel_users/true")
    os.mkdir("mixpanel_users/false")
    os.mkdir("mixpanel_users/error")
    image_list = glob.glob("mixpanel_users/images/*")
    for image in image_list:
        try:
            opened = open(image, "rb")
            response = requests.post("https://ai.dev.doggly.co.kr/predict", files=dict(image=opened))
            opened.close()
            print(response.text)
            result = json.loads(response.text)
            if (result["result"] == "0"):
                copyfile(image, "mixpanel_users/true/" + image.split("/")[-1])
            else:
                copyfile(image, "mixpanel_users/false/" + image.split("/")[-1])
        except Exception as e:
            copyfile(image, "mixpanel_users/error/" + image.split("/")[-1])
            print(e)