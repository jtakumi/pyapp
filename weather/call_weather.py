import schedule
import time

"""
参考サイト
https://note.com/financedog/n/n08a01a502a5b#7172ae1e-448e-4d28-bd79-fa34af53243b
"""

#この関数でweather.pyを呼び出す
def work():
    import weather
    print("running")

#AM9:00実行
schedule.every().day.at("9:00").do(work)

while True:
    schedule.run_pending()
    time.sleep(1)