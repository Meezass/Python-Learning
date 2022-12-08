# Write your solution here
def longest(strings: list):
    best=strings[0]
    for words in strings:
        if len(best)<len(words):
            best=words
    return best

if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))