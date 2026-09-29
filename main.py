import mellea

m = mellea.start_session()

def create_study_plan(topics):
    prompt =f"""
        Create study plan for the given topics: (topics)
        
        For each topic, make sure you explain why it is important and give examples that can be easily understood by a student. 
    """
    response = m.instruct(prompt)
    return str(response)


def main():
    topics = [
        "Python functions",
        "Git and GitHub",
        "Machine learning",
        "Linear regression",
        "Neural networks",
    ]

    print("MY STUDY TOPICS")
    print("-" * 40)

    for i, topic in enumerate(topics, 1):
        print(f"{i}. {topic}")

    print("\nAI STUDY PLAN")
    print("-" * 40)

    result = create_study_plan(topics)
    print(result)


if __name__ == "__main__":
    main()
