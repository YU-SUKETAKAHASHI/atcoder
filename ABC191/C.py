H, W = map(int, input().split())
S = [list(map(int, input().split())) for _ in range(H)]

# 頂点の位置関係がわかればいいのかな
# 四方のますの関係だけに注目して機械的に処理したい

# 左右が黒だったら頂点じゃない
# 上下が黒だったら頂点じゃない

# 一方だけが黒なら+3
# 方向違いの二方が黒なら+1
# 三方が黒なら+2

# ......
# .#.#..
# .####.
# .####.
# .###..
# ..#...
# ......

