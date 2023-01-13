from youtube_transcript_api import YouTubeTranscriptApi
import csv


with open('yt_info.csv', "r", newline='') as csvfile:
    yt_info = csv.reader(csvfile, delimiter=',')
    listReport = list(yt_info)

for title, link in listReport:
    title = title.replace('?', '').replace('|', '').replace('/', '').replace(':', '')
    path = (f'yt_trans_text/{title}.txt')
    with open(path, 'w', encoding='utf-8-sig') as f:
        try:
            transcript_list = YouTubeTranscriptApi.get_transcript(link, languages=['zh-Hant', 'en'])
            for trans in transcript_list:
                f.writelines(str(trans['text'] + ", start: " + str(trans['start']) + ", end: " + str(round(
                    trans['start'] + trans['duration'])+'\n')))
        except:
            continue

