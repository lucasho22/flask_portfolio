def swap(a, b):
    arranged_lst = []
    lst = [a, b]
    while len(lst) > 0:
        smallest = min(lst)
        arranged_lst.append(smallest)
        lst.remove(smallest)
    return arranged_lst[0], arranged_lst[1]

def test_swap():
    a = int(input("Enter first age: "))
    b = int(input("Enter second age: "))
    x, y = swap(a, b)
    print(x, y)