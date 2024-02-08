conversation = [
    {
        "role": "system",
        "content": "Today's date is 2024-02-08.\nThe current working directory is /Users/jakekoenig/rawdog, which IS a git repository.\nThe user's operating system is Darwin\n        "
    },
    {
        "role": "user",
        "content": "Can you read the readme and use the information to change rawdog to use mixtral with ollama?"
    }
]
metadata = {
    "model": "openai/gpt-4-turbo-preview",
    "cost": "0.0108700000",
    "timestamp": "2024-02-07_09-00-03",
    "log_version": 0.1
}
def main():
    with open("README.md", "r") as f:
        content = f.read()
        print(content)
    print("CONTINUE")
if __name__ == "__main__":
    main()