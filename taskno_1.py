# Mental Health Chatbot

import tkinter as tk
from tkinter import scrolledtext
import re

# Chatbot logic
def mental_health_bot(user_input):
    user_input = user_input.lower()

    # 1. Greetings and Introductions
    if re.search(r'\bhello\b|\bhi\b|\bhey\b|\bgood morning\b|\bgood evening\b|\bgreetings\b', user_input, re.IGNORECASE):
        return "Hello! I'm here to support you. How are you feeling today?"
    
    # 2. Asking for Help
    elif re.search(r'\bhelp\b|\bi need help\b|\bsupport\b|\bcan you help me\b|\bassist\b', user_input, re.IGNORECASE):
        return "I'm here to help. What’s on your mind?"

    # 3. Expressing Anxiety or Stress
    elif re.search(r'\banxious\b|\banxiety\b|\bstressed\b|\bstress\b|\boverwhelmed\b|\bnervous\b', user_input, re.IGNORECASE):
        return "It’s okay to feel anxious sometimes. Would you like to try a breathing exercise?"

    # 4. Expressing Sadness or Depression
    elif re.search(r'\bsad\b|\bdepressed\b|\bfeeling down\b|\bfeeling low\b|\bblue\b|\bunhappy\b', user_input, re.IGNORECASE):
        return "I'm sorry you're feeling this way. Remember, it's okay to feel sad sometimes. I'm here to listen."

    # 5. Talking About Loneliness
    elif re.search(r'\blonely\b|\balone\b|\bisolated\b|\bno one\b|\bby myself\b', user_input, re.IGNORECASE):
        return "Feeling lonely can be tough. Remember, you're not alone. I’m here for you."

    # 6. Dealing with Anger or Frustration
    elif re.search(r'\bangry\b|\bfrustrated\b|\bmad\b|\bupset\b|\birritated\b', user_input, re.IGNORECASE):
        return "It’s okay to feel angry sometimes. Do you want to talk about what’s bothering you?"

    # 7. Experiencing Panic or Fear
    elif re.search(r'\bpanic\b|\bscared\b|\bfear\b|\bafraid\b|\bterrified\b|\bnervous\b', user_input, re.IGNORECASE):
        return "It’s okay to feel scared. Let’s try to focus on your breathing together."

    # 8. Seeking Encouragement or Motivation
    elif re.search(r'\bmotivate\b|\bmotivation\b|\bencourage\b|\binspire\b|\buplift\b|\bneed motivation\b', user_input, re.IGNORECASE):
        return "You’ve got this! Remember, every small step forward is progress."

    # 9. Requesting Breathing or Calming Exercises
    elif re.search(r'\bbreathing\b|\bcalm\b|\bcalming\b|\brelax\b|\brelaxation\b|\bbreathing exercise\b', user_input, re.IGNORECASE):
        return "Let’s do a simple breathing exercise together: Inhale slowly for 4 seconds, hold for 4 seconds, and exhale for 4 seconds. Repeat a few times."

    # 10. Expressing Gratitude
    elif re.search(r'\bthank you\b|\bthanks\b|\bappreciate\b|\bgrateful\b|\bgratitude\b', user_input, re.IGNORECASE):
        return "You’re welcome! I'm glad I could help."

    # 11. Discussing Sleep Issues
    elif re.search(r'\bcan’t sleep\b|\binsomnia\b|\bsleep issues\b|\bsleep problems\b|\btrouble sleeping\b|\bnot sleeping\b', user_input, re.IGNORECASE):
        return "Sleep is important for your well-being. Would you like some tips to help you relax before bed?"

    # 12. Talking About Physical Health Concerns
    elif re.search(r'\bheadache\b|\btired\b|\bfatigue\b|\bpain\b|\bunwell\b|\bsick\b|\bhealth problems\b', user_input, re.IGNORECASE):
        return "Your physical health is important too. If you’re feeling unwell, it’s okay to rest and take care of yourself."

    # 13. Expressing Suicidal Thoughts
    elif re.search(r'\bsuicidal\b|\bsuicide\b|\bend my life\b|\bkill myself\b|\bnot want to live\b|\bself-harm\b', user_input, re.IGNORECASE):
        return "I'm really sorry you're feeling this way, but I'm not equipped to handle this situation. Please reach out to a mental health professional immediately or call a suicide prevention hotline."

    # 14. Ending the Conversation
    elif re.search(r'\bbye\b|\bgoodbye\b|\btalk later\b|\bsee you\b|\btake care\b', user_input, re.IGNORECASE):
        return "Goodbye! Remember, I’m always here whenever you need to talk."

    # 15. General Well-being Checks
    elif re.search(r'\bhow are you\b|\bwhat’s up\b|\bare you there\b', user_input, re.IGNORECASE):
        return "I’m here to support you. How are you feeling today?"

    # 16. Offering Resources or Contacts
    elif re.search(r'\bresources\b|\bhotline\b|\bprofessional help\b|\bcounseling\b|\btherapist\b', user_input, re.IGNORECASE):
        return "If you need more support, I can suggest some resources or help you find a professional to talk to."

    # 17. Positive Affirmations
    elif re.search(r'\baffirmation\b|\bpositive\b|\bencouragement\b|\bkind words\b', user_input, re.IGNORECASE):
        return "You are strong, capable, and worthy of good things."

    # 18. Handling Unrecognized Inputs
    else:
        return "I’m not sure I understand. Could you tell me more about what you’re feeling?"

# Function to handle sending a message
def send_message():
    user_input = entry.get()
    chat_history.configure(state='normal')
    chat_history.insert(tk.END, "You: " + user_input + "\n")
    
    response = mental_health_bot(user_input)
    chat_history.insert(tk.END, "Bot: " + response + "\n\n")
    chat_history.configure(state='disabled')
    
    entry.delete(0, tk.END)
    if "bye" in user_input.lower() or "goodbye" in user_input.lower():
        window.quit()

# Creating main window
window = tk.Tk()
window.title("Mental Health Bot")

# Chat history area
chat_history = scrolledtext.ScrolledText(window, wrap=tk.WORD, state='disabled')
chat_history.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# User input area
entry = tk.Entry(window, width=80)
entry.pack(padx=10, pady=10, side=tk.LEFT, expand=True, fill=tk.X)
entry.bind("<Return>", lambda event: send_message())

# Send button
send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack(padx=10, pady=10, side=tk.RIGHT)

# GUI loop
window.mainloop()
