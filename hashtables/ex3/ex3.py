def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

    # setup hash table
    integer_list = {}

    # setup  list
    result = []

    # single list within hash table
    for single_list in arrays:
        for integer in single_list:
            if integer != integer_list:
                integer_list[integer] = 1
            else:
                # add integer to the intersection
                result.append(integer)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
