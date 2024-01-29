### Aribaでの請求書提出を自動化

- 前提
1. Pythonが実行できる環境であること.
1. 使用するライブラリがインストール済み.
1. WebDriverがインストール済み.
1. 前回の請求書、今回の請求書がPDF形式でフォルダに保存されている.（前回の請求書情報をコピーする形）

- 使用前作業
1. webdriver_path,pdf_path4this_time,pdf_path4last_time,username,passwd,URL
上記を全て自分の環境通り変更する。

- 実行方法
```
python ariba.pyのパス
```

- pythonがクライアント機でインストールされてない場合

inst_py_and_webDriv.ps1を実行してpythonとWebDriverをインストールする(管理者権限で実行).