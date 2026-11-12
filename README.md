# Hands-On Assignment 3 — Create a Simple Q&A Chatbot with Python

- **Student:** Hari Prasad Rayala
- **Course:** MSCS-633-B01 — Advance Artificial Intelligence, University of the Cumberlands
- **Assignment:** Hands-On Assignment 3: Create a Simple Q&A Chatbot with Python
- **Due date:** Sunday, November 22, 2026, 10:59 PM CST
- **Points:** 50

## What this project is

A simple Q&A chatbot about artificial intelligence fundamentals, built with a
Django web user interface and the ChatterBot package, exactly as the assignment
asks. The chatbot is trained on 28 question-and-answer pairs (in
`chat/training_data.py`) covering artificial intelligence, machine learning,
deep learning, natural language processing, Python, Django, and ChatterBot
itself. The user types a question in the browser, Django sends it to
ChatterBot, and ChatterBot's BestMatch logic returns the best trained answer.

## Project structure

```
mscs-633-hands-on-3-chatbot/
├── Hands-On-Assignment-3_QA-Chatbot.docx   # Word submission document (with screenshot)
├── MANIFEST.in
├── README.md                               # this file
├── manifest.txt                            # list of every deliverable file
├── requirements.txt                        # pinned versions
├── manage.py                               # Django entry point
├── qa_chatbot/                             # Django project (settings, urls, wsgi)
│   ├── settings.py
│   └── urls.py
├── chat/                                   # Django app
│   ├── chatbot.py                          # ChatterBot setup (singleton, training)
│   ├── training_data.py                    # 28 Q&A pairs + flattened ListTrainer list
│   ├── views.py                            # home page, chat page, /api/chat/
│   ├── urls.py                             # /, /chat/, /api/chat/
│   ├── templates/chat/home.html            # home page
│   ├── templates/chat/chat.html            # chat UI (input box, Send, chat history)
│   └── management/commands/train_chatbot.py
├── screenshots/
│   └── chatbot-running.png                 # real screenshot of the working chatbot
├── db.sqlite3                              # Django database (created by migrate)
└── chatbot_db.sqlite3                      # ChatterBot storage (created by training)
```

## Versions used (tested, working)

Tested on this machine on November 12, 2026:

| Component | Version |
|---|---|
| Python | 3.12.3 |
| Django | 5.1.4 |
| ChatterBot | 1.2.15 |
| spaCy | 3.8.18 |
| spaCy English model (`en_core_web_sm`) | 3.8.0 |
| SQLAlchemy | 2.0.57 |
| python-docx | 1.2.0 |

Note on compatibility: the original ChatterBot 1.1.0 does not support Python 3.12.
ChatterBot 1.2.15 is the maintained release line that does — it installed
cleanly on Python 3.12.3 with Django 5.1.4, and it requires the spaCy English
model `en_core_web_sm`, which is installed with
`python -m spacy download en_core_web_sm` (see setup below). No older Python
was available on this machine (only Python 3.12.3), and none was needed.

## How to install and run

```bash
# 1. From this project folder, create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate        # on Windows: venv\Scripts\activate

# 2. Install the pinned dependencies
pip install -r requirements.txt

# 3. Install the spaCy English model that ChatterBot needs
python -m spacy download en_core_web_sm

# 4. Apply Django migrations
python manage.py migrate

# 5. Train the chatbot (28 Q&A pairs; stored in chatbot_db.sqlite3)
python manage.py train_chatbot

# 6. Start the development server
python manage.py runserver
```

Then open http://127.0.0.1:8000/ in a browser, click **Open the chatbot**,
type a question, and click **Send**.

Useful URLs:

- Home page: http://127.0.0.1:8000/
- Chat page: http://127.0.0.1:8000/chat/
- Chat API (POST JSON `{"message": "..."}`): http://127.0.0.1:8000/api/chat/
- Example deep link that asks a question on load:
  http://127.0.0.1:8000/chat/?ask=What+is+machine+learning%3F

## How the chatbot works

