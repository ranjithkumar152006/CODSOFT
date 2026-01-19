# Movie Recommendation System (Task 4)

## Project Overview

This project implements a **content-based movie recommendation system** that suggests **three movies** related to a movie selected by the user.  
The recommendations are generated based on **genre similarity** using **Cosine Similarity**.

## Objectives

- Recommend **3 similar movies** based on user input
- Ensure the recommended movies **do not include the selected movie**
- Handle **case-insensitive user input**
- Demonstrate basic concepts of **Machine Learning & Recommendation Systems**

## Technique Used

**Content-Based Filtering**

- Movie genres are converted into numerical vectors
- Similarity between movies is calculated using **Cosine Similarity**
- Movies with the highest similarity scores are recommended

## Technologies & Libraries

- Python 3.12+
- pandas
- scikit-learn

## Installation

Install the required libraries using:

pip install pandas scikit-learn

## How to Run the Project

- Clone or download the project folder
- Open the folder in VS Code
- Run the Python file:
  python recommendation_system.py
- Enter a movie name from the displayed list (case-insensitive)

## Sample Output

Available Movies:

- Avengers
- Iron Man
- Batman
- Superman
- Titanic
- The Notebook
- Inception
- Interstellar

Enter a movie name: Avengers
Top 3 movies similar to 'Avengers':
✔ Iron Man
✔ Batman
✔ Superman

# Execution Video

Watch the execution of the tic_tac_toe AI here:
Click here to view execution video : https://drive.google.com/file/d/1HVmWoMqSFnReHW3ud03ak2NTATurqrxK/view?usp=sharing

## Author

Ranjith kumar.A
