import A

print('top-level B.py')
A.func()

if __name__ == '__main__':
    print('B 가 시랭')
else:
    print('B 가 임포트')