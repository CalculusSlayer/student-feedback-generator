import random
from fpdf import FPDF
from jinja2 import Environment, FileSystemLoader

# Load Jinja environment
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('feedback_template.html')

class PDF(FPDF):
    def add_feedback_page(self, presented_group, your_group, name, motivation_score, presentation_score, completeness_score, what_went_well, what_could_be_improved):
        self.add_page()
        html = template.render(presented_group=presented_group,
                               your_group=your_group,
                               name=name,
                               motivation_score=motivation_score,
                               presentation_score=presentation_score,
                               completeness_score=completeness_score,
                               what_went_well=what_went_well,
                               what_could_be_improved=what_could_be_improved)
        self.write_html(html)

# Create a PDF object
pdf = PDF()

# Lists of strings for 'What went well' and 'What could be improved'
positive_feedback = [
    "The application of neural networks in your project demonstrated a deep understanding of complex machine learning models. Your approach to layer selection and activation functions was particularly impressive.",
    "Your regression model showed a strong grasp of the fundamentals. The way you handled overfitting and underfitting issues was exemplary, and your feature engineering added significant value to the model's performance.",
    "The utilization of SVMs (Support Vector Machines) in your project was innovative and well-executed. Your choice of kernel and the tuning of hyperparameters were spot-on, leading to impressive results.",
    "The accuracy of your model was noteworthy. You've not only achieved a high accuracy rate but also demonstrated a thorough understanding of its implications and limitations in the context of your dataset.",
    "Your interpretation of the MSE (Mean Squared Error) and R2 scores was insightful. It was clear that you've mastered these evaluation metrics, providing a well-rounded analysis of your model's performance."
]

areas_for_improvement = [
    "While your project showed promise, a deeper dive into the intricacies of neural networks could enhance your model's performance. Exploring different architectures and training methods could yield better results.",
    "Your regression model would benefit from a more robust approach to feature selection. Consider applying dimensionality reduction techniques to improve model efficiency and performance.",
    "The application of SVMs in your project could be improved by exploring a wider range of kernels. Additionally, a more detailed analysis of the impact of hyperparameter tuning would be beneficial.",
    "While your model achieved good accuracy, focusing more on other metrics like F1-score and precision could provide a more comprehensive understanding of its performance, especially in imbalanced datasets.",
    "A more detailed analysis of MSE and R2 scores in different segments of your data could provide more insights. Segmenting the dataset and analyzing the model's performance in each segment could be a valuable addition."
]

group_order = [6, 16, 19, 20, 31, 34, 38, 9, 12, 18, 21, 25, 29, 30, 1, 7, 22, 24, 26, 27, 35, 36, 3, 5, 8, 10, 13, 23, 32, 2, 4, 11, 15, 17, 28, 33, 14]

# Generate feedback
for group_number in group_order:
    feedback = {
        "presented_group": group_number,
        "your_group": "25",  # Adjust as needed
        "name": "Nayeel Imtiaz",     # Adjust as needed
        "motivation_score": random.randint(1, 5),
        "presentation_score": random.randint(1, 5),
        "completeness_score": random.randint(1, 5),
        "what_went_well": random.choice(positive_feedback),
        "what_could_be_improved": random.choice(areas_for_improvement)
    }
    pdf.add_feedback_page(**feedback)

# Save the PDF
pdf.output("nayeel_imtiaz_student_feedback.pdf")
