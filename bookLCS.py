# returns recurrence for 's' matrix
def cost(s, v, w, i, j):
    if v[i - 1] == w[j - 1]:
        return s[i - 1][j - 1] + 1
    else:
        return max(s[i - 1][j], s[i][j - 1])


# returns recurrence for 'b' matrix
def direction(s, i, j):
    if s[i][j] == s[i - 1][j]:
        return "up"
    elif s[i][j] == s[i][j - 1]:
        return "left"
    else:
        return "diagonal"


# calculates cost matrix and returns direction matrix
def lcs(v, w):
    len_v = len(v)
    len_w = len(w)
    s = [[0 for i in range(len_w + 1)] for j in range(len_v + 1)]
    b = [[0 for i in range(len_w + 1)] for j in range(len_v + 1)]

    for i in range(1, len_v + 1):
        for j in range(1, len_w + 1):
            s[i][j] = cost(s, v, w, i, j)
            b[i][j] = direction(s, i, j)

    return b


# finds the lcs in the direction matrix
def print_lcs(b, v, i, j):
    if i == 0 or j == 0:
        return
    if b[i][j] == "diagonal":
        print_lcs(b, v, i - 1, j - 1)
        print(v[i - 1], end="")
    else:
        if b[i][j] == "up":
            print_lcs(b, v, i - 1, j)
        else:
            print_lcs(b, v, i, j - 1)


def run_book_lcs(v, w):
    b = lcs(v, w)
    print_lcs(b, v, len(v), len(w))
    print()
