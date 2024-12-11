# Text Data Noise Generator and Cleaner

A toolkit for generating and cleaning data quality issues in text, designed for educational and testing purposes.

## Project Overview

This project provides tools to:
1. Generate realistic data quality issues in clean text
2. Clean noisy text data using prompt engineering
3. Test and validate data cleaning approaches

## Components

### 1. Noise Generator (`noise_generator.py`)
Introduces controlled noise into clean text data:
- Unicode corruption and invisible characters
- Random string injection
- Word duplication patterns
- HTML/XML artifacts
- Control characters and encoding issues
- Whitespace corruption

### 2. Cleaning Prompt (`cleaning_prompt.txt`)
Prompt for Large Language Models to clean noisy text:
- Detailed cleaning instructions
- Two-shot examples
- Specific noise type handling

## Requirements

```bash
Python 3.7+
```

## Installation

```bash
git clone https://github.com/yourusername/text-data-noise-toolkit.git
cd text-data-noise-toolkit
pip install -r requirements.txt
```

## Usage

### Adding Noise to Clean Data

```python
from noise_generator import add_noise_to_text

add_noise_to_text(
    text_file='clean_data.txt',
    output_file='noisy_data.txt',
    noise_probability=0.3
)
```

### Cleaning Noisy Data
1. Copy the cleaning prompt from `cleaning_prompt.txt`
2. Use it with your preferred LLM
3. Input your noisy text for cleaning

## Example

Input (Clean):
```
The quick brown fox jumps over the lazy dog.
```

With Noise:
```
The quick⁠ brown\u200B fox‎ jumps jumps jumps jumps over the lazy dog &nbsp; #R$T2k9pL@
```

Cleaned:
```
The quick brown fox jumps over the lazy dog
```

## Configuration

Adjust noise parameters in `noise_generator.py`:
```python
noise_probability = 0.3  # 30% chance of noise per line
noise_functions = [add_unicode_noise, add_random_string]  # Select noise types
```
