# ray-e2e-pipeline
[![Python >=3.12](https://img.shields.io/badge/python-%3E%3D3.12-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Ray](https://img.shields.io/badge/ray-%E2%9A%A1-blueviolet)](https://www.ray.io/)
[![issues](https://img.shields.io/badge/issues-open%20one!-orange)](https://github.com/amugoodbad229/ray-e2e-pipeline/issues)
>A cheerful, hands-on guide to scale Python apps with Ray — from single-thread scripts to distributed multi-node pipelines. ⚡️🐍


> [!Important]
> Start here — Planning board: [Open the tldraw board](https://www.tldraw.com/f/T6oHe2VW4S5P4fRhE0Aqv?d=v2922.-359.12368.5875.iKOg-CiMHSQvCW_rsxAyU)

Why you'll like this
- Practical, incremental examples you can run immediately.
- No manual dependency installs — uv handles environment & tooling.
- Modern patterns: Ray tasks, actors, object store, placement & multi-node basics.
- Targets Python >= 3.12 (tested locally with 3.12).

Quickstart — clone and run (Windows / macOS / Linux)
1. Clone:
```bash
git clone https://github.com/amugoodbad229/ray-e2e-pipeline.git
cd ray-e2e-pipeline
```
2. Sync with uv (cross-platform, no manual installs):
```bash
uv sync
```
3. Run examples with your Python 3.12 interpreter:
```bash
python examples/01_single_thread.py
python examples/02_ray_tasks.py
python examples/03_ray_actors.py
```
(Windows tip: run the same commands from PowerShell or cmd; uv will handle the setup.)

Tiny example — Ray task
```python
import ray

ray.init()  # local by default

@ray.remote
def slow_square(x):
    import time; time.sleep(1)
    return x * x

futures = [slow_square.remote(i) for i in range(8)]
print(ray.get(futures))
```

Quick visual reference
```text
[your app] --> [refactor hot func -> Ray task] --> [use actors for state] --> [object store -> multi-node]
```

Tips (short & useful)
- Start by moving one hot function to a Ray task.
- Use actors when you need stateful workers.
- Tag resources (cpus/gpus) for predictable placement.
- Measure end-to-end latency, not just CPU time.

Report issues
- Found something off or want a feature? Please open an issue and I’ll look into it.

Thanks for checking out ray-e2e-pipeline — small steps, real code, big speedups. 🚀
