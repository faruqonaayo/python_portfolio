def calculate_xp(score, difficulty_multiplier, time_bonus):
    """
        This function calculates the experience points (XP) a player earns based on:
        their score, difficulty multiplier, and time bonus.
    """
    base_xp = score * difficulty_multiplier
    total_xp = base_xp + (time_bonus * base_xp / 100)
    return total_xp