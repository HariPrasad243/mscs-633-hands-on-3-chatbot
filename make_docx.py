"""Build Hands-On-Assignment-3_QA-Chatbot.docx with python-docx.

Run from the project root:
    venv/bin/python make_docx.py
Requires screenshots/chatbot-running.png to exist.
"""

import os

from docx import Document
from docx.shared import Inches, Pt

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SCREENSHOT = os.path.join(BASE_DIR, "screenshots", "chatbot-running.png")
OUTPUT = os.path.join(BASE_DIR, "Hands-On-Assignment-3_QA-Chatbot.docx")

doc = Document()

style = doc.styles["Normal"]
style.font.name = "Calibri"
style.font.size = Pt(11)

title = doc.add_heading(
    "Hands-On Assignment 3: Create a Simple Q&A Chatbot with Python", level=0
)
title.alignment = 1  # centred

doc.add_paragraph("Student: Hari Prasad Rayala")
doc.add_paragraph("Course: MSCS-633-B01 — Advance Artificial Intelligence")
doc.add_paragraph("University: University of the Cumberlands")
doc.add_paragraph("Due date: Sunday, November 22, 2026, 10:59 PM CST")
doc.add_paragraph("Points: 50")

doc.add_heading("1. Description", level=1)
doc.add_paragraph(
    "This assignment asks for a simple Q&A chatbot with a Django user "
    "interface, built with the ChatterBot package. The chatbot in this "
    "submission is trained on 28 question-and-answer pairs about "
    "artificial intelligence fundamentals: artificial intelligence, machine "
    "learning, deep learning, natural language processing, Python, Django, "
    "and ChatterBot itself. The user types a question in the browser, "
    "Django sends it to ChatterBot, and ChatterBot's BestMatch logic "
    "returns the best trained answer, which is shown in the chat window."
)

doc.add_heading("2. How to install and run", level=1)
doc.add_paragraph(
    "Tested on Python 3.12.3 with Django 5.1.4 and ChatterBot 1.2.15. "
    "From the project folder, run:"
)
commands = [
    "python3 -m venv venv",
    "source venv/bin/activate        # on Windows: venv\\Scripts\\activate",
    "pip install -r requirements.txt",
    "python -m spacy download en_core_web_sm",
    "python manage.py migrate",
    "python manage.py train_chatbot",
    "python manage.py runserver",
]
for command in commands:
    doc.add_paragraph(command, style="List Bullet")
doc.add_paragraph(
    "Then open http://127.0.0.1:8000/ in a browser, click 'Open the "
    "chatbot', type a question, and click 'Send'. The chat page is at "
    "http://127.0.0.1:8000/chat/ and the API is POST /api/chat/ with "
    "JSON {\"message\": \"...\"}."
)

doc.add_heading("3. Training Q&A topics", level=1)
doc.add_paragraph(
    "The 28 training pairs in chat/training_data.py cover: greetings and "
    "what the bot can do; artificial intelligence; machine learning; deep "
    "learning; the difference between AI, machine learning, and deep "
    "learning; natural language processing and what it is used for; "
    "chatbots; neural networks; supervised, unsupervised, and reinforcement "
    "learning; large language models; computer vision; overfitting; "
    "training datasets; Python and why it is popular for AI; Python AI "
    "libraries; Django; ChatterBot, how it works, and how to train it; and "
    "how this chatbot itself works."
)
doc.add_paragraph(
    "Example trained pairs: 'What is artificial intelligence?' -> "
    "'Artificial intelligence (AI) is the simulation of human intelligence "
    "by machines...'; 'What is machine learning?' -> 'Machine learning is "
    "a branch of artificial intelligence in which a computer learns "
    "patterns from data...'; 'What is ChatterBot?' -> 'ChatterBot is a "
    "Python library for building chatbots...'"
)

doc.add_heading("4. Test evidence", level=1)
doc.add_paragraph(
    "The application was run for real and tested with the live Django "
    "server. 'python manage.py check' reported no issues, migrations "
    "applied, and 'python manage.py train_chatbot' reported 'Trained "
    "chatbot on 28 Q&A pairs. Stored statements: 56'. Six different "
    "questions were sent to POST /api/chat/ and every one returned the "
    "exact trained answer with confidence 1.0:"
)
tests = [
    ("What is artificial intelligence?", "1.0"),
    ("What is machine learning?", "1.0"),
    ("What is deep learning?", "1.0"),
    ("What is ChatterBot?", "1.0"),
    ("What is Django?", "1.0"),
    ("What is natural language processing?", "1.0"),
]
for question, confidence in tests:
    doc.add_paragraph(
        f"{question} — confidence {confidence}", style="List Bullet"
    )

doc.add_heading("5. Screenshot of the running chatbot", level=1)
doc.add_paragraph(
    "The screenshot below shows the working Django chatbot in the browser, "
    "with a question asked and the bot's answer shown in the chat history."
)
if os.path.exists(SCREENSHOT):
    doc.add_picture(SCREENSHOT, width=Inches(6.0))
    doc.paragraphs[-1].alignment = 1
else:
    doc.add_paragraph(
        "[Screenshot missing: screenshots/chatbot-running.png was not found "
        "when this document was built.]"
    )

doc.add_heading("6. Files submitted", level=1)
doc.add_paragraph(
    "Python source code: the full Django project in this folder (see "
    "manifest.txt for the complete file list). Manifest: MANIFEST.in and "
    "manifest.txt. This Word document: "
    "Hands-On-Assignment-3_QA-Chatbot.docx."
)

doc.add_heading("7. GitHub repository URL", level=1)
doc.add_paragraph("https://github.com/HariPrasad243/mscs-633-hands-on-3-chatbot")

doc.save(OUTPUT)
print(f"Saved {OUTPUT}")
