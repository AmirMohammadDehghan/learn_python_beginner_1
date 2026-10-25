# ==========================================
# Python Operators Examples
# فقط با print و بدون استفاده از شرط‌ها
# ==========================================

a = 10
b = 3

# ==========================================
# Arithmetic Operators (عملگرهای حسابی)
# ==========================================

print("=== Arithmetic Operators ===")
print("a + b  =", a + b)     # جمع
print("a - b  =", a - b)     # تفریق
print("a * b  =", a * b)     # ضرب
print("a / b  =", a / b)     # تقسیم
print("a // b =", a // b)    # تقسیم صحیح
print("a % b  =", a % b)     # باقیمانده تقسیم
print("a ** b =", a ** b)    # توان
print("+a     =", +a)        # مثبت
print("-a     =", -a)        # منفی
print()


# ==========================================
# Comparison Operators (عملگرهای مقایسه‌ای)
# ==========================================

print("=== Comparison Operators ===")
print("a == b :", a == b)    # مساوی
print("a != b :", a != b)    # نامساوی
print("a > b  :", a > b)     # بزرگتر
print("a < b  :", a < b)     # کوچکتر
print("a >= b :", a >= b)    # بزرگتر یا مساوی
print("a <= b :", a <= b)    # کوچکتر یا مساوی
print()


# ==========================================
# Logical Operators (عملگرهای منطقی)
# ==========================================

print("=== Logical Operators ===")
print("(a > 5) and (b > 1):", (a > 5) and (b > 1))
print("(a > 5) or (b > 10):", (a > 5) or (b > 10))
print("not (a > 5):", not (a > 5))
print()


# ==========================================
# Assignment Operators (عملگرهای انتساب)
# ==========================================

print("=== Assignment Operators ===")

x = 10
print("x =", x)

x += 5
print("x += 5  ->", x)

x -= 2
print("x -= 2  ->", x)

x *= 3
print("x *= 3  ->", x)

x /= 2
print("x /= 2  ->", x)

x //= 2
print("x //= 2 ->", x)

x %= 3
print("x %= 3  ->", x)

x **= 2
print("x **= 2 ->", x)
print()


# ==========================================
# Bitwise Operators (عملگرهای بیتی)
# ==========================================

print("=== Bitwise Operators ===")

m = 10   # 1010
n = 6    # 0110

print("m & n  =", m & n)     # AND
print("m | n  =", m | n)     # OR
print("m ^ n  =", m ^ n)     # XOR
print("~m     =", ~m)        # NOT
print("m << 1 =", m << 1)    # شیفت چپ
print("m >> 1 =", m >> 1)    # شیفت راست
print()


# ==========================================
# Membership Operators (عملگرهای عضویت)
# ==========================================

print("=== Membership Operators ===")

numbers = [1, 2, 3, 4, 5]

print("3 in numbers     :", 3 in numbers)
print("8 in numbers     :", 8 in numbers)
print("8 not in numbers :", 8 not in numbers)
print()


# ==========================================
# Identity Operators (عملگرهای هویتی)
# ==========================================

print("=== Identity Operators ===")

list1 = [1, 2]
list2 = [1, 2]
list3 = list1

print("list1 is list2     :", list1 is list2)
print("list1 is list3     :", list1 is list3)
print("list1 is not list2 :", list1 is not list2)
print()


# ==========================================
# Ternary Operator (عملگر سه‌تایی)
# ==========================================

print("=== Ternary Operator ===")

result = "a بزرگتر است" if a > b else "b بزرگتر است"
print(result)