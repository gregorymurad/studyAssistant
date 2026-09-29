import mellea
from mellea import start_session
from mellea.stdlib.sampling import RejectionSamplingStrategy

m = mellea.start_session()

def create_study_plan(topics):
    topic_list = "\n".join(f"- {topic}" for topic in topics)
    prompt = f"""
    Use AI to create a study plan for the following topics:
    {topic_list}
    - Include detailed sub topics that the user should learn to master the main topic
    - At most 5 bullets each
    """

    # TODO: Write your Mellea code here
    response = m.instruct(prompt)
    return response;

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
