class Question:
    def __init__(self, text, options, correct):
        self.text = text
        self.options = options
        self.correct = correct

    def show_question(self):
        print(self.text)
        i = 1
        for option in self.options:
            print(i, ")", option)
            i += 1

    def check_answer(self, answer):
        if answer == self.correct:
            return True
        return False


class Quiz:
    def __init__(self):
        self.questions = []
        self.score = 0

    def add_question(self, question):
        self.questions.append(question)

    def start(self):
        for q in self.questions:
            q.show_question()

            answer = int(input("Javobni kiriting (raqam): "))

            if q.check_answer(answer):
                print("To'g'ri!")
                self.score += 1
            else:
                print("Noto'g'ri!")

            print()

    def show_result(self):
        print("Test tugadi!")
        print("To'g'ri javoblar:", self.score)
        print("Jami savollar:", len(self.questions))


def main():
    q1 = Question(
        "Python qaysi turdagi til?",
        ["Compiled", "Interpreted", "Assembly"],
        2
    )

    q2 = Question(
        "HTML nima?",
        ["Programming language", "Markup language", "Database"],
        2
    )

    quiz = Quiz()

    quiz.add_question(q1)
    quiz.add_question(q2)

    quiz.start()

    quiz.show_result()


main()
