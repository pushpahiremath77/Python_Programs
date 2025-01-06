def wash_hands(N, nM):
    total_seconds = N * 21 * 30 * nM
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    return f"{minutes} minutes and {seconds} seconds"

print(wash_hands(8, 7))
