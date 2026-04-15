from pathlib import Path
import json

def read_data(file_name, field):
    cwd_path = Path.cwd()
    file_path = cwd_path / file_name

    with open(file_path, mode='r') as file:
        data = json.load(file)

    if field in data.keys():
        return data[field]
    else:
        return None

def linear_search(searched_data, searched_number):
    idx = 0
    count = 0
    positions = []
    searched_dictionary = {}
    while idx < len(searched_data):
        if searched_data[idx] == searched_number:
            count += 1
            positions.append(idx)
        idx += 1
    searched_dictionary['positions'] = positions
    searched_dictionary['count'] = count
    return searched_dictionary

def binary_search(searched_data, searched_number):
    left = 0
    right = len(searched_data) - 1
    while left <= right:
        mid = (left + right) // 2
        if searched_data[mid] == searched_number:
            return mid
        elif searched_data[mid] < searched_number:
            left = mid + 1
        elif searched_data[mid] > searched_number:
            right = mid - 1
    return None


def main():
    my_data = read_data("sequential.json", "unordered_numbers")
    print(my_data)
    found_number = linear_search(my_data, 37)
    print(found_number)
    found_number_bin = binary_search(my_data, 24)
    print(found_number_bin)


if __name__ == "__main__":
    main()
