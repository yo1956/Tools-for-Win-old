#outlookのテンプレが書き込まれた状態で新規メッセージ作成する
#windows用

import win32com.client as win                              #outlookやexcelの操作を可能にするモジュール #pip install pywin32でインストール
import datetime

#outlookオブジェクト(COMオブジェクト)の設定
outlook = win.Dispatch('Outlook.Application')              #これ以後、outlookオブジェクトでVBAコマンドを使うことでOutlookの操作が可能になる
mail = outlook.CreateItem(0)                               #outlookアイテムを作成 #引数が0だとメールのオブジェクトを作れる

#メールの内容
#sign =                                                    #署名

mail.BodyFormat = 1                                        #メールフォーマット: 1 テキスト, 2 HTML, 3 リッチテキスト
to_list = ['~@gmail.com', #宛先メールアドレス
           ]
mail.To =  ';'.join(to_list)
#mail.cc = '~@gmail.com'
#mail.Bcc = 
current_date = datetime.datetime.now()
mail.Subject = '件名を入力' + str(current_date.month) + '/' + str(current_date.day)      #件名を入力
mail.Body = '''
   テンプレ本文を入力


'''

#path = r'C:\\'                                           #添付ファイルは絶対パスで指定
#mail.Attachments.Add(path)

#作ったテンプレを表示
mail.Display(True)