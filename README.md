# Chinese-Checkers

現在はselfplay, alphabeta, mcts エージェントが使用可能です.
(9/10 現在, mctsの性能はCPUの性能に依存しています)

# 使い方

git clone などをしてレポジトリをコピーしてください. 実際に遊ぶには, まずmain.py を実行してください. プレイ人数やプレイヤーを変更したい場合にはsettings.py のplayers を変更してください.

## Selfplay

実際にコマを動かして遊ぶことができます.

## Alphabeta

アルファベータ法を用いて実装されたエージェントです. 現在, 評価関数はval_func があります.

## MCTS

モンテカルロ木探索を用いて実装されたエージェントです. 評価にはUCB1 を用いています.

## AMAF( 未実装 )

モンテカルロ木探索にAMAF(As Move As First) という手法を用いて実装されたエージェントです. 
