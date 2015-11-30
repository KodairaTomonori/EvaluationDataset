# Evaluation Dataset for Japanese Lexical Simplification
日本語語彙平易化の評価データセット

注意：
　BCCWJから、文を選んだため、文をそのまま公開することができません。
　そのため、BCCWJからデータセットで使う文の抽出プログラムを公開しています。
　うまく文が抽出できない場合は、BCCWJを持っているという証明ができれば直接お渡しすることができます。
  プログラムを動かすには、python2.7の環境が必要です。

手順：
  # 配布可能なデータと文抽出のスクリプトとデータ
  git clone https://github.com/KodairaTomonori/EvaluationDataset
  
  # 次にScriptディレクトリに移動しBCCWJから文を取ってくるスクリプトを実行(xxxxにBCCWJまでのpathを入力)
  python get\sent\_from\_BCCWJ.py xxxx/BCCWJ/SUW/
  すると、BCCWJ/originalにBCCWJのすべての文がtxtデータとして保存されます。

  # 次に、extract_sentence_from_location.pyを実行すると、データセットで使う文の抽出ができます
  python extract_sentence_from_location.py


その他説明：
　言い換えのランキングについては、substitutesのフォルダ内にあります。
　subs.csvには、言い換えの載っている順番とその品詞について書いてあります。。
　ave_rank.csvとmle_rank.csvには、それぞれ、平均と最尤推定で求めたランキングがあります。
　2つのファイルの並びは、平易な順で並んでいます。(平易--->難解)
　コンマ区切りで各順位を表していて、スペースで句切られている場合、同順となります。


---------------
　首都大学東京・システムデザイン・情報通信スステム・小町研究室
　小平　知範
　e-mail: kodaira-tomonori-at-ed.tmu.ac.jp
---------------
