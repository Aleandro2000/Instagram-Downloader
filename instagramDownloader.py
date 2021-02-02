import requests
import webbrowser
import re
from os import system
import sys

def get_response(url):
    r=requests.get(url)
    while r.status_code!=200:
        r=requests.get(url)
    return r.text

def prepare_urls(matches):
    return list({match.replace("\\u0026", "&") for match in matches})

if len(sys.argv)==1:

    while True:
        print("############################")
        print("#Instagram Media Downloader#")
        print("############################\n")
        url=input('Enter Instagram URL or type EXIT to exit: ')
        if url.lower()=="exit":
            break
        else:
            response=get_response(url)

            vid_matches=re.findall('"video_url":"([^"]+)"', response)
            pic_matches=re.findall('"display_url":"([^"]+)"', response)

            vid_urls=prepare_urls(vid_matches)
            pic_urls=prepare_urls(pic_matches)

            if vid_urls:
                print('\nDetected Videos:\n{0}'.format('\n'.join(vid_urls)))
                webbrowser.open(vid_urls[0])

            if pic_urls:
                print('\nDetected Pictures:\n{0}'.format('\n'.join(pic_urls)))
                webbrowser.open(pic_urls[0])

            if not (vid_urls or pic_urls):
                print('\nMay not recognize the media in the provided URL.')

            print("\nDo you want to exit (type y for yes and other key for no)?")
            url=input()
            if(url.lower()=="y"):
                break

            system("@cls||clear")

elif len(sys.argv)==2:

    url=sys.argv[-1]
    response=get_response(url)

    vid_matches=re.findall('"video_url":"([^"]+)"', response)
    pic_matches=re.findall('"display_url":"([^"]+)"', response)

    vid_urls=prepare_urls(vid_matches)
    pic_urls=prepare_urls(pic_matches)

    if vid_urls:
        print('\nDetected Videos:\n{0}'.format('\n'.join(vid_urls)))
        webbrowser.open(vid_urls[0])

    if pic_urls:
        print('\nDetected Pictures:\n{0}'.format('\n'.join(pic_urls)))
        webbrowser.open(pic_urls[0])

    if not (vid_urls or pic_urls):
        print('\nMay not recognize the media in the provided URL.')

else:
    print("*BAD SINTAX!*")