# Chinese-Checkers

現在はselfplay, alphabeta, mcts エージェントのみ使うことができます.
(9/10 現在, mctsの性能はCPUの性能に依存しています)

# 使い方

まずはmain.py を実行してください. エージェントを変更したい場合にはsettings.py のplayers を変更してください.

## Selfplay

実際にコマを動かして遊ぶことができます.

## Alphabeta

アルファベータ法を用いて実装されたエージェントです. 現在, 評価関数はval_func があります.