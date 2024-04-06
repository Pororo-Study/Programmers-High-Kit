def solution(array, commands):
    ans = []
    for i, j, k in commands:
        tmp = array[i-1:j]
        tmp.sort()
        ans.append(tmp[k-1])
    return ans