# Evaluation Dataset for Japanese Lexical Simplification

BCCWJから、文を選んだため、文をそのまま公開することができません。
そのため、BCCWJからデータセットで使う文の抽出プログラムを公開します。

BCCWJコーパスからデータセットの文を抽出するプログラムがあります。
BCCWJが手元にないとこのデータセットは作れません。
プログラムを動かすには、python2.7の環境が必要です。

手順：
mkdir EvaluationDataset/Orig\_Data でを作ります
ここにBCCWJのSUWにあるすべてのフォルダにあるzipファイルを解凍し、でてきた.txtファイルを入れます。

mkdir EvaluationDataset/Orig\_Sent　で作ります
次にScriptディレクトリに移動し
python get\sent\_from\_BCCWJ\_SUW.py　　を実行
すると、Orig\_SentにBCCWJのすべての文がtextデータとして保存されます。

次に、extract_sentence_from_location.pyを実行すると、データセットで使う文の抽出ができます

言い換えのランキングについては、substitutesのフォルダ内にあります。
subs.csvには、言い換え対象の語と、その品詞についてのデータがあります。
ave_rank.csvとmle_rank.csvには、それぞれ、平均と最尤推定で求めたランキングがあります。
2つのファイルの並びは、平易な順で並んでいます。(平易---難解)


