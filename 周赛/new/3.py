from typing import List
import collections


class DetectSquares:

    def __init__(self):
        self.cnt = collections.Counter()


    def add(self, point: List[int]) -> None:
        self.cnt[(point[0], point[1])] += 1


    def count(self, point: List[int]) -> int:
        x, y = point
        ans = 0
        for xi, yi in self.cnt:
            if abs(xi - x) == abs(yi - y) and xi != x:
                if (xi, y) in self.cnt and (x, yi) in self.cnt:
                    ans += self.cnt[(xi, yi)] * self.cnt[(xi, y)] * self.cnt[(x, yi)]
        return ans

def test():
    d = DetectSquares()
    d.add([3, 10])
    d.add([11, 2])
    d.add([3, 2])
    print(d.count([11, 10]))
    print(d.count([14, 8]))
    d.add([11, 2])
    print(d.count([11, 10]))
    # ["DetectSquares", "add", "add", "add", "count", "add", "add", "add", "count", "add", "add", "add", "count", "add",
    #  "add", "add", "count", "add", "add", "add", "count", "add", "add", "add", "count", "add", "add", "add", "count",
    #  "add", "add", "add", "count", "add", "add", "add", "count", "add", "add", "add", "count", "add", "add", "add",
    #  "count"]
    # [[], [[419, 351]], [[798, 351]], [[798, 730]], [[419, 730]], [[998, 1]], [[0, 999]], [[998, 999]], [[0, 1]],
    #  [[226, 561]], [[269, 561]], [[226, 604]], [[269, 604]], [[200, 274]], [[200, 793]], [[719, 793]], [[719, 274]],
    #  [[995, 99]], [[146, 948]], [[146, 99]], [[995, 948]], [[420, 16]], [[962, 558]], [[420, 558]], [[962, 16]],
    #  [[217, 833]], [[945, 105]], [[217, 105]], [[945, 833]], [[26, 977]], [[26, 7]], [[996, 7]], [[996, 977]],
    #  [[96, 38]], [[96, 483]], [[541, 483]], [[541, 38]], [[38, 924]], [[961, 1]], [[961, 924]], [[38, 1]], [[438, 609]],
    #  [[818, 609]], [[818, 229]], [[438, 229]]]
    # [null, null, null, null, 1, null, null, null, 1, null, null, null, 1, null, null, null, 1, null, null, null, 1,
    #  null, null, null, 1, null, null, null, 1, null, null, null, 1, null, null, null, 1, null, null, null, 1, null,
    #  null, null, 1]
    d.add([419, 351])
    d.add([798, 351])
    d.add([798, 730])
    print(d.count([419, 730]))

if __name__ == '__main__':
    test()