# Evaluation Dataset for Japanese Lexical Simplification


BCCWJコーパスからデータセットの文を抽出するプログラムがあります。
BCCWJが手元にないとこのプログラムは作れません。

ここから下の作業はShellScriptでのちに書く予定です。

手順：
mkdir EvaluationDataset/Orig\_Data でを作ります
ここにBCCWJのSUWにあるすべてのフォルダにあるzipファイルを解凍し、でてきた.txtファイルを入れます。

mkdir EvaluationDataset/Orig\_Sent　で作ります
次にScriptディレクトリに移動し
python get\sent\_from\_BCCWJ\_SUW.py　　を実行
すると、Orig\_SentにBCCWJのすべての文がpickleデータとして保存されます。

ToDo: データセットで使う文の抽出
