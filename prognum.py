#再帰的な関数を利用してフィボナッチ数列を実装する１
def fibo(x):
    if x == 1:
        return 1
    if x == 2:
        return 1
    if x >= 3:
        return fibo(x-1) + fibo(x-2)
