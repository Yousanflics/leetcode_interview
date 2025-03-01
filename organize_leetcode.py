import os
import re
import shutil
from collections import defaultdict

# Define the main folders
MAIN_FOLDERS = ["Easy", "Medium", "Hard", "Job"]

# Define company folders under Job
COMPANY_FOLDERS = ["TikTok", "Doordash", "Amazon", "Google", "Meta", "Microsoft"]

# Define data structure topics for difficulty folders
TOPIC_FOLDERS = {
    "Tree": ["94", "102", "103", "105", "144", "145", "637", "662", "993"],
    "LinkedList": ["2", "19", "23", "24", "25", "61", "138", "146", "148"],
    "Array": ["1", "11", "33", "34", "39", "40", "49", "56", "57", "74", "75", "78", "80", "128", "209", "215", "560", "735"],
    "String": ["3", "5", "12", "13", "14", "43", "71", "76", "139"],
    "DynamicProgramming": ["72", "115", "131"],
    "Backtracking": ["39", "40", "77", "78", "131"],
    "BinarySearch": ["33", "34", "74", "209"],
    "Math": ["29", "43", "50"],
    "HashTable": ["1", "49", "128", "138", "146", "560"],
    "TwoPointers": ["11", "19", "75", "76", "80"],
    "Stack": ["71", "735"],
    "Heap": ["215", "23"],
    "Graph": [],
    "Greedy": [],
    "Recursion": ["24", "25", "77", "78"],
    "BitManipulation": ["29"],
    "Sort": ["75", "148", "215"],
    "Other": ["44", "115", "30", "32", "42", "60", "16", "18", "31", "36"]  # Add problems that don't fit other categories
}

# Create main folders if they don't exist
for folder in MAIN_FOLDERS:
    if not os.path.exists(folder):
        os.makedirs(folder)

# Create company folders under Job
for company in COMPANY_FOLDERS:
    company_path = os.path.join("Job", company)
    if not os.path.exists(company_path):
        os.makedirs(company_path)

# Create topic folders under difficulty folders
for difficulty in ["Easy", "Medium", "Hard"]:
    for topic in TOPIC_FOLDERS:
        topic_path = os.path.join(difficulty, topic)
        if not os.path.exists(topic_path):
            os.makedirs(topic_path)

