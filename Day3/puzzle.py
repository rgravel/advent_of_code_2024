import re

FILE_NAME = "input.txt"


# Return the site example string
def data_from_example():
    return "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"


# Return the entire input file string
def data_from_input_file():
    with open(FILE_NAME, "r") as file:
        return file.read()


# Execute the multiplication
def mul(x, y):
    return x*y


if __name__ == '__main__':
    # Find all occurences
    mul_list = re.findall(r"mul\([0-9]*,[0-9]*\)", data_from_input_file())
    
    # Do calculation
    result = sum([eval(x) for x in mul_list])

    # Print result
    print(result)
