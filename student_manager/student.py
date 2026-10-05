class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score < 0 or self.score > 100:
            raise ValueError("score must be between 0 and 100")

        if self.score >= 80:
            return "A"
        elif self.score >= 60:
            return "B"
        else:
            return "C"

    def __str__(self):
        return f"Student(name={self.name}, score={self.score}, grade={self.get_grade()})"