"""
ChatterBot setup for the Q&A chatbot.

A single shared ChatBot instance is created lazily and reused for the
life of the Django process. Training data is stored in a SQLite file
(chatbot_db.sqlite3) so the bot does not need to be retrained on every
request. Run ``python manage.py train_chatbot`` once to train it, or
let ``get_chatbot()`` train automatically if the database is empty.
"""

import os

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

from django.conf import settings

from .training_data import TRAINING_CONVERSATION

# The ChatterBot storage database lives in the Django project root.
DATABASE_PATH = os.path.join(settings.BASE_DIR, "chatbot_db.sqlite3")

# One shared instance per process.
_CHATBOT = None


def create_chatbot():
    """Create a ChatterBot instance backed by SQLite storage."""
    return ChatBot(
        "AI Fundamentals Chatbot",
        storage_adapter="chatterbot.storage.SQLStorageAdapter",
        database_uri=f"sqlite:///{DATABASE_PATH}",
        logic_adapters=[
            {
                "import_path": "chatterbot.logic.BestMatch",
                "default_response": (
                    "I am not sure about that yet. Please ask me about "
                    "artificial intelligence, machine learning, deep "
                    "learning, NLP, Python, Django, or ChatterBot."
                ),
                "maximum_similarity_threshold": 0.90,
            }
        ],
    )


def train_chatbot(chatbot):
    """Train the bot on the Q&A pairs in training_data.py."""
    trainer = ListTrainer(chatbot)
    trainer.train(TRAINING_CONVERSATION)
    return chatbot


def get_chatbot():
    """Return the shared bot, training it first if its database is empty."""
    global _CHATBOT  # noqa: PLW0603 - intentional process-wide singleton
    if _CHATBOT is None:
        _CHATBOT = create_chatbot()
        # Train only when there is nothing stored yet, so a restart is fast.
        if _CHATBOT.storage.count() == 0:
            train_chatbot(_CHATBOT)
    return _CHATBOT


def get_answer(message):
    """Ask the bot a question and return (answer_text, confidence)."""
    chatbot = get_chatbot()
    response = chatbot.get_response(message)
    return str(response), float(response.confidence)
