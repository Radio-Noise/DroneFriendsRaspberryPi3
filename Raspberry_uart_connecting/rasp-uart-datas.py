'''
-----------------------------------------------------
twelite uart 確認方法

*minicom使用
コマンド入力後受信待機状態になる
　$ sudo minicom -b 115200 -o -D /dev/ttyAMA0
　デフォルトではuart接続をした場合ttyAMA0に設定されているはず

*cu使用
コマンド入力後受信待機状態になる
 $ cu -s 115200 -l /dev/ttyAMA0
 終了方法は~.と入力
 ----------------------------------------------------
 接続デバイス確認方法(linux)
 ls /dev 
 ls -l /dev/serial/by-id/
 引用:https://qiita.com/sttn/items/567c9f49b88ff275b51a
 lsblk (-o)
 *PCIデバイス一覧
 lspci
 *読み込まれているモジュール一覧
 lsmod
 ls -la /dev/serial?
 参照元:http://note.kurodigi.com/linux-systeminfo/
'''
#以下コマンドと説明の記載
import serial

#デバイスをttyAMA0,ポートレートを115200に設定
ser = serial.Serial('dev/ttyAMA0',115200)

#指定ポートからのuart受信待ち(終端\nを読み込みまで読み込む)
ser.readline()

#一文字読み込み
c = ser.read()

#指定文字数読み込み
str = ser.read({int型:指定文字数})

#指定データ送信
ser.write({char型:送信内容})

#デバイスのポートを閉じる(最後に必ず実行すること)
ser.close()

#チェックサム計算方法
data = ':0000000000000000000000000000'

#データ頭の:を取り除く
data = data[1:]

#二桁ずつ区切って16進数として抽出
ans = [int(data[i:i+2], 16) for i in range(0, len(data), 2)]

#総和を計算
num = sum(ans)
#チェックサム計算(0になるはず)
hex(num & 0b1111)#=0
#----------------------------------------------------------------
#以下プログラム本文に追加する予定

#送信予定データの宣言(char型で固定)
global submit_datas =''

#press関数内
#送信予定データに気圧を追加
submit_datas = submit_datas + str(気圧データ変数)

#tempture関数内
#送信予定データに気温を追加
submit_datas = submit_datas + str(気温データ変数)

#humid関数内
#送信予定データに湿度を追加
submit_datas = submit_datas + str(湿度データ変数)

#main関数内
#submit_datasのこの地点での内容:気圧気温湿度(各4桁、合計12桁10進数)
#10進数のある数列を16進素に変換する
submit_datas = hex(submit_datas)

#送信データリセット
submit_datas =''
