def calculateStats(numbers):
    stats = {k: float("nan") for k in ["avg", "min", "max"]}
    if len(numbers):
        stats["avg"] = sum(numbers) / len(numbers)
        stats["max"] = max(numbers)
        stats["min"] = min(numbers)
    return stats
