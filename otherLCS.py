ans_map = {}
visit_map = {}


# compares two strings and return the longer one
def max_string(a, b):
    if len(a) > len(b):
        return a
    return b


def fix(ans, w):
    c = 0
    prev = 0
    for x in range(len(ans)):
        for y in range(prev, len(w)):
            if ans[x] == w[y]:
                c += 1
                prev = y + 1
                break
    if c == len(ans):
        return False
    return True


# recursive function that calculates the lcs and returns it
def lcs(v, w):
    global ans_map, visit_map
    len_v = len(v)
    len_w = len(w)

    if len_v == 0 or len_w == 0:
        return ""

    pair = (v, w)

    try:
        ans_map[pair]
    except KeyError:
        ans_map[pair] = ""

    try:
        if visit_map[pair] == 1:
            return ans_map[pair]
    except KeyError:
        visit_map[pair] = 1

    if v[len_v - 1] == w[len_w - 1]:
        ans_map[pair] += v[len_v - 1]
        v = v[:-1]
        w = w[:-1]
        ans_map[pair] += lcs(v, w)
        return ans_map[pair]

    ans_map[pair] += max_string(lcs(v[:-1], w), lcs(v, w[:-1]))

    return ans_map[pair]


def run_other_lcs(v, w):
    ans = lcs(v, w)
    ans = ans[::-1]
    print(ans)
