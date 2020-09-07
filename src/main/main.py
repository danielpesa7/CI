from utils.checkers import integer_checker, float_checker, string_checker

if __name__ == "__main__":
    variable = input('Type anything: ')
    integer_check = integer_checker(variable)
    float_check = float_checker(variable)
    string_check = string_checker(variable)