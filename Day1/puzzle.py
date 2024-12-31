DELIMITER = "   "
FILE_NAME = "input.txt"


# Return lists from the example given
def input_from_example():
    return [[3,4,2,1,3,3], [4,3,5,3,9,3]]


# Parse the input file line by line to create 2 lists of locations
def input_from_file():
    local_lists = [[],[]]

    with open(FILE_NAME, "r") as file:
        [[local_lists[index].append(int(location)) for index,location in enumerate(line.strip().split(DELIMITER))] for line in file]
    
    return local_lists


if __name__ == '__main__':
    #lists = input_from_example()
    lists = input_from_file()
    
    lists[0].sort()
    lists[1].sort()

    distance = sum([abs(lists[0][i]-lists[1][i]) for i in range(0,len(lists[0]))])
    print(f"Distance: {distance}")

    similarity = sum([x*lists[1].count(x) for x in lists[0]])
    print(f"Similarity: {similarity}")
