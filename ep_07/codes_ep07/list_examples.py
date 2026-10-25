# ===============================================================
# جلسه هفتم دوره پایتون مقدماتی
# مبحث : List (لیست ها)
# مدرس : امیر محمد دهقان
# ===============================================================

# ===============================================================
# بخش 1 : List چیست؟
# ===============================================================

# لیست (List) یکی از پرکاربردترین ساختمان داده‌ها در پایتون است.
#
# از لیست برای نگهداری چندین مقدار در یک متغیر استفاده می‌شود.
#
# ویژگی‌های List
# -----------------
# ✔ ترتیب اعضا حفظ می‌شود (Ordered)
# ✔ قابل تغییر است (Mutable)
# ✔ اعضای تکراری مجاز هستند
# ✔ می‌تواند انواع مختلف داده را نگهداری کند

print("\n==============================")
print("List Introduction")
print("==============================\n")


# ساخت یک لیست ساده

fruits = ["Apple", "Banana", "Orange", "Mango"]

print(fruits)


# ===============================================================
# بخش 2 : انواع داده در List
# ===============================================================

print("\n==============================")
print("Different Data Types")
print("==============================\n")

# درون یک لیست می‌توان انواع مختلف داده را قرار داد.

student = [
    "Ali",      # رشته
    18,         # عدد صحیح
    18.75,      # عدد اعشاری
    True        # مقدار بولین
]

print(student)

print()

# همچنین می‌توان نوع داده هر عضو را بررسی کرد.

print(type(student[0]))
print(type(student[1]))
print(type(student[2]))
print(type(student[3]))


# ===============================================================
# بخش 3 : ایجاد List
# ===============================================================

print("\n==============================")
print("Create List")
print("==============================\n")

# روش اول (رایج‌ترین)

colors = ["Red", "Green", "Blue"]

print(colors)

print()

# روش دوم با استفاده از تابع list()

numbers = list((10, 20, 30, 40))

print(numbers)

print()

# ساخت لیست خالی

shopping_cart = []

print(shopping_cart)

print()

# اضافه کردن اعضا به لیست خالی

shopping_cart.append("Laptop")
shopping_cart.append("Mouse")
shopping_cart.append("Keyboard")

print(shopping_cart)


# ===============================================================
# بخش 4 : Index
# ===============================================================

print("\n==============================")
print("Positive Index")
print("==============================\n")

# هر عضو یک شماره (Index) دارد.
#
# اندیس از صفر شروع می‌شود.

fruits = [
    "Apple",
    "Banana",
    "Orange",
    "Mango"
]

print("First :", fruits[0])
print("Second :", fruits[1])
print("Third :", fruits[2])
print("Fourth :", fruits[3])


# ===============================================================
# بخش 5 : Negative Index
# ===============================================================

print("\n==============================")
print("Negative Index")
print("==============================\n")

# اندیس منفی از انتهای لیست شروع می‌شود.
#
# -1 یعنی آخرین عضو
# -2 یعنی یکی مانده به آخر

print("Last :", fruits[-1])

print("Second Last :", fruits[-2])

print("Third Last :", fruits[-3])


# ===============================================================
# بخش 6 : Slicing
# ===============================================================

print("\n==============================")
print("List Slicing")
print("==============================\n")

numbers = [10, 20, 30, 40, 50, 60]

# از اندیس 1 تا قبل از اندیس 4

print(numbers[1:4])

print()

# از ابتدا تا قبل از اندیس 3

print(numbers[:3])

print()

# از اندیس 2 تا انتها

print(numbers[2:])

print()

# سه عضو آخر

print(numbers[-3:])

print()

# تمام لیست

print(numbers[:])


# ===============================================================
# بخش 7 : تغییر اعضای List
# ===============================================================

print("\n==============================")
print("Change Item")
print("==============================\n")

fruits = [
    "Apple",
    "Banana",
    "Orange"
]

