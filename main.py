# Problem 75:
#     Singular Integer Right Triangles
#
# Description:
#     It turns out that 12 cm is the smallest length of wire that can be bent
#       to form an integer sided right angle triangle in exactly one way,
#       but there are many more examples.
#
#         12 cm: ( 3,  4,  5)
#         24 cm: ( 6,  8, 10)
#         30 cm: ( 5, 12, 13)
#         36 cm: ( 9, 12, 15)
#         40 cm: ( 8, 15, 17)
#         48 cm: (12, 16, 20)
#
#     In contrast, some lengths of wire, like 20 cm,
#       cannot be bent to form an integer sided right angle triangle,
#       and other lengths allow more than one solution to be found;
#       for example, using 120 cm it is possible to form exactly three different integer sided right angle triangles.
#
#         120 cm: (30, 40, 50), (20, 48, 52), (24, 45, 51)
#
#     Given that L is the length of the wire,
#       for how many values of L ≤ 1,500,000 can exactly one integer sided right angle triangle be formed?

from collections import defaultdict
from math import floor, gcd, sqrt


def main(p_max: int) -> int:
    """
    Returns the number of perimeters `p` ≤ `p_max`,
      from which exactly one integer right triangle can be formed.

    Args:
        p_max (int): Natural number

    Returns:
        (int): Count of `p` ≤ `p_max`, such that `p` is the perimeter of exactly one integer right triangle.

    Raises:
        AssertError: if incorrect args are given
    """
    assert type(p_max) == int and p_max > 0

    # Idea:
    #     Generate primitive triples using Euclid's formula.
    #     For arbitrary integers `m` and `n`,
    #       where m > n, gcd(m,n) = 1, and one of `m` and `n` is even,
    #       the following produces side lengths of a primitive integer right triangle:
    #         a = m^2 - n^2
    #         b = 2*m*n
    #         c = m^2 + n^2
    #
    #     Also, given a primitive triple,
    #       we can obtain the non-primitive triples by simply multiplying by some multiplier `k`.
    #
    #     We can establish a rough bound for `m` since we know c = m^2 + n^2.
    #     c is bound to be at most `p_max`.
    #     Estimating c to be 2*m^2, we then get the upper bound of c = sqrt(p_max/2).

    # Keep track of number of triangles formed per perimeter `p`
    triangle_counts = defaultdict(lambda: 0)
    count = 0

    m_max = floor(sqrt(p_max/2)) + 1
    for m in range(2, m_max):
        for n in range(1, m):
            if (m+n) % 2 == 1 and gcd(m, n) == 1:
                m2 = m ** 2
                n2 = n ** 2
                a = m2 - n2
                b = 2 * m * n
                c = m2 + n2
                p_primitive = a + b + c
                p = p_primitive
                while p <= p_max:
                    triangle_counts[p] += 1
                    pc = triangle_counts[p]
                    if pc == 1:
                        count += 1
                    elif pc == 2:
                        count -= 1
                    p += p_primitive

    return count


if __name__ == '__main__':
    maximum_perimeter = int(input('Enter a natural number: '))
    singular_triangle_count = main(maximum_perimeter)
    print('Number of distinct perimeters (≤ {}) forming exactly one integer right triangle:'.format(maximum_perimeter))
    print('  {}'.format(singular_triangle_count))
