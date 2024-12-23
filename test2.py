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
]

# Randomize questions
random.shuffle(questions)

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Project Management Quiz")
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
            text="Welcome to the Project Management Quiz!", 
            font=("Arial", 16), 
            justify="center"
        ).pack(pady=20)

        # Name Input
        ttk.Label(self.root, text="Please enter your name:", font=("Arial", 12)).pack(pady=10)
        self.name_entry = ttk.Entry(self.root, width=30, font=("Arial", 12))
        self.name_entry.pack(pady=10)

        # Start Button
        ttk.Button(
            self.root, 
            text="Start Quiz", 
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
        self.answer_buttons = []
        for i in range(4):  # Assuming 4 choices
            button = ttk.Button(
                self.root, text="", width=40, command=lambda i=i: self.check_answer(i)
            )
            button.pack(pady=5)
            self.answer_buttons.append(button)
        
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