print("Before")

print(fruits)

print()

# تغییر دومین عضو

fruits[1] = "Mango"

print("After")

print(fruits)


# ===============================================================
# بخش 8 : تغییر چند عضو
# ===============================================================

print("\n==============================")
print("Change Multiple Items")
print("==============================\n")

numbers = [10, 20, 30, 40, 50]

print("Before")

print(numbers)

print()

# اعضای اندیس 1 و 2 با دو مقدار جدید جایگزین می‌شوند.

numbers[1:3] = [200, 300]

print("After")

print(numbers)

print()

# حتی تعداد اعضای جدید می‌تواند بیشتر باشد.

numbers[2:4] = [500, 600, 700]

print(numbers)


# ===============================================================
# بخش 9 : بررسی وجود عضو
# ===============================================================

print("\n==============================")
print("Check Item")
print("==============================\n")

fruits = [
    "Apple",
    "Banana",
    "Orange",
    "Mango"
]

# بررسی وجود یک عضو

print("Apple" in fruits)

print("Kiwi" in fruits)

print()

# بررسی نبودن عضو

print("Kiwi" not in fruits)

print("Apple" not in fruits)


# ===============================================================
# بخش 10 : طول List
# ===============================================================

print("\n==============================")
print("Length Of List")
print("==============================\n")

students = [
    "Ali",
    "Sara",
    "Reza",
    "Amir",
    "Nima"
]

# تابع len تعداد اعضای لیست را برمی‌گرداند.

print("Student Count :", len(students))

print()

# بررسی خالی بودن لیست

cart = []

print("Cart Length :", len(cart))

if len(cart) == 0:

    print("Shopping Cart Is Empty")

print()

# مثال واقعی

products = [
    "Laptop",
    "Mouse",
    "Keyboard",
    "Monitor",
    "Printer",
    "Speaker"
]

print("Products Count :", len(products))


# ===============================================================
# بخش 11 : append()
# ===============================================================

print("\n==============================")
print("append()")
print("==============================\n")

# متد append() برای اضافه کردن یک عضو
# به انتهای لیست استفاده می‌شود.

fruits = ["Apple", "Banana", "Orange"]

print("Before :", fruits)

# اضافه کردن یک عضو

fruits.append("Mango")

print("After :", fruits)

print()

# append فقط یک عضو اضافه می‌کند.
# اگر یک لیست را append کنیم،
# کل آن لیست به عنوان یک عضو جدید اضافه می‌شود.

numbers = [1, 2, 3]

numbers.append([4, 5])

print(numbers)

# خروجی
# [1,2,3,[4,5]]


# ===============================================================
# بخش 12 : insert()
# ===============================================================

print("\n==============================")
print("insert()")
print("==============================\n")

# insert عضو جدید را در اندیس دلخواه قرار می‌دهد.

students = ["Ali", "Sara", "Reza"]

print("Before :", students)

students.insert(1, "Amir")

print("After :", students)

print()

# همه اعضای بعد از اندیس مشخص شده
# یک خانه به سمت راست منتقل می‌شوند.

colors = ["Red", "Blue"]

colors.insert(0, "Green")

print(colors)


# ===============================================================
# بخش 13 : extend()
# ===============================================================

print("\n==============================")
print("extend()")
print("==============================\n")

# extend اعضای یک لیست دیگر را
# به انتهای لیست فعلی اضافه می‌کند.

list1 = [10, 20, 30]
list2 = [40, 50, 60]

print("Before :", list1)

list1.extend(list2)

print("After :", list1)

print()

# تفاوت append و extend

numbers = [1, 2]

numbers.append([3, 4])

print("append :", numbers)

numbers = [1, 2]

numbers.extend([3, 4])

print("extend :", numbers)

# append
# [1,2,[3,4]]

# extend
# [1,2,3,4]


# ===============================================================
# بخش 14 : remove()
# ===============================================================

