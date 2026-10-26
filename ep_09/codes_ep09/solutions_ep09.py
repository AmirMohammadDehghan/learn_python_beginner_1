"""پاسخ پیشنهادی تمرین‌های جلسه ۹."""

stock = {"pen": 10, "notebook": 5}
stock["pen"] = 8
stock["book"] = 3
print("Pencil:", stock.get("pencil", 0))
stock.pop("notebook")
total = 0
for name, count in stock.items():
    print(name, count)
    total += count
print("Total stock:", total)  # 11

scores = {"Python": 18, "Math": 16, "English": 19}
total = 0
for score in scores.values():
    total += score
# این شرط برای دیکشنری خالی از تقسیم بر صفر جلوگیری می‌کند.
if len(scores) > 0:
    print("Average:", total / len(scores))
else:
    print("No scores")

new_scores = scores.copy()
new_scores["Math"] = 20
print("Original Math:", scores["Math"])  # 16
print("New Math:", new_scores["Math"])  # 20
print("History:", scores.get("History", "Not recorded"))

for subject, score in scores.items():
    if score >= 18:
        print("High score:", subject)