1. `chat/training_data.py` holds 28 (question, answer) pairs.
2. `python manage.py train_chatbot` trains ChatterBot with `ListTrainer` and
   stores the 56 statements (28 questions + 28 answers) in
   `chatbot_db.sqlite3` (SQLite, via `SQLStorageAdapter`).
3. `chat/chatbot.py` creates one shared `ChatBot` instance with the
   `BestMatch` logic adapter. If the storage database is empty it trains
   automatically on first use, so the app also works without step 5 above.
4. `chat/views.py` serves the home and chat pages, and `POST /api/chat/`
   returns `{"answer": "...", "confidence": 0.95}` as JSON.
5. `chat/templates/chat/chat.html` is the Django UI: a chat-history panel, an
   input box, and a Send button. It calls `/api/chat/` with `fetch` and
   appends each question and answer to the history.

## Training topics

The 28 Q&A pairs cover: greetings and what the bot can do; artificial
intelligence; machine learning; deep learning; the AI / ML / deep-learning
distinction; natural language processing; chatbots; neural networks;
supervised, unsupervised, and reinforcement learning; large language models;
computer vision; overfitting; training datasets; Python and why it is popular
for AI; Python AI libraries; Django; ChatterBot, how it works, and how to
train it; and how this chatbot itself works.

## Test evidence (run for real on November 12, 2026)

Setup: `python manage.py check` — no issues. `python manage.py migrate` —
all migrations applied. `python manage.py train_chatbot` — "Trained chatbot
on 28 Q&A pairs. Stored statements: 56". Development server started on
`http://127.0.0.1:8000/` — home page 200, chat page 200.

Six different questions were sent to the live `POST /api/chat/` endpoint
with `curl`. Every one returned the exact trained answer with confidence 1.0:

| # | Question | Answer (exact) | Confidence |
|---|---|---|---|
| 1 | What is artificial intelligence? | Artificial intelligence (AI) is the simulation of human intelligence by machines, so that a computer can perform tasks such as learning, reasoning, problem solving, and understanding language. | 1.0 |
| 2 | What is machine learning? | Machine learning is a branch of artificial intelligence in which a computer learns patterns from data, instead of being given explicit rules for every task, and then uses what it learned to make predictions or decisions on new data. | 1.0 |
| 3 | What is deep learning? | Deep learning is a subfield of machine learning that uses artificial neural networks with many layers to learn complex patterns from large amounts of data, for example in image recognition and natural language processing. | 1.0 |
| 4 | What is ChatterBot? | ChatterBot is a Python library for building chatbots. It stores conversations, learns from training data, and picks the best matching response to a new message. | 1.0 |
| 5 | What is Django? | Django is a high-level Python web framework. It provides routing, templates, an ORM, and an admin interface, so a developer can build a web application quickly and securely. | 1.0 |
| 6 | What is natural language processing? | Natural language processing (NLP) is a branch of AI that helps computers understand, interpret, and generate human language, for example in chatbots, translation, and sentiment analysis. | 1.0 |

A real screenshot of the working chatbot UI is in
`screenshots/chatbot-running.png` and is also included in the Word document.

## Submission

The Blackboard submission instructions ask for: Python source code, a
manifest file, a Word document containing a screenshot, and a GitHub
repository URL link to share the code.

- Source code: this project folder (see `manifest.txt` for the full file list).
- Manifest: `MANIFEST.in` and `manifest.txt` in the project root.
- Word document: `Hands-On-Assignment-3_QA-Chatbot.docx` in the project root —
  it includes the screenshot and a placeholder line for the GitHub URL.
- GitHub repository URL: **https://github.com/HariPrasad243/mscs-633-hands-on-3-chatbot** — the source code for this project is published there.
  The student should paste this URL into the Blackboard submission
  text before submitting.

This project was **not** submitted to Blackboard. It is ready for the student
to review and submit (one attempt allowed in Blackboard, SafeAssign enabled).

## References

- Django: https://www.djangoproject.com/
- ChatterBot: https://pypi.org/project/ChatterBot/
- ChatterBot Django documentation:
  http://chatterbot.readthedocs.io/en/stable/django/index.html
- About ChatterBot: https://chatterbot.readthedocs.io/en/stable/
