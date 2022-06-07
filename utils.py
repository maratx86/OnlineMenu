def has_user_worker_status(user, workers):
    a = list(filter(lambda w: w.user == user, workers))
    return len(a) > 0


def has_user_edit_access(user, workers):
    a = list(filter(lambda w: w.user == user, workers))
    if len(a) == 0:
        return False
    return a[0].role in ('owner',)
