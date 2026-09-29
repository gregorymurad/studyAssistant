import mellea


def create_study_plan(topics):
    """
    Use AI to create a study plan for a list of topics.
    """
    if not topics:
        raise ValueError("At least one study topic is required.")

    topic_list = "\n".join(
        f"{number}. {topic}" for number, topic in enumerate(topics, 1)
    )
    prompt = f"""Create a clear, structured study plan for these topics:

{topic_list}

Include every listed topic exactly once. For each topic, provide a concise
description of what to study and one practical activity. Keep the topics in
the order shown and return only the study plan.
"""

    session = mellea.start_session()
    result = session.instruct(prompt)
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
