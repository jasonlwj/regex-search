#! python3
# regex_search.py - Opens all .txt files in a folder and searches 
#                   for any line that matches a user-supplied 
#                   regular expression.
# Usage: py.exe regexsearch.py - Search all files in current directory for text that matches the user-supplied regex.
#        py.exe regexsearch.py <folder> - Search all files in <folder> for text that matches the user-supplied regex.

import os, re, sys

def main():
  def regex_search(target_dir):
    # Prompt the user for the regex
    user_input = input('Enter regex: ')
    user_regex = re.compile(user_input)

    # Search through each file in the directory
    for dir_file in os.listdir(target_dir):
      file_lines = open(os.path.join(target_dir, dir_file), errors='ignore').readlines()
      file_matches = []

      # Number of matching occurences in this file
      file_match_count = 0

      # Search through each line in the file
      line_num = 0
      for line in file_lines:
        line_num += 1
        matches = user_regex.findall(line)
        if len(matches) > 0:
          file_matches.append('ln{0}: {1}'.format(line_num, line))
          file_match_count += len(matches)
      
      # Summarise and print results for this file
      print('-------------------------------------')
      print('Searching in {0}:\n{1} occurence{2} found.'.format(
        dir_file, 
        file_match_count,
        's' if file_match_count != 1 else ''
      ))
      print('-------------------------------------')
      for match in file_matches:
        print(match)

  if len(sys.argv) == 1:
    # Search all files in current directory
    regex_search('.')
  elif len(sys.argv) == 2:
    # Search all files in <folder>
    if os.path.isdir(sys.argv[1]):
      regex_search(sys.argv[1])
    else:
      print('Directory does not exist.')
  else:
    print('Invalid argument(s). Try something else.')

if __name__ == "__main__":
  main()
  