import random

questions = [
    {
        "question": "Who developed the Python language?",
        "options": ["A. Zim Den", "B. Guido van Rossum", "C. Niene Stom", "D. Wick van Rossum"],
        "answer": "C"
    },
    {
        "question": "What do we use to define a block of code in Python language?",
        "options": ["A. Key", "B. Brackets", "C. Indentation", "D. None of these"],
        "answer": "C"
    },
    {
        "question": "Which of the following statements is correct regarding the object-oriented programming concept in Python?",
        "options": ["A. Classes are real-world entities while objects are not real", 'B. Objects are real-world entities while classes are not real', 'C. Both objects and classes are real-world entities', 'D. All of the above'],
        "answer": "B"
    },
    {
		"question": "What is the method inside the class in python language?",
		"options": ['A. Object', 'B. Function', 'C. Attribute', 'D. Attitude'],
		"answer": "B"
	},
    {
		"question": "Which of the following declarations is incorrect?",
		"options":['A. _x = 2', 'B. __x = 3', 'C. __xyz__ = 5', 'D. None of these'],
		"answer": "D"
	},
    {
		"question": "Why does the name of local variables start with an underscore discouraged?",
		"options": ['A. To identify the variable', 'B. It confuses the interpreter', 'C. It indicates a private variable of a class', 'D. None of these'],
		"answer": "C"
	},
    {
		"question": "Which of the following is not a keyword in Python language?",
		"options": ['A. val', 'B. raise', 'C. try', 'D. with'],
		"answer": "A"
	},
    {
		"question": "Which of the following statements is correct for variable names in Python language?",
		"options": ['A. All variable names must begin with an underscore.', 'B. Unlimited length', 'C. The variable name length is a maximum of 2.', 'D. All of the above'],
		"answer": "B"
	},
    {
		"question": "Which of the following declarations is incorrect in python language?",
		"options": ['A. xyzp = 5,000,000', 'B. x y z p = 5000 6000 7000 8000', 'C. x, y, z, p = 5000, 6000, 7000, 8000', 'D. x_y_z_p = 5,000,000'],
		"answer": "B"
	},
    {
		"question": "print(2 + 2)",
		"options": ['A. 2', 'B. 4', 'C. 2+2', 'D. None'],
		"answer": "B"
	},
    {
		"question": 'What is the correct way to create a list in Python?R',
		"options": ['A. List = []', 'B. list[]', 'C. list', 'D. list()'],
		"answer": "d"
	},
    {
		"question": 'What is the output of the following Python code?\nmy_list = [1, 2, 3, 4, 5]\n print(my_list[2])',
		"options": ['A. 1', 'B. 2', 'C. 3', 'D. 4'],
		"answer": "C"
	},
    {
		"question": 'What is the output of the following Python code?\nmy_list = [1, 2, 3, 4, 5]\nmy_list.append(6)\nprint(my_list)',
		"options": ['A. [1, 2, 3, 4, 5]', 'B. [1, 2, 3, 4, 5, 6]', 'C. None', 'D. Error'],
		"answer": "B"
	},
    {
		"question": 'What is the output of the following Python code? \nmy_list = [1, 2, 3, 4, 5] \nprint(my_list.pop())',
		"options": ['A. 1', 'B. 2', 'C. 3', 'D. 4'],
		"answer": "D"
	},
    {
		"question": 'What is the output of the following Python code? \nmy_string = "Hello, world!" \nprint(my_string[0])',
		"options": ['A. H', 'B. e', 'C. l', 'D. o'],
		"answer": "H"
	},
    {
		"question": 'What is the capital of France?',
		"options": ['A. London', 'B. Paris', 'C. Rome', 'D. Berlin'],
		"answer": "B"
	},
    
    {
		"question": 'What is the square root of 16',
		"options": ['A. 2', 'B. 3', 'C. 4', 'D. 8'],
		"answer": "C"
	},
    {
        "question": 'What is the largest planet in the solar system?',
		"options": ['A. Jupiter', 'B. Saturn', 'C. Uranus', 'D. Neptune'],
		"answer": "A"
	},
    {
        "question": 'What is the name of the largest ocean on Earth?',
		"options": ['A. Pacific Ocean', 'B. Atlantic Ocean', 'C. Indian Ocean', 'D. Arctic Ocean'],
		"answer": "A"
	},
	{
        "question": 'What is the name of the longest river in the world?',
		"options": ['A. Yangtze River', 'B. Amazon River', 'C. Nile River', 'D. Yangtze River'],
		"answer": "C"
	},
	{
        "question": 'What is the name of the highest mountain peak in the world?',
		"options": ['A. K2', 'B. Kangchenjunga', 'C. Lhotse', 'D. Mount Everest'],
		"answer": "D"
	},
	{
        "question": 'What is the name of the world\'s most populous country?',
		"options": ['A. China', 'B. India', 'C. America', 'D. Indonesia'],
		"answer": "B"
	},
	{
        "question": 'What is the name of the world\'s largest desert?',
		"options": ['A. Sahara Desert', 'B. Arabian Desert', 'C. Arabian Desert', 'D. Thar Desert'],
		"answer": "A"
	},
	{
        "question": 'What is the name of the largest river delta in the world?',
		"options": ['A. Ganges delta', 'B. Mississippi delta', 'C. Mississippi delta', 'D. Nile delta'],
		"answer": "A"
	},
	{
        "question": 'What is the name of the largest rainforest in the world?',
		"options": ['A. Southeast Asian rainforest', 'B. Congo rainforest', 'C. New Guinea rainforest', 'D. Amazon rainforest'],
		"answer": "D"
	},
	{
        "question": 'What is the name of the largest lake in the world?',
		"options": ['A. Lake Superior', 'B. Lake Victoria', 'C. Caspian Sea', 'D. Lake Baikal'],
		"answer": "C"
	},
	{
        "question": 'What is the name of the largest continent in the world?',
		"options": ['A. Africa', 'B. Asia', 'C. South America', 'D. North America'],
		"answer": "B"
	},
	{
        "question": 'What is the name of the largest rainforest biome in the world?',
		"options": ['A. Boreal rainforest', 'B. Cloud forest', 'C. Temperate rainforest', 'D. Tropical rainforest'],
		"answer": "D"
	},
	{
        "question": 'What is the name of the largest lake biome in the world?',
		"options": ['A. Oligotrophic lake', 'B. Mesotrophic lake', 'C. Eutrophic lake', 'D. Dystrophic lake'],
		"answer": "A"
	},
	{
        "question": 'What is the name of the largest mountain range in the world?',
		"options": ['A. Andes', 'B. Andes', 'C. Himalayas', 'D. Alps'],
		"answer": "C"
	}
      
]


