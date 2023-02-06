def sift_up(heap, idx):
    if idx == 1:
        return idx
    parent_idx = idx // 2
    if heap[parent_idx] < heap[idx]:
        heap[parent_idx], heap[idx] = heap[idx], heap[parent_idx]
        idx = sift_up(heap, parent_idx)
    return idx


def main() -> int:
    sample = [-1, 12, 6, 8, 3, 15, 7]
    assert sift_up(sample, 5) == 1
    return 0


if __name__ == '__main__':
    main()