print("\n==============================")
print("remove()")
print("==============================\n")

# remove اولین مقدار پیدا شده را حذف می‌کند.

fruits = [
    "Apple",
    "Banana",
    "Orange",
    "Banana"
]

print("Before :", fruits)

fruits.remove("Banana")

print("After :", fruits)

print()

# فقط اولین Banana حذف شد.

# اگر مقدار وجود نداشته باشد
# ValueError ایجاد می‌شود.

"""
fruits.remove("Kiwi")
"""


# ===============================================================
# بخش 15 : pop()
# ===============================================================

print("\n==============================")
print("pop()")
print("==============================\n")

# pop عضو را حذف می‌کند
# و مقدار حذف شده را برمی‌گرداند.

numbers = [10, 20, 30, 40]

deleted_item = numbers.pop()

print("Deleted :", deleted_item)

print(numbers)

print()

# حذف با اندیس

numbers = [10, 20, 30, 40]

deleted_item = numbers.pop(1)

print("Deleted :", deleted_item)

print(numbers)


# ===============================================================
# تفاوت remove و pop
# ===============================================================

print("\n==============================")
print("remove VS pop")
print("==============================\n")

print("remove => حذف بر اساس مقدار")

print("pop => حذف بر اساس اندیس")


# ===============================================================
# بخش 16 : del
# ===============================================================

print("\n==============================")
print("del")
print("==============================\n")

# del یک کلمه کلیدی است.
# می‌تواند عضو یا حتی کل لیست را حذف کند.

numbers = [10, 20, 30, 40, 50]

print("Before :", numbers)

del numbers[2]

print("After :", numbers)

print()

# حذف چند عضو

numbers = [10, 20, 30, 40, 50]

del numbers[1:4]

print(numbers)

print()

# حذف کل لیست

temp = [1, 2, 3]

del temp

# print(temp)
# NameError


# ===============================================================
# بخش 17 : clear()
# ===============================================================

print("\n==============================")
print("clear()")
print("==============================\n")

# clear تمام اعضای لیست را حذف می‌کند.
# اما خود لیست باقی می‌ماند.

products = [
    "Laptop",
    "Mouse",
    "Keyboard"
]

print("Before :", products)

products.clear()

print("After :", products)

# خروجی
# []


# ===============================================================
# تفاوت clear و del
# ===============================================================

print("\n==============================")
print("clear VS del")
print("==============================\n")

print("clear => فقط اعضا حذف می‌شوند.")

print("del => خود متغیر نیز حذف می‌شود.")


# ===============================================================
# بخش 18 : پیمایش با for
# ===============================================================

print("\n==============================")
print("Loop Through List")
print("==============================\n")

# ساده‌ترین روش پیمایش لیست

fruits = [
    "Apple",
    "Banana",
    "Orange",
    "Mango"
]

for fruit in fruits:

    print(fruit)

print()

# مثال واقعی

students = [
    "Ali",
    "Sara",
    "Amir",
    "Nima"
]

for student in students:

    print("Student :", student)


# ===============================================================
# بخش 19 : پیمایش با range(len())
# ===============================================================

print("\n==============================")
print("Loop With Index")
print("==============================\n")

# زمانی استفاده می‌شود
# که هم مقدار و هم شماره اندیس لازم باشد.

fruits = [
    "Apple",
    "Banana",
    "Orange"
]

for i in range(len(fruits)):

    print(f"Index {i} -> {fruits[i]}")

print()

# مثال دوم

numbers = [10, 20, 30, 40]

for i in range(len(numbers)):

    print(f"numbers[{i}] = {numbers[i]}")


# ===============================================================
# بخش 20 : پیمایش با while
# ===============================================================

print("\n==============================")
print("Loop With While")
print("==============================\n")

# با while باید اندیس را خودمان مدیریت کنیم.

fruits = [
    "Apple",
    "Banana",
    "Orange",
    "Mango"
]

