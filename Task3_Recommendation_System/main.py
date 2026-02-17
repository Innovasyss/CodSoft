from data import ratings
from recommender import recommend_items, cosine_similarity


def main():
    print("Simple Movie Recommendation System")
    print("----------------------------------\n")

    print("Available Users:")
    for user in ratings:
        print("-", user)

    print()

    user_input = input("Enter user name from above list: ").strip()
    
    target_user = None
    for user in ratings:
        if user.lower() == user_input.lower():
            target_user = user
            break

    if not target_user:
        print("User not found.")
        return

    print("\nCalculating similarities...\n")

    for user in ratings:
        if user != target_user:
            sim = cosine_similarity(target_user, user)
            print(f"Similarity between {target_user} and {user}: {sim:.2f}")

    recommendations = recommend_items(target_user)

    print("\nRecommended Movies:")

    if recommendations:
        for movie in recommendations:
            print("-", movie)
    else:
        print("No new recommendations available.")


if __name__ == "__main__":
    main()
