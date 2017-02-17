import sqlite3


#con = sqlite3.connect("hltv.db")
connector = sqlite3.connect("mm.db")
cursor = connector.cursor()

ast = [8394, 7592, 4954, 7398, 7412]

dig = [1485, 2469, 7156, 9032, 9078]

sk = [557, 2023, 8564, 9216, 9217]

nip = [29, 29, 884, 7148, 7527]

mouse = [2730, 7499, 3741, 3997, 7511]

opt = [7805, 8370, 8520, 8507, 8523]

vp = [5386, 317, 161, 2553, 165]

faze = [8095, 695, 8183, 4959, 429]

c9 = [203, 7440, 8349, 8735, 8797]

imo = [7382, 8565, 8566, 8568, 9219]

env = [147, 7167, 7168, 7322, 7429]
#cobblestone,train,overpass
#ast cob 0.2 tr 0.68 over 0.61 win
#nip cob 0.7 tr 0.6 over 0.63

#dust2,mirage,overpass
#dig d2 0.57 mirge 0.5 overpass 0.6
#sk d2 0.81 mirage 0.75 overpass 0.77 win

#train,cache,dust2
#mouse tr 0.39 cac 0.63 d2 0.54
#opt tr 0.57 cah 0.8 d2 0.61 win

#nuke,overpass,cache
#vp nuke 0.61 op 0.36 cach 0.44
#faze nuke 0.6 op 0.66 cache 0.53 win
def opening_stats(p_id):
    cursor.execute("select * from opening_stats_3 where player_id =" + str(p_id))
    test = cursor.fetchall()

    for row in test:
#        print("")
        aa = 0
    return row

def frstkill_rate(p_id):
    rate = opening_stats(p_id)[1] * float(opening_stats(p_id)[4].replace('%', '')) *0.01 / opening_stats(p_id)[2]
    return rate

def overall_stats(p_id):
    cursor.execute("select * from overall_stats_3 where player_id =" + str(p_id))
    test = cursor.fetchall()

    for row in test:
#        print("")
        aa = 0
    return row

def round_stats(p_id):
    cursor.execute("select * from round_stats_3 where player_id=" + str(p_id))
    test = cursor.fetchall()

    for row in test:
#        print("")
        aa = 0
    return row

def kill_rate(p_id):
    kill = float(overall_stats(p_id)[1]) / round_stats(p_id)[1]
    return kill

def survival_rate(p_id):
    survival = (round_stats(p_id)[1] - overall_stats(p_id)[2])  / float(round_stats(p_id)[1])
    return survival

def mkill_rate(p_id):
    mkill = (float(round_stats(p_id)[3]) + 4 * round_stats(p_id)[4] + 9 * round_stats(p_id)[5] + 16 * round_stats(p_id)[6] + 25 * round_stats(p_id)[7]) / round_stats(p_id)[1]
    return mkill

def clu_rate(p_id):
    return clu

def rate(team_id):
    i = -1
    totall = 0
    for num in team_id:
        i += 1
        rate = (mkill_rate(num) + kill_rate(num) + 0.7 * survival_rate(num) + 0.8 * frstkill_rate(num)) / 3.5
        totall += rate
    team = totall / 5
    IGL = team * 0.1
    return team + IGL

map1 = rate(c9) * 0.58 + rate(faze) * 0.61
#map2 = rate(ast) * 0.70 + rate(opt) * 0.59
#map3 = rate(ast) * 0.44 + rate(opt) * 0.40

gou = rate(ast) + rate(opt)

print("s")
print(rate(c9) / gou)
print(rate(faze) / gou)

print("map1")
print("c9")
print (rate(c9) * 0.58  / map1)
print("faze")
print (rate(faze) * 0.61  / map1)

#print("map2")
#print(rate(ast) * 0.70 / map2)
#print(rate(opt) * 0.59 / map2)

#print("map3")
#print(rate(ast) * 0.44 / map3)
#print(rate(opt) * 0.40 / map3)


#op train dust2
#ast train 0.70 op 0.6 d2 0.53
#sk train 0.9 op 0.76 desut2 0.76


#print(mkill_rate(sk[0]))
#print(survival_rate(sk[0]))
#print(kill_rate(sk[0]))
#print(round_stats(sk[0]))
#print(frstkill_rate(sk[0]))
#print(overall_stats(sk[0]))
#print(opening_stats(sk[0]))
#print(openig(sk[0]))
