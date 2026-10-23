import json


file = "students.json"
res_file = "students_processed.json"
try:
    with open(file, "r", encoding="utf-8") as f:
        students = json.load(f)
    best_student = None
    for student in students:
        if student["score"] >= 60:
            student["passed"] = True
        else:
            student["passed"] = False
        if best_student is None or student["score"] > best_student["score"]:
            best_student = student
    if best_student:
        print(f"cтудент с максимальным баллом: {best_student['name']} ({best_student['score']} баллов)")
    with open(res_file, "w", encoding="utf-8") as f:
        json.dump(students, f, indent=4)
except FileNotFoundError:
    print(f"error: {file} не найден.")
