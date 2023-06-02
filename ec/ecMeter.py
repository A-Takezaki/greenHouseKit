#必要なライブラリをインポートします。pyserialをインストールされていない方はpyserialをpip等を用いてインストールしてください。
import serial
import datetime
import os

#保存するファイル名の定義。ここでは、csvファイル形式で保存することにしました。
fileName = '/home/pi/ec/EC_value.csv'

#シリアルポートを開ける。おまじない的なもの笑
ser = serial.Serial("/dev/ttyACM0",9600)

#もしファイルがなかったら作るプロセス
if not os.path.exists(fileName):
    thData = open(fileName,'w')
    thData.write('date_time,EC_value\n')
    thData.close()

#Arduinoからデータを受け取って、ファイルに保存するプロセス
while True:
    Arduino_data = ser.readline().strip().decode('utf-8')
    Arduino_data = [Arduino_data] #listにします
    now = str(datetime.datetime.now())[0:16] #時間は秒まで記載
    date_data = [now]
    data = date_data + Arduino_data
    thData = open(fileName, 'a')
    thData.write(','.join(map(str,data))+'\n')
    thData.close()
    break

ser.close()