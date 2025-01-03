import tkinter as tk
from tkinter import ttk, messagebox
import random
import time

# Questions and Answers
questions = [
    {
        "question": "What is the first stage of a typical project life cycle?",
        "choices": ["Planning", "Executing", "Initiating", "Closing"],
        "answer": "Initiating"
    },
    {
        "question": "Which of the following is NOT a common project constraint?",
        "choices": ["Scope", "Time", "Cost", "Quality"],
        "answer": "Quality"
    },
    {
        "question": "A Gantt chart is a visual tool used to represent:",
        "choices": ["Project budget", "Project timeline", "Project risk assessment", "Project communication plan"],
        "answer": "Project timeline"
    },
    {
        "question": "What does 'PERT' stand for in project management?",
        "choices": [
            "Program Evaluation and Review Technique",
            "Project Evaluation and Risk Tracking",
            "Project Execution and Reporting Tool",
            "Program Evaluation and Resource Tracking"
        ],
        "answer": "Program Evaluation and Review Technique"
    },
    {
        "question": "A Work Breakdown Structure (WBS) is used to:",
        "choices": [
            "Identify project risks",
            "Allocate project resources",
            "Break down project deliverables into smaller tasks",
            "Track project progress"
        ],
        "answer": "Break down project deliverables into smaller tasks"
    },
    {
        "question": "Many people use _______ to have a standard format for preparing various project management documents.",
        "choices": ["Templates", "Methodologies", "Standards", "Closing"],
        "answer": "Templates",
    },
    {
        "question": "Which of the following processes is not part of project integration management?",
        "choices": ["Develop the project charter", "Develop the project management plan", "Develop the project business case", "Close the project or phase"],
        "answer": "Develop the project business case"
    },
    {
        "question": "What is the role of a project sponsor?",
        "choices": ["Manages the project team", "Provides financial support for the project", "Executes the project tasks", "Monitors project progress"],
        "answer": "Provides financial support for the project"
    },
    {
        "question": "A project manager's primary responsibility is to:",
        "choices": [
            "Complete project tasks on time",
            "Ensure the project meets its objectives within \nscope, time, and cost constraints",
            "Manage the project budget",
            "Communicate with stakeholders"
        ],
        "answer": "Ensure the project budget meets its objectives within scope, time, and cost constraints"
    },
    {
        "question": "Initiating involves developing a project charter, which is part of the project _________ management knowledge area.:",
        "choices": [
            "Scope", "Risk", "Communication", "Integration"
        ],
        "answer": "Integration"
    },
    {
        "question": "What type of report do project teams create to reflect on what went right and what went wrong with the project?",
        "choices": ["Business Case", "Progress Report", "Lessons-Learned Report", "Final Project Report"],
        "answer": "Lesson-Learned Report"
    },
    {
        "question": "Which of the following outputs is often completed before initiating a project?",
        "choices": ["Business Case", "Project Charter", "Kick-off meeting", "Stakeholder Register"],
        "answer": "Business Case"
    },
    {
        "question": "Which statement relates to the definition of the Planning Process?",
        "choices": ["Defines and Authorises Project or Phase",
                     "Coordinate resources to carry out the plan",
                     "Defines and refines the project objectives",
                     "Ensuring that project objectives are met"],
        "answer": "Defines and refines the project objectives"
    },
    {
        "question": "You are a Project Manager in a Highway Construction Project. You are now working if there are changes to the scope, schedule, budget of the project. These assignments are part of which process.",
        "choices": [
            "Initiating",
            "Planning",
            "Executing",
            "Monitoring and Controlling"
        ],
        "answer": "Monitoring and Controlling"
    },
    {
        "question": "You are working on a large project which has several smaller projects within it. This is",
        "choices": [
            "Program",
            "Project Life Cycle",
            "Project Subprojects",
            "Operating of Portfolio"
        ],
        "answer": "Project Subprojects"
    },
    {
        "question": "Which of the following factors can definitely make a project fail?",
        "choices": ["The project team does not have insufficient skills",
                    "The customer raises a lot of change requests.",
                    "The project team fails to communicate and\nbuild up working relation with the customer.",
                    "A key team member is pulled away from the\nproject due to changing priority"],
        "answer": "The project team fails to communicate and build up working relation with the customer.",
    },
    {
        "question": "Applying Project Management can help you achieve:",
        "choices": ["Personal and professional success",
                    "A sense of self worth and pride",
                    "A better understanding of how things work",
                    "All of the above"],
        "answer": "All of the above"
    },
    {
        "question": "What is the primary role of a project manager?",
        "choices": ["To manage the project budget",
                    "To manage the project schedule",
                    "To lead the project team",
                    "All of the above"],
        "answer": "To lead the project team"
    },
    {
        "question": "What is the first step in project planning?",
        "choices": [
            "Defining the project scope",
            "Creating a project schedule",
            "Manage the project budget",
            "Identifying project risks"
        ],
        "answer": "Defining the project scope"
    },
    {
        "question": "What is a project baseline?",
        "choices": [
            "A list of project risks",
            "A schedule of project task",
            "A snapshot of project performance",
            "A plan for project completion"
        ],
        "answer": "A snapshot of project performance"
    },
    {
        "question": "What is a project charter?",
        "choices": [
            "A list of project risks",
            "A list of project task",
            "A document that formally authorizs a project",
            "A plan for project completion"
        ],
        "answer": "A document that formally authorizs a project"
    },
    {
        "question": "What is a project schedule?",
        "choices": [
            "A plan for project execution",
            "A list of project task",
            "A schedule of project milestone",
            "A snapshot of project performance"
        ],
        "answer":  "A schedule of project milestone",
    },
    {
        "question": "What is project plan?",
        "choices": [
            "A list of project tasks",
            "A schedule of project milestone",
            "A plan for project execution",
            "Someone who monitors the project",
        ],
        "answer": "A plan for project execution"
    },
    {
        "question": "What is a project risk?",
        "choices": ["An event that could impact the project negatively",
                    "An event that could impact the project positively",
                    "A project milestone",
                    "A project task"],
        "answer": "An event that could impact the project negatively",
    },
    {
        "question": "What is a project deliverable?",
        "choices": ["A project milestone",
                    "A project task",
                    "A product or service produced by the project",
                    "All of the above"],
        "answer": "A product or service produced by the project"
    },
    {
        "question": "During which process group are the majority of the project's budget and resources typically utilized?",
        "choices": ["Initiating",
                    "Planning",
                    "Executing",
                    "Closing"],
        "answer": "Executing"
    },
    {
        "question": "Which type of project organizational sructure best describes a scenario where team members report both to their functional manager and the project manager?",
        "choices": [
            "Functional",
            "Matrix",
            "Projectized",
            "Hierarchical",
        ],
        "answer": "Matrix",
    },
    {
        "question": "What is a critical path in project management?",
        "choices": [
            "The shortest path through the project schedule",
            "The longest sequence of activities determining project duration",
            "A list of critical risks for the project",
            "The sequence of activities requiring the least resources"
        ],
        "answer": " The longest sequence of activities determining project duration"
    },
    {
        "question": "What is scope creep?",
        "choices": [
            "The process of reducing project scope to meet constraints",
            "Uncontrolled changes or growth in a project’s scope",
            "The process of clarifying project deliverables",
            "Reviewing project objectives to align with stakeholder goals"
        ],
        "answer": "Uncontrolled changes or growth in a project’s scope"
    },
    {
        "question": "What is the purpose of a risk register?",
        "choices": [
            "To track the project’s schedule",
            "To record and monitor identified risks and their mitigation plans",
            "To assign resources to project activities",
            "To track project costs and expenditures"
        ],
        "answer":  "A document that outlines the project's objectives, deliverables, and boundaries"
    },
]

