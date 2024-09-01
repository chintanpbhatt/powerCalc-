import re


class StringCalculator:

    def add(self, numbers: str):
        if not numbers:
            return 0

        delimiter = ','
        string_list = re.split(delimiter, numbers)
        numbers_list = [float(string) for string in string_list]
        return int(sum(numbers_list))
