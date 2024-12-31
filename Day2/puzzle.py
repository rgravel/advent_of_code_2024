DELIMITER = " "
FILE_NAME = "input.txt"
ACCEPTED_RANGE = [1,2,3]


# Return data from the site example
def data_from_example():
    return [[7,6,4,2,1],[1,2,7,8,9],[9,7,6,2,1],[1,3,2,4,5],[8,6,4,4,1],[1,3,6,7,9]]


# Return the data line by line of the input file
def data_from_input_file():
    with open(FILE_NAME, "r") as file:
        return [line.strip().split(DELIMITER) for line in file]


# Test report, remove one different value each time to make report work
# -1 mean no value is removed (original report)
# At the end return False if no report variation is working
def is_report_safe(report):
    for n in range(-1, len(report)):
        if is_values_safe(n, report.copy()):
            return True
    return False


# Validate the values of the result following the rules
def is_values_safe(index, report):
    # Remove one value
    if index > -1:
        report.pop(index)
    prev_comp = None
    for i in range(0, len(report)-1):
        current_comp = int(report[i])-int(report[i+1])
        if abs(current_comp) not in ACCEPTED_RANGE: 
            return False
        if prev_comp != None and prev_comp != (current_comp > 0): 
            return False
        prev_comp = (current_comp > 0) 
    return True


if __name__ == '__main__':
    result = [r for r in data_from_input_file() if is_report_safe(r)]
    print(f"{len(result)} results are safe")
