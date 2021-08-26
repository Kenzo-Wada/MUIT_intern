def get_lives_by_premium(lives, premium):
    premium_live = []
    for live in lives:
        if live.premium == premium:
            premium_live.append(live)
    return premium_live