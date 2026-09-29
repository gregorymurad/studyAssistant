import mellea

def create_study_plan(m, topics):
    task = f"""
    Create a study plan for these topics: {topics}
    Ensure that it is concise.
    """

    return m.instruct(task)

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
    
    m = mellea.start_session()

    result = create_study_plan(m, topics)
    print(result)


if __name__ == "__main__":
    main()
