import os
import subprocess
import shutil
import re

def clean_latex_diff(diff_tex):
    """
    Cleans the LaTeX diff file by removing \DIFdel sections and inline \DIFdel{...} deletions.
    
    Args:
    diff_tex (str): Path to the diff file to be cleaned.
    """
    with open(diff_tex, 'r', encoding='utf-8') as file:
        content = file.read()

    # Remove block deletions (\DIFdelbegin to \DIFdelend)
    content = re.sub(r'\\DIFdelbegin.*?\\DIFdelend', '', content, flags=re.DOTALL)

    # Remove inline deletions (\DIFdel{...})
    content = re.sub(r'\\DIFdel\{.*?\}', '', content)

    # Save the cleaned content back to the file
    with open(diff_tex, 'w', encoding='utf-8') as file:
        file.write(content)

    print(f"Cleaned diff saved to {diff_tex}")


def generate_diff(old_tex, new_tex, diff_tex):
    """
    This function generates a LaTeX diff between two .tex files using latexdiff.
    The diff is saved with the original file name in the 'diff' folder, then cleaned.
    
    Args:
    old_tex (str): Path to the old .tex file.
    new_tex (str): Path to the new .tex file.
    diff_tex (str): Path to save the cleaned diff file.
    """
    try:
        # Step 1: Run latexdiff to generate the raw diff
        latexdiff_command = (
            f"latexdiff -s COLOR --disable-auto-mbox --exclude-textcmd='textit,footnote,section,subsection' "
            f"--graphics-markup=0 --math-markup=0 {old_tex} {new_tex} > {diff_tex}"
        )
        subprocess.run(latexdiff_command, shell=True, check=True)

        # Step 2: Clean the diff to remove \DIFdel sections
        clean_latex_diff(diff_tex)

    except subprocess.CalledProcessError as e:
        print(f"Error generating diff: {e}")


def process_tex_files(old_dir, new_dir, diff_dir):
    """
    Processes all .tex files in the 'old' and 'new' directories, generates diffs for matching files,
    and saves the results in the 'diff' directory.
    
    Args:
    old_dir (str): Path to the directory with the old .tex files.
    new_dir (str): Path to the directory with the new .tex files.
    diff_dir (str): Path to the directory where the diffs will be saved.
    """
    # Ensure the diff directory exists
    if not os.path.exists(diff_dir):
        os.makedirs(diff_dir)

    # Get a list of .tex files in both directories
    old_files = set(f for f in os.listdir(old_dir) if f.endswith('.tex'))
    new_files = set(f for f in os.listdir(new_dir) if f.endswith('.tex'))

    # Find common files between old and new directories
    common_files = old_files.intersection(new_files)

    for file in common_files:
        old_tex = os.path.join(old_dir, file)
        new_tex = os.path.join(new_dir, file)
        diff_tex = os.path.join(diff_dir, file)

        print(f"Processing file: {file}")

        # Generate the diff for the matching files
        generate_diff(old_tex, new_tex, diff_tex)

    print(f"All diffs saved to {diff_dir}")

# Example usage
old_dir = 'old'  # Folder containing old .tex files
new_dir = 'new'  # Folder containing new .tex files
diff_dir = 'diff'  # Folder where diffs will be saved

process_tex_files(old_dir, new_dir, diff_dir)
