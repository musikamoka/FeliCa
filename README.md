# FeliCa<br>
こちらはテストカードとソニーのRC-S300を使って、テストカードのIDm（シリアルナンバー）が読み取れるpythonコードです。<br>
応用点はカード特有のIDmを使って：<br>
1.学生や社員の出席や退勤する＊<br>    
2.鍵としてドアの出入り＊       ＊idm無断複製可能、テストカードに暗号化が必要です、具体的に生産メーカーに問い合わせ。<br>
3.システムがidmを読み取り、社員の個人情報を呼び出す＊<br>
......

#注意点<br>
このコードは日本知的財産権と著作権が応用されている。<br>
このコードは完全に自分で考えて、エラーの内容はChatGPTと相談されたコードです。<br>

#環境：<br>
1.python<br>
2.pyscard<br>
(pip install pyscard)<br>

＃メイン<br>
pyscadのインポートは....<br>
from smartcard.Exceptions import NoCardException<br>
from smartcard.System import readers<br>
カードにとってもっとインポート追加可能。<br>

＃注意点<br>
１．複数のカードや周囲のカードがカードリーダーに重ならないでください、エラーが出ます。<br>
２．このコードは：JIS 6319-4 PMm:0X00F1000000014300 (ソニー - FeliCa Lite-S RC-S966)テストカードが使える<br>

by daiichikoukadaigaku 23TE465 ZHA JUNJIE<br>


