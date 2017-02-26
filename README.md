# comozilla.github.io
comozilla Webサイトのソースコード。
静的サイトジェネレータ[Pelican](http://getpelican.com)を利用しています。


## 環境構築
### 要件
- Python 2.7.x or 3.3+

### Pelican及びライブラリのインストール
```
pip install pelican markdown ghp-import webassets
```

デプロイに[Fabric](http://www.fabfile.org/)を使う場合

Python 2.7
```
pip install Fabric
```
Python >= 3
```
pip install Fabric3
```


## コンテンツを書く
基本的には`content`ディレクトリ以下にファイルを置きます。  
ブログのような記事はtumblrで扱うと思うので、静的なページを`content/pages`以下に作成してください。  

以下のようにMarkdownでページを記述していきます。(reStructuredTextとかも使えます)  
先頭にメタデータを記述でき、`Title`は必須です。
```
Title: Hoge Title

Hogehoge Workshop
========
...
```

詳細は[Pelican Docs](http://docs.getpelican.com/en/3.6.3/content.html)を参照


## 使い方
### html生成
```
make html
```

(Fabric)
```
fab build
```

### 変更を検知して自動生成
```
make regenerate
```

(Fabric)
```
fab regenerate
```

### ローカルでサーバを起動
```
make serve
```

(Fabric)
```
fab serve
```

ブラウザで`http://localhost:8000/`にアクセスして表示を確認


## デプロイ
公開用のhtml生成する
```
make publish
```
以下のコマンドで、`output`ディレクトリ以下をmasterブランチにcommitしてpushまで行われます。
```
make github
```

(Fabric)
```
fab gh_pages
```