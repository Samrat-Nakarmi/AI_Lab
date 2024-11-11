class LoanEligibility:
    def __init__(self, age, income, credit_score):
        self.age = age
        self.income = income
        self.credit_score = credit_score

    def check_eligibility(self):
        if self.age < 18:
            return "Not eligible for loan. Age is less than 18."
        elif self.income < 30000:
            return "Not eligible for loan. Income is too low."
        elif self.credit_score < 650:
            return "Not eligible for loan. Credit score is too low."
        else:
            return "Eligible for loan."

# Example Usage
person1 = LoanEligibility(age=25, income=50000, credit_score=700)
print(person1.check_eligibility())

person2 = LoanEligibility(age=17, income=25000, credit_score=600)
print(person2.check_eligibility())
