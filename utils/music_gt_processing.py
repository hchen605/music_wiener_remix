#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
C

https://blog.gtwang.org/programming/python-list-all-files-in-directory/
"""
import os
import numpy as np
import wave
#import matplotlib.pyplot as plt
from scipy.io.wavfile import read
from scipy.io.wavfile import write

from os import listdir
from os.path import isfile, isdir, join






def loadSoundFile(filename):
    _, audio = read(filename)
    #print(np.size(audio.shape))
    #if (audio.shape[1] > 1):#2 channel
    if(np.size(audio.shape) > 1):
        return audio[:, 0]
    else:
        return audio 


index = 401
samplerate = 44100
# 指定要列出所有檔案的目錄
gt_1_path = "music_source/gt_s1/"
gt_2_path = "music_source/gt_s2/"
gt_mix_path = "music_source/gt_mix_2_1/"
#s1_dir = ['acoustic_guitar', 'cello', 'clarinet', 'accordion']
#s2_dir = ['trumpet', 'violin', 'xylophone', 'flute']
s1_dir = ['acoustic_guitar', 'cello', 'clarinet', 'accordion']
s2_dir = ['trumpet', 'violin', 'xylophone', 'flute']

#source_path = "music_source/data/eval/audio/"   
source_path = "music_source/data/eval_3/audio/"  

for s1_path in range(4):
    gt_1_path = source_path + s1_dir[s1_path] + '/NORMALIZED'
    gt_1_files = listdir(gt_1_path)
    for f1 in(gt_1_files):
        gt_1_fullpath = join(gt_1_path, f1)
        gt_1 = loadSoundFile(gt_1_fullpath)
        for s2_path in range(4):
            gt_2_path = source_path + s2_dir[s2_path] + '/NORMALIZED'
            gt_2_files = listdir(gt_2_path)
            for f2 in(gt_2_files):
                gt_2_fullpath = join(gt_2_path, f2)
                gt_2 = loadSoundFile(gt_2_fullpath)
                for i in range(0, 11):
                    gt = i/10 * gt_1[220500:441000] + (10-i)/10 * gt_2[220500:441000]
                    #print(gt)
                    if not os.path.isdir('%s%s' % (gt_mix_path, str(index))):
                        os.mkdir('%s%s' % (gt_mix_path, str(index)))
                    gt_mix = gt_mix_path + str(index) + '/' + 'gt_s1_' + str(i) + '_gt_s2_' + str(10-i) +'.wav'
                    #print(gt_mix)
                    write(gt_mix, samplerate, gt.astype(np.int16))
                    
                fp1 = open(gt_mix_path + str(index) + '/' + 'label_1.txt', "w")
                fp2 = open(gt_mix_path + str(index) + '/' + 'label_2.txt', "w")
                fp1.write(s1_dir[s1_path])
                fp2.write(s2_dir[s2_path])
                fp1.close()
                fp2.close()
                index = index + 1
                
    
    

"""
# 取得所有檔案與子目錄名稱
gt_1_files = listdir(gt_1_path)
gt_2_files = listdir(gt_2_path)



for f1, f2 in zip(gt_1_files, gt_2_files):
    gt_1_fullpath = join(gt_1_path, f1)
    gt_2_fullpath = join(gt_2_path, f2)
    print(gt_1_fullpath)
    print(gt_2_fullpath)
    #print("file：", f1)
    #print("file：", f2)
    gt_1 = loadSoundFile(gt_1_fullpath)
    gt_2 = loadSoundFile(gt_2_fullpath)
    gt_path = join(gt_mix_path, str(index))
    
    for i in range(0, 11):
        gt = i/10 * gt_1[220500:441000] + (10-i)/10 * gt_2[220500:441000]
        #print(gt)
        gt_mix = gt_path + '/' + 'gt_s1_' + str(i) + '_gt_s2_' + str(10-i) +'.wav'
        #print(gt_mix)
        write(gt_mix, samplerate, gt.astype(np.int16))
        #mix = i/10 * sep_1 + (10-i)/10 * sep_2
    index = index + 1
    
"""