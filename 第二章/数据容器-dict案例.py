"""
开发一个教务管理系统,在该系统中可以维护和管理学员的成绩信息,具体要求如下:
1. 添加学生信息: 根据提示录入学生姓名,语文,数学,英语成绩,录入完成保存到系统中
2. 修改学生信息: 要求输入要修改的学生姓名,然后再提示输入语文,数学,英语成绩,输入完成后修改学员信息.
3. 删除学生信息: 要求输入要删除的学生姓名,根据姓名删除学生信息.
4. 查询学生信息: 要求输入要查询的学生姓名,根据姓名查询学生信息并输出
5. 列出所有学生: 遍历所有学生信息并输出
6. 统计班级成绩: 统计班级语文,数学,英语成绩的最高分,最低分,平均分,以及语文,数学,英语最高分和最低分的学员姓名
7. 退出系统
"""
students_dict = {}
print("欢迎使用教务管理系统")
menu = """
================================================================================================================
#1.添加学生信息  2.修改学生信息  3.删除学生信息  4.查询学生信息  5.列出所有学生  6.统计班级成绩  7.退出系统
================================================================================================================
"""
while True:
    print(menu)
    choice = input("请输入您需要执行的操作(1-7):")
    match choice:
        case "1":# 添加学生信息
            student_name = input("请输入要添加的学生姓名:")
            # 如果该学生信息已存在，则不执行添加，提示信息
            if student_name in students_dict:
                print("该学生系统里已有信息，请重新选择是否需要修改该学生信息。")
                continue
            chinese_score = float(input("请输入要添加学生的语文成绩:"))
            math_score = float(input("请输入要添加学生的数学成绩:"))
            english_score = float(input("请输入要添加学生的英语成绩:"))
            students_dict[student_name] = {"chinese": chinese_score, "math": math_score, "english": english_score}
            print(f"{student_name}的信息添加成功.")
        case "2":# 修改学生信息
            student_name = input("请输入要修改信息的学生姓名:")
            if student_name not in students_dict:
                print("无法查到该学生信息,无法做出修改操作,请重新输入.")
                continue
            chinese_score = float(input("请输入要修改学生的最新语文成绩:"))
            math_score = float(input("请输入要修改学生的最新数学成绩:"))
            english_score = float(input("请输入要修改学生的最新英语成绩:"))
            students_dict[student_name] = {"chinese": chinese_score,"math": math_score, "english": english_score}
            print(f"{student_name}的信息修改成功!")

        case "3": # 删除学生信息
            student_name = input("请输入要删除信息的学生姓名:")
            if student_name not in students_dict:
                print("无法查到该学生信息,无法做删除操作,请重新输入.")
                continue
            del students_dict[student_name]
            print(f"{student_name}的信息已成功删除.")

        case "4": # 查询学生信息
            student_name = input("请输入要查询信息的学生姓名:")
            if student_name not in students_dict:
                print("输入错误,无法查到该学生信息.")
                continue
            student_info = students_dict[student_name]
            print(f"该学生的语文成绩为{student_info['chinese']},数学成绩为:{student_info['math']},英语成绩为:{student_info['english']}")

        case "5":# 列出所有学生信息
            for student_name in students_dict.keys():
                student_info = students_dict[student_name]
                print(f"学生姓名：{student_name}，语文成绩为{student_info['chinese']}，数学成绩为:{student_info['math']}，英语成绩为:{student_info['english']}")

        case "6":#统计班级成绩
            # 统计班级语文,数学,英语的最高分,最低分和平均分
            chinese_scores = []
            math_scores = []
            english_scores = []
            # 分别获取所有学科成绩
            for student_name, scores in students_dict.items():
                chinese_scores.append(scores["chinese"])
                math_scores.append(scores["math"])
                english_scores.append(scores["english"])

            #统计最高分,最低分,平均分,平均分
            chinese_max = max(chinese_scores)
            chinese_min = min(chinese_scores)
            chinese_avg = sum(chinese_scores)/len(chinese_scores)


            math_max = max(math_scores)
            math_min = min(math_scores)
            math_avg = sum(math_scores)/len(math_scores)

            english_max = max(english_scores)
            english_min = min(english_scores)
            english_avg = sum(english_scores)/len(english_scores)

            # 统计语文,数学,英语 最高分最低分的学生
            chinese_max_student = [name for name,scores in students_dict.items() if scores['chinese'] == chinese_max]
            chinese_min_student = [name for name, scores in students_dict.items() if scores['chinese'] == chinese_min]

            math_max_student = [name for name,scores in students_dict.items() if scores['math'] == math_max]
            math_min_student = [name for name,scores in students_dict.items() if scores['math'] == math_min]

            english_max_student = [name for name,scores in students_dict.items() if scores['english'] == english_max]
            english_min_student = [name for name,scores in students_dict.items() if scores['english'] == english_min]

            print(f"语文最高分是:{chinese_max},最低分是:{chinese_min},平均分是:{chinese_avg}")
            print(f"数学最高分是:{math_max},最低分是:{math_min},平均分是:{math_avg}")
            print(f"英语最高分是:{english_max},最低分是:{english_min},平均分是:{english_avg}")

            print(f"语文最高分的学生是:{chinese_max_student},最低分的学生是:{chinese_min_student}")
            print(f"数学最高分的学生是:{math_max_student},最低分的学生是:{math_min_student}")
            print(f"英语最高分的学生是:{english_max_student},最低分的学生是:{english_min_student}")


        case "7": # 退出系统
            print("Bye")
            break
        case _:
            print("非法操作,不支持.")
