# market_queue.py - Simulate market price updates with M/M/1 queue
# For King Bran Stark, counseled by Tyrion, Hand of the King, April 10, 2025

import numpy as np
import pandas as pd

# Parameters (adjustable, Your Grace!)
lambda_rate = 100  # Arrival rate: 100 price updates/hour
mu_rate = 120      # Service rate: 120 updates processed/hour
sim_time = 24      # Simulate 24 hours

# Queueing metrics
rho = lambda_rate / mu_rate  # Utilization
if rho >= 1:
    print("Warning: Market unstable—too many updates, too slow processing!")
    exit()

Lq = lambda_rate**2 / (mu_rate * (mu_rate - lambda_rate))  # Avg queue length
Wq = lambda_rate / (mu_rate * (mu_rate - lambda_rate))      # Avg wait time (hours)
Ws = 1 / (mu_rate - lambda_rate)                            # Avg time in system

print(f"Market Utilization: {rho:.2%}")
print(f"Avg Queue Length: {Lq:.2f} updates")
print(f"Avg Wait Time in Queue: {Wq*60:.2f} minutes")
print(f"Avg Time in System: {Ws*60:.2f} minutes")

# Simulate arrivals and service times
np.random.seed(42)  # For consistency, Your Grace
arrivals = np.random.exponential(1/lambda_rate, int(lambda_rate * sim_time))
service_times = np.random.exponential(1/mu_rate, int(lambda_rate * sim_time))

# Calculate event times
arrival_times = np.cumsum(arrivals)
service_starts = [arrival_times[0]]
service_ends = [service_starts[0] + service_times[0]]

for i in range(1, len(arrival_times)):
    service_starts.append(max(arrival_times[i], service_ends[-1]))
    service_ends.append(service_starts[-1] + service_times[i])

# Build DataFrame
df = pd.DataFrame({
    "Arrival": arrival_times,
    "Service Start": service_starts,
    "Service End": service_ends,
    "Wait Time": np.array(service_starts) - arrival_times
})
df.to_excel("docs/market_queue.xlsx", index=False)

print(f"Simulation complete! See SevenVoices/docs/market_queue.xlsx, Your Grace!")