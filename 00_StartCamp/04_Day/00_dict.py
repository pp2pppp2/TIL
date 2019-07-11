#1. 만들기
lunch = {
    '중국집':'02'
}

lunch = dict( 중국집 = '02')

#2. 내용추가
lunch ['분식집'] = '031'

idol ={
    'bts':{
        '지민': 24,
        'RM' : 25
    }
}
#3. 가져오기
# print(idol['bts']['RM'])
# print(idol.get('bts').get('RM'))

#4. 딕셔너리 반복문 활용하기

#4-1 기본활용
# for key in lunch:
#     print(key)
#     print(lunch[key])

#4-2. .items() - key , value 모두 가져오기

# for key,item in lunch.items():
#     print(key,item)

#4-3 .values() -value 만 가져오기

# for value in lunch.values():
#     print(value)

#4-4 .kays() - key 만 가져오기

for key in lunch.keys():
    print(key)