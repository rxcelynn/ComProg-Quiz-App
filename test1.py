import tkinter as tk
from tkinter import ttk, messagebox
import random

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
            "Ensure the project meets its objectives within scope, time, and cost constraints",
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
                    "The project team fails to communicate and build up working relation with the customer.",
                    "A key team member is pulled away from the project due to changing priority"],
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
]

# Shuffle the questions array to randomize the order of questions in the quiz
random.shuffle(questions)
questions = questions[:10]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quest-ion Impossible: Project Management Edition")
        self.root.geometry("500x400")
        self.score = 0
        self.current_question = 0
        self.user_name = None  # Store user's name

        self.create_welcome_screen()
    
    def create_welcome_screen(self):
        """Create the welcome screen where the user inputs their name."""
        # Clear the root window
        for widget in self.root.winfo_children():
            widget.destroy()

        # Welcome Message
        ttk.Label(
            self.root, 
            text="Welcome to the Quest-ion Impossible: Project Management Edition!", 
            font=("Courier New", 20, "bold"), 
            justify="center"
        ).pack(pady=20)

        # Name Input
        ttk.Label(self.root, text="Name mo boss ^^:", font=("Courier New", 12, "bold")).pack(pady=10)
        self.name_entry = ttk.Entry(self.root, width=30, font=("Courier New", 12))
        self.name_entry.pack(pady=10)

        # Define a custom style for the button
        style = ttk.Style()
        style.configure(
            "Custom.TButton", 
            font=("Courier New", 12, "bold")
        )

        # Create the button using the custom style
        ttk.Button(
            self.root, 
            text="Start na boss", 
            style="Custom.TButton", 
            command=self.start_quiz
        ).pack(pady=20)

    def start_quiz(self):
        """Start the quiz after capturing the user's name."""
        self.user_name = self.name_entry.get().strip()
        if not self.user_name:
            messagebox.showwarning("Name Required", "Please enter your name to proceed.")
        else:
            self.load_question_screen()
    
    def load_question_screen(self):
        """Load the question screen for the quiz."""
        # Clear the root window
        for widget in self.root.winfo_children():
            widget.destroy()

        # Question Label
        self.question_label = ttk.Label(
            self.root, text="", wraplength=450, font=("Arial", 14), justify="center"
        )
        self.question_label.pack(pady=20)

        # Answer Buttons
       # Answer Buttons
        self.answer_buttons = []
        self.button_frame = tk.Frame(self.root)  # Create a frame to hold the buttons
        self.button_frame.pack(pady=20)  # Pack the frame

        for i in range(4):  # Assuming 4 choices
            button = ttk.Button(
                self.button_frame,  # Add the buttons to the frame
                text="", 
                command=lambda i=i: self.check_answer(i)
            )
            # Arrange buttons in a 2x2 grid
            button.grid(row=i // 2, column=i % 2, padx=10, pady=10, sticky="ew")  # Use sticky to expand width dynamically
            self.answer_buttons.append(button)

        # Configure the grid columns to adjust dynamically
        for col in range(2):  # Assuming 2 columns
            self.button_frame.columnconfigure(col, weight=1)

        # Load the first question
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
            self.show_score()

    def check_answer(self, index):
        question_data = questions[self.current_question]
        selected_answer = self.answer_buttons[index].cget("text")
        if selected_answer == question_data["answer"]:
            self.score += 1
        
        self.current_question += 1
        self.load_question()

    def show_score(self):
        """Show the final score and thank the user."""
        messagebox.showinfo(
            "Quiz Completed", 
            f"Thank you, {self.user_name}! Your Score: {self.score}/{len(questions)}"
        )
        self.root.destroy()

# Main Application
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()