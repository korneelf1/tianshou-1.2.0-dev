# Tianshou

**Tianshou** ([天授](https://baike.baidu.com/item/%E5%A4%A9%E6%8E%88)) is a reinforcement learning (RL) library based on pure PyTorch and [Gymnasium](http://github.com/Farama-Foundation/Gymnasium).

## Installation

You can install this package in development mode using:

```bash
pip install -e .
```

Or install with specific extras:

```bash
pip install -e .[mujoco,atari]
```

## Features

- Modular low-level interfaces for algorithm developers
- Convenient high-level interfaces for applications
- Support for online and offline RL
- Multi-agent RL support
- Model-based RL support

## Quick Start

```python
import tianshou as ts
print(ts.__version__)
```

For more information, visit the [official documentation](https://tianshou.readthedocs.io).
