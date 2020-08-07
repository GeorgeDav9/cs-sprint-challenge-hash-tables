def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

      # create a hash table
    values = {}
    # using the index loop to search for the key and include each value in the dict
    for i in range(length):
        # find the target weight using get
        target = values.get(limit - weights[i])
        # make sure the none value is accounted for
        if target is not None:
            return i, target
        # the dict needs to be set at the index 'th value
        values[weights[i]] = i

    return None
