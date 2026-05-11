import re
from collections import defaultdict

class MemoryExtractor:
    def __init__(self):
        self.conversation_history = []
        self.requirements = []

    def add_conversation(self, conversation):
        self.conversation_history.append(conversation)

    def filter_conversations(self):
        for convo in self.conversation_history:
            if self.is_relevant(convo):
                self.requirements.append(convo)

    def is_relevant(self, convo):
        keywords = ['requirement', 'design', 'code', 'implementation', 'feature']
        return any(keyword in convo.lower() for keyword in keywords)

    def extract_keywords(self):
        keywords = set()
        for convo in self.requirements:
            words = re.findall(r'\w+', convo)
            keywords.update(words)
        return keywords

    def search(self, term):
        return [convo for convo in self.requirements if term.lower() in convo.lower()]