index = 0

while index < len(fruits):

    print(fruits[index])

    # افزایش اندیس
    index += 1

print()

# مثال واقعی

products = [
    "Laptop",
    "Mouse",
    "Keyboard",
    "Monitor"
]

index = 0

while index < len(products):

    print(f"Product {index+1} : {products[index]}")

    index += 1


# ===============================================================
# مقایسه روش‌های پیمایش
# ===============================================================

print("\n==============================")
print("Loop Comparison")
print("==============================\n")

print("for            -> ساده‌ترین روش")

print("range(len())   -> دسترسی به اندیس")

print("while          -> کنترل کامل روی حلقه")


# ===============================================================
# بخش 21 : sort()
# ===============================================================

print("\n==============================")
print("sort()")
print("==============================\n")

# متد sort() برای مرتب کردن اعضای لیست استفاده می‌شود.
#
# نکته مهم:
# sort() لیست اصلی را تغییر می‌دهد و مقدار جدیدی برنمی‌گرداند.

numbers = [50, 20, 80, 10, 40]

print("Before :", numbers)

numbers.sort()

print("After :", numbers)

print()

# مرتب سازی رشته‌ها

fruits = ["Orange", "Apple", "Banana", "Kiwi"]

print("Before :", fruits)

fruits.sort()

print("After :", fruits)


# ===============================================================
# بخش 22 : مرتب سازی نزولی
# ===============================================================

print("\n==============================")
print("sort(reverse=True)")
print("==============================\n")

# اگر بخواهیم مرتب سازی به صورت نزولی باشد
# از پارامتر reverse=True استفاده می‌کنیم.

numbers = [50, 20, 80, 10, 40]

numbers.sort(reverse=True)

print(numbers)

print()

fruits = ["Orange", "Apple", "Banana", "Kiwi"]

fruits.sort(reverse=True)

print(fruits)


# ===============================================================
# بخش 23 : reverse()
# ===============================================================

print("\n==============================")
print("reverse()")
print("==============================\n")

# reverse() لیست را مرتب نمی‌کند.
# فقط ترتیب فعلی اعضا را برعکس می‌کند.

numbers = [10, 20, 30, 40, 50]

print("Before :", numbers)

numbers.reverse()

print("After :", numbers)

print()

# تفاوت sort و reverse

print("sort()     => مرتب سازی")

print("reverse()  => برعکس کردن ترتیب فعلی")


# ===============================================================
# بخش 24 : copy()
# ===============================================================

print("\n==============================")
print("copy()")
print("==============================\n")

# برای ساخت یک نسخه مستقل از لیست
# از copy() استفاده می‌کنیم.

numbers = [10, 20, 30]

copy_numbers = numbers.copy()

copy_numbers.append(40)

print("Original :", numbers)

print("Copy :", copy_numbers)


# ===============================================================
# بخش 25 : تفاوت = و copy()
# ===============================================================

print("\n==============================")
print("Assignment VS Copy")
print("==============================\n")

# استفاده از = باعث ساخت لیست جدید نمی‌شود.
# هر دو متغیر به یک لیست اشاره می‌کنند.

list1 = [1, 2, 3]

list2 = list1

list2.append(4)

print("list1 :", list1)

print("list2 :", list2)

print()

print("Both Variables Point To Same List")

print()

# حالا با copy()

list3 = [1, 2, 3]

list4 = list3.copy()

list4.append(4)

print("list3 :", list3)

print("list4 :", list4)

print()

print("copy() Creates Independent List")


# ===============================================================
# بخش 26 : اتصال دو لیست
# ===============================================================

print("\n==============================")
print("Join Lists")
print("==============================\n")

# روش اول : +

list1 = [1, 2, 3]

list2 = [4, 5, 6]

result = list1 + list2

print(result)

print()

# روش دوم : extend()

list1 = [1, 2, 3]

list2 = [4, 5, 6]

list1.extend(list2)

