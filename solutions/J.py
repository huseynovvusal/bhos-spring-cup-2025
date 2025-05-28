BLOCK_START = [0 for _ in range(1000)]
BLOCK_END = [0 for _ in range(1000)]
BLOCK_XOR = [0 for _ in range(1000)]
BLOCK_ID = [0 for _ in range(10**6 + 100)]
BLOCK_FREQ = [{} for _ in range(1000)]

prefix_xor = [0 for _ in range(10**5 + 10)]

def build_sqrt_decomposition(n):
    block_size = 1
    while block_size * block_size < n:
        block_size += 1

    num_blocks = 0
    for i in range(0, n, block_size):
        BLOCK_START[num_blocks] = i
        BLOCK_END[num_blocks] = i + block_size - 1
        num_blocks += 1
    BLOCK_END[num_blocks - 1] = n - 1

    for block in range(num_blocks):
        BLOCK_XOR[block] = 0
        for i in range(BLOCK_START[block], BLOCK_END[block] + 1):
            val = prefix_xor[i]
            BLOCK_FREQ[block][val] = BLOCK_FREQ[block].get(val, 0) + 1
            BLOCK_ID[i] = block

    return block_size

n, q = map(int, input().split())
arr = list(map(int, input().split()))

current_xor = 0
for i in range(n):
    current_xor ^= arr[i]
    prefix_xor[i] = current_xor

block_size = build_sqrt_decomposition(n)

for _ in range(q):
    op, index, value = map(int, input().split())
    index -= 1

    if op == 1:
        block = BLOCK_ID[index]
        xor_diff = arr[index] ^ value
        arr[index] = value

        for j in range(index, BLOCK_END[block] + 1):
            BLOCK_FREQ[block][prefix_xor[j]] -= 1
            prefix_xor[j] ^= xor_diff
            BLOCK_FREQ[block][prefix_xor[j]] = BLOCK_FREQ[block].get(prefix_xor[j], 0) + 1

        for b in range(block + 1, block_size + 1):
            BLOCK_XOR[b] ^= xor_diff

    else:
        block = BLOCK_ID[index]
        count = 0

        for j in range(BLOCK_START[block], index + 1):
            if prefix_xor[j] ^ BLOCK_XOR[block] == value:
                count += 1

        for b in range(0, block):
            target = value ^ BLOCK_XOR[b]
            count += BLOCK_FREQ[b].get(target, 0)

        print(count)
