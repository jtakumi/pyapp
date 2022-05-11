from datetime import datetime

import requests

#気象庁のデータを使用する
jma_news= "https://www.jma.go.jp/bosai/forecast/data/forecast/230000.json"
jma_json=requests.get(jma_news).json()

#取得するデータを選択する
jma_date=jma_json[0]['timeSeries'][0]['timeDefines'][0]
jma_weater=jma_json[0]['timeSeries'][0]['areas'][0]['weathers'][0]
jma_rainfall=jma_json['Feature'][0]['Property']['WeatherList']['Weather'][0]['Rainfall']

#全角スペース削除
jma_weater=jma_weater.replace('　','')

#今日の日付を取得してファイル名として結合
fname="weater" + datetime.date.today()
fname=fname + ".txt"

with open(fname,mode='w',encoding='utf-8') as wf:
    print(jma_date)
    print(jma_weater)
    print(jma_rainfall)
wf.close()
print('finish')