print(list1)


# ===============================================================
# بخش 27 : count()
# ===============================================================

print("\n==============================")
print("count()")
print("==============================\n")

# count تعداد تکرار یک مقدار را برمی‌گرداند.

numbers = [10, 20, 10, 30, 10, 40]

print(numbers.count(10))

print(numbers.count(20))

print(numbers.count(100))


# ===============================================================
# بخش 28 : index()
# ===============================================================

print("\n==============================")
print("index()")
print("==============================\n")

# index اندیس اولین مقدار پیدا شده را برمی‌گرداند.

fruits = [
    "Apple",
    "Banana",
    "Orange",
    "Banana"
]

print(fruits.index("Banana"))

print(fruits.index("Orange"))

print()

# اگر مقدار وجود نداشته باشد
# ValueError ایجاد می‌شود.

"""
print(fruits.index("Kiwi"))
"""


# ===============================================================
# بخش 29 : Nested List
# ===============================================================

print("\n==============================")
print("Nested List")
print("==============================\n")

# لیست داخل لیست

matrix = [

    [1, 2, 3],

    [4, 5, 6],

    [7, 8, 9]

]

print(matrix)

print()

print("First Row :", matrix[0])

print("Second Row :", matrix[1])

print()

print("First Item :", matrix[0][0])

print("Center :", matrix[1][1])

print("Last Item :", matrix[2][2])


# ===============================================================
# بخش 30 : List Comprehension
# ===============================================================

print("\n==============================")
print("List Comprehension")
print("==============================\n")

# یکی از قابلیت‌های قدرتمند پایتون
# برای ساخت لیست جدید

numbers = [1, 2, 3, 4, 5]

double_numbers = [

    number * 2

    for number in numbers

]

print(double_numbers)

print()

# مثال دوم

names = [

    "ali",

    "amir",

    "sara"

]

upper_names = [

    name.upper()

    for name in names

]

print(upper_names)


# ===============================================================
# بخش 31 : مثال واقعی
# ===============================================================

print("\n==============================")
print("Real World Example")
print("==============================\n")

# سبد خرید فروشگاه

shopping_cart = [

    "Laptop",

    "Mouse",

    "Keyboard"

]

print("Shopping Cart")

for item in shopping_cart:

    print("-", item)

print()

print("Items Count :", len(shopping_cart))

print()

shopping_cart.append("Monitor")

print(shopping_cart)

print()

shopping_cart.remove("Mouse")

print(shopping_cart)

print()

shopping_cart.sort()

print(shopping_cart)


# ===============================================================
# بخش 32 : اشتباهات رایج
# ===============================================================

print("\n==============================")
print("Common Mistakes")
print("==============================\n")

print("1- استفاده از اندیس خارج از محدوده")

print("2- استفاده اشتباه از append و extend")

print("3- استفاده از = به جای copy()")

print("4- remove برای عضو موجود نبودن")

print("5- تغییر لیست هنگام پیمایش")

print()

# مثال اشتباه

"""
numbers = [1,2,3]

for item in numbers:

    numbers.remove(item)

"""

print("Never Modify List While Iterating.")


# ===============================================================
# بخش 33 : جمع بندی جلسه
# ===============================================================

print("\n==============================")
print("Session Summary")
print("==============================\n")

print("✔ Create List")

print("✔ Access Items")

print("✔ Change Items")

print("✔ Add Items")

print("✔ Remove Items")

print("✔ Loop Through List")

print("✔ Sort List")

print("✔ Reverse List")

print("✔ Copy List")

print("✔ Join Lists")

print("✔ count()")

print("✔ index()")

print("✔ Nested List")

print("✔ List Comprehension")


# ===============================================================
# پیام پایانی
# ===============================================================

print("\n=========================================")
print("Congratulations 🎉")
print("You Finished Python Lists Session")
print("Keep Practicing Every Day 🚀")
print("=========================================")