#assert abs(-42) == -42, "should be absolute value of a number"

a = 5
b = 10
print (f'Five plus ten is {a + b} and not {2 * (a + b)}')

def greet (name, question):
    print (f"Hello, {name}! How is it {question}?")

greet('Bob', 'going')

print("Let's count together: {}, then goes {}, and then {}".format("one", "two", "three"))

str1 = "one"
str2 = "two"
str3 = "three"
print(f"Let's count together: {str1}, then goes {str2}, and then {str3}")

actual_result = "abrakadabra"
print(f"Wrong text, got {actual_result}, something wrong")

def test_input_text (expected_result, actual_result):
    #print (f"expected {expected_result}, got {actual_result}")
    assert expected_result == actual_result, f"expected {expected_result}, got {actual_result}"

test_input_text (8, 11)
