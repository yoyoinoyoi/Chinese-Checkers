# Settings

# 実装済み
# Selfplay: ["selfplay"]
# Alphabeta: ["alphabeta", depth<int>, val_func<str>]
    # depth: 探索の深さ(何手先を読むか)
    # val_func: 評価関数(現在はfunc1 のみ)
# MCTS: ["mcts", thinking_time<float>, val<str>]
    # thinking_time: 思考時間[s]
    # val: 評価指標(現在はUCB1 のみ. "-"で指定してください)

# 未実装
# RAVE: ["RAVE", thinging_time<float>, val<str>]

# example
# players = [["selfplay"], ["alphabeta", 4, "func1"]]
# players の長さは2, 3, 6のいずれかで指定してください

players = [["alphabeta", 4, "func1"], ["mcts", 10.0, "-"]]