# level calculator
#def level()


# condtition simulator
def conditition_simulator(lmd_want, exp_want, days):
    global text
    card_amount = round(exp_want / 1000)
    # first condition_simulator
    # lmd factory 2 exp factory 2 trading post 2
    lmd = []
    exp = []
    lmd_generate = 2*20000*days
    exp_generate = 2*7*days
    lmd.append(lmd_want - lmd_generate)
    exp.append(card_amount - exp_generate)
    # second condition
    # lmd factory 3 exp 0
    lmd_generate = 3*20000*days
    exp_generate = 0*7*days
    lmd.append(lmd_want - lmd_generate)
    exp.append(card_amount - exp_generate)
    # third condition
    # lmd factory 1 exp 4 lmd 1
    lmd_generate = 1*20000
    exp_generate = 4*7*days
    lmd.append(lmd_want - lmd_generate)
    exp.append(card_amount - exp_generate)

    lmd = [0 if b < 0 else b for b in lmd]
    exp = [0 if b < 0 else b for b in exp]
    S0 = []
    S1 = []
    for l in lmd:
        S0.append(round(l/7500))
    for e in exp:
        S1.append(round(e/7))
    c1 = S0[0]+S1[0]
    c2 = S0[1]+S1[1]
    c3 = S0[2] + S1[2]
    c = min(c1,c2,c3)
    condition = [c1,c2,c3].index(c)
    condition += 1

    if condition == 1: text = "lmd factory: 2 ,exp: 2 ,trading post: 2"
    elif condition == 2: text = "lmd factory: 3 ,exp: 0 ,trading post: 3"
    elif condition == 3: text = "lmd factory: 1 ,exp: 4: ,trading post: 1"

    print("best condition = c" + str(condition) + ' ' + text + " ,need total = " + str(c*30) + " sanity")
    print("farm CE5 = " + str(S0[condition-1]) + " times")
    print("farm LS5 = " + str(S1[condition-1]) +  " times")

