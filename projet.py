def tester_pourcentage_superieur_50(us_a, us_b, us_c, us_d):
    us_sup_50 = [] 

    if us_a >= 50:
        us_sup_50.append("US A")
    if us_b >= 50:
        us_sup_50.append("US B")
    if us_c >= 50:
        us_sup_50.append("US C")
    if us_d >= 50:
        us_sup_50.append("US D")

    return us_sup_50