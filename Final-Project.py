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
        "answer": "Lessons-Learned Report"
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
            "The shortest path through \nthe project schedule",
            "The longest sequence of \nactivities determining project duration",
            "A list of critical \nrisks for the project",
            "The sequence of activities \nrequiring the least resources"
        ],
        "answer": " The longest sequence of \nactivities determining project duration"
    },
    {
        "question": "What is scope creep?",
        "choices": [
            "The process of reducing \nproject scope to meet constraints",
            "Uncontrolled changes or \ngrowth in a project’s scope",
            "The process of clarifying\n project deliverables",
            "Reviewing project objectives\n to align with stakeholder goals"
        ],
        "answer": "Uncontrolled changes or \ngrowth in a project’s scope"
    },
    {
        "question": "What is the purpose of a risk register?",
        "choices": [
            "To track the project’s schedule",
            "To record and monitor identified risks and their \nmitigation plans",
            "To assign resources to project activities",
            "To track project costs and expenditures"
        ],
        "answer":  "To record and monitor identified risks and their \nmitigation plans"
    },
    {
        "question": "What is a project scope statement?",
        "choices": [
            "A document that outlines the project's\nobjectives, deliverables, and boundaries",
            "A list of project task",
            "A document that formally authorizes a project",
            "A plan for project completion"
        ],
        "answer": "A document that outlines the project's \nobjectives, deliverables, and boundaries"
    },
]

random.shuffle(questions)
questions = questions[:10]


class PMQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quest-ion Impossible: Project Management Edition")
        self.root.geometry("800x600")
        self.root.config(background="#b6c1ff")

        self.timer_id = None  # Initialize timer_id
        self.reset_quiz()

    def reset_quiz(self):
        """Reset the quiz to its initial state."""
        self.score = 0
        self.current_question = 0
        self.user_name = None
        self.user_answers = []
        self.questions = random.sample(questions, len(questions))
        self.create_welcome_screen()

    def create_welcome_screen(self):
        """Create the welcome screen with instructions and a readiness check."""
        for widget in self.root.winfo_children():
            widget.destroy()

        # Welcome message
        ttk.Label(
            self.root,
            text="Welcome to Quest-ion Impossible:\nProject Management Edition!",
            font=("Courier New", 25, "bold"),
            background="#b6c1ff",
            justify="center"
        ).pack(pady=(40, 20))  # Top=40, Bottom=20

        # "Instructions" Header
        ttk.Label(
            self.root,
            text="Instructions:",
            font=("Arial", 15, "bold"),
            background="#929acc",
            justify="center",
            anchor="w",
            wraplength=600
        ).pack(pady=(10, 5), padx=20)  # Top=10, Bottom=5, Horizontal=20

        # Instructions content
        ttk.Label(
            self.root,
            text=(
                " - You will answer 10 multiple-choice questions.\n"
                " - You have 10 seconds to answer each question, once the time is up it will\nautomatically "
                " - Your score will be displayed at the end."
            ),
            font=("Arial", 13),
            background="#929acc",
            justify="left",
            wraplength=600
        ).pack(pady=(0, 30), padx=20)  # Bottom=30, Horizontal=20

        ttk.Label(
            self.root,
            text="Are you ready to begin?>_<",
            font=("Arial", 15, "bold"),
            background="#929acc",
            justify="center",
            anchor="w",
            wraplength=600
        ).pack(pady=(10, 5), padx=20)  # Top=10, Bottom=5, Horizontal=20

        # Buttons for readiness
        button_frame = tk.Frame(self.root, background="#b6c1ff")
        button_frame.pack(pady=20)

        # "Yes" button
        tk.Button(
            button_frame,
            text=" Yes ",
            command=self.create_name_entry_screen,
            font=("Arial", 10),
            bg="#929acc",  # Button background color
            fg="black"     # Button text color
        ).grid(row=0, column=0, padx=15)

        # "No" button
        tk.Button(
            button_frame,
            text=" No ",
            command=self.not_ready_popup,
            font=("Arial", 10),
            bg="#929acc",  # Button background color
            fg="black"     # Button text color
        ).grid(row=0, column=1, padx=15)



    def create_name_entry_screen(self):
        """Create the screen for entering the user's name."""
        for widget in self.root.winfo_children():
            widget.destroy()

        ttk.Label(
            self.root,
            text="Enter your name to start the quiz:",
            font=("Courier New", 16),
            background="#b6c1ff",
            justify="center"
        ).pack(pady=55)

        self.name_entry = ttk.Entry(self.root, width=30, font=("Courier New", 12))
        self.name_entry.pack(pady=10)

        ttk.Button(
            self.root,
            text="Start Quiz",
            command=self.start_quiz
        ).pack(pady=20)

    def not_ready_popup(self):
        """Display a popup when the user is not ready."""
        if messagebox.showinfo("See You Next Time!", "Okay, see you next time when you're ready!"):
            self.root.quit()


    def start_quiz(self):
        """Start the quiz if the user's name is valid."""
        self.user_name = self.name_entry.get().strip()
        if not self.user_name or not self.user_name.isalpha():
            messagebox.showwarning("Invalid Input", "Please enter a valid name (letters only).")
        else:
            self.load_question_screen()

    def load_question_screen(self):
        """Load the question screen."""
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
        for widget in self.root.winfo_children():
            widget.destroy()

        self.question_progress = ttk.Label(
            self.root,
            text="",
            font=("Courier New", 14, "bold"),
            background="#b6c1ff",
            justify="center"
        )
        self.question_progress.pack(pady=10)

        self.question_label = ttk.Label(
            self.root, text="", wraplength=450, font=("Courier New", 17), background="#b6c1ff", justify="center"
        )
        self.question_label.pack(pady=20)

        self.button_frame = tk.Frame(self.root, background="#b6c1ff")
        self.button_frame.pack(pady=15)

        self.answer_buttons = []
        for i in range(4):
            button = tk.Button(
                self.button_frame,
                text="",
                command=lambda i=i: self.check_answer(i),
                font=("Arial", 11),
                bg="#ccd4ff",  # Set the button background color
                fg="black",    # Set the button text color
                activebackground="white",  # Set the active button background color
                activeforeground="#5b6180"  # Set the active button text color
            )
            button.grid(row=i // 2, column=i % 2, padx=20, pady=20, sticky="ew")
            self.answer_buttons.append(button)

        for col in range(2):
            self.button_frame.columnconfigure(col, weight=1)

        self.timer_label = ttk.Label(
            self.root,
            text="",
            font=("Courier New", 12),
            background="#b6c1ff",
            justify="center"
        )
        self.timer_label.pack(pady=10)

        self.load_question()

    def start_timer(self, countdown=10):
        """Start a countdown timer."""
        if countdown > 0:
            if self.timer_label.winfo_exists():  # Check if the label still exists
                self.timer_label.config(text=f"Time Left: {countdown} seconds")
                self.timer_id = self.root.after(1000, self.start_timer, countdown - 1)
        else:
            if self.timer_label.winfo_exists():
                self.timer_label.config(text="Time's up!")
            # Handle when time runs out
            if self.current_question < len(self.questions):
                question_data = self.questions[self.current_question]
                self.user_answers.append((question_data["question"], "No Answer", question_data["answer"]))
            self.current_question += 1
            self.load_question()
            
    def load_question(self):
        """Load a question and its choices."""
        if self.current_question < len(self.questions):
            if self.timer_id:
                self.root.after_cancel(self.timer_id)

            question_data = self.questions[self.current_question]
            self.question_progress.config(
                text=f"QUESTION {self.current_question + 1} OUT OF {len(self.questions)}"
            )
            self.question_label.config(text=question_data["question"])
            choices = question_data["choices"]
            random.shuffle(choices)
            for i, choice in enumerate(choices):
                self.answer_buttons[i].config(text=choice)
            self.start_timer()
        else:
            self.show_results()

    def check_answer(self, index):
        """Check the user's answer."""
        question_data = self.questions[self.current_question]
        selected_answer = self.answer_buttons[index].cget("text")
        self.user_answers.append((question_data["question"], selected_answer, question_data["answer"]))

        if selected_answer == question_data["answer"]:
            self.score += 1

        self.current_question += 1
        self.load_question()

    def show_results(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        percentage_score = (self.score / len(self.questions)) * 100
        ttk.Label(
            self.root,
            text=f"Quiz finished! Thank you, {self.user_name}!>_<\n\nYour Score: {self.score}/{len(self.questions)} ({percentage_score:.2f}%)",
            font=("Courier New", 14),
            background="#b6c1ff",
            wraplength=550,
            justify="center"
        ).pack(pady=15)

                # Intelligence comparison based on score
        if self.score == len(self.questions):
            comparison_text = "Congratulations! You got a perfect score!\nYou're as intelligent as Albert Einstein!"
        elif self.score >= len(self.questions) * 0.8:
            comparison_text = "Great job! You're a Project Management expert!"
        elif self.score >= len(self.questions) * 0.5:
            comparison_text = "Not bad! You have a solid understanding of Project Management."
        else:
            comparison_text = "Keep learning! You're on the right path to mastering Project Management."

        ttk.Label(
            self.root,
            text=comparison_text,
            font=("Courier New", 12, "italic"),
            background="#b6c1ff",
            wraplength=550,
            justify="center"
        ).pack(pady=10)

        # Display detailed results
        result_frame = tk.Frame(self.root, height=700, width=600)  # Limit the frame size
        result_frame.pack(fill="x", padx=10, pady=10)

        canvas = tk.Canvas(result_frame)
        scrollbar = ttk.Scrollbar(result_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)  
        scrollbar.pack(side="right", fill="y")

        # Populate scrollable frame
        for i, (question, user_answer, correct_answer) in enumerate(self.user_answers):
            ttk.Label(
                scrollable_frame,
                text=f"Q{i + 1}: {question}",
                font=("Arial", 12, "bold"),
                background="#ccd4ff",
                wraplength=500
            ).pack(anchor="w", pady=5)
            ttk.Label(
                scrollable_frame,
                text=f"Your Answer: {user_answer}",
                font=("Arial", 12),
                background="#ccd4ff",
                wraplength=500
            ).pack(anchor="w")
            ttk.Label(
                scrollable_frame,
                text=f"Correct Answer: {correct_answer}",
                font=("Arial", 12),
                background="#ccd4ff",
                wraplength=500,
                foreground="green" if user_answer == correct_answer else "red"
            ).pack(anchor="w", pady=(0, 10))

        # Restart Quiz Button
        ttk.Button(
            self.root,
            text="Restart Quiz",
            command=self.reset_quiz
        ).pack(pady=20)

        
# Main Application
if __name__ == "__main__":
    root = tk.Tk()
    app = PMQuizApp(root)
    root.mainloop()