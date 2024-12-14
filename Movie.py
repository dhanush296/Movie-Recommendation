import tkinter as tk
import random

# Dictionary of movies by genre
movies_by_genre = {
    "Action": ["Gabbar Singh", "Aravinda Sametha Veera Raghava", "Sahoo", "Akhanda", "Rangastalam", "Narappa"],
    "Comedy": ["Nuvvu Naaku Nachchav", "Pelli Choopulu", "Jathi Ratnalu", "Ee Nagaraniki Emaindi", "Tillu Square"],
    "Drama": ["Lucky Baskhar", "Devara", "Pratinidhi 2", "Pushpa: The Rule-2", "Oopiri", "C/o Kancharapalem"],
    "Horror": ["Masooda", "Virupaksha", "Maa Oori Polimera", "Kanchana", "Taxiwala", "Bhaagamathie"],
    "Sci-Fi": ["Aditya 369", "Kaliki 2898-AD", "Oke Oka Jeevitham", "Ismart Shankar", "Adbhutham", "Maanaadu"],
    "Family": ["Murari", "Srikaram", "Balagam", "F2", "Srimanthudu", "Seethamma Vakitlo Sirimalle Chettu", "Ala Vaikunthapurramuloo", "Samajavaragamana"],
    "Love": ["Orange", "Tholi Prema", "Kushi", "Sita Ramam", "Colour Photo", "Radhe Shyam", "Jaanu", "Shyam Singha Roy", "Arjun Reddy", "Joe"],
    "Thriller": ["Drishyam", "Hit", "Mathu Vadhalara", "Agent Sai Srinivasa Athreya", "Kshanam", "Rakshahudu", "V"]
}

# Function to recommend a movie based on genre
def recommend_movie(genre, previous_recommendations):
    if genre in movies_by_genre:
        movies = movies_by_genre[genre][1:]  # Exclude the first movie
        movies = [movie for movie in movies if movie not in previous_recommendations]
        return random.choice(movies) if movies else "No more recommendations available."
    else:
        return "Sorry, we don't have any recommendations for that genre."

# Function to display the recommended movie
def show_recommendation():
    genre = genre_var.get()
    recommendation = recommend_movie(genre, previous_recommendations)
    result_label.config(text=recommendation)
    if recommendation != "No more recommendations available.":
        previous_recommendations.append(recommendation)
    satisfaction_frame.pack(pady=10)

# Function to handle user satisfaction
def handle_satisfaction(satisfied):
    if satisfied:
        result_label.config(text="Thanks for using the Movie Recommendation App! Enjoy the movie!")
        satisfaction_frame.pack_forget()
    else:
        result_label.config(text="")
        satisfaction_frame.pack_forget()

# Main GUI window
root = tk.Tk()
root.title("Movie Recommendation App")
root.geometry("400x400")

# Genre selection
genre_var = tk.StringVar()
genre_label = tk.Label(root, text="Select a genre:", font=('Arial', 14))
genre_label.pack(pady=10)

genre_options = ["Action", "Comedy", "Drama", "Horror", "Sci-Fi", "Family", "Love", "Thriller"]
genre_menu = tk.OptionMenu(root, genre_var, *genre_options)
genre_menu.pack(pady=10)

# Recommend button
recommend_button = tk.Button(root, text="Recommend a Movie", command=show_recommendation, font=('Arial', 14))
recommend_button.pack(pady=20)

# Result label
result_label = tk.Label(root, text="", font=('Arial', 14))
result_label.pack(pady=10)

# Satisfaction frame
satisfaction_frame = tk.Frame(root)
satisfaction_label = tk.Label(satisfaction_frame, text="Are you satisfied with the recommendation?", font=('Arial', 12))
satisfaction_label.pack(side=tk.LEFT)

yes_button = tk.Button(satisfaction_frame, text="Yes", command=lambda: handle_satisfaction(True), font=('Arial', 12))
yes_button.pack(side=tk.LEFT, padx=5)

no_button = tk.Button(satisfaction_frame, text="No", command=lambda: handle_satisfaction(False), font=('Arial', 12))
no_button.pack(side=tk.LEFT, padx=5)

# List to store previous recommendations
previous_recommendations = []

# Run the main loop
root.mainloop()
