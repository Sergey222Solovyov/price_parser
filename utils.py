import time

needless_catalogs = "Скидки, Сейчас актуально, Зоотовары"


def time_track(func):
    def surrogate(*args, **kwargs):
        started_at = time.time()

        result = func(*args, **kwargs)

        ended_at = time.time()
        elapsed = round(ended_at - started_at, 4)
        print(f'The function worked for {elapsed / 60} min')
        return result

    return surrogate
