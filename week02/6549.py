def get_max_blocks_area(blocks, left, right):
    if left == right:
        return blocks[left]

    mid = (left + right) // 2

    left_blocks_max = get_max_blocks_area(blocks, left, mid)
    right_blocks_max = get_max_blocks_area(blocks, mid + 1, right)

    connected_left = mid
    connected_right = mid + 1

    connected_min_height = min(blocks[connected_left], blocks[connected_right])
    connected_max = connected_min_height * 2

    while left < connected_left or connected_right < right:
        left_outer_block = blocks[connected_left - 1] if left < connected_left else -1
        right_outer_block = blocks[connected_right + 1] if connected_right < right else -1

        if left_outer_block < right_outer_block:
            connected_right = connected_right + 1
            connected_min_height = min(connected_min_height, right_outer_block)
        else:
            connected_left = connected_left - 1
            connected_min_height = min(connected_min_height, left_outer_block)

        connected_max = max(connected_max, (connected_right - connected_left + 1) * connected_min_height)

    return max(connected_max, left_blocks_max, right_blocks_max)


while True:
    items = list(map(int, input().split()))

    if items[0] == 0:
        break

    print(get_max_blocks_area(items[1:], 0, items[0] - 1))
