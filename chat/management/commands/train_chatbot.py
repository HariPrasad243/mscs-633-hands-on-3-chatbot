"""Management command to train the ChatterBot from training_data.py.

Usage:
    python manage.py train_chatbot
"""

from django.core.management.base import BaseCommand

from chat.chatbot import create_chatbot, train_chatbot
from chat.training_data import TRAINING_PAIRS


class Command(BaseCommand):
    help = "Train the Q&A chatbot on the pairs in chat/training_data.py."

    def handle(self, *args, **options):
        chatbot = create_chatbot()
        train_chatbot(chatbot)
        self.stdout.write(
            self.style.SUCCESS(
                f"Trained chatbot on {len(TRAINING_PAIRS)} Q&A pairs. "
                f"Stored statements: {chatbot.storage.count()}"
            )
        )