def generate_random_question():
    """Generates a random question from the list of questions."""
    random_index = random.randint(0, len(questions) - 1)
    return questions[random_index]


def check_answer(question, answer):
    """Checks the user's answer to the given question."""
    if answer == question["answer"]:
        return True
    else:
        return False



print("Welcome to the quiz!")

# Generate a random question.
question = generate_random_question()

# Print the question and options.
print(question["question"])
for i in range(len(question["options"])):
    print(f"{i + 1}. {question['options'][i]}")

# Get the user's answer.
answer = input("Your answer: ")

# Check the user's answer.
if check_answer(question, answer):
    print("Correct!")
else:
    print("Incorrect. The correct answer is:", question["answer"])



while True:
    # Ask the user if they want to continue.
    continue_quiz = input("Do you want to continue? (Y/N): ")

    # If the user doesn't want to continue, break out of the loop.
    if continue_quiz.lower() != "y":
        break

    # Generate a new random question.
    question = generate_random_question()

    # Print the question and options.
    print(question["question"])
    for i in range(len(question["options"])):
        print(f"{i + 1}. {question['options'][i]}")

    # Get the user's answer.
    answer = input("Your answer: ")

    # Check the user's answer.
    if check_answer(question, answer):
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", question["answer"])



print("Thank you for playing!, \nHave a nice day!")
