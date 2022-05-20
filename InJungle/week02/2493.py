n = int(input())
towers = list(map(int, input().split()))
candidate_indices = []
answers = [-1] * n

for index, tower in enumerate(towers):

    while len(candidate_indices) > 0 and tower > towers[candidate_indices[-1]]:
        candidate_indices.pop()

    if len(candidate_indices) > 0:
        answers[index] = candidate_indices[-1]

    candidate_indices.append(index)

for answer in answers:
    print(answer + 1, end=" ")
