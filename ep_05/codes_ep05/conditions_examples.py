# ============================================================
# Python Conditional Statements (if, elif, else)
# Complete Practice
#
# Python Basic Course - Session 5
# Amir Mohammad Dehghan
# ============================================================


# ============================================================
# 1. Comparison Operators (عملگرهای مقایسه‌ای)
# ============================================================

print("\n========== Comparison Operators ==========\n")

a = 10
b = 20

print(a == b)      # مساوی
print(a != b)      # نامساوی
print(a > b)       # بزرگتر
print(a < b)       # کوچکتر
print(a >= b)      # بزرگتر یا مساوی
print(a <= b)      # کوچکتر یا مساوی


# ============================================================
# 2. Simple if
# ============================================================

print("\n========== Simple if ==========\n")

age = 20

if age >= 18:
    print("You are an adult.")

print("Program Continues...")


# ============================================================
# 3. Indentation
# ============================================================

print("\n========== Indentation ==========\n")

number = 15

if number > 0:
    print("Positive Number")
    print("This line is also inside the if block")

print("This line is outside the if block")


# ============================================================
# 4. if ... else
# ============================================================

print("\n========== if ... else ==========\n")

age = 15

if age >= 18:
    print("Access Granted")
else:
    print("Access Denied")


# ============================================================
# 5. if ... elif ... else
# ============================================================

print("\n========== if ... elif ... else ==========\n")

score = 82

if score >= 90:
    print("Grade A")

elif score >= 80:
    print("Grade B")

elif score >= 70:
    print("Grade C")

elif score >= 60:
    print("Grade D")

else:
    print("Failed")


# ============================================================
# 6. Order of Conditions
# ============================================================

print("\n========== Order of Conditions ==========\n")

score = 95

if score >= 90:
    print("Excellent")

elif score >= 50:
    print("Passed")

else:
    print("Failed")


# ============================================================
# 7. Logical Operator (and)
# ============================================================

print("\n========== Logical Operator : and ==========\n")

age = 22
has_license = True

if age >= 18 and has_license:
    print("You can drive.")


# ============================================================
# 8. Logical Operator (or)
# ============================================================

print("\n========== Logical Operator : or ==========\n")

temperature = 35
is_holiday = False

if temperature > 30 or is_holiday:
    print("Let's go swimming.")


# ============================================================
# 9. Logical Operator (not)
# ============================================================

print("\n========== Logical Operator : not ==========\n")

is_logged_in = False

if not is_logged_in:
    print("Please Login")


# ============================================================
# 10. Nested if
# ============================================================

print("\n========== Nested if ==========\n")

age = 25
has_license = True

if age >= 18:

    print("Adult")

    if has_license:
        print("Can Drive")

    else:
        print("License Required")

else:
    print("Child")


# ============================================================
# 11. Short Hand if
# ============================================================

print("\n========== Short Hand if ==========\n")

age = 30

if age >= 18: print("Adult")


# ============================================================
# 12. Short Hand if...else (Ternary Operator)
# ============================================================

print("\n========== Ternary Operator ==========\n")

age = 14

message = "Adult" if age >= 18 else "Child"

print(message)


# ============================================================
# 13. pass
# ============================================================

print("\n========== pass ==========\n")

number = 10

if number > 0:
    pass

print("Program Continues...")


# ============================================================
# 14. Truthy Values
# ============================================================

print("\n========== Truthy Values ==========\n")

name = "Amir"

if name:
    print("Name Exists")

numbers = [1, 2, 3]

if numbers:
    print("List is not Empty")


# ============================================================
# 15. Falsy Values
# ============================================================

print("\n========== Falsy Values ==========\n")

empty_text = ""

if empty_text:
    print("This will not execute")

zero = 0

if zero:
    print("This will not execute")


# ============================================================
# 16. Real Example
# ============================================================

print("\n========== Real Example ==========\n")

username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Login Successful")

else:
    print("Username or Password is Incorrect")


# ============================================================
# 17. Multiple Conditions
# ============================================================

print("\n========== Multiple Conditions ==========\n")

age = 21
country = "Iran"

if age >= 18 and country == "Iran":
    print("Eligible")

else:
    print("Not Eligible")


# ============================================================
# 18. Comparing Strings
# ============================================================

print("\n========== Compare Strings ==========\n")

language = "Python"

if language == "Python":
    print("Correct")

else:
    print("Wrong")


# ============================================================
# 19. Comparing Numbers
# ============================================================

print("\n========== Compare Numbers ==========\n")

num1 = 50
num2 = 40

if num1 > num2:
    print("num1 is Greater")

else:
    print("num2 is Greater")


# ============================================================
# 20. Final Example
# ============================================================

print("\n========== Final Example ==========\n")

name = "Ali"
age = 19
average = 18.5

print(f"Student : {name}")

if age >= 18:

    print("Adult Student")

    if average >= 17:
        print("Excellent Student")

    elif average >= 14:
        print("Good Student")

    else:
        print("Normal Student")

else:
    print("Minor Student")


# ============================================================
# End of Session 5
# ============================================================