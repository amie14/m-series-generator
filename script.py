def generate_simulated_series(seed=1558, length=200):
    import numpy as np

    series = [seed]
    rng = np.random.default_rng(seed=42)

    for i in range(1, length):
        wave = 3000 * np.sin(i / 7)
        noise = rng.integers(-1200, 1200)
        correction = -0.1 * (series[-1] - 5500)
        diff = wave + noise + correction
        next_val = int(series[-1] + diff)
        next_val = max(1000, min(9999, next_val))
        series.append(next_val)

    return series

# استخدام
if __name__ == "__main__":
    series = generate_simulated_series()
    for i, val in enumerate(series):
        print(f"M{str(i).zfill(6)},{val}")
