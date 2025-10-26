'''
GOAL: Process multiple images in parallel using Ray Tasks
'''
import numpy as np
import ray
import time
# Starts Ray and uses all available CPU cores
ray.init()

@ray.remote
def process_image(image: np.ndarray) -> np.ndarray:
    """Inverts the image colors and takes 1 second."""
    time.sleep(1)
    return 255 - image

# Input: A list of 8 small, random images.
# Here, (0, 255, (10, 10, 3)) means images of size 10x10 with 3 color channels (RGB), pixel values ranging from 0 to 255.
images = [np.random.randint(0, 255, (10, 10, 3)) for _ in range(8)]

# Action: Process them in parallel.
start_time = time.time()

# --- The Changed Section ---
# This call --> (process_image.remote(img)) is non-blocking, meaning it promises to return immediately in future (ObjectRef)
# ObjectRef is a placeholder for the actual result that will be computed in the background.
# ray.get() needs to be used to retrieve the actual results once they are ready.
# --------------------------------------------------------------
results = ray.get([process_image.remote(img) for img in images])
# --------------------------------------------------------------

end_time = time.time()
print(f"Processed {len(results)} images in {end_time - start_time:.2f} seconds.")

# Shutdown Ray when done
ray.shutdown()  