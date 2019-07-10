"""
문제 1 . 문자열을 입력받아 문자열의 첫 글자와 마지막 글자를 출력하는 만드세요
"""

# str_1 = input('문자를 입력하세요 : ')

# print(str_1[0])

# len_str = len(str_1)

# print(str_1[len_str-1])

# print(str_1[-1])

# str_2 = list(str_1)

# str_2.reverse()

# print(str_2[0])

"""
문제 2. 자연수 n 이 주어질 때 , 1부터 n 까지 한 줄에 하나씩 출력하는 프로그램을 만드세요.
"""

# n = int(input('숫자를 입력하세요 : ')) 
# for i in range(1,n+1):
#     print(i)

"""
문제 3. 숫자를 입력받아 짝수/홀수를 구분하는 코드를 작성하세요
"""

# cnt = 0
# while cnt<5:
#     try :
#         number = int(input('숫자를 입력하세요 : '))
#         cnt +=1
#         if number % 2 == 0:
#             print('짝')
#         else :
#             print('홀')
            
#     except ValueError:
#         print('숫자를 입력하라구요.')


"""
문제 4 . 표준 입력으로 국어, 영어, 수학, 과학 점수가 입력됩니다.
국어는 90점 이상
영어는 80점 초과,
수학은 85점 초과,
과학은 80점 이상일 때 합격이라고 정했습니다.
(한 과목이라도 조건에 만족하지 않으면 불합격)
다음 코드를 완성하여 합격이면 True , 불합격이면 False가 출력되도록 작성하세요.
"""

# kor = int(input ('국어 : '))
# eng = int(input ('영어 : '))
# mat = int(input ('수학 : '))
# sci = int(input ('과학 : '))

# if kor >= 90 and eng > 80 and mat > 85 and sci >= 80 :
#     print('True')
# else :
#     print('false')

"""
문제 5 . 표준 입력으로 물품 가격 여러 개가 문자열 한 줄로 입력되고, 각 가격은 ;(세미콜론)으로 구분되어 있습니다.
입력된 가격을 높은 가격순으로 한줄에 하나씩 출력하는 프로그램을 만드세요.
입력예시 : 30000; 2000; 40000
출력예시
40000
30000
2000
"""

prices = input('물품 가격을 입력하세요 : ')

prices_list = prices.split(';')
boxs=[]
for box in prices_list:
    boxs.append(int(box))
boxs.sort(reverse=True)
for price in boxs:
    print (price)
