# input
INPUT_FILE_NAME = "input.txt"
EXAMPLE_FILE_NAME = "example.txt"

MAS = "MAS"
SAM = "SAM"


# Validate coordinates exist then return letter or nothing
def get_letter_at(a, b, matrix):
    return (matrix[a][b] if (a>=0 and a<len(matrix)) and (b>=0 and b<len(matrix[a])) else '')                                
    

def check_X_mas(matrix, a, b):
    # check first diagonal
    word_1 = get_letter_at(a-1, b-1, matrix) + get_letter_at(a, b, matrix) + get_letter_at(a+1, b+1, matrix)
    # check second diagonal
    word_2 = get_letter_at(a-1, b+1, matrix) + get_letter_at(a, b, matrix) + get_letter_at(a+1, b-1, matrix)
    
    if (word_1 == MAS or word_1 == SAM) and (word_2 == MAS or word_2 == SAM):
        return 1
    return 0


if __name__ == '__main__':
    # Build matrix for the input file
    with open(INPUT_FILE_NAME, "r") as file:
        matrix = [list(line.strip()) for line in file]

    # Found and keep each coordinate of 'X' in the matrix
    start_coordinates = []
    [[start_coordinates.append((line_idx, col_idx)) for col_idx, c in enumerate(line) if c == 'A'] for line_idx, line in enumerate(matrix)]

    # Look for each direction and count the result
    print(sum([check_X_mas(matrix, a, b) for a,b in start_coordinates]))