# Manual mapping of problem numbers to difficulties and titles
PROBLEM_INFO = {
    # Easy problems
    "1": {"difficulty": "Easy", "title": "Two Sum"},
    "9": {"difficulty": "Easy", "title": "Palindrome Number"},
    "13": {"difficulty": "Easy", "title": "Roman to Integer"},
    "14": {"difficulty": "Easy", "title": "Longest Common Prefix"},
    "20": {"difficulty": "Easy", "title": "Valid Parentheses"},
    "21": {"difficulty": "Easy", "title": "Merge Two Sorted Lists"},
    "26": {"difficulty": "Easy", "title": "Remove Duplicates from Sorted Array"},
    "27": {"difficulty": "Easy", "title": "Remove Element"},
    "35": {"difficulty": "Easy", "title": "Search Insert Position"},
    "94": {"difficulty": "Easy", "title": "Binary Tree Inorder Traversal"},
    "144": {"difficulty": "Easy", "title": "Binary Tree Preorder Traversal"},
    "145": {"difficulty": "Easy", "title": "Binary Tree Postorder Traversal"},
    "349": {"difficulty": "Easy", "title": "Intersection of Two Arrays"},
    "350": {"difficulty": "Easy", "title": "Intersection of Two Arrays II"},
    "637": {"difficulty": "Easy", "title": "Average of Levels in Binary Tree"},
    "993": {"difficulty": "Easy", "title": "Cousins in Binary Tree"},
    
    # Medium problems
    "2": {"difficulty": "Medium", "title": "Add Two Numbers"},
    "3": {"difficulty": "Medium", "title": "Longest Substring Without Repeating Characters"},
    "5": {"difficulty": "Medium", "title": "Longest Palindromic Substring"},
    "11": {"difficulty": "Medium", "title": "Container With Most Water"},
    "12": {"difficulty": "Medium", "title": "Integer to Roman"},
    "16": {"difficulty": "Medium", "title": "3Sum Closest"},
    "18": {"difficulty": "Medium", "title": "4Sum"},
    "19": {"difficulty": "Medium", "title": "Remove Nth Node From End of List"},
    "24": {"difficulty": "Medium", "title": "Swap Nodes in Pairs"},
    "29": {"difficulty": "Medium", "title": "Divide Two Integers"},
    "31": {"difficulty": "Medium", "title": "Next Permutation"},
    "33": {"difficulty": "Medium", "title": "Search in Rotated Sorted Array"},
    "34": {"difficulty": "Medium", "title": "Find First and Last Position of Element in Sorted Array"},
    "36": {"difficulty": "Medium", "title": "Valid Sudoku"},
    "39": {"difficulty": "Medium", "title": "Combination Sum"},
    "40": {"difficulty": "Medium", "title": "Combination Sum II"},
    "43": {"difficulty": "Medium", "title": "Multiply Strings"},
    "49": {"difficulty": "Medium", "title": "Group Anagrams"},
    "50": {"difficulty": "Medium", "title": "Pow(x, n)"},
    "56": {"difficulty": "Medium", "title": "Merge Intervals"},
    "57": {"difficulty": "Medium", "title": "Insert Interval"},
    "61": {"difficulty": "Medium", "title": "Rotate List"},
    "71": {"difficulty": "Medium", "title": "Simplify Path"},
    "74": {"difficulty": "Medium", "title": "Search a 2D Matrix"},
    "75": {"difficulty": "Medium", "title": "Sort Colors"},
    "76": {"difficulty": "Medium", "title": "Minimum Window Substring"},
    "77": {"difficulty": "Medium", "title": "Combinations"},
    "78": {"difficulty": "Medium", "title": "Subsets"},
    "80": {"difficulty": "Medium", "title": "Remove Duplicates from Sorted Array II"},
    "102": {"difficulty": "Medium", "title": "Binary Tree Level Order Traversal"},
    "103": {"difficulty": "Medium", "title": "Binary Tree Zigzag Level Order Traversal"},
    "105": {"difficulty": "Medium", "title": "Construct Binary Tree from Preorder and Inorder Traversal"},
    "128": {"difficulty": "Medium", "title": "Longest Consecutive Sequence"},
    "131": {"difficulty": "Medium", "title": "Palindrome Partitioning"},
    "138": {"difficulty": "Medium", "title": "Copy List with Random Pointer"},
    "139": {"difficulty": "Medium", "title": "Word Break"},
    "146": {"difficulty": "Medium", "title": "LRU Cache"},
    "148": {"difficulty": "Medium", "title": "Sort List"},
    "209": {"difficulty": "Medium", "title": "Minimum Size Subarray Sum"},
    "215": {"difficulty": "Medium", "title": "Kth Largest Element in an Array"},
    "560": {"difficulty": "Medium", "title": "Subarray Sum Equals K"},
    "662": {"difficulty": "Medium", "title": "Maximum Width of Binary Tree"},
    "735": {"difficulty": "Medium", "title": "Asteroid Collision"},
    
    # Hard problems
    "4": {"difficulty": "Hard", "title": "Median of Two Sorted Arrays"},
    "23": {"difficulty": "Hard", "title": "Merge k Sorted Lists"},
    "25": {"difficulty": "Hard", "title": "Reverse Nodes in k-Group"},
    "30": {"difficulty": "Hard", "title": "Substring with Concatenation of All Words"},
    "32": {"difficulty": "Hard", "title": "Longest Valid Parentheses"},
    "42": {"difficulty": "Hard", "title": "Trapping Rain Water"},
    "44": {"difficulty": "Hard", "title": "Wildcard Matching"},
    "60": {"difficulty": "Hard", "title": "Permutation Sequence"},
    "72": {"difficulty": "Hard", "title": "Edit Distance"},
    "115": {"difficulty": "Hard", "title": "Distinct Subsequences"},
}

# Function to determine the topic for a problem
def get_problem_topic(problem_number):
    for topic, problems in TOPIC_FOLDERS.items():
        if problem_number in problems:
            return topic
    return "Other"  # Default topic if not found

