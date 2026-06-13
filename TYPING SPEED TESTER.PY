# ==========================================================
# TYPING SPEED TESTER
# ==========================================================
#
# What is this project?
# ---------------------
# This program measures:
# 1. Typing Speed (Words Per Minute)
# 2. Typing Accuracy
# 3. Time Taken
#
# How does it work?
# -----------------
# 1. A random sentence is selected.
# 2. User presses Enter to begin.
# 3. Timer starts.
# 4. User types the sentence.
# 5. Timer stops.
# 6. Program calculates:
#       - Time Taken
#       - Words Typed
#       - Typing Speed
#       - Accuracy
#
# ==========================================================


# ==========================================================
# IMPORT MODULES
# ==========================================================
#
# Why import time?
# ----------------
# We need to measure how long the user takes to type.
#
# Example:
# time.time() -> 1750001234.123
#
# It returns the current timestamp in seconds.
#
import time


# Why import random?
# ------------------
# We want a different sentence each time.
#
# Example:
# random.choice(["A", "B", "C"])
#
# Possible Output:
# "B"
#
import random


# ==========================================================
# CREATE CLASS
# ==========================================================
#
# What is a class?
# ----------------
# A class is a blueprint for creating objects.
#
# Example:
#
# Car Blueprint
#      ↓
# Creates many cars
#
# Similarly:
#
# TypingSpeedTester Blueprint
#      ↓
# Creates typing test objects
#
class TypingSpeedTester:


    # ======================================================
    # CONSTRUCTOR METHOD
    # ======================================================
    #
    # What is __init__()?
    # -------------------
    # Constructor method.
    #
    # It automatically runs whenever an object is created.
    #
    # Example:
    #
    # tester = TypingSpeedTester("Hello")
    #
    # Python automatically calls:
    #
    # __init__("Hello")
    #
    def __init__(self, text):

        # self refers to the current object

        # Store the sentence user must type
        #
        # Example:
        # self.text = "The quick brown fox"
        #
        self.text = text

        # No start time yet
        #
        # Will be assigned when test starts
        #
        self.start_time = None

        # No end time yet
        #
        # Will be assigned when test finishes
        #
        self.end_time = None


    # ======================================================
    # START TEST METHOD
    # ======================================================
    #
    # Purpose:
    # --------
    # Controls the entire typing test process.
    #
    def start_test(self):

        # Display title
        print("Typing Speed Test")

        # Display instructions
        print("Type the following text as fast as you can:")

        # Show random sentence selected earlier
        print(self.text)

        # Pause until user presses Enter
        #
        # Why?
        # User needs time to get ready.
        #
        input("Press Enter to start...")

        # Record starting timestamp
        #
        # Example Output:
        # 1750001456.231
        #
        self.start_time = time.time()

        # Take user input
        #
        # Whatever user types gets stored
        # inside user_input variable.
        #
        user_input = input("Start typing: ")

        # Record ending timestamp
        self.end_time = time.time()

        # Send typed text to speed calculator
        self.calculate_speed(user_input)


    # ======================================================
    # CALCULATE SPEED METHOD
    # ======================================================
    #
    # Purpose:
    # --------
    # Calculate:
    # 1. Time Taken
    # 2. Words Typed
    # 3. WPM
    # 4. Accuracy
    #
    def calculate_speed(self, user_input):

        # Calculate time taken
        #
        # Formula:
        # End Time - Start Time
        #
        elapsed_time = self.end_time - self.start_time

        # Split sentence into words
        #
        # Example:
        #
        # "I love Python"
        #
        # becomes
        #
        # ["I", "love", "Python"]
        #
        user_words = user_input.split()

        # Count words in list
        #
        # Example:
        #
        # len(["I","love","Python"])
        #
        # Output:
        # 3
        #
        words_typed = len(user_words)

        # Calculate Words Per Minute (WPM)
        #
        # Formula:
        #
        # WPM = Words Typed / Minutes Taken
        #
        # Example:
        #
        # Words = 20
        #
        # Time = 30 seconds
        #
        # Convert seconds to minutes:
        #
        # 30 / 60
        # = 0.5 minute
        #
        # WPM:
        #
        # 20 / 0.5
        # = 40
        #
        speed = words_typed / (elapsed_time / 60)

        # Calculate accuracy
        accuracy = self.calculate_accuracy(user_input)

        # Display results

        print(f"\nTime taken: {elapsed_time:.2f} seconds")

        print(f"Words typed: {words_typed}")

        print(f"Typing speed: {speed:.2f} words per minute")

        print(f"Accuracy: {accuracy:.2f}%")


    # ======================================================
    # CALCULATE ACCURACY METHOD
    # ======================================================
    #
    # Purpose:
    # --------
    # Compare original sentence and user input.
    #
    def calculate_accuracy(self, user_input):

        # Count matching characters
        #
        # Example:
        #
        # Original:
        # Hello
        #
        # User:
        # Helxo
        #
        # zip() creates:
        #
        # ('H','H')
        # ('e','e')
        # ('l','l')
        # ('l','x')
        # ('o','o')
        #
        correct_chars = sum(

            # Add 1 whenever characters match
            1

            # Loop through character pairs
            for a, b in zip(self.text, user_input)

            # Only count matching characters
            if a == b
        )

        # Count total characters
        #
        # Example:
        #
        # len("Hello")
        #
        # Output:
        # 5
        #
        total_chars = len(self.text)

        # Calculate accuracy percentage
        #
        # Formula:
        #
        # Accuracy =
        # (Correct Characters / Total Characters) * 100
        #
        accuracy = (
            (correct_chars / total_chars) * 100
            if total_chars > 0
            else 0
        )

        # Send result back
        return accuracy


