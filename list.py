"""
スライスを使って要素を削除
"""
def use_slice():
    def remove_evenindex(ln):
        del ln[0:len(ln):2]
        return ln
    print(remove_evenindex(['a', 'b', 'c', 'd', 'e', 'f', 'g']) == ['b', 'd', 'f'] )
    print(remove_evenindex([1, 2, 3, 4, 5]) == [2, 4])
# use_slice()

"""
多次元リスト
"""
def multidimensional():
    l = [['a', 'b', 'c'],
         ['d', 'e', 'f'],
         ['g', 'h', 'i']]

    newl = [l,l[1],l[1][0:2]]
    print(newl)

# multidimensional()

def slice_vertical():
    l = [['a', 'b', 'c'],
         ['d', 'e', 'f'],
         ['g', 'h', 'i']]

    # print(l[0:2][1])#縦を取り出せない

    # b,e,hを取り出す
    for i in range(len(l)):
        print(l[i][1])

# slice_vertical()

"""
max関数を自分で作る
"""
# data = [-1, -2, -3]
def max_data(d):
    n = d.pop(0)
    for i in d:
        if i > n:
            n = i
    return n

# print(max_data(data))

"""
sum関数
"""
def try_sum():
    data = [3, 4, 5]
    print(sum(data))

    n = 0
    for i in data:
        n = n + i
    print(n)

# try_sum()