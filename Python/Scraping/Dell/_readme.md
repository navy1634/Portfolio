
## 概要
Dell Technologies Japan Inc. のホームページで販売されているPCの情報に関してスクレイピングを行う



## 関数
- `main.py`
    ・`main` 関数　           : スクレイピングの実行

- `Crawer.py`
    ・ `Crawer()`             : ブラウザの立ち上げ、ページ外の遷移に関するクラス

- `Parser.py`
    ・ `Dell_Parser()`        : Clawerで立ち上げたページ内を遷移するクラス、各製品ページへのリンクの取得を主に行う

- `Dell_ProdData_Parser.py`
    ・`Dell_Index_Perser()`   : 製品に関するデータの取得を行うクラス

