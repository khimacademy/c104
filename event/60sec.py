import time

msg = {
        0: 'Perfect!',
        1: 'Great!',
        2: 'Good!',
        3: 'Not Bad!'
        }

input('시작하려면 엔터를 누르세요.')
start = time.time()

input('멈추려면 엔터를 누르세요.')
end = time.time()

elapsed = 60 - int(end - start)
print(elapsed, '초')

print(msg.get(abs(elapsed) // 5, '꽝-.-;;'))

