def my_add(n, m):
    return n+m
def my_sub(n, m):
    return n-m
def my_mul(n, m):
    return n*m
def my_div(n, m):
    try:
        div = n/m
    except ZeroDivisionError:
        return '0으로는 나눌 수 없습니다.'