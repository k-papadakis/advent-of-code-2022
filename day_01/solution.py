import heapq


def read_data():
    with open('input.txt') as f:
        items = []
        for line in f:
            if line == '\n':
                yield items
                items = []
            else:
                items.append(int(line))
        yield items


def max_sum():
    return max(map(sum, read_data()))


def sum_top3_sum():
    heap = []
    for s in map(sum, read_data()):
        if len(heap) < 3:
            heapq.heappush(heap, s)
        else:
            heapq.heappushpop(heap, s)
    return sum(heap)


def main():
    part1 = max_sum()
    part2 = sum_top3_sum()
    print(f'part1: {part1}\npart2: {part2}')


if __name__ == '__main__':
    main()
