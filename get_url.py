import requests
import xml.etree.ElementTree as ElementTree
from urllib.parse import urlparse, quote, unquote

ARIA2_INPUT_FILE = 'get_url.txt'

COOKIE_FEDAUTH = ""

SHAREPOINT_ROOT = ""

SESSION = requests.Session()


def main():
    global COOKIE_FEDAUTH, SHAREPOINT_ROOT, SESSION, DLPATH_PRIFIX
    # SHAREPOINT_ROOT = input("SharePoint Real Path (eg. https://xxxx-my.sharepoint.com/personal/aaaa_t_cccc_cn/Documents/):\n")
    SHAREPOINT_PATH = urlparse(SHAREPOINT_ROOT).path

    # COOKIE_FEDAUTH = input("FedAuth cookie (base64 value only):\n")
    cookies = {
        'FedAuth': COOKIE_FEDAUTH
    }
    requests.utils.add_dict_to_cookiejar(SESSION.cookies, cookies)

    print("Fetching file list ...")
    resp = SESSION.request("PROPFIND", SHAREPOINT_ROOT)
    try:
        xml_root = ElementTree.fromstring(resp.content.decode('utf8'))
    except ElementTree.ParseError:
        print(
            f"ERROR! Got Response <{resp.status_code}>: {resp.content.decode('utf8')}\nPossible invalid Real Path or FedAuth.")
        exit()

    print("Generating aria2 file list ...")
    fw = open(ARIA2_INPUT_FILE, 'w', encoding='utf-8')
    for e in xml_root.findall('.//{DAV:}href'):
        file_url = e.text
        if file_url.endswith('/'):
            continue
        url_info = urlparse(file_url)

        encoded_url = url_info.geturl()
        fw.write(f'{encoded_url}\n')

    print('Please run the download.py')


if __name__ == "__main__":
    main()
