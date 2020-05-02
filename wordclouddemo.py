import wordcloud
import matplotlib.pyplot as plt
import pandas as pd


path = "D:/myfile/cultureD/doc_list.txt"
#df = pd.read_excel(path,index_col=0,encoding='UTF-8')
fnl_words = [dd.replace('\n','') for dd in open(path,encoding='UTF-8').readlines()]


#fnl_words = list(df)
wc = wordcloud.WordCloud(width=1000, font_path='simhei.ttf',background_color='white',height=600,collocations=False)#设定词云画的大小字体，一定要设定字体，否则中文显示不出来
wordjoin = " ".join(str(fnl_words))
print(wordjoin)

wc.generate(str(fnl_words))
wc.to_file("D:/myfile/cultureD/新闻.png")