# Guessing Game
#### Video Demo: https://youtu.be/RwJrnTkFCVM
#### Description:

This is my final project for CS50’s Introduction to Programming with Python.  
The project is a number guessing game created using Python. The player has to guess a randomly generated number within a certain range and limited number of attempts. The program keeps track of each player’s highest score in a CSV file and updates it only if the player achieves a higher score in later rounds.

When the game starts, the user is asked to enter their name and choose a level of difficulty.  
Level 1 has numbers between 1 and 10, level 2 has numbers between 1 and 50, and level 3 has numbers between 1 and 100.  
After that, the program generates a random number within that range. The player then has 5 chances to guess the correct number. Each wrong guess reduces the total score by 20 points, starting from 100.  
After finishing one round, the player can either continue to the next round or quit the game. When they quit, the program displays their highest score saved in the CSV file.


### Files Included

1. **project.py** – This is the main Python file that runs the game.  
2. **score.csv** – This file stores the name of the player and their highest score.  
3. **test_project.py** – This file contains test cases for the functions used in the main program.  
4. **README.md** – This file explains the project, its structure, and how it works.


### Functions Used

1. **main()** – Runs the whole game and controls user interaction.  
2. **validate_level()** – Makes sure the user enters a valid level (1, 2, or 3).  
3. **generate_randomnumber(level)** – Generates a random number based on the level selected by the player.  
4. **get_input(upperlimit)** – Checks that the user’s input is a number within the valid range.  
5. **guess_check(level)** – Gives the player five chances to guess the number and returns their score.  
6. **highest_score(user, score)** – Reads and updates the CSV file to store the player’s highest score.


### Concepts Used

- Functions and loops  
- Conditional statements  
- Exception handling using try and except  
- File handling with CSV files  
- Random number generation  
- Input validation  


### How to Run the Project

1. Open the project folder in VS Code or any terminal.  
2. Run the file by typing:
python project.py
3. Follow the instructions on the screen to play the game.  
4. To run the test file, type:
pytest test_project.py


### Requirements

This project only uses Python’s built-in libraries:
- csv  
- random  

No external installations are required.


### Design Decisions

I decided to keep the game simple and interactive so that it is easy to understand for beginners.  
I used a CSV file to store the scores because it is lightweight and works well for text-based data.  
The program also checks for invalid inputs and handles errors like entering non-numeric values gracefully.


### Conclusion

Through this project, I learned how to combine multiple concepts of Python like loops, file handling, random number generation, and error handling into one complete working program.  
It was a fun experience building and testing this project for the CS50P course, and it helped me understand how to design and structure a small but functional software project from scratch.