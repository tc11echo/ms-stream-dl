import os
import requests
import bs4
from http import cookiejar

from authentication import USERNAME, PASSWORD

with open(r"source.txt", "r", encoding="utf-8") as fpr:
    data=fpr.read()
root=bs4.BeautifulSoup(data, "html.parser")
paths=root.find_all("a", class_="c-hyperlink c-caption-1 video-list-item-title no-hover")

count=0
download_links=[]
with open(r"download_links.txt", "w", encoding="utf-8") as fpw:
    for i in paths:
        fpw.write("https://web.microsoftstream.com"+i["href"]+"\n")
        download_links.append("https://web.microsoftstream.com"+i["href"])
        count+=1
        print(str(count)+". https://web.microsoftstream.com"+i["href"])
print(f"done, in total {count} video(s)")
print("================================")
print("start downloading")

path=os.path.join(os.getcwd(), "video")
if(not os.path.exists("video")):
    os.mkdir(path)
os.chdir(path)

#os.system(r"powershell yt-dlp -f 'bestvideo+bestaudio' --merge-output-format mp4 --cookies '../microsoftstream.com_cookies.txt' --batch-file '../download_links.txt'")

for download_link in download_links:
    header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
    mozilla_cookie_jar=cookiejar.MozillaCookieJar(filename='../microsoftstream.com_cookies.txt')
    mozilla_cookie_jar.load('../microsoftstream.com_cookies.txt', ignore_discard=True, ignore_expires=True)
    cookie_json=requests.utils.dict_from_cookiejar(mozilla_cookie_jar)
    response=requests.get('https://web.microsoftstream.com/', cookies=cookie_json, headers=header, auth=(USERNAME, PASSWORD))
    mozilla_cookie_jar.save(ignore_discard=True, ignore_expires=True)
    #print(response.cookies)

    if "?" in download_link:
        temp=download_link.split("?")
        download_link=temp[0]
    os.system(f"powershell yt-dlp -f 'bestvideo+bestaudio' --merge-output-format mp4 --cookies '../microsoftstream.com_cookies.txt' '{download_link}'")

"""
    if "?" in download_link:
        download_link.replace("?", "\?")
    if "&" in download_link:
        download_link.replace("&", "\&")
    os.system(f"powershell yt-dlp -f 'bestvideo+bestaudio' --merge-output-format mp4 --cookies \"../microsoftstream.com_cookies.txt\" \"{download_link}\"")
"""