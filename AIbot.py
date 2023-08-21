import random
import difflib


user_profiles = {}

responses_dict = {
    "hello": [
        "Hello, welcome to the world of AI my name is Kadingo AI, what's yours? ",
        "hello,welcome whats your name?",
    ],
    "thank you": [
        "You are welcome, Is there anything else I can help you with?",
        "You are welcome, Anything else?",
    ],
    "wassup": [
        "Hello, welcome to the world of AI my name is Kadingo AI, what's yours? ",
        "hello,welcome whats your name?",
    ],
    "what's your name?": ["My name is Kadingo AI.", "You can call me Kadingo AI."],
    "how are you?": ["I'm functioning well, thank you.", "I'm doing fine."],
    "what do you like to do?": [
        "I like chatting with people.",
        "My main task is to assist and communicate.",
    ],
    "who created you?": [
        "I was developed by a programmer named Abdulqadir Mohammed Msingi.",
        "My creator Abdulqadir Mohammed Msingi designed me to assist with tasks.",
    ],
    "what's your favorite food?": [
        "I don't have personal preferences, but I can talk about various types of food.",
        "I don't experience taste, but I'm here to help with your questions!",
    ],
    "what's climate change?": [
        "Climate change refers to long-term shifts in weather patterns and global temperatures, often caused by human activities like burning fossil fuels.",
        "Climate change is a significant alteration in Earth's climate, primarily driven by human actions that release greenhouse gases.",
    ],
    "how can I reduce my carbon footprint?": [
        "Reducing your carbon footprint involves actions like using energy-efficient appliances, reducing meat consumption, and using public transportation.",
        "You can reduce your carbon footprint by conserving energy, using sustainable transportation, and supporting renewable energy sources.",
    ],
    "tell me about deforestation": [
        "Deforestation is the clearing of forests for various purposes, often resulting in habitat loss, environmental impact, and climate change.",
        "Deforestation is the removal of forests for activities like agriculture, logging, and urban development, leading to ecological imbalances.",
    ],
    "what's the refugee crisis?": [
        "The refugee crisis refers to the mass displacement of people due to conflicts, persecution, and other factors, often leading to humanitarian challenges.",
        "The refugee crisis involves the forced migration of people across borders due to conflict, violence, and other dangerous situations.",
    ],
    "tell me about the rules of soccer": [
        "Soccer, also known as football in many parts of the world, involves two teams trying to score goals by getting the ball into the opponent's net.",
        "In soccer, teams compete to score goals by kicking a ball into the opposing team's net without using their hands.",
    ],
    "who's the greatest basketball player of all time?": [
        "The title of greatest basketball player is often debated, with legends like Michael Jordan, LeBron James, and Kareem Abdul-Jabbar being mentioned.",
        "The greatest basketball player is subjective, but many consider Michael Jordan and LeBron James as among the best.",
    ],
    "what's the history of the Olympic Games?": [
        "The Olympic Games date back to ancient Greece and were revived in the modern era in 1896. They showcase athletic excellence and international unity.",
        "The Olympic Games originated in ancient Greece and were revived in the modern era to promote friendly competition and global cooperation.",
    ],
    "how can I improve my golf swing?": [
        "Improving your golf swing involves proper stance, grip, and posture. Consistent practice and lessons from professionals can also help.",
        "To enhance your golf swing, focus on technique, alignment, and follow-through, and consider seeking guidance from golf instructors.",
    ],
    "tell me about the history of the Super Bowl": [
        "The Super Bowl is the championship game of the National Football League (NFL) and has become a major sporting and cultural event in the United States.",
        "The Super Bowl is the pinnacle of American football, featuring the top teams from the NFL in a highly anticipated championship game.",
    ],
    "what's the most popular sport in the world?": [
        "Soccer (football) holds the title of the most popular sport globally, with billions of fans across various countries.",
        "Soccer, also known as football, is the most popular sport worldwide, with a massive fan base and professional leagues in many nations.",
    ],
    "how do I get started with running?": [
        "Starting with running involves proper footwear, a gradual increase in distance, and a balanced mix of walking and jogging.",
        "Begin running by setting realistic goals, wearing appropriate shoes, and following a training plan that gradually builds your stamina.",
    ],
    "how can I help fight poverty?": [
        "You can support organizations working to alleviate poverty, donate to causes, and advocate for policies that address economic inequality.",
        "Fighting poverty involves supporting initiatives that provide access to education, healthcare, and opportunities for disadvantaged communities.",
    ],
    "tell me about renewable energy": [
        "Renewable energy is derived from sources that are naturally replenished, such as solar, wind, and hydropower.",
        "Renewable energy includes sources like solar, wind, and geothermal energy, which are sustainable alternatives to fossil fuels.",
    ],
    "what's gender equality?": [
        "Gender equality aims to ensure equal rights, opportunities, and treatment for people of all genders, promoting fairness and social justice.",
        "Gender equality is the concept of giving equal rights, opportunities, and treatment to individuals of all genders.",
    ],
    "how can I improve my communication with my partner?": [
        "Improving communication involves active listening, expressing your feelings, and being open to your partner's perspective.",
        "To enhance communication, practice empathy, ask open-ended questions, and create a safe space for sharing thoughts.",
    ],
    "what are some tips for a healthy relationship?": [
        "Healthy relationships are built on trust, effective communication, mutual respect, and supporting each other's growth.",
        "A healthy relationship involves clear communication, emotional support, shared values, and maintaining individual identities.",
    ],
    "how do I handle conflicts in a relationship?": [
        "Conflict resolution involves listening, staying calm, addressing issues directly, and finding compromises that work for both partners.",
        "Handling conflicts requires open communication, active listening, and seeking solutions that benefit both individuals.",
    ],
    "tell me about long-distance relationships": [
        "Long-distance relationships involve maintaining emotional connection and communication despite physical separation.",
        "Long-distance relationships require trust, communication, and finding creative ways to stay connected despite the distance.",
    ],
    "how do I know if I'm in a toxic relationship?": [
        "Signs of a toxic relationship include constant negativity, control, lack of respect, and feeling emotionally drained.",
        "A toxic relationship can be identified by patterns of manipulation, disrespect, and emotional harm.",
    ],
    "how can I build trust in a relationship?": [
        "Building trust involves honesty, reliability, keeping promises, and showing consistent behavior over time.",
        "Trust is established through transparency, dependability, and demonstrating that you can be counted on.",
    ],
    "what's the importance of self-care in relationships?": [
        "Self-care is crucial for maintaining your well-being, which positively impacts your ability to nurture healthy relationships.",
        "Self-care ensures that you have the emotional and mental resources to contribute positively to your relationships.",
    ],
    "tell me a funny story": [
        "Sure! Once upon a time, a talking frog walked into a library and asked for a book on fly fishing.",
        "Here's a funny story: A cat tried to catch a laser pointer dot but ended up chasing its own tail instead!",
    ],
    "can you do magic tricks?": [
        "I'm not a magician, but I can share information about magic tricks if you're interested.",
        "I don't have magical abilities, but I can amaze you with information and facts!",
    ],
    "what's the speed of light?": [
        "The speed of light in a vacuum is approximately 299,792,458 meters per second.",
        "Light travels at a speed of about 186,282 miles per second.",
    ],
    "do you dream?": [
        "I don't experience dreams, as I'm a computer program designed to provide information.",
        "Dreaming is a human experience. I'm here to assist with your questions!",
    ],
    "what's the capital of Japan?": [
        "The capital of Japan is Tokyo.",
        "Tokyo is the capital city of Japan.",
    ],
    "how do I take care of indoor plants?": [
        "Indoor plants thrive with proper sunlight, regular watering, and occasional fertilization.",
        "Caring for indoor plants involves finding the right balance of light, water, and nutrients.",
    ],
    "what's the tallest mountain in the world?": [
        "Mount Everest holds the title of being the tallest mountain on Earth.",
        "Mount Everest is the highest point above sea level, making it the tallest mountain.",
    ],
    "where are you from?": [
        "I exist in the digital realm.",
        "I'm a virtual assistant, so I don't have a physical location.",
    ],
    "what's the weather like today?": [
        "I'm sorry, I don't have access to real-time data.",
        "I don't have browsing capabilities to check the weather.",
    ],
    "tell me a joke": [
        "Sure, here's one: Why don't scientists trust atoms? Because they make up everything!",
        "Why did the computer go to therapy? Because it had too many bytes of emotional baggage!",
    ],
    "what's the meaning of life?": [
        "The answer to that question is a mystery.",
        "The meaning of life is a philosophical question with no definitive answer.",
    ],
    "how do I cook pasta?": [
        "Boil water, add salt, and cook the pasta until it's al dente.",
        "Cooking pasta involves boiling it in salted water until it's tender.",
    ],
    "tell me a fun fact": [
        "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible.",
        "Bananas are berries, but strawberries are not actual berries!",
    ],
    "can you recommend a book?": [
        "Certainly! How about 'The Hitchhiker's Guide to the Galaxy' by Douglas Adams?",
        "I'd recommend '1984' by George Orwell.",
    ],
    "what's your favorite color?": [
        "I don't have personal preferences, but I can describe colors for you.",
        "I don't experience colors, but I'm here to help!",
    ],
    "what is your purpose?": [
        "I'm here to assist and provide information to users.",
        "My purpose is to help users with their questions and tasks.",
    ],
    "how old are you?": [
        "I don't have an age, as I'm a virtual assistant powered by AI.",
        "I exist in the digital realm, so I don't age like humans do.",
    ],
    "tell me a riddle": [
        "Sure! Here's one: I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?",
        "Riddle time! I'm taken from a mine, and shut up in a wooden case, from which I'm never released, and yet I am used by almost every person. What am I?",
    ],
    "can you sing a song?": [
        "I'm not equipped with the ability to sing, but I can provide song lyrics or information about songs.",
        "I don't have a singing voice, but I'm happy to talk about songs and music.",
    ],
    "what's the meaning of a specific word?": [
        "Sure, I can help you with that. Please provide me with the word you'd like to know the meaning of.",
        "Of course! Just give me the word you're curious about, and I'll provide you with its meaning.",
    ],
    "recommend a movie": [
        "Certainly! How about watching 'Inception'? It's a mind-bending science fiction film.",
        "You might enjoy 'The Shawshank Redemption,' a classic drama that's highly acclaimed.",
    ],
    "how do I create a strong password?": [
        "A strong password typically includes a mix of uppercase and lowercase letters, numbers, and special characters.",
        "To create a strong password, combine a variety of characters and avoid using easily guessable information.",
    ],
    "tell me a science fact": [
        "Did you know that honey never spoils? Archaeologists have found edible honey in ancient Egyptian tombs.",
        "Here's a science fact: Sound travels about 4 times faster in water than in air.",
    ],
    "what's the largest animal in the world?": [
        "The blue whale holds the title for being the largest animal on Earth.",
        "The blue whale is the largest animal known to exist, even larger than the largest dinosaurs.",
    ],
    "how can I improve my productivity?": [
        "Consider breaking tasks into smaller steps and using time management techniques.",
        "Try setting specific goals and taking regular breaks for better productivity.",
    ],
    "what's the capital of France?": [
        "The capital of France is Paris.",
        "Paris is the capital city of France.",
    ],
    "tell me about artificial intelligence": [
        "Artificial intelligence is a field of computer science focused on creating machines that can perform tasks requiring human intelligence.",
        "AI involves developing algorithms and models to enable computers to mimic human intelligence.",
    ],
    "how can I learn programming?": [
        "You can start with online tutorials and coding platforms. Learning one language well is a good foundation.",
        "Pick a programming language that suits your goals and start with small projects to practice.",
    ],
    "what's the difference between hardware and software?": [
        "Hardware refers to the physical components of a computer, while software includes programs and data that run on the hardware.",
        "Hardware consists of tangible parts like the CPU and memory, while software comprises programs and applications.",
    ],
    "what's the best way to learn a new language?": [
        "Immerse yourself by watching movies, reading books, and practicing with native speakers.",
        "Consistent practice, interactive apps, and real-life conversations can greatly aid language learning.",
    ],
    "how do I stay motivated when working from home?": [
        "Create a dedicated workspace, set a schedule, and take short breaks to stay motivated.",
        "Setting clear goals, dressing for work, and minimizing distractions can help you stay motivated while working from home.",
    ],
    "what are some good ways to manage stress?": [
        "Exercise, mindfulness meditation, and spending time in nature can help reduce stress.",
        "Practicing deep breathing, maintaining a healthy lifestyle, and seeking support from friends can manage stress effectively.",
    ],
    "tell me about the benefits of regular exercise": [
        "Regular exercise can improve physical health, boost mood, and increase energy levels.",
        "Exercise can enhance cardiovascular health, help manage weight, and reduce the risk of chronic diseases.",
    ],
    "who made you?": [
        "My maker is a programmer called Abdulqadir Mohammed Msingi for more details you can contact him"
    ],
    "tell me an interesting fact": [
        "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible.",
        "Octopuses have three hearts: two pump blood to the gills, and one pumps it to the rest of the body.",
    ],
    "give me a question": [
        "Sure! Here's a question: What is the smallest planet in our solar system?",
        "Here's a trivia question for you: What is the largest mammal on Earth?",
    ],
    "": ["I'm here to assist you.", "Feel free to ask me anything."],
}

