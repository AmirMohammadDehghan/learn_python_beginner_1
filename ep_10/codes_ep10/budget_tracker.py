"""پروژه پایانی: دفتر هزینه و کنترل بودجه با مباحث پایتون مقدماتی ۱.

اجرا: python budget_tracker.py
مبالغ، عدد صحیح مثبت و بر حسب تومان هستند.
داده‌ها فقط تا پایان اجرای برنامه در حافظه می‌مانند.
"""

# Tuple: دسته‌های ثابت. List: فهرست هزینه‌هایی که تغییر می‌کند.
categories = ("خوراک", "رفت‌وآمد", "آموزش", "سایر")
expenses = []
next_id = 1

print("دفتر هزینهٔ شخصی")
print("مبلغ‌ها را به تومان، بدون جداکننده و حداکثر با ۹ رقم بنویسید.")
print("با خروج از برنامه، داده‌های این اجرا پاک می‌شوند.")

# اعتبارسنجی پیش از int: رقم‌های ده‌دهی فارسی و انگلیسی پذیرفته می‌شوند.
while True:
    budget_text = input("بودجهٔ این دوره: ").strip()
    if not budget_text.isdecimal() or len(budget_text) > 9:
        print("بودجه باید یک عدد صحیح مثبت با حداکثر ۹ رقم باشد.")
        continue
    budget = int(budget_text)
    if budget <= 0:
        print("بودجه باید بزرگ‌تر از صفر باشد.")
        continue
    break

while True:
    print("\n1. ثبت هزینه")
    print("2. نمایش هزینه‌ها")
    print("3. گزارش بودجه و دسته‌ها")
    print("4. حذف هزینه با شناسه")
    print("0. خروج")
    choice_text = input("انتخاب: ").strip()
    if not choice_text.isdecimal() or len(choice_text) != 1:
        print("گزینهٔ نامعتبر؛ عدد ۰ تا ۴ را وارد کنید.")
        continue
    choice = int(choice_text)

    if choice == 0:
        print("پایان برنامه؛ داده‌های این اجرا در فایل ذخیره نشده‌اند.")
        break

    elif choice == 1:
        title = input("عنوان هزینه: ").strip()
        if title == "":
            print("عنوان هزینه نباید خالی باشد.")
            continue

        amount_text = input("مبلغ به تومان: ").strip()
        if not amount_text.isdecimal() or len(amount_text) > 9:
            print("مبلغ باید عدد صحیح مثبت با حداکثر ۹ رقم باشد.")
            continue
        amount = int(amount_text)
        if amount <= 0:
            print("مبلغ باید بزرگ‌تر از صفر باشد.")
            continue

        for index in range(len(categories)):
            print(index + 1, categories[index])
        category_text = input("شمارهٔ دسته: ").strip()
        if not category_text.isdecimal() or len(category_text) != 1:
            print("شمارهٔ دسته نامعتبر است.")
            continue
        category_number = int(category_text)
        if category_number < 1 or category_number > len(categories):
            print("شمارهٔ دسته باید بین ۱ و ۴ باشد.")
            continue

        # در هر ثبت، یک دیکشنری تازه ساخته می‌شود.
        expense = {
            "id": next_id,
            "title": title,
            "amount": amount,
            "category": categories[category_number - 1],
        }
        expenses.append(expense)
        print(f"هزینه با شناسهٔ {next_id} ثبت شد.")
        next_id += 1

    elif choice == 2:
        if len(expenses) == 0:
            print("هنوز هزینه‌ای ثبت نشده است.")
        else:
            for expense in expenses:
                print(f"شناسه: {expense['id']} | {expense['title']}")
                print(f"مبلغ: {expense['amount']} تومان | {expense['category']}")

    elif choice == 3:
        # هر بار از داده‌های فعلی گزارش می‌سازیم تا حذف‌ها هم اثر کنند.
        total = 0
        category_totals = {}
        used_categories = set()
        for category in categories:
            category_totals[category] = 0
        for expense in expenses:
            total += expense["amount"]
            category_totals[expense["category"]] += expense["amount"]
            used_categories.add(expense["category"])

        remaining = budget - total
        print(f"بودجه: {budget} تومان")
        print(f"مجموع هزینه: {total} تومان")
        print(f"باقی‌مانده: {remaining} تومان")
        if remaining < 0:
            print(f"هشدار: {-remaining} تومان بیشتر از بودجه خرج شده است.")
        elif remaining == 0:
            print("بودجه دقیقاً مصرف شده است.")
        else:
            print("هنوز از بودجه باقی مانده است.")

        print(f"تعداد دسته‌های استفاده‌شده: {len(used_categories)}")
        for category, category_total in category_totals.items():
            print(f"{category}: {category_total} تومان")

    elif choice == 4:
        id_text = input("شناسهٔ هزینه برای حذف: ").strip()
        if not id_text.isdecimal() or len(id_text) > 9:
            print("شناسه باید یک عدد صحیح مثبت با حداکثر ۹ رقم باشد.")
            continue
        target_id = int(id_text)
        if target_id <= 0:
            print("شناسه باید بزرگ‌تر از صفر باشد.")
            continue
        found = False
        for index in range(len(expenses)):
            if expenses[index]["id"] == target_id:
                removed = expenses.pop(index)
                print(f"هزینهٔ «{removed['title']}» حذف شد.")
                found = True
                # پس از تغییر List، پیمایش را بلافاصله پایان می‌دهیم.
                break
        if not found:
            print("هزینه‌ای با این شناسه پیدا نشد.")

    else:
        print("گزینهٔ نامعتبر؛ عدد ۰ تا ۴ را وارد کنید.")
