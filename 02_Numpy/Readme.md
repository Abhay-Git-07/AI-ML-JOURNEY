# NumPy & Matplotlib Learning

This folder contains my learning and practice notebooks focused on **NumPy** and **Matplotlib**, organized into different phases.

The goal of this section is to build a strong foundation in numerical computing, array manipulation, and data visualization using Python.

## 📁 Contents

| File | Description |
|------|-------------|
| `Phase_01.ipynb` | NumPy fundamentals and basic operations |
| `Phase_02.ipynb` | NumPy concepts and array operations |
| `Phase_03.ipynb` | NumPy practice and visualization with Matplotlib |
| `Phase_04.ipynb` | Advanced NumPy practice and applications |

## 🛠️ Technologies & Libraries

- **Python** — Programming language
- **NumPy** — Numerical computing and array operations
- **Matplotlib** — Data visualization and plotting
- **Jupyter Notebook** — Running and documenting the notebooks

## ⚙️ Setup

The virtual environment (`.venv`) is **not included** in this repository.

After cloning the repository, navigate to the project directory:

```powershell
cd "AIML Journey"
```

Create a virtual environment:

```powershell
python -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\Activate.ps1
```

Install the required packages:

```powershell
pip install numpy matplotlib notebook
```

## ▶️ Run the Notebooks

Start Jupyter Notebook:

```powershell
jupyter notebook
```

Then navigate to:

```text
02_Numpy/
```

and open any of the `Phase_*.ipynb` files.

## 📌 Libraries Used

The main libraries used in these notebooks are:

```python
import numpy as np
import matplotlib.pyplot as plt
```

- NumPy is used for numerical operations, arrays, mathematical computations, and data manipulation.

- Matplotlib is used for creating visualizations and displaying graphical representations of data.


## 🧪 Example

### Loading a NumPy array stored in a .npy file:

```python
import numpy as np

logo = np.load("numpy_logo.npy")
```

### Displaying the array as an image:

```python
import matplotlib.pyplot as plt

plt.imshow(logo)
plt.axis("off")
plt.show()
```

### Creating an inverted version:

```python
dark_logo = 1 - logo

plt.imshow(dark_logo)
plt.axis("off")
plt.show()
```

This demonstrates how NumPy arrays can be manipulated mathematically and visualized using Matplotlib.

## 📚 Learning Progress
 - NumPy Fundamentals
 - NumPy Array Operations
 - NumPy Mathematical Operations
 - NumPy Practice
 - Matplotlib Basics
 - Working with Image Arrays
 - .npy File Handling
 - Array Manipulation & Visualization
 - Phase 1
 - Phase 2
 - Phase 3
 - Phase 4

## 📝 Note

- The .venv directory is intentionally excluded from this repository.

- Virtual environments are machine-specific, so anyone cloning this project should create their own environment and install the required dependencies locally.

## 🚀 AIML Journey

This NumPy section is part of my AIML Journey, where I am building my skills step-by-step in Python, data analysis, and machine learning.

NumPy — Completed ✅
