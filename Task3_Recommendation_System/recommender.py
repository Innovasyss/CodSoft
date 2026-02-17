import math
from data import ratings


def cosine_similarity(user1, user2):
    """
    Compute cosine similarity between two users.
    """

    common_items = set(ratings[user1]).intersection(ratings[user2])

    if not common_items:
        return 0  

    numerator = sum(ratings[user1][item] * ratings[user2][item] for item in common_items)

    sum1 = sum(r**2 for r in ratings[user1].values())
    sum2 = sum(r**2 for r in ratings[user2].values())

    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if denominator == 0:
        return 0

    return numerator / denominator


def recommend_items(target_user):
    """
    Recommend items using weighted collaborative filtering.
    Calculates a predicted score for unrated items based on similar users' ratings.
    """
    totals = {}
    sim_sums = {}

    for other_user in ratings:
        if other_user == target_user:
            continue

        sim = cosine_similarity(target_user, other_user)

        if sim <= 0:
            continue

        for item, rating in ratings[other_user].items():
          
            if item not in ratings[target_user]:
                totals.setdefault(item, 0)
                totals[item] += sim * rating
                
                sim_sums.setdefault(item, 0)
                sim_sums[item] += sim

    rankings = [(total / sim_sums[item], item) for item, total in totals.items() if sim_sums[item] > 0]
    rankings.sort(reverse=True)

    return [item for score, item in rankings]
