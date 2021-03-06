def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

    # Instantiate a cache dict 'occurences'
    occurrences = dict()

    for i in range(len(arrays)):
        for num in arrays[i]:
            if num not in occurrences:
                occurrences[num] = 1

            else:
                occurrences[num] +=1

    # Instantiate result
    result = []

    # If number has occurred in every list in the arrays then
    # we add it to result
    l = len(arrays)
    result = result + [k for k,v in occurrences.items() if v == l]


    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
