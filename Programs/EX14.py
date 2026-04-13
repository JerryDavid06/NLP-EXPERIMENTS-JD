def check(sentence):
    w = sentence.lower().split()
    
    if len(w) < 2:
        return "Invalid"

    subject, verb = w[0], w[1]

    if subject in ["he", "she", "it"]:
        return "Correct" if verb.endswith("s") else "Incorrect"
    elif subject in ["i", "you", "we", "they"]:
        return "Correct" if not verb.endswith("s") else "Incorrect"
    else:
        return "Invalid"

print("Input: he runs\nOutput:", check("he runs"))
print("\nInput: they run\nOutput:", check("they run"))
