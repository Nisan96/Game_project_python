class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def run_quiz(self):
        for question in self.questions:
            answer = input(question.prompt + ":" + "\n")
            if answer.lower() == question.answer:
                self.score += 1
                print("Correct!")
            else:
                print("Incorrect!")
        print("You got", self.score, "correct answer out of", len(self.questions), "questions.")
        print("So, You got", ((100 * self.score)/len(self.questions)),"% marks out of 100% marks")


question_prompts = [
    "What color is the sky? (a) Blue (b) Red",
    "What is the capital of France? (a) London (b) Paris",
    "What is 2.7 + 3.3? (a) 6 (b) 5",
    "What is national animal of Bangladesh? (a) Bear, (b) Tiger",
    "What is the biggest mammal of the planet? (a) Eliphant, (b) Blue whale, (c) Giraffe"
]

answer_list = ['a','b','a','b','b']


if __name__=="__main__":
    print("-------------------------------Quiz Game Start-------------------------------------")
    question_list = []
    score = 0
    counter = 0
    for question in question_prompts:
        question_list.append(Question(question, answer_list[counter]))
        counter += 1

    quiz = Quiz(question_list)
    quiz.run_quiz()

