import pyodbc
from tkinter import Tk, Label, Button, StringVar, Entry, Text, Toplevel, END
from PIL import Image, ImageTk
# Establish database connection
def get_connection():
    server = 'DESKTOP-A9A5RA8'
    database = 'movie_recommendations_Database'
    try:
        conn = pyodbc.connect(
            f'DRIVER={{ODBC Driver 17 for SQL Server}};'
            f'SERVER={server};'
            f'DATABASE={database};'
            f'Trusted_Connection=yes;'
        )
        print("Connection successful!")
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None

# Fetch movies by genre
def list_movies_by_genre(genre_name, conn):
    try:
        query = """
        SELECT DISTINCT m.MovieTitle
        FROM Movie m
        JOIN MovieGenres mg ON m.Movie_ID = mg.Movie_ID
        JOIN Genre g ON mg.Genre_ID = g.Genre_ID
        WHERE g.GenreName = ?;
        """
        cursor = conn.cursor()
        cursor.execute(query, (genre_name,))
        return cursor.fetchall()
    except Exception as e:
        print(f"Error fetching movies by genre: {e}")
        return []

# Fetch movies by director
def list_movies_by_director(director_name, conn):
    try:
        query = """
        SELECT DISTINCT m.MovieTitle
        FROM Movie m
        JOIN Director d ON m.Director_ID = d.Director_ID
        JOIN Person p ON d.Director_ID = p.Person_ID
        WHERE p.Name = ?;
        """
        cursor = conn.cursor()
        cursor.execute(query, (director_name,))
        return cursor.fetchall()
    except Exception as e:
        print(f"Error fetching movies by director: {e}")
        return []

# Fetch movies by leading actor
def list_movies_by_leading_actor(leading_actor_name, conn):
    try:
        query = """
        SELECT DISTINCT m.MovieTitle
        FROM Movie m
        JOIN MovieActors ma ON m.Movie_ID = ma.Movie_ID
        JOIN LeadingActor la ON ma.Actor_ID = la.LeadingActor_ID
        JOIN Person p ON la.LeadingActor_ID = p.Person_ID
        WHERE p.Name = ?;
        """
        cursor = conn.cursor()
        cursor.execute(query, (leading_actor_name,))
        return cursor.fetchall()
    except Exception as e:
        print(f"Error fetching movies by leading actor: {e}")
        return []

def recommend_movies_by_genre(movie_title, conn):
    try:
        query = """
        SELECT DISTINCT m2.MovieTitle
        FROM Movie m1
        JOIN MovieGenres mg1 ON m1.Movie_ID = mg1.Movie_ID
        JOIN MovieGenres mg2 ON mg1.Genre_ID = mg2.Genre_ID
        JOIN Movie m2 ON mg2.Movie_ID = m2.Movie_ID
        WHERE m1.MovieTitle = ? AND m1.Movie_ID != m2.Movie_ID;
        """
        cursor = conn.cursor()
        cursor.execute(query, (movie_title,))
        return cursor.fetchall()
    except Exception as e:
        print(f"Error fetching recommendations by genre: {e}")
        return []

def recommend_movies_by_director(movie_title, conn):
    try:
        query = """
        SELECT DISTINCT m2.MovieTitle
        FROM Movie m1
        JOIN Director d ON m1.Director_ID = d.Director_ID
        JOIN Movie m2 ON d.Director_ID = m2.Director_ID
        WHERE m1.MovieTitle = ? AND m1.Movie_ID != m2.Movie_ID;
        """
        cursor = conn.cursor()
        cursor.execute(query, (movie_title,))
        return cursor.fetchall()
    except Exception as e:
        print(f"Error fetching recommendations by director: {e}")
        return []


def recommend_movies_by_leading_actor(movie_title, conn):
    try:
        query = """
        SELECT DISTINCT m2.MovieTitle
        FROM Movie m1
        JOIN MovieActors ma1 ON m1.Movie_ID = ma1.Movie_ID
        JOIN LeadingActor la ON ma1.Actor_ID = la.LeadingActor_ID
        JOIN MovieActors ma2 ON la.LeadingActor_ID = ma2.Actor_ID
        JOIN Movie m2 ON ma2.Movie_ID = m2.Movie_ID
        WHERE m1.MovieTitle = ? AND m1.Movie_ID != m2.Movie_ID;
        """
        cursor = conn.cursor()
        cursor.execute(query, (movie_title,))
        return cursor.fetchall()
    except Exception as e:
        print(f"Error fetching recommendations by leading actor: {e}")
        return []


from tkinter import Tk, Label, Button
from PIL import Image, ImageTk  # Import Pillow modules

# Add movie posters to the main menu
from tkinter import Tk, Label, Button
from PIL import Image, ImageTk  # Import Pillow modules