# Get all source code files
source_files = []
for file in os.listdir('.'):
    if file.endswith('.cpp') or file.endswith('.py'):
        # Extract problem number from filename
        match = re.match(r'^(\d+)\.(cpp|py)$', file)
        if match:
            problem_number = match.group(1)
            file_extension = match.group(2)
            source_files.append((problem_number, file, file_extension))

# Check for existing company folders and their contents
company_files = {}
for company in COMPANY_FOLDERS:
    company_path = os.path.join("Job", company)
    if os.path.exists(company_path):
        for file in os.listdir(company_path):
            if file.endswith('.cpp') or file.endswith('.py'):
                company_files[file] = company

# Also check for existing company folders at the root level
for company in COMPANY_FOLDERS:
    if os.path.exists(company):
        for file in os.listdir(company):
            if file.endswith('.cpp') or file.endswith('.py'):
                company_files[file] = company

# Check for TT, Doordash, and other potential company folders
additional_companies = ["TT", "Doordash", "BinaryTree", "DP", "TwoPointers", "Basic"]
for company in additional_companies:
    if os.path.exists(company):
        for file in os.listdir(company):
            if file.endswith('.cpp') or file.endswith('.py'):
                # Map TT to TikTok, keep others as is
                mapped_company = "TikTok" if company == "TT" else company
                company_files[file] = mapped_company

# Organize files by difficulty and topic
for problem_number, file, extension in source_files:
    # Determine difficulty
    if problem_number in PROBLEM_INFO:
        difficulty = PROBLEM_INFO[problem_number]["difficulty"]
    else:
        difficulty = "Medium"  # Default to Medium if unknown
    
    # Determine topic
    topic = get_problem_topic(problem_number)
    
    # Create topic folder path
    topic_path = os.path.join(difficulty, topic)
    if not os.path.exists(topic_path):
        os.makedirs(topic_path)
    
    # Copy the file to the appropriate difficulty/topic folder
    dest_path = os.path.join(topic_path, file)
    shutil.copy2(file, dest_path)
    print(f"Copied {file} to {topic_path}/")
    
    # If the file is associated with a company, also copy it to the company folder
    if file in company_files:
        company = company_files[file]
        if company in COMPANY_FOLDERS:
            company_path = os.path.join("Job", company)
            company_dest_path = os.path.join(company_path, file)
            shutil.copy2(file, company_dest_path)
            print(f"Copied {file} to {company_path}/")

# Generate README.md
with open("README.md", "w") as readme:
    readme.write("# LeetCode Solutions\n\n")
    readme.write("Solutions to LeetCode problems organized by difficulty and topic.\n\n")
    
    # Create table headers
    readme.write("| # | Title | Difficulty | Topic | Solution |\n")
    readme.write("|---|-------|------------|-------|----------|\n")
    
    # Group problems by number
    problem_solutions = defaultdict(list)
    for problem_number, file, extension in source_files:
        if problem_number in PROBLEM_INFO:
            difficulty = PROBLEM_INFO[problem_number]["difficulty"]
        else:
            difficulty = "Medium"  # Default to Medium if unknown
        topic = get_problem_topic(problem_number)
        problem_solutions[problem_number].append((difficulty, topic, file, extension))
    
    # Sort problems by number
    sorted_problems = sorted(problem_solutions.items(), key=lambda x: int(x[0]))
    
    # Add each problem to the table
    for problem_number, solutions in sorted_problems:
        difficulty = solutions[0][0]  # Get difficulty from first solution
        topic = solutions[0][1]  # Get topic from first solution
        
        # Get title from PROBLEM_INFO or use default
        if problem_number in PROBLEM_INFO:
            title = PROBLEM_INFO[problem_number]["title"]
        else:
            title = f"Problem {problem_number}"
        
        # Create solution links
        solution_links = []
        for sol_difficulty, sol_topic, file, ext in solutions:
            solution_links.append(f"[{ext.upper()}]({sol_difficulty}/{sol_topic}/{file})")
        
        solution_text = " ".join(solution_links)
        
        readme.write(f"| {problem_number} | {title} | {difficulty} | {topic} | {solution_text} |\n")

print("Organization complete. README.md has been updated.") 
