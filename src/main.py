from utils import TypeChecker

checkers = TypeChecker()

if __name__ == "__main__":
    variable = input('Type anything: ')
    integer_check = checkers.integer_checker(variable)
    float_check = checkers.float_checker(variable)
    string_check = checkers.string_checker(variable)