def main_menu():
    root = Tk()
    root.title("Movie System: Main Menu  ** MADE BY: OMAR ELZARKA , AHMED ELMEHALAWY - AHMED AMER")
    root.configure(bg="black")

    # Define movie poster paths (ensure these images are in the same directory)
    posters = [
        {"title": "Inception", "file": "inception.jpg"},
        {"title": "The Matrix", "file": "matrix.jpg"},
        {"title": "The Godfather", "file": "godfather.jpg"},
        {"title": "The Shawshank Redemption", "file": "shawshank.jpg"},
        {"title": "Goodfellas", "file": "goodfellas.jpg"},
        {"title": "The Truman Show", "file": "truman.jpg"},
        {"title": "seven", "file": "seven.jpg"},
        {"title": "Avatar", "file": "avatar.jpg"},
        {"title": "scent_of_a_woman", "file": "scent_of_a_woman.jpg"},
        {"title": "Interstellar", "file": "interstellar.jpg"},
    ]

    def open_movie_search_engine():
        root.destroy()
        run_movie_search_engine()

    def open_movie_recommendation_system():
        root.destroy()
        run_movie_recommendation_system()

    def on_enter(e):
        e.widget["bg"] = "white"
        e.widget["fg"] = "black"

    def on_leave(e):
        e.widget["bg"] = "gray"
        e.widget["fg"] = "white"

    # Main title
    Label(
        root,
        text="Welcome to the Movie Management System ** MADE BY OMAR ELZARKA , AHMED ELMEHALAWY , AHMED AMER",
        font=("Arial", 20, "bold"),
        bg="black",
        fg="white"
    ).pack(pady=20)

    # Navigation buttons
    search_button = Button(
        root,
        text="Movie Search Engine",
        command=open_movie_search_engine,
        font=("Arial", 14),
        width=25,
        height=2,
        bg="gray",
        fg="white"
    )
    search_button.pack(pady=10)
    search_button.bind("<Enter>", on_enter)
    search_button.bind("<Leave>", on_leave)

    recommendation_button = Button(
        root,
        text="Movie Recommendation System",
        command=open_movie_recommendation_system,
        font=("Arial", 14),
        width=25,
        height=2,
        bg="gray",
        fg="white"
    )
    recommendation_button.pack(pady=10)
    recommendation_button.bind("<Enter>", on_enter)
    recommendation_button.bind("<Leave>", on_leave)

    # Add posters in a grid layout with spacing
    poster_frame = Label(root, bg="black")
    poster_frame.pack(pady=20)

    row, col = 0, 0
    for poster in posters:
        try:
            img = Image.open(poster["file"])
            img = img.resize((150, 200), Image.Resampling.LANCZOS)  # Resize the image
            img = ImageTk.PhotoImage(img)

            # Poster image
            poster_label = Label(poster_frame, image=img, bg="black")
            poster_label.image = img  # Keep a reference to prevent garbage collection
            poster_label.grid(row=row, column=col, padx=30, pady=30)  # Spaced apart

            col += 1
            if col > 4:  # Limit to 5 posters per row
                col = 0
                row += 1  # Move to the next row
        except Exception as e:
            print(f"Error loading poster for {poster['title']}: {e}")


    root.mainloop()




