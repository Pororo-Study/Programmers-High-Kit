from collections import defaultdict

def solution(genres, plays):
    answer = []
    
    dic1 = defaultdict(int)     # key에 장르, value에 재생횟수 합계를 저장
    dic2 = defaultdict(list)    # key에 장르, value에 '(재생횟수, 고유번호)로 이루어진 리스트'를 저장
    
    # 딕셔너리에 데이터 저장
    for i in range(len(genres)):
        dic1[genres[i]] += plays[i]
        dic2[genres[i]].append((plays[i], i))

    # 장르의 재생횟수 합계로 정렬
    genre_list = []             # (재생횟수 합계, 장르)로 이루어진 리스트
    for genre in dic1.keys():
        genre_list.append((dic1[genre], genre)) # (재생횟수 합계, 장르)
    genre_list.sort(reverse=True)               # 재생횟수 합계가 큰 순서대로 정렬
    
    # 각 장르마다 dic2의 value값을 정렬
    for _, genre in genre_list:
        # 장르에 곡이 2개 이상일 경우
        if len(dic2[genre]) > 1:
            dic2[genre].sort(key=lambda x: (-x[0], x[1]))   # 재생횟수가 크고, 고유번호가 낮은 순서로 정렬
            # 2개만 answer에 저장
            for i in range(2):
                answer.append(dic2[genre][i][1])
        # 장르에 곡이 1개일 경우 answer에 저장
        else:
            answer.append(dic2[genre][0][1])
                
    return answer