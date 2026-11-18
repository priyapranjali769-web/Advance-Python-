
import threading
import time

# Function to count numbers
def count_numbers():
    for i in range(1, 6):
        print("Counting:", i)
        time.sleep(1)

# Function to calculate squares
def calculate_square():
    for i in range(1, 6):
        print("Square of", i, "=", i * i)
        time.sleep(1)

# Function to calculate cubes
def calculate_cube():
    for i in range(1, 6):
        print("Cube of", i, "=", i * i * i)
        time.sleep(1)

# Create threads
t1 = threading.Thread(target=count_numbers)
t2 = threading.Thread(target=calculate_square)
t3 = threading.Thread(target=calculate_cube)

# Start threads
t1.start()
t2.start()
t3.start()

# Wait for all threads to complete
t1.join()
t2.join()
t3.join()

print("All tasks completed successfully!")
