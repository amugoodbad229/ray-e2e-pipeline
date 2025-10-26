'''
GOAL: Process a collection of images sequentially without Ray
'''

import numpy as np
from time import time, sleep

# A dummy function that simulates a slow image filter.
def process_image(image: np.ndarray) -> np.ndarray:
    """Inverts the image colors and takes 1 second."""
    sleep(1)
    return 255 - image

# Input: A list of 8 small, random images.
images = [np.random.randint(0, 255, (10, 10, 3)) for _ in range(8)]

# Action: Process them sequentially.
start_time = time()

# ----------------------------------------------
results = [process_image(img) for img in images]
# ----------------------------------------------

end_time = time()
print(f"Processed {len(results)} images in {end_time - start_time:.2f} seconds.")