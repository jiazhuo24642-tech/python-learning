import json
from student import Student


def load_students(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"文件不存在: {filename}")
    except json.JSONDecodeError:
        raise ValueError("JSON 文件格式错误")

    students = []

    for item in data:
        if "name" not in item or "score" not in item:
            raise ValueError("学生数据缺少 name 或 score")

        student = Student(
            item["name"],
            item["score"]
        )
        students.append(student)

    return students