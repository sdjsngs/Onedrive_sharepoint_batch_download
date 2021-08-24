"""
下载文件
"""

import requests
import os
import webbrowser
import time

if __name__ == "__main__":

    ucf_txt = r"./get_url.txt"
    save_path = r""
    with open(ucf_txt, "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if line[:5] == "https":
                # download
                file_name = line.split("/")[-1]
                save_file = os.path.join(
                    save_path, file_name
                )
                if os.path.exists(save_file):
                    continue

                webbrowser.open(line)
                print("down load file:{}".format(
                    file_name
                ))
                time.sleep(100)
