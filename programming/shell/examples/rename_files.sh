#/bin/sh

# Author:   Jaroslav Langer
# Date:     2020, Dec. 12th
# Desc.:    Examples of how to rename multiple files in shell

# Rename 'PSH_HW_01' to 'assignment_01'
for file in *; do echo assignment_${file##*_}.sh; done # Look at the result first
# Remove the longest anyting ending with '_' from the beginning, prepend 'assignment_' append '.sh'
for file in *; do mv ${file} assignment_${file##*_}.sh; done

# Remove redundant .sh extension e.g. rename 'my_file.sh.sh' to 'my_file.sh'
for file in *; do mv ${file} ${file%%.sh*}.sh; done

