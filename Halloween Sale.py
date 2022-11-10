def howManyGames(p, d, m, s):
    # Return the number of games you can buy
    games = []
    g_sum = p
    while sum(games)<=s:
        if g_sum>m:
            games.append(g_sum)
            g_sum-=d
        if g_sum<=m:
            games.append(m)
    print(len(games)-1)
         
    
first_multiple_input = input().rstrip().split()
p = int(first_multiple_input[0])
d = int(first_multiple_input[1])
m = int(first_multiple_input[2])
s = int(first_multiple_input[3])
answer = howManyGames(p, d, m, s)