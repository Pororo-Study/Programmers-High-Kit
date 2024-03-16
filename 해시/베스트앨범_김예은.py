from collections import defaultdict
def solution(genres, plays):
    answer = []
    
    count = defaultdict(dict)
    genre_count = defaultdict(dict)
    
    # {고유번호 : 재생횟수}
    for i in range(len(plays)):
        count[i] = plays[i]
        
    # {장르 : {고유번호: 재생횟수, 고유번호:재생횟수...}}
    for i in range(len(genres)):
        genre_count[genres[i]][i] = count[i]
        
    # 제일 많이 재생된 장르 순서         
    sd = sorted(genre_count, key = lambda x:sum(genre_count[x].values()), reverse=True)
    
    # 장르에서 많이 재생된 노래
    for s in sd:
        answer += sorted(genre_count[s], key = lambda x:genre_count[s][x], reverse=True)[:2]
        
    return answer
    

