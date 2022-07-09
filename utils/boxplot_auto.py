#
"""
wt = [41, 35, 33, 36, 40, 46, 31, 37, 34, 30, 38, 52, 57, 62, 55, 64, 57, 56, 55, 60, 59]
cl = ["H","H","H","H","H","H","H","H","H","H","H","U","U","U","U","U","U","U","U","U","U"]
dat = {'Weight':wt,'Class':cl}
import pandas as pd   # 呼叫pandas程式套件
df = pd.DataFrame(dat)   # 將資料組合成名稱為df的data frame
df   # 顯示資料，可檢查資料格式是否正確
第二步: 呼叫seaborn程式套件
  import seaborn as sns
第三步: 畫圖。
  sns.set(style="whitegrid")
ax = sns.boxplot(x = "Class", y = "Weight", data = df, width=0.2, palette="Set3")
ax = sns.swarmplot(x = "Class", y = "Weight", data = df, color = "red")
"""

import seaborn as sns
import pandas as pd
#        0                                                                                                                                        16

odg = []

#odg_path = 'music_source/odg/'
odg_path = 'music_source/odg_2_2/'

for ii in range(1,600):
    #print(ii)
    f = open(odg_path + str(ii) )#+ '.txt')
    for l in range(11):
        odg_value = f.readline()
        odg.append(float(odg_value))
    f.close()
        
mix = []
for j in range(1,600):
    for i in range(11):
        str = '{}/{}'.format(i, 10-i)
        mix.append(str)
        
#print(mix)

dat = {'ODG Improvement':odg,'mix level':mix}
df = pd.DataFrame(dat)

sns.set(style="whitegrid")
ax = sns.boxplot(x = "mix level", y = "ODG Improvement", data = df, width=0.2, palette="Set3")
#sns.plt.savefig('box.png')
ax.get_figure().savefig('ax.png')
