def binary_search(score_list, minimun_score):
    left = 0
    right = len(score_list) - 1
    mx_passing = 0
    
    if len(score_list) < 2:
        for i in score_list:
            if i >= minimun_score:
                mx_passing += 1
    else:    
        while left <= right:
            mid = (left + right) // 2

            if score_list[mid] < minimun_score:
                left = mid + 1
            else:
                right = mid - 1
                if mx_passing < len(score_list) - mid:
                    mx_passing = len(score_list) - mid

    return mx_passing


def solution(info, query):
    answer = []
    people_info = dict()
    languages = ["cpp", "java", "python"]
    positions = ["backend", "frontend"]
    careers = ["junior", "senior"]
    soulfoods = ["chicken", "pizza"]

    for i in languages:
        keys = [0, 0, 0, 0]
        keys[0] = i
        for j in positions:
            keys[1] = j
            for k in careers:
                keys[2] = k
                for l in soulfoods:
                    keys[3] = l
                    people_info[''.join(keys)] = []

    for person in info:
        info_result = ''
        language, position, career, soulfood, score = person.split()
        info_result = language + position + career + soulfood
        people_info[info_result].append(int(score))
        people_info[info_result].sort()

    for temp in query:
        q = temp.split()
        minimun_score = int(q[7])
        requirements = []
        parsing_queries = [0, 0, 0, 0]

        if q[0] == '-':
            parsing_queries[0] = languages
        else:
            parsing_queries[0] = [q[0]]
        if q[2] == '-':
            parsing_queries[1] = positions
        else:
            parsing_queries[1] = [q[2]]
        if q[4] == '-':
            parsing_queries[2] = careers
        else:
            parsing_queries[2] = [q[4]]
        if q[6] == '-':
            parsing_queries[3] = soulfoods
        else:
            parsing_queries[3] = [q[6]]

        for lan in parsing_queries[0]:
            for pos in parsing_queries[1]:
                for car in parsing_queries[2]:
                    for food in parsing_queries[3]:
                        requirements.append(lan + pos + car + food)
        passing = 0
        for key in requirements:
            passing += binary_search(people_info[key], minimun_score)
        answer.append(passing)

    return answer