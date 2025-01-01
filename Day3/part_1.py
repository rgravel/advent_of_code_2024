import re
import input


# Execute the multiplication
def mul(x, y):
    return x*y


if __name__ == '__main__':
    # Find all occurences
    mul_list = re.findall(r"mul\([0-9]*,[0-9]*\)", input.data_from_input_file())
    
    # Do calculation
    result = sum([eval(x) for x in mul_list])

    # Print result
    print(result)
