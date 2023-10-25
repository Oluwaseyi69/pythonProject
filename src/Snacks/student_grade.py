
def class_summary(scores, number_of_subjects):
    print("=================================================")
    print(f"Class summary - {number_of_subjects} SUBJECTS")
    print("=================================================")
    print("STUDENT\t\t", end="")

    for subject in range (1, number_of_subjects + 1):
        print(f"SUB{subject}\t", end="")

    print("TOT\t\tAVE\t\tPOS")
    print("=================================================")

    sorted_scores = sorted([(sum(student), i) for i, student in enumerate(scores)], reverse=True)
    sorted_position = {student[1]: pos for pos, student in enumerate(sorted_scores, start=1)}

    for index in range(len(scores)):
        total = sum(scores[index])
        average = total/number_of_subjects
        pos = sorted_position[index]

        print(f"Student {index + 1}", end="\t")
        for score in scores[index]:
            print(f"{score}\t\t", end="")
        print(f"{total}\t\t{average:.2f}\t\t{pos}")

    print("==================================================")


def subject_summary(scores):
    print("SUBJECT SUMMARY")

    for row in range(len(scores[0])):
        highest = -1
        lowest = 101
        total = 0
        passes = 0
        failures = 0
        highest_student = -1
        lowest_student = -1

        for column in range(len(scores)):
            score = scores[column][row]
            total+= score

            if score >= 50:
                passes += 1
            else:
                failures += 1

            if score > highest:
                highest = score
                highest_student = column
            if score < lowest:
                lowest = score
                lowest_student = column
        average = total / len(scores)

        print(f"Subject {row + 1}")
        print(f"Highest scoring student is: Student {highest_student + 1} scoring {highest}")
        print(f"Lowest scoring student is: Student {lowest_student + 1} scoring {lowest}")
        print(f"Total score is: {total}")
        print(f"Average score is: {average:.2f}")
        print(f"Number of passes: {passes}")
        print(f"NUmber of failures: {failures}\n")


def hardest_and_easiest_subjects(scores):
    hardest_subject = -1
    easiest_subject = -1
    min_failures = len(scores) + 1
    max_passes = -1

    for j in range(len(scores [0])):
        failures = 0
        passes = 0

        for i in range(len(scores)):
            score = scores[i][j]

            if score < 50:
                failures +=1

            else:
                passes += 1

        if failures < min_failures:
            hardest_subject = j
            min_failures = failures
        if passes > max_passes:
            easiest_subject = j
            max_passes = passes

    print(f"The hardest subject {hardest_subject + 1} with {min_failures} failures")
    print(f"The easiest subject{easiest_subject + 1} with {max_passes}")


def print_subject(number_of_subject):
    for _ in range(1, number_of_subject + 1):
        print('Subject 1')


def display_overall_scores(scores):
    best_student = -1
    worst_student = -1
    max_total = -1
    min_total = len(scores[0]) * 101
    total_scores = 0

    for i in range(len(scores)):
        total = sum(scores[i])
        total_scores += total

        if total > max_total:
            best_student = 1
            max_total = total

        if total < min_total:
            worst_student = 1
            min_total = total

    print("CLASS SUMMARY")
    print("==================================")
    print(f" Best Graduating Student is: Student {best_student + 1} scoring {max_total}")
    print("==================================")

    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print(f" Worst Graduating Student is: Student {worst_student + 1} scoring {min_total}")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    class_average = total_scores / len(scores) + len(scores[0])
    print("=================================")
    print(f"class total score is: {total_scores}")
    print(f"class average score is: {class_average: .2f}")
    print("=================================")


def main():
    number_of_student = int(input("How many students do you have: "))
    number_of_subject = int(input("How many subjects do thay offer: "))
    scores = []

    for x in range(number_of_student):
        print(f'Entering scores for student {x + 1}:')
        student_scores = []
        for y in range(number_of_subject):
            score = int(input(f"Enter score for subject {y + 1}: "))
            student_scores.append(score)
        scores.append(student_scores)

    class_summary(scores, number_of_subject)
    subject_summary(scores)
    hardest_and_easiest_subjects(scores)
    display_overall_scores(scores)

if __name__=="__main__":
    main()

















