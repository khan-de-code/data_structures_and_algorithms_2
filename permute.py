def permute(iterable):
    pool = tuple(iterable)
    iterable_length = len(pool)

    indices = list(range(iterable_length))
    cycles = list(range(iterable_length, 0, -1))
    yield tuple(pool[i] for i in indices[:iterable_length])
    while True:
        for i in reversed(range(iterable_length)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = iterable_length - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:iterable_length])
                break
        else:
            return
