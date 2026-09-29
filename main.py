import mellea


def create_study_plan(topics):
    """
    Use AI to create a study plan for a list of topics.

    TODO:
    Please, work on implementing this function using Mellea.
    """

    # TODO: Write your Mellea code here
    m = mellea.start_session()
    reply = m.instruct("Create a study plan covering every topic listed below + \n".join(f" {topic}" for topic in topics))
    text = str(reply)
    return text


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
