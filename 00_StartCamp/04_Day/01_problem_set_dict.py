"""
Python dictionary 문제
"""

#1. 평균을 구하세요

# score = {
#     '수학' : 80,
#     '국어' : 90,
#     '음악' : 100
# }

# total_score = 0
# for subject_score in score.values():
#     total_score += subject_score

# average_score = total_score / len(score)

# # print(average_score)

scores = {
    'a' : {
        '수학' : 80,
        '국어' : 90,
        '음악' : 100
    },
    'b' : {
        '수학' : 80,
        '국어' : 90,
        '음악' : 100
    }
}
total_score = 0
length = 0

for key,person_score in scores.items():
    for subject_score in person_score.values():
        total_score += subject_score
        length += 1
    average_score = total_score / length
    print(f'{key} 반의 평균 점수는 {average_score}입니다.')\

#3. 도시별 최근 3일 온도입니다.

city = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9]
}

# #3-1. 도시별 최근 3일의 온도 평균은?
# temp = 0
# length = 0
# avtemp = 0

# for key,sub_temps in city.items():
#     temp = 0
#     length = 0
#     for sub_temp in sub_temps:
#         temp += sub_temp
#         length += 1
#     avtemp = temp / length
#     print(f'{key}의 평균 온도는 {avtemp} 입니다.')


# # #3-2. 도시 중 최근 3일 중에 가장 추웠던, 가장 더웠던 곳은?
# Min = ''
# Max = ''
# temp = 0
# length = 0
# min_temp = 0
# max_temp = 0
# for key,sub_temps in city.items():
#     for sub_temp in sub_temps:
#         if (min_temp > sub_temp):
#             Min = key
#             min_temp = sub_temp
#         if (max_temp < sub_temp):
#             Max = key
#             max_temp = sub_temp
# print(f'가장 추웠던 곳은 {Min}로 {min_temp}도 이구요 가장 더웠던 곳은 {Max}로 {max_temp}')
 

#3-3. 서울은 영상 2도였던 적이 있나요? -> ex . 네 있어요!

# for key,sub_temps in city.items():
#     temp_text = '아뇨 없는데요'
#     for sub_temp in sub_temps:
#         if (sub_temp == 2):
#             temp_text = '네 있어요'
#     print(f'{key}은 영상 2도 였던 적이 있나요?  -> {temp_text}')

