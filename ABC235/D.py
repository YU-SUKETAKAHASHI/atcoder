A , N = map(int, input().split())

# Aの乗数にすれば勝ち
# 実行できる操作は２種類

# 変化させられない場合 : aの桁数がNの桁数以上で、

# まずA乗を繰り返して黒板の数を10以上にする
# その後、どちらかの操作をする
#  1.さらにA乗する
#  2.末尾の数字を先頭に移動させる


# 桁数を小さくすることはできないので、通り過ぎてしまったらアウト

x = 1
action = 0
# while not x>10:
#     x *= A
#     action += 1

# NがAの倍数でなければどこかで処理2をしている
# NがAの倍数でなければその前の処理は処理2で確定
# 一度処理2を実行したら次は処理1をする
# 処理の途中でAのn乗の形にできるならば、処理2をする

A_factorials = [A**i for i in range(22)]


pre_action = 0
while True:
    # print(N)
    if N%A != 0:
        # 処理2を実行できなかったら詰みなので終了
        if N<10 or str(N)[-1]==0:
            exit(print(-1))

        # 二回連続処理2をしたら無限ループなので終了
        # if pre_action==2:
        #     exit(print(-1))

        # print('shori2')

        N = int(str(N)[-1]+str(N)[:-1])
        action += 1
        # pre_action = 2



        # print('action', action)


    else:

        if int(str(N)[-1]+str(N)[:-1]) in A_factorials:
            action += A_factorials.index(int(str(N)[-1]+str(N)[:-1]))
            exit(print(action))
        # print('shori1')
        N //= A
        action += 1
        pre_action = 1

        # print('action', action)

