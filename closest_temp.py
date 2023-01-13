import sys
from contextlib import redirect_stdout


def compute_closest_to_zero(ts):
    if not ts:
        return 0
    min_ts = 0
    for i, t in enumerate(ts):
        subs_value = abs(t - 0)
        if min_ts:
            if subs_value - abs(min_ts - 0) < 0:
                min_ts = t
            if subs_value - abs(min_ts - 0) == 0:
                min_ts = abs(t)
        else:
            min_ts = t
    return min_ts