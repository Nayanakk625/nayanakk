import tkinter as tk
from tkinter import messagebox
import string

def analyze_password():
    password = entry_password.get()
    score = 0
    feedback = ""

    if len(password) >= 8:
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    if score == 5:
        feedback = "Strong password!"
    elif score >= 3:
        feedback = "Moderate password."
    else:
        feedback = "Weak password. Consider making it longer and including uppercase letters, numbers, and symbols."

    crack_time = {0: "a few seconds", 1: "a few minutes", 2: "a few hours", 3: "a few days", 4: "several months", 5: "years"}
    result_label.config(text=f"Score: {score}/5\nEstimated Crack Time: {crack_time[score]}\nFeedback: {feedback}")

def generate_wordlist():
    name = entry_name.get().lower()
    pet = entry_pet.get().lower()
    year = entry_year.get()

    base_words = [name, pet, year, name + pet, pet + name, name + year, pet + year]
    special_chars = ['!', '@', '#', '$', '123', '2024']
    variations = []

    leet_map = str.maketrans("aeynsob", "@3y!n$0")  # ✅ Fixed length

    for word in base_words:
        variations.append(word)
        variations.append(word.upper())
        variations.append(word.capitalize())
        variations.append(word[::-1])
        variations.append(word.translate(leet_map))
        for char in special_chars:
            variations.append(word + char)
            variations.append(char + word)

    # Remove duplicates
    variations = list(set(variations))

    with open("wordlist.txt", "w") as f:
        for item in variations:
            f.write(item + "\n")

    messagebox.showinfo("Success", "Wordlist generated and saved as 'wordlist.txt'!")

# GUI
root = tk.Tk()
root.title("Password Analyzer + Wordlist Generator")

tk.Label(root, text="Enter Password:").grid(row=0, column=0, sticky="e")
entry_password = tk.Entry(root, show="*")
entry_password.grid(row=0, column=1)

tk.Label(root, text="Name:").grid(row=1, column=0, sticky="e")
entry_name = tk.Entry(root)
entry_name.grid(row=1, column=1)

tk.Label(root, text="Pet Name:").grid(row=2, column=0, sticky="e")
entry_pet = tk.Entry(root)
entry_pet.grid(row=2, column=1)

tk.Label(root, text="Birth Year:").grid(row=3, column=0, sticky="e")
entry_year = tk.Entry(root)
entry_year.grid(row=3, column=1)

tk.Button(root, text="Analyze Password", command=analyze_password).grid(row=4, column=0, pady=10)
tk.Button(root, text="Generate Wordlist", command=generate_wordlist).grid(row=4, column=1, pady=10)

result_label = tk.Label(root, text="", fg="blue")
result_label.grid(row=5, column=0, columnspan=2)

root.mainloop()
