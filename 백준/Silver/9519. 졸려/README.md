# [Silver I] 졸려 - 9519 

[문제 링크](https://www.acmicpc.net/problem/9519) 

### 문제 설명
- 잘라서 만들어진 랜선의 갯수가 최소 k개는 될 때 길이의 최댓값을 구해야 하는 문제로 파라메트릭 서치로 해결 가능하다.
- 랜선의 길이로 존재할 수 있는 최솟값인 1을 left로 주어진 랜선의 길이 중 최댓값을 right로 설정하였다.
- 이 범위의 중간값부터 mid로 설정하여 생성될 수 있는 랜선의 길이가 최소 k개를 만족하는 left 범위를 mid + 1로 이동시킨다(컷팅할 길이를 증가시켜 봄). k보다 작은 경우는 right 범위를 mid - 1 로 이동시킨다(컷팅할 길이를 감소시켜 봄).

### 코드
```python
import sys

n, k = map(int, input().split())
lans = []

for _ in range(n):
    lans.append(int(sys.stdin.readline().rstrip()))

left = 1
right = max(lans)
max_length = 0

while left <= right:
    mid = (left + right) // 2
    cnt = 0

    for lan in lans:
        cnt = cnt + (lan // mid)

    if cnt < k:
        right = mid - 1
    else:
        if max_length < mid:
            max_length = mid
        left = mid + 1

print(max_length)
```
- 처음에는 `left`를 0으로 설정해서 `ZeroDivisionError`가 발생하였다.
  - 테스트 케이스로 `n = 1`, `k = 1`, `랜선에 1`을 넣으면 발생하는 것을 알았다.
  - 이때 **left는 0 + right 1 이기 때문에 mid 값은 0**이 된다.
- 답으로 도출해야 하는 것은 k개 이상의 랜선을 일정 길이로 만들 수 있을때 해당 길이의 최댓값을 구하려고 하는 것이기 때문에 0으로 설정한 것은 길이의 의미와도 맞지 않다. 따라서 나올 수 있는 길이의 최솟값은 1로 설정해야 한다.
  - 같은 유형의 문제인 [2110번 공유기설치](https://www.acmicpc.net/problem/2110)는 `left`를 0으로 두고 풀어서 맞았었는데 [이 문제 해설은 여기서](https://github.com/jinlee9270/algo/blob/master/%EB%B0%B1%EC%A4%80/Gold/2110.%E2%80%85%EA%B3%B5%EC%9C%A0%EA%B8%B0%E2%80%85%EC%84%A4%EC%B9%98/README.md)

### 성능 요약

메모리: 30840 KB, 시간: 300 ms

### 분류

구현(implementation), 수학(math), 시뮬레이션(simulation), 문자열(string)

