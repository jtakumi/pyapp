#電卓はtkinterを使う
from ast import Expression
from tkinter import *

#グローバル変数
expression=""

#ボタンが押されたとき
def press(num):
    global expression

    #文字列の足し算
    expression+=str(num)
    #equationメゾットを使用
    equation.set(expression)

#イコール
def equalpress():

    try:
        global expression
        #文字列を結果に変換
        total=str(eval(expression))
        equation.set(total)
        #空白で初期化
        expression=""

    #エラー発生
    except:
        equation.set("error")
        expression=""

#クリア機能
def clear():
    global expression
    expression=""
    equation.set("")

#コード実行
if __name__ =="__main__":
    #GUIウィンドウを作成
    gui=Tk()
    #ウィンドウの背景の色
    gui.configure(background="black")
    #タイトル
    gui.title("Calculator by python")
    #ウィンドウのサイズ
    gui.geometry("450x300")
    """StrningVar()は変数クラス
    このクラスのインスタンスを作成"""
    equation=StringVar()
    """expressionを表示 
    テキストボックスを作成"""
    expression_field=Entry(gui,textvariable=equation)
    #グリッドメゾット移動のために使う
    expression_field.grid(columnspan=4,ipadx=70)
    #ボタンを作成
    #数字ボタン
    button1=Button(gui,text='  1  ',fg='green',bg='gray',
                  command=lambda:press(1),height=2,width=10)
    button1.grid(row=2,column=0)
    button2=Button(gui,text='  2  ',fg='green',bg='gray',
                  command=lambda:press(2),height=2,width=10)
    button2.grid(row=2,column=1)
    button3=Button(gui,text='  3  ',fg='green',bg='gray',
                  command=lambda:press(3),height=2,width=10)
    button3.grid(row=2,column=2)
    button4=Button(gui,text='  4  ',fg='green',bg='gray',
                  command=lambda:press(4),height=2,width=10)
    button4.grid(row=3,column=0)
    button5=Button(gui,text='  5  ',fg='green',bg='gray',
                  command=lambda:press(5),height=2,width=10)
    button5.grid(row=3,column=1)
    button6=Button(gui,text='  6  ',fg='green',bg='gray',
                  command=lambda:press(6),height=2,width=10)
    button6.grid(row=3,column=2)
    button7=Button(gui,text='  7  ',fg='green',bg='gray',
                  command=lambda:press(7),height=2,width=10)
    button7.grid(row=4,column=0)
    button8=Button(gui,text='  8  ',fg='green',bg='gray',
                  command=lambda:press(8),height=2,width=10)
    button8.grid(row=4,column=1)
    button9=Button(gui,text='  9  ',fg='green',bg='gray',
                  command=lambda:press(9),height=2,width=10)
    button9.grid(row=4,column=2)
    button9=Button(gui,text='  0  ',fg='green',bg='gray',
                  command=lambda:press(0),height=2,width=10)
    button9.grid(row=5,column=0)
    #プラスボタン
    plus=Button(gui,text='  +  ',fg='green',bg='gray',
                  command=lambda:press("+"),height=2,width=10)
    plus.grid(row=2,column=3)
    #マイナス
    minus=Button(gui,text='  -  ',fg='green',bg='gray',
                  command=lambda:press("-"),height=2,width=10)
    plus.grid(row=3,column=3)
    #掛ける
    multiply=Button(gui,text='  x  ',fg='green',bg='gray',
                  command=lambda:press("*"),height=2,width=10)
    multiply.grid(row=4,column=3)
    #割り算
    divide=Button(gui,text='  ÷  ',fg='green',bg='gray',
                  command=lambda:press("/"),height=2,width=10)
    divide.grid(row=5,column=3)
    #イコール
    equal=Button(gui,text='  =  ',fg='green',bg='gray',
                  command=equalpress,height=2,width=10)
    equal.grid(row=5,column=2)
    #クリアボタン
    clear=Button(gui,text='  C  ',fg='green',bg='gray',
                  command=clear,height=2,width=10)
    clear.grid(row=5,column=1)
    #小数点
    decimal=Button(gui,text='  .  ',fg='green',bg='gray',
                  command=lambda:press("."),height=2,width=10)
    decimal.grid(row=6,column=0)
    #guiスタート
    gui.mainloop()
