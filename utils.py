import re
import random
class RuleBot():
    negative_responses = ("no","nope","nah","naw","not a chance","sorry")
    exit_commands = ("quit","pause","exit","goodbye","bye","later")
    random_questions = (
        "Why are you here?",
        "Are there any humans like you?",
        "What do you consume for sustenance?",
        "Is there intelligent life on this planet?",
        "Does earth have a leader?",
        "What planets have you visited?",
        "What technology do you have on this planet?"
      )
    def __init__(self):
        self.alienbabble = {
            'describe_planet_intent': r'.*\s*yourplanet.*',
            'answer_why_intent': r'why\sare.*',
            'about_intellipat': r'.*\s*intellipaat'
        }
    def greet(self):
        self.name = input("What is your name?\n")
        will_help = input(
            f"Hi {self.name},I am a Rule-Bot. Will you help me learn about your planet?\n")
        if will_help in self.negative_responses:
            print("Ok,have a nice Earth day!")
            return
        self.chat()  
    def make_exit(self,reply):
        for command in self.exit_commands: 
            if reply == command:
                print("Okay, have a nice Earth day!")
                return True 
    def chat(self):
        reply = input(random.choice(self.random_questions)).lower()
        while not self.make_exit(reply):
            reply = input(self.match_reply(reply)) 
    def match_reply(self,reply):
        for key,value in self.alienbabble.items():
            intent = key
            regex_pattern = value
            found_match = re.match(regex_pattern,reply)
            if found_match and intent == 'describe_planet_intent':
                return self.describe_planet_intent()
            elif found_match and intent == 'answer_why_intent':
                return self.answer_why_intent()
            elif found_match and intent == 'about_intellipat':
                return self.about_intellipat()
        if not found_match:
            return self.no_match_intent()
    def describe_planet_intent(self):
        responses = ("My planet is utopia of diverse organisms and species.\n",
        "I am from Opidius, the capital of the Wayward Galaxies.\n") 
        return random.choice(responses)
    def answer_why_intent(self):
        responses = ("i come in peace\n","I am here to collect data on your planet\n",
        "I heard the coffee is good\n")
        return random.choice(reaponses)
    def about_intellipat(self):
        responses = ("Intellipaat is world's largest professional education company\n","Intellipaat will make you learn concepts in depth",
        "Intelipaat is where your career and skill grows\n")
        return random.choice(responses)
    def no_match_intent(self):
        responses = (
            "please tell me more\n","Tell me More!\n","Why do you say that?\n",
            "I see. Can you elaborate?\n","Interesting. Can you tell me more?\n","I see.How do you think?\n",
            "why?\n","How do you think I feel when you say that?\n"
        )
        return random.choice(responses) 
AlienBot = RuleBot()
AlienBot.greet()           




