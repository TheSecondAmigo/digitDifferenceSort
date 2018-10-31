#!/usr/bin/env python3

"""
https://app.codesignal.com/arcade/code-arcade/sorting-outpost/2SFFWqkhkqC7mMBse

Given an array of integers, sort its elements by the difference of their largest
and smallest digits. In the case of a tie, that with the larger index in the
array should come first.

Example

For a = [152, 23, 7, 887, 243], the output should be
digitDifferenceSort(a) = [7, 887, 23, 243, 152].

Here are the differences of all the numbers:

152: difference = 5 - 1 = 4;
23: difference = 3 - 2 = 1;
7: difference = 7 - 7 = 0;
887: difference = 8 - 7 = 1;
243: difference = 4 - 2 = 2.
23 and 887 have the same difference, but 887 goes after 23 in a, so in the
sorted array it comes first.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer a

An array of integers.

Guaranteed constraints:
0 ≤ sequence.length ≤ 104,
1 ≤ sequence[i] ≤ 105.

[output] array.integer

Array a sorted as described above.


"""


def digitDifferenceSort(a):

    slist = list()

    for ind, item in enumerate(a):
        slist.append((int(max(str(item))) - int(min(str(item))), len(a) - ind, item))

    slist.sort()
    # print(slist)

    return [item[2] for item in slist]


if __name__ == "__main__":

    a1 = [152, 23, 7, 887, 243]
    exp1 = [7, 887, 23, 243, 152]

    tests = [(a1, exp1)]

    for a, exp in tests:
        print(f"a = {a}")
        rc = digitDifferenceSort(a)
        print(f"exp = {exp}")
        print(f"rc  = {rc}")
        print("{}".format(exp == rc))

