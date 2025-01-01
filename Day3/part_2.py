import re
import input

DO = "do()"
DONT = "don\'t()"


class Day3_Part2:

    _mul_list = []
    _start = 0
    _done = False
    

    def __init__(self):
        self._input_str = input.data_from_input_file()
        self._mul_list = []
        self._toggle = True
    
    
    def find_next_toggle(self, str, current_toggle):
        index = str.find(DONT if current_toggle else DO)
        if current_toggle:
            self._mul_list.extend(re.findall(r"mul\([0-9]*,[0-9]*\)", str[:index]))
        return index


    def parse_input(self):
        sub_str = self._input_str
        while not self._done:
            next_index = self.find_next_toggle(sub_str, self._toggle)
            if next_index == -1: 
                self._done = True
            else:
                self._toggle = False if self._toggle else True
                sub_str = sub_str[next_index:]


# Execute the multiplication
def mul(x, y):
    return x*y

if __name__ == '__main__':
    day3 = Day3_Part2()
    day3.parse_input()
    
    # Do calculation
    result = sum([eval(x) for x in day3._mul_list])

    # Print result
    print(result)
