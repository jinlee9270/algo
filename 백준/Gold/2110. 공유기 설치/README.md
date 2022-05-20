# [Gold V] 공유기 설치 - 2110 

[문제 링크](https://www.acmicpc.net/problem/2110)

### 문제 설명
- 파라메트릭 서치로 해결할 수 있는 문제
- 이런 유형의 문제는 어떤 것을 이분 탐색해서 답을 찾을 수 있을지를 먼저 생각해야 한다.
- 본 문제에서는 가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치하려고 하고 C개의 공유기를 N개의 집들 중 적당히 모두 설치하여 가장 인접한 두 공유기 사이의 거리가 최대일때를 찾아야한다.

>`최소를 최대로` or `최대를 최소`로 라는 키워드는 대부분 파라메트릭 서치가 적용된다.

### 코드_1
```python
n, c = map(int, input().split())

home = []
for i in range(0, n):
    home.append(int(input()))
home.sort()

left = 0
right = home[-1]
dis = 0
MX_dis = 0
while left <= right:
    start_point = home[0]
    wifi = 1
    dis = (left + right) // 2

    for i in range(0, n):
        if home[i] - start_point >= dis:
            start_point = home[i]
            wifi = wifi + 1

    if wifi >= c:
        left = dis + 1
        if MX_dis < dis:
            MX_dis = dis
    else:
        right = dis - 1

print(MX_dis)
```
### 코드_2(left, right 범위 수정)
```python
n, c = map(int, input().split())

home = []
for i in range(0, n):
    home.append(int(input()))
home.sort()

left = 1
right = home[-1] - 1
dis = 0
MX_dis = 0
while left <= right:
    start_point = home[0]
    wifi = 1
    dis = (left + right) // 2

    for i in range(0, n):
        if home[i] - start_point >= dis:
            start_point = home[i]
            wifi = wifi + 1

    if wifi >= c:
        left = dis + 1
        if MX_dis < dis:
            MX_dis = dis
    else:
        right = dis - 1
print(MX_dis)
```
- 이전에 포스팅한 같은 유형의 문제인 랜선자르기 문제에서 변수가 가지는 의미에 대해서 서술한 바 있다.[(최소 시작점 설정을 왜 0으로 하면 안되는가)](https://velog.io/@jinlee/%EB%B0%B1%EC%A4%80-%EB%9E%9C%EC%84%A0-%EC%9E%90%EB%A5%B4%EA%B8%B0) 여기서 이전에 이 문제를 풀었던 것이 생각나 의문이 발생했다.
- **코드_1과 코드_2 모두 정답처리 되었다.**
  - 최소 시작점을 0으로 두고 문제를 맞았었는데 이 문제에서 매개변수 탐색을 해야 하는 최소 거리는 1이다.(같은 곳에는 설치하지 않으니 공유기가 설치된 두 집 사이 거리가 0이 될 수는 없다.)
  - 같은 의미로 최댓값은 설치할 수 있는 처음 집과 설치할 수 있는 마지막 집 사이의 거리다.
- 틀린 부분이 두 부분이나 있었는데 어떻게 맞을 수 있었을까?
  - 이 문제 같은 경우는 공유기가 설치 된 가장 인접한 두 집 사이의 거리가 dis(mid)값으로 설정되기 때문에 dis가 0이 되기 전에 답이 찾아졌다고 생각할 수 있다. 하지만 명확한 의미로의 변수 설정이 중요하다는 것을 배웠다. 
 
>변수의 역할과 의미에 대한 정의가 중요하다.

### 성능 요약

메모리: 127652 KB, 시간: 284 ms

### 분류

이분 탐색(binary_search), 매개 변수 탐색(parametric_search)

### 문제 설명

<p>도현이의 집 N개가 수직선 위에 있다. 각각의 집의 좌표는 x<sub>1</sub>, ..., x<sub>N</sub>이고, 집 여러개가 같은 좌표를 가지는 일은 없다.</p>

<p>도현이는 언제 어디서나 와이파이를 즐기기 위해서 집에 공유기 C개를 설치하려고 한다. 최대한 많은 곳에서 와이파이를 사용하려고 하기 때문에, 한 집에는 공유기를 하나만 설치할 수 있고, 가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치하려고 한다.</p>

<p>C개의 공유기를 N개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 집의 개수 N (2 ≤ N ≤ 200,000)과 공유기의 개수 C (2 ≤ C ≤ N)이 하나 이상의 빈 칸을 사이에 두고 주어진다. 둘째 줄부터 N개의 줄에는 집의 좌표를 나타내는 x<sub>i</sub> (0 ≤ x<sub>i</sub> ≤ 1,000,000,000)가 한 줄에 하나씩 주어진다.</p>

### 출력 

 <p>첫째 줄에 가장 인접한 두 공유기 사이의 최대 거리를 출력한다.</p>

