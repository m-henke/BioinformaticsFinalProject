from bookLCS import run_book_lcs
from otherLCS import run_other_lcs
from sys import setrecursionlimit
import matplotlib.pyplot as plt
from time import perf_counter
from random import randint


setrecursionlimit(9999)


def get_test_values():
    while True:
        choice = int(input("1) use preselected values\n2) enter new values\n> "))
        if choice == 1:
            return 5, [10, 25, 50, 100, 250, 500, 1000]
        elif choice == 2:
            num_trials = int(input("enter the number of trials\n> "))
            lengths = input("enter the string lengths to test (10,50,100)\n> ").split(',')
            return num_trials, [int(length) for length in lengths]
        print("enter 1 or 2")


# generates two random strings of length length
def create_strings(length):
    letters = ['A', 'T', 'C', 'G']
    return "".join([letters[randint(0, len(letters) - 1)] for x in range(length)]), \
           "".join([letters[randint(0, len(letters) - 1)] for x in range(length)])


# runs the passed function and returns the time it took
def time_function(function, v, w):
    start = perf_counter()
    function(v, w)
    end = perf_counter()
    return end - start


# graphs the runtime results
def graph_results(o_res, b_res, lengths):
    fig, ax = plt.subplots()
    ax.plot(lengths, o_res, '--ro', label="Other LCS")
    ax.plot(lengths, b_res, '--bo', label="Book LCS")
    ax.set_title("Book vs Other LCS Algorithm")
    ax.set_xlabel("strings lengths")
    ax.set_ylabel("seconds")
    ax.set_xticks(lengths)
    ax.legend()
    plt.show()
    plt.close()


def main():
    num_trials, lengths = get_test_values()
    b_res = []
    o_res = []

    for x in range(len(lengths)):
        t1 = 0
        t2 = 0
        for y in range(num_trials):
            v, w = create_strings(lengths[x])
            print(f"v: {v}, w: {w}\n" if lengths[x] <= 10 else "", end="")
            t1 += time_function(run_other_lcs, v, w)
            t2 += time_function(run_book_lcs, v, w)
        o_res.append(float(t1 / num_trials))
        b_res.append(float(t2 / num_trials))

    graph_results(o_res, b_res, lengths)


if __name__ == "__main__":
    main()
