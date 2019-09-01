from random import shuffle

def insertion_sort(xs):
    for i in range(1, len(xs)):
        counter = 0
        for j in reversed(range(i)):
            index = i - counter
            if xs[index] < xs[j]:
                xs[index], xs[j] = xs[j], xs[index]
            else:
                break
            counter += 1
    return xs

xs = list(range(100))
xss = sorted(xs)

for i in range(10):
    shuffle(xs)
    if insertion_sort(xs) != xss:
        print('Tests failed!')
        break
else:
    print('Tests passed!')


