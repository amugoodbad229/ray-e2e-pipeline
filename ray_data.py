'''
GOAL: Process a large collection of images stored in S3 using Ray Data
'''
import ray
import numpy as np

# We connect to our running Ray cluster.
# Address='auto' connects to an existing cluster.
# Without address='auto', it will start a new local cluster.
# So it is a good practice to always use address='auto' in production code.
ray.init(address='auto')

# Our original remote function from ray_task.py, slightly adapted to
# handle the dictionary format that Ray Data uses for rows.

# Difference: We now return both the processed image and the original row's ID.
@ray.remote
def process_image(row: dict) -> dict:
    image = row['image']
    inverted_image = 255 - image
    return {'processed_image': inverted_image, 'original_id': row.get('id', None)}

# Now, we set up the full data pipeline in three steps:

# 1. Create a lazy reference to the massive dataset in S3.
print("Creating dataset reference...")
ds = ray.data.read_images("s3://your-bucket-name/raw-images/")

# 2. Define the distributed transformation.
print("Defining map transformation...")
processed_ds = ds.map(process_image)

# NOTE: We use ds.map() to apply the process_image function to each image in the dataset.
#       map() in ray data and map() in built-in function of Python are totally different.
#       map() of ray data uses DAG under the hood to optimize execution. 
#       ray's map() is connected to the previous ds object which holds the ray data.
# Info: DAG = Directed Acyclic Graph, a structure that Ray uses to manage tasks and their dependencies.

# 3. Trigger the computation by writing the results.
print("Executing pipeline and writing results...")
processed_ds.write_parquet("s3://your-bucket-name/processed-images/")

# Info: Parquet is a columnar storage file format optimized for use with big data processing frameworks.

print("Pipeline complete!")