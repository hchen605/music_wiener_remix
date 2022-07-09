
"""
https://github.com/ytdl-org/youtube-dl/issues/6724
"""

import csv

path = 'val_new_2.csv'
f = open(path, 'r')
rows = csv.reader(f, delimiter=',')

fp = open("eval.zsh", "w")

for row in rows:
    #print(row[0], row[1])
    #print('youtube-dl -x --audio-format wav -o {}.wav  https://youtu.be/{}' .format(row[0],row[0]))
    fp.write('youtube-dl -x --audio-format wav -o "./gt_eval_s2/{}.%(ext)s" https://youtu.be/{}\n' .format(row[0],row[0]))

#print(rows[1])
fp.close()
