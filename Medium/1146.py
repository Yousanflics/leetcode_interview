# Snapshot Array

import bisect

class SnapshotArray:
    # 元组中 0 位置是 snap_id 而 1 位置是 val
    def __init__(self, length: int):
        self.arr = [[(0, 0)] for _ in range(length)]
        self.snap_id = 0
    
    def set(self, index: int, val: int) -> None:
        if self.arr[index][-1][0] == self.snap_id:
            self.arr[index][-1] = (self.snap_id, val)
        else:
            self.arr[index].append((self.snap_id, val))

    def snap(self) -> int:
        current_id = self.snap_id
        self.snap_id += 1
        return current_id

    # arr 中的 snap_id 是有序递增的
    def get(self, index: int, snap_id: int) -> int:
        history = self.arr[index]
        left, right = 0, len(history) - 1
        pos = bisect.bisect_right(history, (snap_id, float('inf'))) - 1
        return history[pos][1]
