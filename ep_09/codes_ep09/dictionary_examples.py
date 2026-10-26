"""جلسه ۹: مثال‌های مستقل Dictionary. اجرا: python dictionary_examples.py"""

# ۱. ایجاد دیکشنری: هر کلید، یک مقدار را مشخص می‌کند.
student = {"name": "Sara", "age": 20, "active": True}
print("1) Create:", student)
print("Name:", student["name"])
print("Length:", len(student))

# ۲. کلید تکراری، مقدار قبلی را جایگزین می‌کند.
settings = {"theme": "light", "theme": "dark"}
print("2) Duplicate key:", settings)  # {'theme': 'dark'}

# ۳. get برای کلیدی که ممکن است وجود نداشته باشد مناسب است.
print("3) Missing city:", student.get("city", "Unknown"))
print("Has city:", "city" in student)  # in کلیدها را بررسی می‌کند.

# ۴. همان دستور برای تغییر کلید موجود و افزودن کلید جدید به کار می‌رود.
student["age"] = 21
student["city"] = "Tehran"
student.update({"age": 22, "active": False})
print("4) Change and add:", student)

# ۵. pop مقدار حذف‌شده را برمی‌گرداند. مقدار پیش‌فرض مانع KeyError می‌شود.
city = student.pop("city")
print("5) Removed:", city)
print("Missing phone:", student.pop("phone", "Not found"))
del student["active"]
print("After del:", student)

# ۶. clear محتوا را خالی می‌کند، خود متغیر هنوز وجود دارد.
temporary = {"note": "draft"}
temporary.clear()
print("6) Clear:", temporary)

# ۷. حلقهٔ مستقیم روی Dictionary، کلیدها را می‌دهد.
scores = {"Python": 18, "Math": 16, "English": 19}
print("7) Keys:")
for subject in scores:
    print(subject, scores[subject])

# ۸. keys و values و items نما هستند. برای یک عکس لحظه‌ای می‌توان list ساخت.
print("8) Keys:", list(scores.keys()))
print("Values:", list(scores.values()))
print("Items:", list(scores.items()))
for subject, score in scores.items():
    print(subject, "=", score)

# ۹. جمع‌زدن با حلقه، بدون نیاز به تابع‌نویسی.
total = 0
for score in scores.values():
    total += score
print("9) Average:", total / len(scores))

# ۱۰. انتساب، کپی نمی‌سازد. دو نام به همان دیکشنری اشاره می‌کنند.
original = {"pen": 3, "book": 2}
alias = original
alias["pen"] = 8
print("10) Alias changes original:", original["pen"])  # 8

# ۱۱. copy برای کلیدها و مقادیر ساده، کپی جداگانه می‌سازد.
copied = original.copy()
copied["pen"] = 1
print("11) Original:", original["pen"], "Copy:", copied["pen"])

# ۱۲. copy سطحی است: لیست داخلی همچنان بین دو دیکشنری مشترک است.
profile = {"name": "Sara", "skills": ["Python"]}
other_profile = profile.copy()
other_profile["skills"].append("HTML")
print("12) Shared inner list:", profile["skills"])

# ۱۳. هر هزینه یک Dictionary است. چند هزینه را در List نگه می‌داریم.
expenses = [
    {"title": "Book", "amount": 200000, "category": "Education"},
    {"title": "Bus", "amount": 50000, "category": "Transport"},
]
total = 0
for expense in expenses:
    total += expense["amount"]
    print(expense["title"], expense["amount"])
print("13) Total:", total)  # 250000
