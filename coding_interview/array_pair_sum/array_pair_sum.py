def array_pair_sum(arr,k):
    if len(arr) < 2:
        return

    seen = set()
    output = set()

    for val in arr:
        target = k - val

        if target not in seen:
            seen.add(val)
        else:
            output.add(((min(target,val)),max(target,val)))

    return len(output)
