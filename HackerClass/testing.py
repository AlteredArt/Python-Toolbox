# Each match is represented by a string in the format "x:y", where x is our team's score and y is our opponents score.
# For example: ["3:1", "2:2", "0:1", ...]
# Points are awarded for each match as follows:

    # if x > y: 3 points (win)
    # if x < y: 0 points (loss)
    # if x = y: 1 point (tie)

# We need to write a function that takes this collection and returns the number of points our team (x) got in the championship by the rules given above.

# Notes:

    # our team always plays 10 matches in the championship
    # 0 <= x <= 4
    # 0 <= y <= 4
# def points(games):
#     points = 0
    
#     for score in games:
#         print(score)
#         if games[0][0] > games[0][2]:
#             points += 3
#         elif games[0][0] == games[0][2]:
#             points += 1
#         elif games[0][0] < games[0][2]:
#             continue
#     print(points)

# points(['1:0','2:0','3:0','4:0','2:1','1:3','1:4','2:3','2:4','3:4'])


def remove_char(s):
    print(s.split())
    split = s.split()
    print(split[0][0])
    
    for letter in split:
        print(letter)

remove_char('sowhat')