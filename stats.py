def number_of_words(input_string):
    input_array = input_string.split()
    num_words = len(input_array)
    return num_words

def wie_oft(string):
    wie_oft_dict = {}
    for i in string:
        i = i.lower()
        if i in wie_oft_dict:
            wie_oft_dict[i] += 1
        else:
            wie_oft_dict[i] = 1

    return wie_oft_dict

def sort_on(items):
    return items["num"]

def sorted_dict(input_dict):
    list_of_dict = []
    for key in input_dict:
        list_of_dict.append({"char": key, "num": input_dict[key]})
    list_of_dict.sort(reverse=True, key=sort_on)
    return list_of_dict
