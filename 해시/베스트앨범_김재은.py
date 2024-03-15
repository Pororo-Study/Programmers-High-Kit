def solution(genres, plays):

    #genres별 재생횟수 확인
    set_genres = set(genres)
    dict_plays = {}
    for set_genre in set_genres:
        tot_plays = 0
        for genre, play in zip(genres, plays):
            if genre == set_genre:
                tot_plays += play
        dict_plays[set_genre] = tot_plays

    #수록 순서 정렬
    sorted_plays = sorted(dict_plays.items(), key = lambda item: item[1], reverse = True)

    #장르별 고유번호와 재생회수를 묶어서 재생회수로 내림차순 정렬
    sorted_list = []
    for i, (genre, play) in enumerate(zip(genres,plays)):
        sorted_list.append([genre, i, play])
    sorted_list = sorted(sorted_list, key = lambda x: x[2], reverse=True)

    #장르별로 가장 많이 재생된 노래 출력
    answer = []
    for seq_genre, _ in sorted_plays:
        #두 개이상 체크
        num = 0
        for genre, i, _ in sorted_list:
            if genre == seq_genre:
                answer.append(i)
                num += 1

            if num >= 2:
                break


    return answer