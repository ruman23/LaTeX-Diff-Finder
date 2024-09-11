**Automated LaTeX Diff Finder for Comparing and Highlighting Differences in Tex Files**

---

### Description:
This project is a Python-based tool that automates the comparison of two LaTeX (`.tex`) files by finding differences between them. Using `latexdiff`, the tool highlights changes made in the newer version of a document compared to an older one. It generates a diff that shows added content and marks the deleted content, which is subsequently removed for clearer visualization of changes.

### Features:
- Automatically generates a diff between two LaTeX files using `latexdiff`.
- Highlights added content (`\\DIFadd`) and removes deleted content (`\\DIFdel`).
- Processes multiple `.tex` files in bulk, comparing files with the same name in two different directories.
- Saves the diff results in a specified directory, showing only the changes made in the new version.

---

### Installation:

#### Prerequisites:
1. **Python 3.x**: Ensure that Python 3.x is installed on your system.
2. **`latexdiff`**: Install `latexdiff` for generating diffs between LaTeX files. It can be installed via a TeX distribution like TeX Live or MikTeX:
    - For TeX Live: `sudo apt-get install latexdiff` (Linux) or `brew install latexdiff` (macOS with Homebrew).

#### Clone the repository:
```bash
git clone <repository-url>
cd latex-diff-finder
```


# LaTeX Diff Script

This script compares `.tex` files from two directories and generates a diff highlighting the changes.

## Running the Script

1. **Prepare Directories:**
   - Place the old versions of your `.tex` files in a directory named `old/`.
   - Place the new versions of your `.tex` files in a directory named `new/`.
   - Create a directory for storing the diff output files, e.g., `diff/`.

2. **Run the Script:**
   ```bash
   python script.py

