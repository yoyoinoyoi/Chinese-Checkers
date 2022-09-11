# Settings

# 
# Selfplay: ["selfplay"]
# Alphabeta: ["alphabeta", depth<int>, val_func<str>]
# MCTS: ["mcts", thinking_time<float>, val<str>]
# RAVE: ["RAVE", thinging_time<float>, val<str>]
# example
# players = [["selfplay"], ["alphabeta", 4, "func1"]]

players = [["alphabeta", 4, "func1"], ["mcts", 10.0, "-"]]