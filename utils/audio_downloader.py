import os
import sys
import pandas as pd


def m_link(youtube_id):

    link = 'https://www.youtube.com/watch?v=' + youtube_id
    return link


def download(loc, name, link, sr=44100, type='audio'):

    if type == 'audio':
        command = 'cd %s;' % loc
        command += 'youtube-dl -x --audio-format wav -o "' + name + '.%(ext)s" ' + link + ';'
        os.system(command)


def m_audio(loc, data_frame):

    cat_list = data_frame['videos'].keys()

    for i in range(0, len(cat_list)):
        # replace space in duet directory naming to '-'
        cat = cat_list[i]
        cat_dir = cat_list[i].replace(' ', '-')

        if not os.path.isdir('%s%s' % (loc, cat_dir)):
            os.mkdir('%s%s' % (loc, cat_dir))

        for j in range(0, len(data_frame['videos'][cat])):

            yt_id = data_frame['videos'][cat][j]
            link = m_link(yt_id)
            download((loc + cat_dir), yt_id, link)


if __name__ == '__main__':

    train = pd.read_json('MUSIC_dataset/MUSIC_solo_videos.json')
    test = pd.read_json('MUSIC_dataset/MUSIC_duet_videos.json')

    m_audio('data/train/audio/', train)
    #m_audio('data/test/audio/', test)
