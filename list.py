def remove_evenindex(ln):
    del ln[0:len(ln):2]
    return ln
print(remove_evenindex(['a', 'b', 'c', 'd', 'e', 'f', 'g']) == ['b', 'd', 'f'] )
print(remove_evenindex([1, 2, 3, 4, 5]) == [2, 4])