#必要環境//ローカルで使用する必要
from smartcard.Exceptions import NoCardException
from smartcard.System import readers
#csvnに変換環境
import csv,os
#カードリーダーを読む
def read_felica_lite_idm():
    try:#<1>
        reader = readers()
        print("利用可能なカードリーダー:", reader) #結果はリーダー名前
        #connectionはこのリーダー使う、その変数は後に使える
        connection = reader[0].createConnection()
        #このリーダーを接続
        connection.connect()
        #カードにIDm読み出し指令です
        GET_IDM_APDU = [0xFF, 0xCA, 0x00, 0x00, 0x00]
        #カードからの数字、response is IDm，sw1，sw2 is 成功かどうか（sw1 == 0x90 and sw2 == 0x00は成功）
        response, sw1, sw2 = connection.transmit(GET_IDM_APDU)
        #もし０ｋなら、——結果から16bitに引換
        if sw1 == 0x90 and sw2 == 0x00:
            idm = response
            idm_hex = ''.join(format(byte, '02X') for byte in idm)
            print("Felica Lite-SカードのIDm:", idm_hex)
            #失敗なら、エラーに
            #この値は他の関数でも使うにする
            return idm_hex
        else:
            print("Felica Lite-SカードのIDmを取得できませんでした")
        #close    
        connection.disconnect()
        #if 前の手数出来なかったら
    except NoCardException:#<1>
        print("カードが読み込めませんでした")
#前の関数を使う、
#read_felica_lite_idm()


#前の関数から次の関数を使う、
idm_hex = read_felica_lite_idm()
if idm_hex:#空内容検査
#csvファイルに書き込み・・あモード追加モードです、ファイルいないば、新しい作る
    with open("idm.csv","a",newline='') as f:
        writer= csv.writer(f)
        writer.writerow([idm_hex])
