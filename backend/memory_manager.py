class MemoryManager:
    def __init__(self):
        self.memory = []

    def add_memory(self, conversation):
        """ Adds a new conversation to memory. """
        self.memory.append(conversation)

    def get_memory(self):
        """ Retrieves the entire conversation memory. """
        return self.memory

    def extract_memory(self, query):
        """ Extracts relevant information from memory based on a query. """
        relevant_memory = [c for c in self.memory if query in c]
        return relevant_memory

# Example usage:
# memory_manager = MemoryManager()
# memory_manager.add_memory("Hello, how can I help you?")
# print(memory_manager.get_memory())
# print(memory_manager.extract_memory("help"))