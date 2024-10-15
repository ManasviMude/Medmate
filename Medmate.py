import time
import streamlit as st

MAX_QUESTIONS = 5

class Disease:
    def __init__(self, name, questions, base_probability, treatment, medication, hospital_contact):
        self.name = name
        self.questions = questions
        self.base_probability = base_probability
        self.treatment = treatment
        self.medication = medication
        self.hospital_contact = hospital_contact

    def ask_questions(self):
        positive_answers = 0

        st.subheader(f"Answer the following questions related to {self.name} (yes/no):")
        for question in self.questions:
            answer = st.radio(question, ('Yes', 'No'))
            if answer == 'Yes':
                positive_answers += 1
        return positive_answers

    def calculate_probability(self, positive_answers):
        probability = (self.base_probability * positive_answers) / MAX_QUESTIONS
        return probability

    def provide_info(self, probability):
        risk_level = self.determine_risk_level(probability)
        st.markdown(f"### Based on your answers, the estimated likelihood of having **{self.name}** is approximately {probability:.2f}%")
        st.markdown(f"**Risk Level:** {risk_level}")
        st.markdown(f"**Suggested Treatment:** {self.treatment}")
        st.markdown(f"**Recommended Medication:** {self.medication}")
        st.markdown(f"**For further assistance, please contact:**\n{self.hospital_contact}")
        st.markdown("### Warning: The above medication is provided for study purposes only. Consuming any medication without consultation from a certified practitioner may lead to life-threatening issues.")

        st.markdown("**Note:** This is a prediction based on your responses. Please consult a healthcare professional for further diagnosis and avoid using any medication without a prescription, as it can be dangerous to consume medicine without proper guidance.")

    def determine_risk_level(self, probability):
        if probability >= 75:
            return "High Risk"
        elif probability >= 50:
            return "Moderate Risk"
        else:
            return "Low Risk"

def init_diseases():
    return [
        Disease(
            "Diabetes",
            [
                "Do you have frequent urination?",
                "Do you feel very thirsty?",
                "Do you feel very hungry?",
                "Do you experience fatigue?",
                "Do you have blurred vision?"
            ],
            70.0,
            "Maintain a balanced diet and exercise regularly.",
            """
            - [Metformin](https://pharmeasy.in/medicine-online/metformin)
            - [Glipizide](https://pharmeasy.in/medicine-online/glipizide)
            - [Pioglitazone](https://pharmeasy.in/medicine-online/pioglitazone)
            - [Sitagliptin](https://pharmeasy.in/medicine-online/sitagliptin)
            - [Empagliflozin](https://pharmeasy.in/medicine-online/empagliflozin)
            """,
            "City Hospital A - 123-456-7890\nCity Hospital B - 7655432290\nCity Hospital C - 4455667890"
        ),
        # Add other diseases here...
    ]

def main():
    st.title("Medmate Chatbot")
    st.write("Your Personal Health Coach")

    diseases = init_diseases()

    choice = st.selectbox("Choose a disease to get more information:", [disease.name for disease in diseases])
    disease = next(d for d in diseases if d.name == choice)

    positive_answers = disease.ask_questions()
    if st.button("Submit"):
        probability = disease.calculate_probability(positive_answers)
        disease.provide_info(probability)

if __name__ == "__main__":
    main()
