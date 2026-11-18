
import gc
import tracemalloc

# Start memory tracking
tracemalloc.start()

# Disable automatic garbage collection
gc.disable()

# Display garbage collection thresholds
print("Garbage collection thresholds:", gc.get_threshold())

# Create objects with circular references
objects = []

for i in range(10000):
    a = []
    b = []
    a.append(b)
    b.append(a)
    objects.append(a)

# Display memory before deleting objects
current, peak = tracemalloc.get_traced_memory()
print("\nMemory before deletion:", current, "bytes")

# Delete objects
del objects

# Display memory before manual garbage collection
current, peak = tracemalloc.get_traced_memory()
print("Memory before garbage collection:", current, "bytes")

# Perform manual garbage collection
collected = gc.collect()

# Display memory after garbage collection
current, peak = tracemalloc.get_traced_memory()
print("Memory after garbage collection:", current, "bytes")

print("\nGarbage objects collected:", collected)

# Enable automatic garbage collection
gc.enable()

# Stop memory tracking
tracemalloc.stop()

print("\nManual garbage collection completed successfully!")
