"""
Training data for the Hands-On Assignment 3 Q&A chatbot.

Topic: Artificial Intelligence fundamentals.
Each pair is (question, answer). Answers are concise and factual.
The pairs are used with ChatterBot's ListTrainer (see chat/chatbot.py).
"""

# A list of (question, answer) pairs. 28 pairs in total.
TRAINING_PAIRS = [
    (
        "Hello",
        "Hello! I am the AI Fundamentals chatbot. Ask me anything about "
        "artificial intelligence, machine learning, deep learning, NLP, "
        "Python, Django, or ChatterBot.",
    ),
    (
        "Hi",
        "Hi there! Ask me a question about artificial intelligence, machine "
        "learning, deep learning, or Python.",
    ),
    (
        "What can you do?",
        "I can answer questions about artificial intelligence fundamentals, "
        "including machine learning, deep learning, natural language "
        "processing, Python, Django, and ChatterBot.",
    ),
    (
        "What is artificial intelligence?",
        "Artificial intelligence (AI) is the simulation of human intelligence "
        "by machines, so that a computer can perform tasks such as learning, "
        "reasoning, problem solving, and understanding language.",
    ),
    (
        "What is machine learning?",
        "Machine learning is a branch of artificial intelligence in which a "
        "computer learns patterns from data, instead of being given explicit "
        "rules for every task, and then uses what it learned to make "
        "predictions or decisions on new data.",
    ),
    (
        "What is the difference between AI and machine learning?",
        "Artificial intelligence is the broad field of making machines behave "
        "intelligently. Machine learning is a subfield of AI that learns "
        "patterns from data. So all machine learning is AI, but not all AI "
        "is machine learning.",
    ),
    (
        "What is deep learning?",
        "Deep learning is a subfield of machine learning that uses artificial "
        "neural networks with many layers to learn complex patterns from "
        "large amounts of data, for example in image recognition and "
        "natural language processing.",
    ),
    (
        "What is the difference between deep learning and machine learning?",
        "Machine learning includes many methods, such as decision trees and "
        "regression. Deep learning is one kind of machine learning that uses "
        "multi-layer neural networks and usually needs more data and "
        "computing power.",
    ),
    (
        "What is natural language processing?",
        "Natural language processing (NLP) is a branch of AI that helps "
        "computers understand, interpret, and generate human language, "
        "for example in chatbots, translation, and sentiment analysis.",
    ),
    (
        "What is NLP used for?",
        "NLP is used for chatbots, machine translation, text summarisation, "
        "sentiment analysis, speech recognition, and search.",
    ),
    (
        "What is a chatbot?",
        "A chatbot is a program that uses natural language processing to "
        "hold a conversation with a user, usually by matching a question "
        "to the best answer it was trained on.",
    ),
    (
        "What is a neural network?",
        "A neural network is a machine learning model inspired by the human "
        "brain. It is made of layers of connected units, called neurons, "
        "that transform an input step by step into an output.",
    ),
    (
        "What is supervised learning?",
        "Supervised learning is machine learning from labelled examples. "
        "The model is shown inputs together with the correct outputs, "
        "learns the mapping between them, and then predicts outputs for "
        "new inputs.",
    ),
    (
        "What is unsupervised learning?",
        "Unsupervised learning is machine learning from data without labels. "
        "The model finds structure in the data itself, for example by "
        "clustering similar items together or finding patterns.",
    ),
    (
        "What is reinforcement learning?",
        "Reinforcement learning is machine learning in which an agent learns "
        "by trial and error. It takes actions, receives rewards or penalties, "
        "and learns a strategy that maximises the total reward over time.",
    ),
    (
        "What is a large language model?",
        "A large language model is a deep learning model trained on very "
        "large amounts of text. It learns the patterns of language and can "
        "generate text, answer questions, summarise, and translate.",
    ),
    (
        "What is computer vision?",
        "Computer vision is a branch of AI that helps computers understand "
        "images and video, for example to recognise objects, faces, and "
        "gestures.",
    ),
    (
        "What is overfitting?",
        "Overfitting happens when a model memorises its training data, "
        "including its noise, instead of learning general patterns. It "
        "performs well on training data but poorly on new data.",
    ),
    (
        "What is a training dataset?",
        "A training dataset is a collection of examples used to teach a "
        "machine learning model. In this project, the training data is the "
        "list of question-and-answer pairs in training_data.py.",
    ),
    (
        "What is Python?",
        "Python is a high-level, general-purpose programming language. It is "
        "widely used in AI because it is readable, has a large community, "
        "and has libraries such as NumPy, pandas, scikit-learn, and "
        "TensorFlow.",
    ),
    (
        "Why is Python popular for AI?",
        "Python is popular for AI because it is easy to read and write, it "
        "has powerful AI and data libraries, and it has a large community "
        "and many tutorials and tools.",
    ),
    (
        "What libraries are used in Python for AI?",
        "Common Python libraries for AI are NumPy and pandas for data, "
        "scikit-learn for machine learning, TensorFlow and PyTorch for "
        "deep learning, and NLTK and spaCy for natural language processing.",
    ),
    (
        "What is Django?",
        "Django is a high-level Python web framework. It provides routing, "
        "templates, an ORM, and an admin interface, so a developer can "
        "build a web application quickly and securely.",
    ),
    (
        "What is ChatterBot?",
        "ChatterBot is a Python library for building chatbots. It stores "
        "conversations, learns from training data, and picks the best "
        "matching response to a new message.",
    ),
    (
        "How does ChatterBot work?",
        "ChatterBot stores statements it has been trained on. When it "
        "receives a new message, its BestMatch logic adapter compares the "
        "message with the stored statements and returns the response with "
        "the highest confidence.",
    ),
    (
        "How do I train ChatterBot?",
        "You train ChatterBot with a trainer, for example ListTrainer, by "
        "passing it a list of questions and answers. In this project, "
        "ListTrainer trains the bot on the pairs in training_data.py.",
    ),
    (
        "How does this chatbot work?",
        "This chatbot is a Django web application. The browser sends your "
        "question to Django, Django asks the ChatterBot model for a "
        "response, and the answer is shown in the chat window.",
    ),
    (
        "Thank you",
        "You are welcome! Ask me another question about AI, machine learning, "
        "or Python any time.",
    ),
]

# Flattened conversation for ListTrainer: question, answer, question, answer, ...
TRAINING_CONVERSATION = [
    item for pair in TRAINING_PAIRS for item in pair
]
