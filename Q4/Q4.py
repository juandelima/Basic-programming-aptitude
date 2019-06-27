def divide(a, b, k):
    cnt = 0
    if 1 <= a <= b and b < 10000:
        for i in range(a, b+1):
            if 1 <= k < 10000:
                if i % k == 0:
                    cnt += 1
    return cnt

def main():
    t = int(input())
    result = []
    if 1 <= t <= 100:
        for i in range(1, t+1):
            a = int(input())
            b = int(input())
            k = int(input())
            div = divide(a, b, k)
            result.append(div)
        for i in range(len(result)):
            print("Case %d: %d"%(i+1, result[i]))
if __name__ == "__main__":
    main()
