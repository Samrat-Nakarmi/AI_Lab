class DiseaseExpertSystem:
    def __init__(self):
        self.disease_knowledge_base = {
            "flu": {
                "fever": True,
                "cough": True,
                "headache": True,
                "fatigue": True
            },
            "cold": {
                "fever": False,
                "cough": True,
                "headache": False,
                "fatigue": False
            },
            "malaria": {
                "fever": True,
                "cough": False,
                "headache": True,
                "fatigue": True
            }
        }
    
    def predict_disease(self, symptoms):
        possible_diseases = []
        for disease, disease_symptoms in self.disease_knowledge_base.items():
            match_score = sum(1 for symptom, is_present in disease_symptoms.items()
                              if symptoms.get(symptom) == is_present)
            if match_score >= 2: 
                possible_diseases.append(disease)
        
        if not possible_diseases:
            return "No disease prediction found based on the symptoms."
        return f"Possible diseases: {', '.join(possible_diseases)}"


symptoms_input = {
    "fever": True,
    "cough": True,
    "headache": True,
    "fatigue": False
}

disease_system = DiseaseExpertSystem()
predicted_diseases = disease_system.predict_disease(symptoms_input)
print(predicted_diseases)
