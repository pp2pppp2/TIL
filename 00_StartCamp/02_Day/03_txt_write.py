#1. 파일 쓰기 (옛날 방식)

f = open('ssafy.txt', 'w')
for i in range(10):
    f.write(f'This is line{i}.\n')
f.close()