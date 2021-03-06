# 使い方
特定のツイッターアカウントのフォロワー一覧をcsvファイルで出力するプログラムです。pythonというプログラミング言語を使って作成しているため、まずpythonの環境を構築する必要があります。勉強もかねて作ったのでぜひやってみてください。

# 環境構築
## 必要なもの
* python
* git

### gitのインストール
まずgitというものをインストールする必要があります。既にある人は飛ばしてください。たぶんgoogleで「git インストール」とか調べたら詳しいやり方が乗ってます。  
gitのインストールが完了したら、ターミナル（コマンドプロンプト）を開いて作業ディレクトリに移動します（cd desktop みたいに）。  
```
git clone https://github.com/ichiru1222/python_scraping.git
```
を実行することで、このコードが載っているgithubというサイトから、ソースコードをコピーしてくることができます。
ここまでで、gitのインストールとソースコードのコピーは完了です。

### pythonのインストールと環境構築
次にpythonをインストールする必要があります。pythonのインストールもググるといろいろ方法が出てきますが、自分はAnacondaというものを使っています。Anacondaはpythonとそのライブラリをまとめてインストールできる便利な機能のついたpythonディストリビューションというものらしいです。Anacondaのインストールもググると出てくるのでやってみてください。そんな難しくないです。ここでうまくインストールできていたら、
```
conda -V
```
でバージョンが表示されるはずです。ここでうまくいかない人は多分パスが通っていないので、「anaconda path」とかで調べてください。

### pythonの仮想環境作成
今回は仮想環境というものを使います。仮想環境とは実行するコードごとに別の環境を分けてあげることで、予期せぬエラーを防ぐみたいな役割があります。
今回は"twitter"という名前で仮想環境を作りたいと思うので、
```
conda create -n twitter python=3.9 anaconda
```
で実行します。ここでうまくいった場合、
```
conda info -e
```
で"twitter"が表示されると思います。
もしうまくいかない人は、anacondaのインストール時に入るanaconda promptで同様に実行してみてください。
ここまで来たらもう少しです。
```
conda activate twitter
```
で仮想環境を有効化します。
ここでうまくいくと
```
(twitter) PS C:\Users\HP\Desktop\python_scraping> 
```
みたいな感じで一番左に（仮想環境名）となると思います。
### 必要なライブラリのインストール
今回はpythonでtwitterのAPIを扱えるtweepyというライブラリを使います。このライブラリはanacondaの中にないのでインストールする必要があります。**仮想環境を有効にした状態で**、
```
pip install tweepy
```
をコマンドプロンプトで実行します。
これで準備は完了です。
コマンドプロンプトで `cd`コマンドを使ってコピーしたソースコードが入っているフォルダ（ディレクトリ）まで移動します。
そこで、
```
python get_follower.py
```
で実行できます。

### 実行
```
「@ユーザー名」を入力してください：  
```
と出るのでフォロワーを取得したいユーザのTwitterIDを@から入力します。
Enterで実行が始まります。フォロワーが多いと時間がかかります。1000人超えると20分くらいかかります。これはtwitterのAPI制限によるものです。

実行が終わると
```
ファイル名を入力してください：
```
と出るので、任意のファイル名を入力してエンターを押すと、
ファイル名.csvのファイルが吐き出されます。
あとはこれをgoogleスプレッドシートにインポートするとかして、うまく活用してください！

## 参考文献
[PythonでTwitterのタイムラインを取得する](https://www.pytry3g.com/entry/python-twitter-timeline)

[【Python】Twitterのフォロワー情報の取得方法](https://fresopiya.com/2019/04/05/getfollowerinfo/)

あとはツイッターのAPIを取得して、アクセスキーを取ってくる工程も本当は必要になります。