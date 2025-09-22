#!/usr/bin/env python3
"""Setup script for Tianshou package."""

from setuptools import setup, find_packages
import os

# Read the README file for long description
def read_readme():
    """Read the README file for long description."""
    readme_path = os.path.join(os.path.dirname(__file__), "README.md")
    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as f:
            return f.read()
    return "A Library for Deep Reinforcement Learning"

# Read version from __init__.py
def get_version():
    """Get version from tianshou/__init__.py."""
    # Try multiple possible locations for the __init__.py file
    possible_paths = [
        os.path.join(os.path.dirname(__file__), "tianshou", "__init__.py"),
        os.path.join(os.path.dirname(__file__), "__init__.py"),
        os.path.join(os.path.dirname(__file__), "..", "tianshou", "__init__.py"),
    ]
    
    for init_path in possible_paths:
        if os.path.exists(init_path):
            try:
                with open(init_path, "r", encoding="utf-8") as f:
                    for line in f:
                        if line.startswith("__version__"):
                            return line.split('"')[1]
            except (FileNotFoundError, IndexError):
                continue
    
    # Fallback version if __init__.py is not found
    return "1.2.0-dev"

# Core dependencies
install_requires = [
    "deepdiff>=7.0.1,<8.0.0",
    "gymnasium>=0.28.0,<0.29.0",
    "h5py>=3.9.0,<4.0.0",
    "matplotlib>=3.0.0",
    "numba>=0.60.0",
    "numpy>=1,<2",
    "overrides>=7.4.0,<8.0.0",
    "packaging",
    "pandas>=2.0.0",
    "pettingzoo>=1.22,<2.0",
    "sensai-utils>=1.2.1,<2.0.0",
    "tensorboard>=2.5.0,<3.0.0",
    "torch>=2.0.0,<3.0.0,!=2.0.1,!=2.1.0",
    "tqdm",
    "virtualenv>=20.4.3,<21.0.0,!=20.4.5,!=20.4.6; sys_platform != 'win32'",
    "virtualenv<20.16.4; sys_platform == 'win32'",
]

# Optional dependencies (extras)
extras_require = {
    "argparse": [
        "docstring-parser>=0.15,<0.16",
        "jsonargparse>=4.24.1,<5.0.0",
    ],
    "atari": [
        "ale-py>=0.8.1,<0.9.0",
        "autorom[accept-rom-license]>=0.4.2,<0.5.0",
        "opencv_python",
        "shimmy>=0.1.0,<1.0",
    ],
    "box2d": [
        "box2d_py==2.3.5",
        "pygame>=2.1.3",
        "swig==4.*",
    ],
    "classic-control": [
        "pygame>=2.1.3",
    ],
    "envpool": [
        "envpool>=0.8.2,<0.9.0; sys_platform != 'darwin'",
    ],
    "eval": [
        "docstring-parser>=0.15,<0.16",
        "joblib",
        "jsonargparse>=4.24.1,<5.0.0",
        "rliable==1.2.0",
        "scipy",
    ],
    "mujoco": [
        "imageio>=2.14.1",
        "mujoco>=2.1.5,<3",
    ],
    "mujoco-py": [
        "cython>=0.27.2",
        "mujoco-py>=2.1,<2.2",
    ],
    "pybullet": [
        "pybullet",
    ],
    "robotics": [
        "gymnasium-robotics",
    ],
    "vizdoom": [
        "vizdoom",
    ],
}

# All extras combined
extras_require["all"] = [
    dep for deps in extras_require.values() for dep in deps
]

setup(
    name="tianshou",
    version=get_version(),
    author="TSAIL",
    author_email="trinkle23897@gmail.com",
    description="A Library for Deep Reinforcement Learning",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/thu-ml/tianshou",
    project_urls={
        "Homepage": "https://github.com/thu-ml/tianshou",
        "Documentation": "https://tianshou.readthedocs.io",
        "Bug Reports": "https://github.com/thu-ml/tianshou/issues",
        "Source": "https://github.com/thu-ml/tianshou",
    },
    packages=find_packages(),
    package_data={
        "tianshou": ["py.typed"],
    },
    python_requires=">=3.11,<4.0",
    install_requires=install_requires,
    extras_require=extras_require,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="reinforcement learning, deep learning, pytorch, gymnasium, rl",
    license="MIT",
    zip_safe=False,
    include_package_data=True,
)