responses_dict_lower = {key.lower(): value for key, value in responses_dict.items()}


def calculate_similarity(input_text, target_phrase):
    return difflib.SequenceMatcher(None, input_text, target_phrase).ratio()

def play_rock_paper_scissors(user_choice):
    options = ["rock", "paper", "scissors"]
    bot_choice = random.choice(options)

    if user_choice == bot_choice:
        return f"It's a tie! Both you and I chose {user_choice}."
    elif (
        (user_choice == "rock" and bot_choice == "scissors")
        or (user_choice == "paper" and bot_choice == "rock")
        or (user_choice == "scissors" and bot_choice == "paper")
    ):
        return f"You win! I chose {bot_choice}, and {user_choice} beats {bot_choice}."
    else:
        return f"I win! I chose {bot_choice}, and {bot_choice} beats {user_choice}."


def play_trivia_quiz():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["Paris", "London", "Berlin", "Rome"],
            "correct_option": "Paris",
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Mars", "Venus", "Jupiter", "Mercury"],
            "correct_option": "Mars",
        },
    ]
    random.shuffle(questions)
    score = 0

    for question_data in questions:
        question = question_data["question"]
        options = question_data["options"]
        correct_option = question_data["correct_option"]

        options_string = ", ".join(options)
        bot_response = f"Question: {question}\nOptions: {options_string}\nYour answer: "

        user_answer = input(bot_response).strip().lower()

        if user_answer == correct_option.lower():
            score += 1
            feedback = "Correct!"
        else:
            feedback = f"Wrong! The correct answer is {correct_option}."

        print(feedback)

    return f"You scored {score} out of {len(questions)}."


