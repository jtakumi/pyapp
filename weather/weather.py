import datetime
import imp
from os import times

import requests
import csv
import json

"""
参照サイト
https://www.gis-py.com/entry/weather-json"""


#地域ごとのコード
area_dic={'北海道/釧路':'014100',
            '北海道/旭川':'012000',
            '北海道/札幌':'016000',
            '青森県':'020000',
            '岩手県':'030000',
            '宮城県':'040000',
            '秋田県':'050000',
            '山形県':'060000',
            '福島県':'070000',
            '茨城県':'080000',
            '栃木県':'090000',
            '群馬県':'100000',
            '埼玉県':'110000',
            '千葉県':'120000',
            '東京都':'130000',
            '神奈川県':'140000',
            '新潟県':'150000',
            '富山県':'160000',
            '石川県':'170000',
            '福井県':'180000',
            '山梨県':'190000',
            '長野県':'200000',
            '岐阜県':'210000',
            '静岡県':'220000',
            '愛知県':'230000',
            '三重県':'240000',
            '滋賀県':'250000',
            '京都府':'260000',
            '大阪府':'270000',
            '兵庫県':'280000',
            '奈良県':'290000',
            '和歌山県':'300000',
            '鳥取県':'310000',
            '島根県':'320000',
            '岡山県':'330000',
            '広島県':'340000',
            '山口県':'350000',
            '徳島県':'360000',
            '香川県':'370000',
            '愛媛県':'380000',
            '高知県':'390000',
            '福岡県':'400000',
            '佐賀県':'410000',
            '長崎県':'420000',
            '熊本県':'430000',
            '大分県':'440000',
            '宮崎県':'450000',
            '鹿児島県':'460100',
            '沖縄県/那覇':'471000',
            '沖縄県/石垣':'474000'}

#今日の日付を文字列に変換する
today=datetime.date.today()
d1=today.strftime("%y-%m-%d")
#今日の日付を取得してファイル名として結合
fname="weather" + d1 + ".csv"

#csvのヘッダー
header=['都道府県','データ配信元','報告日時',
        '地域名','予報日時','天気','風','波']

#実行する関数
def main():
    make_csv()

#csvを作るなり
def make_csv():
    with open(fname,'w',encoding='utf-8') as wf:
        #開業まで書きます
        writer=csv.writer(wf,lineterminator='\n')
        #ヘッダーを書き出す
        writer.writerow(header)

        #jsonファイルから情報を取得
        write_lists=get_info()
        #csvへ書き込み
        writer.writerows(write_lists)

def get_info():
    write_lists=[]
    #気象庁のデータにアクセスするためのベースとなるURL
    base_url="https://www.jma.go.jp/bosai/forecast/data/forecast/"
    #先に作成した配列を参照して地域別に天気情報を取得する
    for k,v in area_dic.items():

        if k.find('/'):
            prefecture=k[0:k.find('/')]
        else:
            prefecture=k

        #地域コードをurlに結合
        url=base_url + v + '.json'
        res=requests.get(url).json()
        
        
        for re in res:
            publishingOffice=re['publishingOffice']
            reportDatetime=re['reportDatetime']
            timeSeries=re['timeSeries']

            for time in timeSeries:
                #今回取得するデータ以外を排除する
                if 'pops' in time['areas'][0]:
                    pass
                elif 'temps' in time['areas'][0]:
                    pass
                elif 'tempsMax' in time['areas'][0]:
                    pass
                else:
                    for i in range(len(time['areas'])):
                        local_name=time['areas'][i]['area']['name']
                        
                        for j in range(len(timeSeries[0]['timeDefines'])):
                            if 'weathers' not in time['areas'][i]:
                                weather=''
                            else:
                                weather=time['areas'][i]['weathers'][j]
                            
                            if 'winds'not in time['areas'][i]:
                                wind=''
                            else:
                                wind=time['areas'][i]['winds'][j]

                            if 'waves' not in time['areas'][i]:
                                wave=''
                            else:
                                wave=time['areas'][i]['waves'][j]

                            timeDefine=time['timeDefines'][j]

                            #各種情報をリストに格納する
                            write_list=[]
                            write_list.append(prefecture)
                            write_list.append(publishingOffice)
                            write_list.append(reportDatetime)
                            write_list.append(local_name)
                            write_list.append(timeDefine)
                            write_list.append(weather)
                            write_list.append(wind)
                            write_list.append(wave)

                            write_lists.append(write_list)
    return write_lists

if __name__=='__main__':
    main()


print('finish')