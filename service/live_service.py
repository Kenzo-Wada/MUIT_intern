def get_lives_by_premium(lives, premium):
    premium_live = []
    for live in lives:
        if live.premium == premium:
            premium_live.append(live)
    return premium_live

def get_live_by_liveId(liveId, lives):
    for live in lives:
        if live.id == liveId:
            return live

def get_live_by_ticket(ticket, lives):
    for live in lives:
        print(live)
        if live.id == ticket.liveId:
            return live