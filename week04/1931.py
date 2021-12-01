import sys

input_meetings = []
meetings = []

for _ in range(int(sys.stdin.readline())):
    start, end = map(int, sys.stdin.readline().split())
    input_meetings.append((end, start))

input_meetings.sort()

for meeting in input_meetings:
    meetings.append({
        'start': meeting[1],
        'end': meeting[0]
    })

stack = []

for meeting in meetings:
    if len(stack) == 0:
        stack.append(meeting)
    else:
        if stack[-1]['end'] <= meeting['start']:
            stack.append(meeting)

print(len(stack))
