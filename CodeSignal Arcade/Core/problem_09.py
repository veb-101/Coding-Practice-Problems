# https: // app.codesignal.com/arcade/code-arcade/at-the-crossroads/m9wjpkCjgofg7gs8N/

'''
You are playing an RPG game. Currently your experience points (XP) total is
equal to experience. To reach the next level your XP should be at least at
threshold. If you kill the monster in front of you, you will gain more experience
points in the amount of the reward.

Given values experience, threshold and reward, check if you reach the next level
after killing the monster.

Example

For experience = 10, threshold = 15, and reward = 5, the output should be
reachNextLevel(experience, threshold, reward) = true;
For experience = 10, threshold = 15, and reward = 4, the output should be
reachNextLevel(experience, threshold, reward) = false.
'''


def reachNextLevel(experience, threshold, reward):
    return experience + reward >= threshold


experience = 10
threshold = 15
reward = 5
print(reachNextLevel(experience, threshold, reward))

experience = 10
threshold = 15
reward = 4
print(reachNextLevel(experience, threshold, reward))
