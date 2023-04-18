"""
Task
Given the participants score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.
The first line contains . The second line contains an array  A[] of n integers each separated by a space.
"""

# En tête
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

# Réponse : (ici on modifie l'entête en rajoutant list()au map du début)
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    # On trie le tableau par ordre décroissant
    arr.sort(reverse=True)

    # On initialise le score du runner-up
    runner_up_score = None

    # On parcourt le tableau trié et on trouve le premier score différent du score maximum
    for score in arr:
        if score != arr[0]:
            runner_up_score = score
            break

    # On affiche le score du runner-up
    print(runner_up_score)
