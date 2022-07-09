#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
C

https://blog.gtwang.org/programming/python-list-all-files-in-directory/
"""

import numpy as np
import wave
#import matplotlib.pyplot as plt
from scipy.io.wavfile import read
from scipy.io.wavfile import write

from os import listdir
from os.path import isfile, isdir, join


"""
# 以迴圈處理
for f in files:
  # 產生檔案的絕對路徑
  fullpath = join(mypath, f)
  # 判斷 fullpath 是檔案還是目錄
  if isfile(fullpath):
    print("file：", f)
  elif isdir(fullpath):
    print("dir：", f)
"""



def loadSoundFile(filename):
    _, audio = read(filename)

    if (audio.shape[1] > 1):#2 channel
        return audio[:, 0]
    else:
        return audio 

"""
if __name__ == "__main__":
    
    cello = loadSoundFile("./music_source/cello_solo.wav")
    guitar = loadSoundFile("./music_source/guitar_solo.wav")
    
    mix_1 = loadSoundFile("./music_source/cello_solo.wav")
    mix_2 = loadSoundFile("./music_source/cello_solo.wav")
    
    cello_ = cello[0:500000]
    guitar_ = guitar[600000:1100000]
    
    samplerate = 44100
    
    for i in range(1, 10):
        gt = i/10 * cello_ + (10-i)/10 * guitar_
        mix = i/10 * mix_1 + (10-i)/10 * mix_2
        gt_path = "./music_source/gt_s1_{}_s2_{}.wav" .format(i,10-i)
        mix_path = "./music_source/mix_s1_{}_s2_{}.wav" .format(i,10-i)
        
        write(gt_path, samplerate, gt.astype(np.int16))
        write(mix_path, samplerate, gt.astype(np.int16))
    
"""


if __name__ == "__main__":
    
    
    # 指定要列出所有檔案的目錄
    gt_1_path = "music_source/gt_s1/"
    gt_2_path = "music_source/gt_s2/"
    gt_mix_path = "music_source/gt_mix/"

    # 取得所有檔案與子目錄名稱
    gt_1_files = listdir(gt_1_path)
    gt_2_files = listdir(gt_2_path)
    
    index = 1
    samplerate = 44100
    
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
    gt_1 = loadSoundFile("./music_source/cello_solo.wav")
    gt_2 = loadSoundFile("./music_source/guitar_solo.wav")
    
    sep_1 = loadSoundFile("./music_source/cello_solo.wav")
    sep_2 = loadSoundFile("./music_source/cello_solo.wav")

    samplerate = 44100
    
    for i in range(1, 10):
        gt = i/10 * gt_1 + (10-i)/10 * gt_2
        mix = i/10 * sep_1 + (10-i)/10 * sep_2
        gt_path = "./music_source/gt_mix/gt_s1_{}_s2_{}.wav" .format(i,10-i)
        mix_path = "./music_source/sep_mix/mix_s1_{}_s2_{}.wav" .format(i,10-i)
        
        write(gt_path, samplerate, gt.astype(np.int16))
        write(mix_path, samplerate, gt.astype(np.int16))

"""