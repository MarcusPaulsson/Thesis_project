import argparse
import os
def analyze_file(file_path):
    """
    Analyzes a file to determine:
    - Total lines
    - Lines that are only comments (ignoring whitespace)
    - Lines that are considered code (non-empty and not pure comments)
    
    Note: This simple analysis assumes a language where comments start with '#'
    (like Python). For other languages, adjust the logic accordingly.
    """
    total_lines = 0
    comment_lines = 0
    code_lines = 0
    
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            total_lines += 1
            stripped = line.strip()
            # Consider a line as a comment if it starts with '#' after stripping
            if stripped.startswith("#"):
                comment_lines += 1
            # Skip blank lines
            elif stripped == "":
                continue
            else:
                code_lines += 1
                
    return total_lines, comment_lines, code_lines

def main():
    # Define the file names. Ensure these files are in the same folder as this script.
    files = ["responses_expert.csv", "responses_student.csv"]

    grand_total = 0
    grand_comments = 0
    grand_code = 0

    for file_name in files:
        file_path = os.path.join(os.getcwd(), file_name)
        total, comments, code = analyze_file(file_path)
        grand_total += total
        grand_comments += comments
        grand_code += code

        print(f"File: {file_name}")
        print(f"  Total lines:    {total}")
        print(f"  Comment lines:  {comments}")
        print(f"  Code lines:     {code}")
        if total:
            print(f"  Comment ratio:  {comments / total:.2%}")
        print("-" * 30)



if __name__ == "__main__":
    main()



    