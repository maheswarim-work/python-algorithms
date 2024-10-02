# "I love arrays they are my favorite" ==> ["I", "love", "arrays", "they", "are", "my", "favorite"]

def string_to_array(input_string):
    result_array = input_string.split(' ')
    print(result_array)
    return result_array

string_to_array("I love arrays they are my favorite")
