"""Views for the Q&A chatbot: home page, chat page, and chat API."""

import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST

from .chatbot import get_answer


def home(request):
    """Simple home page describing the chatbot and how to use it."""
    return render(request, "chat/home.html")


def chat_page(request):
    """The chat page: input box, send button, and chat history."""
    return render(request, "chat/chat.html")


@require_POST
def chat_api(request):
    """Accept a JSON question and return the bot's answer as JSON.

    Request body:  {"message": "What is machine learning?"}
    Response body: {"answer": "...", "confidence": 0.95}
    """
    try:
        data = json.loads(request.body.decode("utf-8"))
    except (json.JSONDecodeError, UnicodeDecodeError):
        return JsonResponse({"error": "Request body must be valid JSON."}, status=400)

    message = str(data.get("message", "")).strip()
    if not message:
        return JsonResponse({"error": "Please enter a question."}, status=400)

    answer, confidence = get_answer(message)
    return JsonResponse({"answer": answer, "confidence": confidence})
