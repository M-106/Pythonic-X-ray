# Pythonic-X-ray
Python code analyzer



### Installation

Just make a conda env with matplotlib:
```bash
conda create -n xray python pip -y
conda activate xray
pip install matplotlib
```
([See here for help with anaconda](https://github.com/xXAI-botXx/Project-Helper#anaconda))

Now clone this repo and run it (see next chapter).

<br><br>

### How to Run

You can run the analyzer script from the command line. It supports analyzing both Python files and folders containing Python files.

```bash
python analyze.py [OPTIONS]
```

Or use add it as submodule/clone it and call the code in your code: 
<br>
There are two options:

1. **Clone the repository** and import it:
    ```bash
    git clone https://github.com/yourusername/code-analyzer.git
    ```
    Then in your Python script:
    ```python
    import os
    import code_analyzer as ca

    # Analyze a single file
    ca.analyse_code("path/to/file.py", name="My Project", should_print=True, should_save=True, save_path="./")

    # Or analyze a folder
    folder_path = "../my_project"
    for root, dirs, files in os.walk(folder_path):
        for f in files:
            if f.endswith(".py"):
                ca.analyse_code(os.path.join(root, f), name="My Project", should_print=True, should_save=True, save_path="./")
    ```

2. **Add it as a submodule** in your own project (if using git):
    ```bash
    git submodule add https://github.com/yourusername/code-analyzer.git submodules/code_analyzer
    ```
    Then import it the same way in your code:
    ```python
    from submodules import code_analyzer as ca
    ```
    This allows you to directly call `analyse_code` on files or folders from within your scripts, without running the CLI.


<br><br>

### Parameters / Options

| Option        | Type | Default                | Description                                                         |
| ------------- | ---- | ---------------------- | ------------------------------------------------------------------- |
| `--path`      | str  | `.`                    | Path to a Python file or folder containing Python files to analyze. |
| `--name`      | str  | `"My Awesome Project"` | Name of your project (used in saved results).                       |
| `--verbose`   | flag | `True`                 | If included, prints the analysis results in the console.            |
| `--save`      | flag | `True`                 | If included, saves the analysis results to a file.                  |
| `--save_path` | str  | `"./"`                 | Folder path where analysis results will be saved.                   |

<br><br>

### Examples

1. **Analyze current folder, print results, but don’t save**:

```bash
python analyze.py --verbose
```

2. **Analyze a specific folder and save results**:

```bash
python analyze.py --path ./example_python_project --save --save_path ./results
```

3. **Analyze a single Python file with a custom project name**:

```bash
python analyze.py --path ./example_python_project/examples/pytorch/tsmixer.py --name "TSMixer" --verbose --save
```




