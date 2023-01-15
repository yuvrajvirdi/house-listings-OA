def get_most_recent(listings):
    """
    gets the most recent
    listing of each address in listings 
    O(n) time complexity
    O(n) space complexity 
    assumes listings is a 2D array with 3 values: [name, address, date]
    assumes name and address are string types, and date is integer type
    """

    # hash map to track recents
    # key = address : val = [name, address, date]
    recent = {}
    
    # traverse listings
    for name, address, date in listings:
        # if listing exists
        if address in recent:
            # update date if it has a greater value
            if date > recent[address][2]:
                recent[address] = [name, address, date]
        # otherwise add listing
        else:
            recent[address] = [name, address, date]
    
    # make a list of the values in the hash map, and return it
    res = recent.values()
    return list(res)

# testing
listings = [["L1", "123 kings road", 2020],
            ["L2", "20 queen road", 1990],
            ["L3", "20 queen road", 1992],
            ["L4", "123 kings road", 2022]]

print(get_most_recent(listings))
# prints [['L4', '123 kings road', 2022], ['L3', '20 queen road', 1992]]

