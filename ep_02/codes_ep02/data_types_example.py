# ======================================================
# Python Data Types
# معرفی انواع داده‌ها در پایتون
# ======================================================


# ======================================================
# Numeric Types (اعداد)
# ======================================================

integer_number = 100
float_number = 3.14
complex_number = 2 + 5j

print("=== Numeric Types ===")

print(integer_number)
print(type(integer_number))
print(isinstance(integer_number, int))
print()

print(float_number)
print(type(float_number))
print(isinstance(float_number, float))
print()

print(complex_number)
print(type(complex_number))
print(isinstance(complex_number, complex))
print()


# ======================================================
# Boolean
# ======================================================

is_student = True

print("=== Boolean ===")

print(is_student)
print(type(is_student))
print(isinstance(is_student, bool))
print()


# ======================================================
# String
# ======================================================

text = "Hello Python"

print("=== String ===")

print(text)
print(type(text))
print(isinstance(text, str))
print()


# ======================================================
# List
# ======================================================

numbers = [10, 20, 30, 40]

print("=== List ===")

print(numbers)
print(type(numbers))
print(isinstance(numbers, list))
print()


# ======================================================
# Tuple
# ======================================================

colors = ("Red", "Green", "Blue")

print("=== Tuple ===")

print(colors)
print(type(colors))
print(isinstance(colors, tuple))
print()


# ======================================================
# Set
# ======================================================

fruits = {"Apple", "Banana", "Orange"}

print("=== Set ===")

print(fruits)
print(type(fruits))
print(isinstance(fruits, set))
print()


# ======================================================
# Dictionary
# ======================================================

student = {
    "name": "Ali",
    "age": 20,
    "score": 19.5
}

print("=== Dictionary ===")

print(student)
print(type(student))
print(isinstance(student, dict))
print()


# ======================================================
# NoneType
# ======================================================

value = None

print("=== NoneType ===")

print(value)
print(type(value))
print(isinstance(value, type(None)))
print()


# ======================================================
# Bytes
# ======================================================

binary_data = b"Python"

print("=== Bytes ===")

print(binary_data)
print(type(binary_data))
print(isinstance(binary_data, bytes))
print()


# ======================================================
# Bytearray
# ======================================================

byte_array = bytearray(b"Python")

print("=== Bytearray ===")

print(byte_array)
print(type(byte_array))
print(isinstance(byte_array, bytearray))
print()


# ======================================================
# Frozen Set
# ======================================================

fixed_set = frozenset({1, 2, 3, 4})

print("=== Frozen Set ===")

print(fixed_set)
print(type(fixed_set))
print(isinstance(fixed_set, frozenset))
print()


# ======================================================
# مقایسه همه انواع داده
# ======================================================

print("=" * 60)
print("Summary")
print("=" * 60)

values = [
    integer_number,
    float_number,
    complex_number,
    is_student,
    text,
    numbers,
    colors,
    fruits,
    student,
    value,
    binary_data,
    byte_array,
    fixed_set
]

for item in values:
    print(f"{str(item):30} ---> {type(item).__name__}")

print("=" * 60)