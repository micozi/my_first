import sys
print('HELLO WORLD')
print('Production?')

def continue_queue_on_input(student_name: str):
    user_input = input("Continue? (y/n): ")
    if user_input == "y":
        user_imput2 = input(f"Retry {student_name}? (y/n): ")
        if user_imput2 == "y":
            return "retry"
        elif user_imput2 == "n":
            return "do not retry"
    elif user_input == "n":
        sys.exit()

def main():
    """
    EUD Retry fields
    # Class Lectio ID
    # Class name
    # Student Lectio ID
    # Student name
    # Physical delinquency
    # Written delinquency
    """

    student_delinquency_data = [['class id 1','class 1','student id 1','student 1', 'del-a 1', 'del-b 1'],
                                ['class id 2','class 2','student id 2','student 2', 'del-a 2', 'del-b 2'],
                                ['class id 3','class 3','student id 3','student 3', 'del-a 3', 'del-b 3'],
                                ['class id 4','class 4','student id 4','student 4', 'del-a 4', 'del-b 4']]

    for student in student_delinquency_data:
        print(student)
        shall_retry = continue_queue_on_input(student)
        if shall_retry == "retry":
            retry_temp = []
            retry_temp.append(student[0])
            retry_temp.append(student[1])
            retry_temp.append(student[2])
            retry_temp.append(student[3])
            retry_temp.append(student[4])
            retry_temp.append(student[5])
            student_delinquency_data.append(retry_temp)
            print(f'{student[3]} is re-added to the queue.')


if __name__ == "__main__":
    main()