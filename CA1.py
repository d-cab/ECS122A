n, d = map(int, input().split())
a = list(map(int, input().split()))

for i in range(0, n):
    ans = 0
    # check to the left and right until distance to next node is greater than d
    # need to check edges and prevent out of bounds errors
    for j in range (0,n):
        if ( (a[i] - a[i-j]) <= d):
            ans += 1
        else:
            break

    for j in range (0,n):
        if ( (a[i] - a[i+j]) <= d):
            ans += 1
        else:
            break

    print(ans)
ans = 0
# Compute `ans` as the maximum number of cities that can be covered by a single tower
print(ans)