def regular_expression_matching(T, P):
    # Return whether the text string match the pattern
    return True

tc = int(input())
for _ in range(tc):
    T = input()
    P = input()
    result = regular_expression_matching(T, P)
    print('YES' if result else 'NO')