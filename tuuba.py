import requests
from config import youtube_api_key, discord_webhook, relevanceLanguage, keyword
from datetime import datetime, timedelta
import json
import sys

def get_yesterday_iso():
    yesterday = datetime.utcnow() - timedelta(days=1)
    start_of_day = datetime(yesterday.year, yesterday.month, yesterday.day, 0, 0, 0)
    iso_start = start_of_day.isoformat() + "Z"
    end_of_day = datetime(yesterday.year, yesterday.month, yesterday.day, 23, 59, 59)
    iso_end = end_of_day.isoformat() + "Z"
    return iso_start, iso_end

def discord_post_webhook(text):
    url = discord_webhook
    payload = {"content": text}
    headers = {"User-Agent": "Tuuba"}
    r = requests.request("POST", url, json=payload, headers=headers)
    return r.status_code

def youtube_get_stp():
    url = "https://www.googleapis.com/youtube/v3/search"
    headers = {"User-Agent": "Tuuba"}

    aftertime, beforetime = get_yesterday_iso()

    querystring = {
        "part":"snippet",
        "type":"video",
        "q":keyword,
        "publishedAfter":aftertime,
        "publishedBefore":beforetime,
        "key":youtube_api_key,
        "order":"date",
        "relevanceLanguage":relevanceLanguage,
        "safeSearch":"none"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.status_code, response.text

def main():
    status_code, content = youtube_get_stp()
    if status_code == 200:
        content = json.loads(content)
        for categories in content['items']:
            videotitle = categories['snippet']['title']
            videoid = categories['id']['videoId']
            fullurl = 'https://www.youtube.com/watch?v={}'.format(videoid)
            #Post to Discord at this point
            discord_post = discord_post_webhook(fullurl)
    else:
        sys.exit()

    return


if __name__ == "__main__":
    main()
