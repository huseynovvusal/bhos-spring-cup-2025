def max_segment_length(k, lengths):
    left = 1
    right = max(lengths)
    result = 0

    while left <= right:
        mid = (left + right) // 2
        count = sum(l // mid for l in lengths)

        if count >= k:
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    return result

n, k = map(int, input().split())
lengths = [int(input()) for _ in range(n)]

print(max_segment_length(k, lengths))
