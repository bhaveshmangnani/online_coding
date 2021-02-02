#URL: https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
def minimumSwaps(n, arr):
    i = 0
    cnt = 0
    while i<n:
        if arr[i]!=i+1:
            num = arr[i]
            temp = arr[num-1]
            arr[num-1] = arr[i]
            arr[i] = temp
            cnt+=1
        else:
            i+=1
    return cnt
