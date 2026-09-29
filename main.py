import mellea
from mellea import start_session



m = start_session()

def create_study_plan(topics):
    
    prompt = f"""Create a study plan for the following topics:
      {topics}
    For each topic, please make sure:
        - it is concise;
        - explain waht the student should review;
        - organize the topics into a logic study order;

    """
    result = m.instruct(prompt)

    return str(result)


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
