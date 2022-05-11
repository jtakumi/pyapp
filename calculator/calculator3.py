#電卓はtkinterを使う
from ast import Expression
from tkinter import *
import winsound

#グローバル変数
expression=""

#電卓のボタンの色を変数でまとめる
#fg=数字,bg=背景
fgc='green'
bgc='snow'

#ボタンが押されたとき
def press(num):
    global expression

    #文字列の足し算
    expression+=str(num)
    #equationメゾットを使用
    equation.set(expression)
    #440Hzのビープ音を200ms流す
    winsound.Beep(440,200)

#イコール
def equalpress():

    try:
        global expression
        #文字列を結果に変換
        total=str(eval(expression))
        equation.set(total)
        #空白で初期化
        expression=""
        #492HzBeep
        winsound.Beep(492,200)

    #エラー発生
    except:
        equation.set("error")
        expression=""
        #492HzBeep
        winsound.Beep(492,200)

#クリア機能
def clear():
    global expression
    expression=""
    equation.set("")
    #392HzBeep
    winsound.Beep(392,200)

#コード実行
if __name__ =="__main__":
    #GUIウィンドウを作成
    gui=Tk()
    #ウィンドウの背景の色
    gui.configure(background="bisque")
    #タイトル
    gui.title("Calculator3 powerd  by python")
    #ウィンドウのサイズ
    gui.geometry("600x600")
    """StrningVar()は変数クラス
    このクラスのインスタンスを作成"""
    equation=StringVar()
    """expressionを表示 
    テキストボックスを作成"""
    expression_field=Entry(gui,textvariable=equation,fg='green',bg='lavender',font=("Arial",16))
    #グリッドメゾット移動のために使う
    expression_field.grid(columnspan=4,ipadx=70)
    #ボタンを作成

    
    #数字ボタン,フォントサイズ16px
    button1=Button(gui,text='  1  ',fg=fgc,bg=bgc,
                  command=lambda:press(1),height=2,width=10,font=("Arial",16))
    button1.grid(row=4,column=0)
    button2=Button(gui,text='  2  ',fg=fgc,bg=bgc,
                  command=lambda:press(2),height=2,width=10,font=("Arial",16))
    button2.grid(row=4,column=1)
    button3=Button(gui,text='  3  ',fg=fgc,bg=bgc,
                  command=lambda:press(3),height=2,width=10,font=("Arial",16))
    button3.grid(row=4,column=2)
    button4=Button(gui,text='  4  ',fg=fgc,bg=bgc,
                  command=lambda:press(4),height=2,width=10,font=("Arial",16))
    button4.grid(row=3,column=0)
    button5=Button(gui,text='  5  ',fg=fgc,bg=bgc,
                  command=lambda:press(5),height=2,width=10,font=("Arial",16))
    button5.grid(row=3,column=1)
    button6=Button(gui,text='  6  ',fg=fgc,bg=bgc,
                  command=lambda:press(6),height=2,width=10,font=("Arial",16))
    button6.grid(row=3,column=2)
    button7=Button(gui,text='  7  ',fg=fgc,bg=bgc,
                  command=lambda:press(7),height=2,width=10,font=("Arial",16))
    button7.grid(row=2,column=0)
    button8=Button(gui,text='  8  ',fg=fgc,bg=bgc,
                  command=lambda:press(8),height=2,width=10,font=("Arial",16))
    button8.grid(row=2,column=1)
    button9=Button(gui,text='  9  ',fg=fgc,bg=bgc,
                  command=lambda:press(9),height=2,width=10,font=("Arial",16))
    button9.grid(row=2,column=2)
    button0=Button(gui,text='  0  ',fg=fgc,bg=bgc,
                  command=lambda:press(0),height=2,width=10,font=("Arial",16))
    button0.grid(row=5,column=0)
    #小数点
    decimal=Button(gui,text='  .  ',fg=fgc,bg=bgc,
                  command=lambda:press("."),height=2,width=10,font=("Arial",16))
    decimal.grid(row=5,column=1)
    #プラスボタン
    plus=Button(gui,text='  +  ',fg=fgc,bg=bgc,
                  command=lambda:press("+"),height=2,width=10,font=("Arial",16))
    plus.grid(row=1,column=3)
    #マイナス
    minus=Button(gui,text='  -  ',fg=fgc,bg=bgc,
                  command=lambda:press("-"),height=2,width=10,font=("Arial",16))
    plus.grid(row=2,column=3)
    #掛ける
    multiply=Button(gui,text='  x  ',fg=fgc,bg=bgc,
                  command=lambda:press("*"),height=2,width=10,font=("Arial",16))
    multiply.grid(row=3,column=3)
    #割り算
    divide=Button(gui,text='  ÷  ',fg=fgc,bg=bgc,
                  command=lambda:press("/"),height=2,width=10,font=("Arial",16))
    divide.grid(row=4,column=3)
    #イコール
    equal=Button(gui,text='  =  ',fg=fgc,bg=bgc,
                  command=equalpress,height=2,width=10,font=("Arial",16))
    equal.grid(row=5,column=3)
    #クリアボタン
    clear=Button(gui,text='  C  ',fg=fgc,bg=bgc,
                  command=clear,height=2,width=10,font=("Arial",16))
    clear.grid(row=5,column=2)
    #guiスタート
    gui.mainloop()
