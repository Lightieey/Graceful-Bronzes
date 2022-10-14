#커트라인 문제
N, K = map(int, input().split()) #N = 응시자 수, K = 상받는 사람 수

score_list = list(map(int, input().split()))
score_list.sort(reverse=True) #내림차순으로 정렬
print(score_list[K-1])