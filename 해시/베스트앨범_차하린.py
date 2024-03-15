def solution(genres, plays):
    ans = []
    total = {} # {장르: 총 재생 횟수}
    genres_plays = {} # {장르: [(플레이 횟수, 고유번호)]}

    for i in range(len(genres)):
        total[genres[i]] = total.get(genres[i], 0) + plays[i]
        genres_plays[genres[i]] = genres_plays.get(genres[i], []) + [(plays[i], i)]

	# 재생 횟수 내림차순으로 장르별 정렬
    genSort = sorted(total.items(), key=lambda x: x[1], reverse=True)

	# 재생 횟수 내림차순, 인덱스 오름차순 정렬
    for (genre, totalPlay) in genSort:
        genres_plays[genre] = sorted(genres_plays[genre], key=lambda x: (-x[0], x[1]))
        ans += [idx for (play, idx) in genres_plays[genre][:2]]

    return ans