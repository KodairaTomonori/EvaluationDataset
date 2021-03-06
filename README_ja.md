# Evaluation Dataset for Japanese Lexical Simplification
日本語語彙平易化の評価データセット

注意：
　※言い換えについている助詞が足りなかったり、余分についてる可能性があるので報告してもらえると助かります。
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
  
  # 次に、extract\_sentence\_from\_location.pyを実行すると、データセットで使う文の抽出ができます  
  python extract\_sentence\_from\_location.py  

  
平易化ランキングについて：  
  言い換えのランキングについては、substitutesのフォルダ内にあります。  
  subs.csvには、言い換えの載っている順番とその品詞について書いてあります。  
  ave_rank.csvとmle_rank.csvには、それぞれ、平均と最尤推定で求めたランキングがあります。
  各対象語、10個ごと並べています。
  2つのファイルの並びは、平易な順で並んでいます。(平易--->難解)  
  コンマ区切りで各順位を表していて、スペースで句切られている場合、同順となります。

その他の説明
　substitutesフォルダのave, mleのファイルの 一列めの番号は、アノテーションした時の並びです。
　アノテーションした際は、各言い換えが重ならないようランダムにしていました。

  annotation_dataのフォルダには、rankの方のファイルには各言い換えに付与されているランキングについてのデータがあるます。
  subの方のファイルには、アノテーション時の並びで言い換えが並べられています。
　こちらは、各対象語10文ごとには並べておらず、ばらばらです。
　こちらのデータの詳細ですが
  タスク番号：01,02,03,04,05,06,07,08,09,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29
  タスク文数：65,65,65,65,65,65,65,65,65,61,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,284
  各タスク約60文毎5人のアノテータに言い換えの並び替えの作業してもらいました。
  最後の29番めは、研究室の学生にやってもらったものです。
  ランキングのデータはこれを参考にしてください。
  
　
論文： https://www.aclweb.org/anthology/P16-3001.pdf

 ```
 @inproceedings{kodaira-etal-2016-controlled,
    title = "Controlled and Balanced Dataset for {J}apanese Lexical Simplification",
    author = "Kodaira, Tomonori  and
      Kajiwara, Tomoyuki  and
      Komachi, Mamoru",
    booktitle = "Proceedings of the {ACL} 2016 Student Research Workshop",
    year = "2016",
    pages = "1--7",
}
 ```
  

---------------
  首都大学東京・システムデザイン・情報通信スステム・小町研究室  
  小平 知範  
  e-mail: kodaira-tomonori-at-ed.tmu.ac.jp  
---------------