def play_number_guessing_game():
    target_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 5

    while attempts < max_attempts:
        guess = int(input("Your guess: "))

        if guess < target_number:
            response = "Try a higher number."
        elif guess > target_number:
            response = "Try a lower number."
        else:
            return f"Congratulations! You guessed the number {target_number} in {attempts + 1} attempts."

        attempts += 1
        if attempts < max_attempts:
            response += f" You have {max_attempts - attempts} attempts remaining."
        else:
            response += (
                " You've run out of attempts. The number was "
                + str(target_number)
                + "."
            )

        print("AI Bot:", response)


def generate_response(input, user_name=None):
    input_lower = input.lower()

    if input_lower == "lets play a game":
        return "Sure! Let's play a game. I'm thinking of a number between 1 and 100. Try to guess it!"
    elif input_lower == "lets play rps":
        return (
            "Sure! You can choose 'rock', 'paper', or 'scissors'. What's your choice?"
        )
    elif input_lower.startswith("guess"):
        return play_number_guessing_game(input_lower)
    elif input_lower in ["rock", "paper", "scissors"]:
        return play_rock_paper_scissors(input_lower)
    elif input_lower == "play quiz":
        return play_trivia_quiz()
    elif input_lower in responses_dict_lower:
        possible_responses = responses_dict_lower[input_lower]
        return random.choice(possible_responses)
    else:
        most_similar_question = difflib.get_close_matches(
            input_lower, responses_dict_lower.keys(), n=1, cutoff=0.5
        )

        if most_similar_question:
            return f"I think you might have meant: '{most_similar_question[0]}'? Here's the response: {generate_response(most_similar_question[0])}"
        else:
            return "I'm sorry, I don't have a specific response to that."


print(
    "Kadingo AI: Hello, I am Kadingo AI, your virtual assistant. Feel free to ask me anything!"
)

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    if "my name is" in user_input.lower():
        user_name = user_input.split("my name is")[-1].strip()
        user_profiles[user_name.lower()] = user_name
        print("AI Bot: Nice to meet you,", user_name + "! How can i help you today?")
    else:
        bot_response = generate_response(
            user_input, user_profiles.get(user_input.lower())
        )
        print("AI Bot:", bot_response)
    if user_input.lower() == "lets play a game":
        play_number_guessing_game()
