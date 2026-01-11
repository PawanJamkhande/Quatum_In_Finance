import time

def evaluate(start_time, energy):
    runtime = time.time() - start_time
    return {
        "energy": energy,
        "runtime": runtime
    }
