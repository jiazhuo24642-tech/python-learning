from utils import load_students


def show_all_students(students):
    print("\n所有学生：")

    for student in students:
        print(student)


def find_student(students, name):
    for student in students:
        if student.name == name:
            return student

    return None


def show_average_score(students):
    if not students:
        print("没有学生数据")
        return

    total = sum(student.score for student in students)
    average = total / len(students)

    print(f"\n平均分：{average:.2f}")


def show_highest_score(students):
    if not students:
        print("没有学生数据")
        return

    student = max(students, key=lambda s: s.score)

    print(f"\n最高分：{student}")


def show_a_students(students):
    print("\nA等级学生：")

    for student in students:
        if student.get_grade() == "A":
            print(student)


def main():
    try:
        students = load_students("students.json")
    except (FileNotFoundError, ValueError) as e:
        print(f"加载失败：{e}")
        return

    while True:
        print("\n====== 学生成绩管理系统 ======")
        print("1. 查看所有学生")
        print("2. 查询学生")
        print("3. 查看平均分")
        print("4. 查看最高分")
        print("5. 查看所有A等级学生")
        print("0. 退出")

        choice = input("请选择功能：")

        if choice == "1":
            show_all_students(students)

        elif choice == "2":
            name = input("请输入学生姓名：")
            student = find_student(students, name)

            if student:
                print(student)
            else:
                print("没有找到该学生")

        elif choice == "3":
            show_average_score(students)

        elif choice == "4":
            show_highest_score(students)

        elif choice == "5":
            show_a_students(students)

        elif choice == "0":
            print("程序退出")
            break

        else:
            print("无效选项，请重新输入")


if __name__ == "__main__":
    main()