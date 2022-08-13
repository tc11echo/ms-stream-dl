with open(r"source.txt", "r", encoding="utf-8") as fpr:
    data=fpr.read()

import bs4
root=bs4.BeautifulSoup(data, "html.parser")
links=root.find_all("a", class_="c-hyperlink c-caption-1 video-list-item-title no-hover")

count=0

with open(r"video_links.txt", "w", encoding="utf-8") as fpw:
    for i in links:
        fpw.write("https://web.microsoftstream.com"+i["href"]+"\n")
        print(str(count+1)+". https://web.microsoftstream.com"+i["href"])
        count+=1
print(f"done, in total {count} video(s)")
print("================================")
print("start downloading")

import os
path=os.path.join(os. getcwd(), "video")
if(not os.path.exists("video")):
    os.mkdir(path)

os.chdir(path)
os.system(r"powershell yt-dlp -f 'bestvideo+bestaudio' --merge-output-format mp4 --cookies '../microsoftstream.com_cookies.txt' --batch-file '../video_links.txt'")
#os.system(r"powershell yt-dlp -f 'bestvideo+bestaudio' --merge-output-format mp4 --cookies 'microsoftstream.com_cookies.txt' --batch-file 'video_links.txt'")