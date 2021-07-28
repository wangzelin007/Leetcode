def solution(A: int,B: int, C: int,D: int) -> int:
    ans = []
    s = [str(A), str(B), str(C), str(D)]
    def _process(s, i, ans):
        if i == 1 and s[0] > '2': return
        if i == 2 and s[0] == '2' and s[1] > '4': return
        if i == 3 and s[2] > '5': return
        if len(s) == i:
            ans.append(''.join(s))
            return
        visit = set()
        for j in range(i, len(s)):
            if s[j] not in visit:
                visit.add(s[j])
                s[i], s[j] = s[j], s[i]
                _process(s, i+1, ans)
                s[i], s[j] = s[j], s[i]

    _process(s, 0, ans)
    return len(ans)

def test():
    A = 1; B = 8; C = 3; D = 2
    assert solution(A, B, C, D) == 6
    A = 2; B = 3; C = 3; D = 2
    assert solution(A, B, C, D) == 3
    A = 6; B = 2; C = 4; D = 7
    assert solution(A, B, C, D) == 0

if __name__ == '__main__':
    test()