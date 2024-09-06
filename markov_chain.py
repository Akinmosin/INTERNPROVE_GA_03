import random

class MarkovChain:
    def __init__(self):
        self.chain = {}

    def train(self, text):
        words = text.split()
        for i in range(len(words) - 1):
            current_word = words[i]
            next_word = words[i + 1]
            
            if current_word not in self.chain:
                self.chain[current_word] = []
            self.chain[current_word].append(next_word)

    def generate_text(self, length=20):
        # Start with a random word
        current_word = random.choice(list(self.chain.keys()))
        result = [current_word]

        for _ in range(length - 1):
            next_words = self.chain.get(current_word, None)
            if not next_words:
                break
            current_word = random.choice(next_words)
            result.append(current_word)

        return ' '.join(result)

# Example usage:
if __name__ == "__main__":
    text = "the quick brown fox jumps over the lazy dog the quick brown dog runs away"
    markov = MarkovChain()
    markov.train(text)
    generated_text = markov.generate_text(15)
    print(generated_text)