def run_movie_search_engine():
    conn = get_connection()
    if not conn:
        return

    def clear_results():
        result_box.delete(1.0, END)

    def show_recommendations():
        clear_results()
        user_input = input_entry.get().strip()
        rec_type = rec_type_var.get()

        if not user_input:
            result_box.insert(END, "Please enter a value.\n")
            return

        try:
            if rec_type == "Genre":
                results = list_movies_by_genre(user_input, conn)
            elif rec_type == "Director":
                results = list_movies_by_director(user_input, conn)
            elif rec_type == "Leading Actor":
                results = list_movies_by_leading_actor(user_input, conn)
            else:
                results = []

            if results:
                result_box.insert(END, f"Results for {rec_type}: {user_input}\n")
                result_box.insert(END, "-" * 40 + "\n")
                for result in results:
                    result_box.insert(END, f"- {result[0]}\n")
            else:
                result_box.insert(END, f"No results found for {rec_type}: {user_input}.\n")
        except Exception as e:
            result_box.insert(END, f"Error executing query: {e}\n")
            print(f"Error: {e}")

    root = Tk()
    root.title("Movie Search Engine")
    root.configure(bg="black")

    Label(
        root, text="Enter Value:", font=("Arial", 14), bg="black", fg="white"
    ).grid(row=0, column=0, padx=10, pady=10)

    input_entry = Entry(root, width=40, font=("Arial", 12))
    input_entry.grid(row=0, column=1, padx=10, pady=10)

    rec_type_var = StringVar(value="Genre")
    Label(
        root, text="Search By:", font=("Arial", 14), bg="black", fg="white"
    ).grid(row=1, column=0, padx=10, pady=10)

    Button(
        root, text="Genre", command=lambda: rec_type_var.set("Genre"),
        font=("Arial", 12), width=12, height=2, bg="gray", fg="white"
    ).grid(row=1, column=1, padx=5, pady=5)

    Button(
        root, text="Director", command=lambda: rec_type_var.set("Director"),
        font=("Arial", 12), width=12, height=2, bg="gray", fg="white"
    ).grid(row=1, column=2, padx=5, pady=5)

    Button(
        root, text="Leading Actor", command=lambda: rec_type_var.set("Leading Actor"),
        font=("Arial", 12), width=12, height=2, bg="gray", fg="white"
    ).grid(row=1, column=3, padx=5, pady=5)

    Button(
        root, text="Show Results", command=show_recommendations,
        font=("Arial", 14), width=25, height=2, bg="gray", fg="white"
    ).grid(row=2, column=1, columnspan=2, pady=10)

    Label(
        root, text="Results:", font=("Arial", 14), bg="black", fg="white"
    ).grid(row=3, column=0, padx=10, pady=10)

    result_box = Text(root, width=60, height=20, font=("Arial", 12), bg="black", fg="white")
    result_box.grid(row=3, column=1, columnspan=3, padx=10, pady=10)

    root.mainloop()
    conn.close()


# Movie Recommendation System
def run_movie_recommendation_system():
    conn = get_connection()
    if not conn:
        return

    def clear_results():
        result_box.delete(1.0, END)

    def show_recommendations():
        clear_results()
        movie_name = input_entry.get().strip()
        rec_type = rec_type_var.get()

        if not movie_name:
            result_box.insert(END, "Please enter a movie name.\n")
            return

        try:
            if rec_type == "Genre":
                results = recommend_movies_by_genre(movie_name, conn)
            elif rec_type == "Director":
                results = recommend_movies_by_director(movie_name, conn)
            elif rec_type == "Leading Actor":
                results = recommend_movies_by_leading_actor(movie_name, conn)
            else:
                results = []

            if results:
                result_box.insert(END, f"Movies similar to '{movie_name}' (by {rec_type}):\n")
                result_box.insert(END, "-" * 40 + "\n")
                for result in results:
                    result_box.insert(END, f"- {result[0]}\n")
            else:
                result_box.insert(END, f"No similar movies found for '{movie_name}' (by {rec_type}).\n")
        except Exception as e:
            result_box.insert(END, f"Error executing query: {e}\n")
            print(f"Error: {e}")

    root = Tk()
    root.title("Movie Recommendation System")
    root.configure(bg="black")

    Label(
        root, text="Enter Movie Name:", font=("Arial", 14), bg="black", fg="white"
    ).grid(row=0, column=0, padx=10, pady=10)

    input_entry = Entry(root, width=40, font=("Arial", 12))
    input_entry.grid(row=0, column=1, padx=10, pady=10)

    rec_type_var = StringVar(value="Genre")
    Label(
        root, text="Recommendation Type:", font=("Arial", 14), bg="black", fg="white"
    ).grid(row=1, column=0, padx=10, pady=10)

    Button(
        root, text="Genre", command=lambda: rec_type_var.set("Genre"),
        font=("Arial", 12), width=12, height=2, bg="gray", fg="white"
    ).grid(row=1, column=1, padx=5, pady=5)

    Button(
        root, text="Director", command=lambda: rec_type_var.set("Director"),
        font=("Arial", 12), width=12, height=2, bg="gray", fg="white"
    ).grid(row=1, column=2, padx=5, pady=5)

    Button(
        root, text="Leading Actor", command=lambda: rec_type_var.set("Leading Actor"),
        font=("Arial", 12), width=12, height=2, bg="gray", fg="white"
    ).grid(row=1, column=3, padx=5, pady=5)

    Button(
        root, text="Show Recommendations", command=show_recommendations,
        font=("Arial", 14), width=25, height=2, bg="gray", fg="white"
    ).grid(row=2, column=1, columnspan=2, pady=10)

    Label(
        root, text="Recommendations:", font=("Arial", 14), bg="black", fg="white"
    ).grid(row=3, column=0, padx=10, pady=10)

    result_box = Text(root, width=60, height=20, font=("Arial", 12), bg="black", fg="white")
    result_box.grid(row=3, column=1, columnspan=3, padx=10, pady=10)

    root.mainloop()
    conn.close()



# Run the Main Menu
if __name__ == "__main__":
    main_menu()