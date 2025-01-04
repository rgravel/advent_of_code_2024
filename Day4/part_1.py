# input
INPUT_FILE_NAME = "input.txt"
EXAMPLE_FILE_NAME = "example.txt"

LETTERS = ['X', 'M', 'A', 'S']


# Validate coordinates exist then return letter
def get_letter_at(a, b, matrix):
    return (matrix[a][b] if (a>=0 and a<len(matrix)) and (b>=0 and b<len(matrix[a])) else None)                                
    

# Starting at X possition, check for XMAS word for each direction
# Break direction is not letter is not matching
def check_possibility(matrix, a, b):
    counter = 0
    for x in range(-1,2):
        for y in range(-1,2):
            factor = 1
            done = False
            while not done and factor <= 3:
                if get_letter_at(a+(x*factor), b+(y*factor), matrix) != LETTERS[factor]:
                    done = True
                elif factor == 3:
                    counter += 1
                factor += 1
    return counter


if __name__ == '__main__':
    # Build matrix for the input file
    with open(INPUT_FILE_NAME, "r") as file:
        matrix = [list(line.strip()) for line in file]

    # Found and keep each coordinate of 'X' in the matrix
    start_coordinates = []
    [[start_coordinates.append((line_idx, col_idx)) for col_idx, c in enumerate(line) if c == 'X'] for line_idx, line in enumerate(matrix)]

    # Look for each direction and count the result
    print(sum([check_possibility(matrix, a, b) for a,b in start_coordinates]))
