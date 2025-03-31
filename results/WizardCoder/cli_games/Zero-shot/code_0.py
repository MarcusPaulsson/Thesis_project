def group_strings_by_length(strings):
    grouped_strings = {}

    for string in strings:
        length = len(string)
        if length not in grouped_strings:
            grouped_strings[length] = []
        grouped_strings[length].append(string)

    return grouped_strings