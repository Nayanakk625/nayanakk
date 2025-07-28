# password_tool.py

from zxcvbn import zxcvbn
import itertools

def analyze_password(password):
    result = zxcvbn(password)
    print("\n🔐 Password Strength Report:")
    print(f"Password: {password}")
    print(f"Score (0-4): {result['score']}")
    print(f"Crack time (offline): {result['crack_times_display']['offline_fast_hashing_1e10_per_second']}")
    print(f"Feedback: {result['feedback']['suggestions']}")

def generate_wordlist(keywords):
    leet_dict = {'a': ['a', '@', '4'], 'e': ['e', '3'], 'i': ['i', '1'], 'o': ['o', '0'], 's': ['s', '$', '5']}
    years = ['2024', '2025', '123', '321']

    combos = set()
    for word in keywords:
        base_variants = [''.join(c) for c in itertools.product(*[leet_dict.get(ch.lower(), [ch]) for ch in word])]
        for variant in base_variants:
            for year in years:
                combos.add(variant)
                combos.add(variant + year)
                combos.add(year + variant)

    return sorted(combos)

def save_to_file(words, filename="wordlist.txt"):
    with open(filename, 'w') as f:
        for word in words:
            f.write(word + '\n')
    print(f"\n✅ Wordlist saved to {filename}")

if __name__ == "__main__":
    print("🔒 Password Strength Analyzer + Wordlist Generator")

    pwd = input("\nEnter a password to analyze: ")
    analyze_password(pwd)

    print("\n--- Wordlist Generator ---")
    name = input("Name: ")
    pet = input("Pet name: ")
    dob = input("DOB (e.g., 1998): ")

    keywords = [name, pet, dob]
    wordlist = generate_wordlist(keywords)
    save_to_file(wordlist)
