import random

def shuffle_answers(question, choices):
    """Shuffle the answer choices for a given question."""
    answer = choices[0]
    random.shuffle(choices)
    return question, choices, choices.index(answer) + 1

def ask_question(question, choices):
    """Display the question and answer choices, and get the user's answer."""
    print(f"\n{question}")
    for i, choice in enumerate(choices, start=1):
        print(f"  {i}) {choice}")
    while True:
        try:
            user_choice = int(input("Your answer: "))
            if 1 <= user_choice <= len(choices):
                return user_choice
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Please enter a number.")

def display_results(score, total_questions, correct_answers):
    """Display the user's score and which questions they answered incorrectly."""
    percentage = (score / total_questions) * 100
    print(f"\nYour score: {score}/{total_questions} ({percentage:.2f}%)")
    if correct_answers:
        print("\nReview of your answers:")
        for idx, details in correct_answers.items():
            question, user_answer, correct_choice, correct_answer = details
            print(f"\nQuestion: {question}")
            print(f"Your answer: {user_answer}) {correct_choice}")
            print(f"Correct answer: {correct_answer}) {correct_choice}")

questions = [
    ("What is the first stage of a typical project life cycle?", ["Initiating", "Planning", "Executing", "Closing"]),
    ("Which of the following is NOT a common project constraint?", ["Quality", "Scope", "Time", "Cost"]),
    ("A Gantt chart is a visual tool used to represent:", ["Project timeline", "Project budget", "Project risk assessment", "Project communication plan"]),
    ("What does the acronym 'PERT' stand for in project management?", ["Program Evaluation and Review Technique", "Project Evaluation and Risk Tracking", "Project Execution and Reporting Tool", "Program Evaluation and Resource Tracking"]),
    ("A Work Breakdown Structure (WBS) is used to:", ["Break down project deliverables into smaller tasks", "Identify project risks", "Allocate project resources", "Track project progress"]),
    ("Many people use _______ to have a standard format for preparing various project management documents.", ["Templates", "Methodologies", "Standards", "Project Management Software"]),
    ("Which of the following processes is not part of project integration management?", ["Develop the project business case", "Develop the project charter", "Develop the project management plan", "Close the project or phase"]),
    ("What is the role of a project sponsor?", ["Provides financial support for the project", "Manages the project team", "Executes the project tasks", "Monitors project progress"]),
    ("A project manager's primary responsibility is to:", ["Ensure the project meets its objectives within scope, time, and cost constraints", "Complete project tasks on time", "Manage the project budget", "Communicate with stakeholders"]),
    ("Initiating involves developing a project charter, which is part of the project _________ management knowledge area.", ["Integration", "Scope", "Risk", "Communication"]),
    ("What type of report do project teams create to reflect on what went right and what went wrong with the project?", ["Lessons-Learned Report", "Business Case", "Progress Report", "Final Project Report"]),
    ("Which of the following outputs is often completed before initiating a project?", ["Business Case", "Project Charter", "Kick-off meeting", "Stakeholder Register"]),
    ("Which statement relates to the definition of the Planning Process?", ["Defines and refines the project objectives", "Defines and Authorizes Project or Phase", "Coordinate resources to carry out the plan", "Ensuring that project objectives are met"]),
    ("You are a Project Manager in a Highway Construction Project. You are now working if there are changes to the scope, schedule, budget of the project. These assignments are part of which process.", ["Monitoring and Controlling", "Initiating", "Planning", "Executing"]),
    ("You are working on a large project which has several smaller projects within it. This is:", ["Program", "Project Subprojects", "Project Life Cycle", "Operating of Portfolio"]),
    ("Which of the following factors can definitely make a project fail?", ["The project team fails to communicate and build up working relations with the customer.", "The project team does not have insufficient skills", "The customer raises a lot of change requests.", "A key team member is pulled away from the project due to changing priority."]),
    ("Applying Project Management can help you achieve:", ["All of the above", "Personal and professional success", "A sense of self worth and pride", "A better understanding of how things work"])
]

def main():
    num_questions = 10
    selected_questions = random.sample(questions, num_questions)
    score = 0
    correct_answers = {}

    for idx, (question, answers) in enumerate(selected_questions, start=1):
        question, shuffled_choices, correct_index = shuffle_answers(question, answers)
        user_choice = ask_question(question, shuffled_choices)

        if user_choice == correct_index:
            score += 1
        else:
            correct_answers[idx] = (
                question,
                user_choice,
                shuffled_choices[user_choice - 1],
                correct_index,
            )

    display_results(num_questions, correct_answers)

main()
