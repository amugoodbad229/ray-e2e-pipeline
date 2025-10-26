'''
GOAL: Count total number of pixels processed across multiple images using Ray Actors
'''
import ray
from ray.actor import ActorProxy  # Added for type hinting
import numpy as np
import time

ray.init()

@ray.remote
class PixelCounter:
    def __init__(self):
    # This is the actor's private, internal state. self.total_pixels = 0
        self.total_pixels = 0

    def add(self, num_pixels: int):
    # This method will update the actor's state.
        self.total_pixels += num_pixels

    # Method to get the current total.
    def get_total(self) -> int:
        return self.total_pixels

@ray.remote
def process_image_with_actor(image: np.ndarray, counter: ActorProxy[PixelCounter]):
    
    # Call the actor's .add() method remotely.
    counter.add.remote(image.size)
    time.sleep(1)

# 2. Create a single instance of the Actor.
images = [np.random.randint(0, 255, (10, 10, 3)) for _ in range(8)]
image_size = images[0].size

# 3. Create a single instance of the Actor.
counter = PixelCounter.remote()

#   4. Launch tasks, passing the same actor handle to each one.
ray.get([process_image_with_actor.remote(img, counter) for img in images])

# 5. Check the final state of the actor.
expected_total = image_size * len(images)
final_total = ray.get(counter.get_total.remote())

print(f"Expected total pixels: {expected_total}")
print(f"Actual total from actor: {final_total}")

# assert keyword is used to verify that the expected and actual totals match.
# not using assert would not raise an error if the values differ.
# This is a simple way to do a sanity check in code.
assert final_total == expected_total

time.sleep(120)
ray.shutdown()