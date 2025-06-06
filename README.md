# FeliCa
こちらはテストカードとソニーのRC-S300を使って、テストカードのIDm（シリアルナンバー）が読み取れるpythonコードです。
応用点はカード特有のIDmを使って：
1.学生や社員の出席や退勤する＊    
2.鍵としてドアの出入り＊       ＊idm無断複製可能、テストカードに暗号化が必要です、具体的に生産メーカーに問い合わせ。
3.システムがidmを読み取り、社員の個人情報を呼び出す＊
......

#注意点
このコードは日本知的財産権と著作権が応用されている。
このコードは完全に自分で考えて、エラーの内容はChatGPTと相談されたコードです。

#環境：
1.python
2.pyscard
(pip install pyscard)

＃メイン
pyscadのインポートは....
from smartcard.Exceptions import NoCardException
from smartcard.System import readers
カードにとってもっとインポート追加可能。

＃注意点
１．複数のカードや周囲のカードがカードリーダーに重ならないでください、エラーが出ます。
２．このコードは：JIS 6319-4 PMm:0X00F1000000014300 (ソニー - FeliCa Lite-S RC-S966)テストカードが使える

by daiichikoukadaigaku 23TE465 ZHA JUNJIE


