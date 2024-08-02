a,b,c,d = list(map(int, input().split()))

v = 'Vasya'
m = 'Misha'
t = 'Tie'

def formula(p, time):
    return max( 3 * p / 10, p - (p / 250 ) * time)

vasya = formula(b, d)
misha = formula(a, c)

if vasya > misha:
    print(v)
elif vasya < misha:
    print(m)
else:
    print(t)