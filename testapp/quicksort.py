def quick_sort(data):

    if len(data) <= 1:
        return data

    pivot = data[0]

    left = []
    right = []

    for i in data[1:]:

        if i['age'] < pivot['age']:
            left.append(i)

        else:
            right.append(i)

    return quick_sort(left) + [pivot] + quick_sort(right)