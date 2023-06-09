import random
import numpy


def question_generator(mode):
    numbers = []
    question_outline = []

    if mode == "easy":
        in_bracket = random.randint(-10, 9)
        if in_bracket == 0:
            in_bracket = 10
        out_of_bracket = random.randint(-10, 9)
        if out_of_bracket == 0:
            out_of_bracket = 10
        final_number = in_bracket * out_of_bracket
        if in_bracket > 0:
            in_bracket = f"+{in_bracket}"
        brackets_outline = f"{out_of_bracket}(x{in_bracket})"
        question_outline.append(brackets_outline)
        if final_number > 0:
            final_number = f"+{final_number}"
        answer = f"{out_of_bracket}x{final_number}"

    elif mode == "normal" or mode == "hard":
        for number in range(1, 3):

            while True:
                number = random.randint(-10, 9)
                number_2 = -1 * number
                if number == 0:
                    number = 10
                if number not in numbers and number_2 not in numbers:
                    numbers.append(number)
                    break

            if number < 0:
                brackets_outline = f"(x{number})"
            else:
                brackets_outline = f"(x+{number})"
            question_outline.append(brackets_outline)
            if len(question_outline) == 2:
                break

        x_value_one = sum(numbers)
        integer = numpy.prod(numbers)

        if mode == "normal":
            if x_value_one > 0:
                x_value_one = f"+{x_value_one}"
            if integer > 0:
                integer = f"+{integer}"
            answer = f"x^2{x_value_one}x{integer}"

        elif mode == "hard":
            while True:
                third_number = random.randint(-10, 9)
                third_number_2 = -1 * third_number
                if third_number == 0:
                    third_number = 10
                if third_number not in numbers and third_number_2 not in numbers:
                    numbers.append(third_number)
                    break

            if third_number > 0:
                third_brackets = f"(x+{third_number})"
            else:
                third_brackets = f"(x{third_number})"

            question_outline.append(third_brackets)

            final_x_squared_value = x_value_one + third_number
            final_x_value = third_number * x_value_one + integer
            final_integer = integer * third_number

            if final_integer > 0:
                final_integer = f"+{final_integer}"
            if final_x_value > 0:
                final_x_value = f"+{final_x_value}"
            if final_x_squared_value > 0:
                final_x_squared_value = f"+{final_x_squared_value}"

            answer = f"X^3{final_x_squared_value}x^2{final_x_value}x{final_integer}"

    print()
    print(*question_outline, sep="")
    print(answer)
    get_answer = input(f"Please solve this question: ")
    if get_answer == answer:
        result = "correct"
    else:
        print(answer)
        result = "wrong"
    return result


while True:
    easy_test = question_generator("easy")

    if easy_test == "correct":
        print("Correct! Congratulations!")
    else:
        print("Incorrect.")

    normal_test = question_generator("normal")

    if normal_test == "correct":
        print("Correct! Congratulations!")
    else:
        print("Incorrect.")

    hard_test = question_generator("hard")

    if hard_test == "correct":
        print("Correct! Congratulations!")
    else:
        print("Incorrect.")