# ==========================================================
# MAIN PROGRAM
# ==========================================================
#
# __name__
#
# When file runs directly:
#
# python typing_test.py
#
# __name__ becomes "__main__"
#
# This block executes.
#
# If imported:
#
# import typing_test
#
# __name__ becomes "typing_test"
#
# This block will NOT execute.
#
if __name__ == "__main__":

    # Create list of sample sentences
    sample_texts = [

        "The quick brown fox jumps over the lazy dog.",

        "Typing speed tests are a great way to improve your typing skills.",

        "Practice makes perfect, so keep typing and you'll get better.",

        "Python is a versatile programming language used for many applications.",

        "Consistency and dedication are key to mastering any skill."
    ]

    # Select random sentence
    #
    # Example:
    #
    # random.choice(list)
    #
    # Output:
    # Any one sentence from list
    #
    random_text = random.choice(sample_texts)

    # Create TypingSpeedTester object
    #
    # Constructor automatically runs
    #
    tester = TypingSpeedTester(random_text)

    # Start the typing test
    tester.start_test()





//Code
import time
import random

class TypingSpeedTester:
    def __init__(self, text):
        self.text = text
        self.start_time = None
        self.end_time = None

    def start_test(self):
        print("Typing Speed Test")
        print("Type the following text as fast as you can:")
        print(self.text)
        input("Press Enter to start...")
        self.start_time = time.time()
        user_input = input("Start typing: ")
        self.end_time = time.time()
        self.calculate_speed(user_input)

    def calculate_speed(self, user_input):
        elapsed_time = self.end_time - self.start_time
        words_typed = len(user_input.split())
        speed = words_typed / (elapsed_time / 60)  # words per minute
        accuracy = self.calculate_accuracy(user_input)
        
        print(f"\nTime taken: {elapsed_time:.2f} seconds")
        print(f"Words typed: {words_typed}")
        print(f"Typing speed: {speed:.2f} words per minute")
        print(f"Accuracy: {accuracy:.2f}%")

    def calculate_accuracy(self, user_input):
        correct_chars = sum(1 for a, b in zip(self.text, user_input) if a == b)
        total_chars = len(self.text)
        accuracy = (correct_chars / total_chars) * 100 if total_chars > 0 else 0
        return accuracy
    
if __name__ == "__main__":
    sample_texts = [
        "The quick brown fox jumps over the lazy dog.",
        "Typing speed tests are a great way to improve your typing skills.",
        "Practice makes perfect, so keep typing and you'll get better.",
        "Python is a versatile programming language used for many applications.",
        "Consistency and dedication are key to mastering any skill."
    ]
    
    random_text = random.choice(sample_texts)
    tester = TypingSpeedTester(random_text)
    tester.start_test() 

