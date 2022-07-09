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

    #if (audio.shape[1] > 1):#2 channel
        #return audio[:, 0]
    #else:
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
        sep_path = "./music_source/sep_s1_{}_s2_{}.wav" .format(i,10-i)
        mix_path = "./music_source/mix_s1_{}_s2_{}.wav" .format(i,10-i)
        
        write(sep_path, samplerate, gt.astype(np.int16))
        write(mix_path, samplerate, gt.astype(np.int16))
    
"""


if __name__ == "__main__":
    
    
    # 指定要列出所有檔案的目錄
    sep_1_path = "music_source/sep_s1/"
    sep_2_path = "music_source/sep_s2/"
    sep_mix_path = "music_source/sep_mix/"

    # 取得所有檔案與子目錄名稱
    sep_1_files = listdir(sep_1_path)
    sep_2_files = listdir(sep_2_path)
    
    index = 7
    samplerate = 44100
    
    for f1, f2 in zip(sep_1_files, sep_2_files):
        sep_1_fullpath = join(sep_1_path, f1)
        sep_2_fullpath = join(sep_2_path, f2)
        #print(sep_1_fullpath)
        #print(sep_2_fullpath)
        #print("file：", f1)
        #print("file：", f2)
        sep_1 = loadSoundFile(sep_1_fullpath)
        #print(sep_1)
        sep_2 = loadSoundFile(sep_2_fullpath)
        sep_path = join(sep_mix_path, str(index))
        
        for i in range(0, 11):
            sep = i/10 * sep_1*20000 + (10-i)/10 * sep_2*20000
            print(sep)
            sep_mix = sep_path + '/' + 'sep_s1_' + str(i) + '_sep_s2_' + str(10-i) +'.wav'
            #print(sep_mix)
            write(sep_mix, samplerate, sep.astype(np.int16))
            #mix = i/10 * sep_1 + (10-i)/10 * sep_2
        index = index + 1
        
"""
    sep_1 = loadSoundFile("./music_source/cello_solo.wav")
    sep_2 = loadSoundFile("./music_source/guitar_solo.wav")
    
    sep_1 = loadSoundFile("./music_source/cello_solo.wav")
    sep_2 = loadSoundFile("./music_source/cello_solo.wav")

    samplerate = 44100
    
    for i in range(1, 10):
        gt = i/10 * sep_1 + (10-i)/10 * sep_2
        mix = i/10 * sep_1 + (10-i)/10 * sep_2
        sep_path = "./music_source/sep_mix/sep_s1_{}_s2_{}.wav" .format(i,10-i)
        mix_path = "./music_source/sep_mix/mix_s1_{}_s2_{}.wav" .format(i,10-i)
        
        write(sep_path, samplerate, gt.astype(np.int16))
        write(mix_path, samplerate, gt.astype(np.int16))

"""