# Shuffle the questions array to randomize the order of questions in the quiz
random.shuffle(questions)
questions = questions[:10]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quest-ion Impossible: Project Management Edition")
        self.root.geometry("800x600")
        self.root.configure(bg="white")

        self.score = 0
        self.current_question = 0
        self.user_name = None
        self.user_answers = []

        # Timer variables
        self.start_time = None
        self.end_time = None

        self.create_welcome_screen()

    def create_welcome_screen(self):
        """Create the welcome screen where the user inputs their name."""
        for widget in self.root.winfo_children():
            widget.destroy()

        # Define a custom style for the label
        style = ttk.Style()
        style.configure(
            "Welcome.TLabel", 
            font=("Courier New", 20, "bold"), 
            foreground="#000080"
        )

        # Apply the custom style to the label
        ttk.Label(
            self.root, 
            text="Welcome to Quest-ion Impossible:\nProject Management Edition!", 
            style="Welcome.TLabel", 
            justify="center"
        ).pack(pady=20)

        ttk.Label(self.root, text="Enter your name:", font=("Courier New", 13)).pack(pady=10)
        self.name_entry = ttk.Entry(self.root, width=30, font=("Courier New", 12))
        self.name_entry.pack(pady=10)

        style = ttk.Style()
        style.configure(
            "Custom.TButton", 
            font=("Courier New", 12, "bold")
        )

        ttk.Button(
            self.root, 
            text="Start", 
            style="Custom.TButton", 
            command=self.start_quiz
        ).pack(pady=20)

    def show_timer_popup(self):
        """Show a popup window indicating that the timer has started."""
        popup = tk.Toplevel(self.root)
        popup.title("Notice")
        popup.geometry("300x150")

        ttk.Label(
            popup,
            text="Your timer starts now!",
            font=("Courier New", 14),
            justify="center"
        ).pack(pady=20)

        ttk.Button(
            popup,
            text="OK",
            command=lambda: [popup.destroy(), self.start_timer()]
        ).pack(pady=10)

    def start_timer(self):
        """Start the timer and load the first question."""
        self.start_time = time.time()
        self.load_question_screen()

    def start_quiz(self):
        """Start the quiz and show the timer popup."""
        self.user_name = self.name_entry.get().strip()
        if not self.user_name:
            messagebox.showwarning("Name Required", "Please enter your name to proceed.")
        else:
            self.show_timer_popup()

    def load_question_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.question_label = ttk.Label(
            self.root, text="", wraplength=450, font=("Courier New", 17), justify="center"
        )
        self.question_label.pack(pady=20)

        self.answer_buttons = []
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=15)

        for i in range(4):
            button = ttk.Button(
                self.button_frame,
                text="", 
                command=lambda i=i: self.check_answer(i)
            )
            button.grid(row=i // 2, column=i % 2, padx=20, pady=20, sticky="ew")
            self.answer_buttons.append(button)

        for col in range(2):
            self.button_frame.columnconfigure(col, weight=1)

        self.load_question()

    def load_question(self):
        if self.current_question < len(questions):
            question_data = questions[self.current_question]
            self.question_label.config(text=question_data["question"])
            choices = question_data["choices"]
            random.shuffle(choices)
            for i, choice in enumerate(choices):
                self.answer_buttons[i].config(text=choice)
        else:
            self.show_results_button()

    def check_answer(self, index):
        question_data = questions[self.current_question]
        selected_answer = self.answer_buttons[index].cget("text")
        self.user_answers.append(selected_answer)

        if selected_answer == question_data["answer"]:
            self.score += 1
        
        self.current_question += 1
        self.load_question()

    def show_results_button(self):
        self.question_label.config(text="Quiz Finished! Click the button below to see your results.")
        for button in self.answer_buttons:
            button.destroy()

        ttk.Button(
            self.root,
            text="See Results",
            style="Custom.TButton",
            command=self.show_results
        ).pack(pady=20)

    def show_results(self):
        """Display the user's score and the time taken to complete the quiz."""
        for widget in self.root.winfo_children():
            widget.destroy()

        self.end_time = time.time()  # End the timer
        time_taken = self.end_time - self.start_time
        minutes, seconds = divmod(time_taken, 60)

        percentage_score = (self.score / len(questions)) * 100
        ttk.Label(
            self.root,
            text=(
                f"Thank you, {self.user_name}!\n\n"
                f"Your Score: {self.score}/{len(questions)} ({percentage_score:.2f}%)\n\n"
                f"Time Taken: {int(minutes)} minutes and {int(seconds)} seconds."
            ),
            font=("Courier New", 14),
            wraplength=550,
            justify="center"
        ).pack(pady=20)
    
        answer_frame = ttk.Frame(self.root)
        answer_frame.pack(fill="both", expand=True, padx=10, pady=10)

        canvas = tk.Canvas(answer_frame)
        scrollbar = ttk.Scrollbar(answer_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        for i, question in enumerate(questions):
            user_answer = self.user_answers[i]
            correct_answer = question["answer"]

            ttk.Label(scrollable_frame, text=f"Q{i+1}: {question['question']}", font=("Arial", 12, "bold"), wraplength=500).pack(anchor="w", pady=5)
            ttk.Label(scrollable_frame, text=f"Your Answer: {user_answer}", font=("Arial", 12), wraplength=500).pack(anchor="w")
            ttk.Label(scrollable_frame, text=f"Correct Answer: {correct_answer}", font=("Arial", 12), wraplength=500, foreground="#000080").pack(anchor="w", pady=(0, 10))


        ttk.Button(
            self.root,
            text="Restart Quiz",
            style="Custom.TButton",
            command=self.create_welcome_screen
        ).pack(pady=20)


# Main Application
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
