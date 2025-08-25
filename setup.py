#!/usr/bin/env python3
"""
Setup para el Sistema Experto CLIPS
===================================

Configuración del paquete Python para el sistema experto
de finanzas personales basado en CLIPS.
"""

from setuptools import setup, find_packages
import os

# Leer el README
def read_readme():
    readme_path = os.path.join(os.path.dirname(__file__), 'docs', 'README.md')
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            return f.read()
    return "Sistema Experto CLIPS para Finanzas Personales"

setup(
    name="sistema-experto-clips",
    version="2.0.0",
    author="Sistema Experto CLIPS Team",
    author_email="",
    description="Sistema experto para finanzas personales usando CLIPS",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Intended Audience :: Financial and Insurance Industry",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Office/Business :: Financial",
    ],
    python_requires=">=3.8",
    install_requires=[
        "clips>=1.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0.0",
            "black>=21.0.0",
            "flake8>=3.8.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "sistema-experto-gui=src.gui.main_window:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
