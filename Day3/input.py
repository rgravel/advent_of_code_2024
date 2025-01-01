FILE_NAME = "input.txt"


# Return the site example string
def data_from_example(part):
    if part == 1:
        return "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    else :
        return "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"


# Return the entire input file string
def data_from_input_file():
    with open(FILE_NAME, "r") as file:
        return file.read()