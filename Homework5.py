# HW1/HW2 Review: The Terminal + Command Line + Git
# 1. The command pwd will tell what the working directory is.
# 2. The command ls will list all the files in the current working directory.
# 3. The command cd ~/python_decal/brianna_repo will change you to the directory containing homework.py. Then, use the command git pull origin main (or master) to pull the latest changes. 
# 4. The command mv ~/brianna_repo/homework.py ~/python_decal/judy_decal/homework/homework.py should move the homework file to the personal homework repository.
# 5. Assuming, we are in the homework directory, nano homework.py will allow you to view the homework file in the terminal from the personal repository. Otherwise from brianna_repo use cd ../judy_decal/homework to move to the homework directory. Then use nano homework.py to open the file.
# 6. After using nano homework.py to open the file in the terminal, you can edit the document. Then press command x to exit the file. There will be a prompt asking if you want to save the changes. Press y to save the changes.
# 7. You can use the following commands to save the changes and push from your local repository to your remote repository: git add homework.py, git commit -m "Adding homework.py file", git push origin main (or master).
# 8. The command git pull origin main (or master) should be called. Judy did not pull the local changes before pushing them to the remote repository.
# 9. The absolute path cd ~/Recent will move you to the directory named "Recent"
# Sources: 
# https://www.git-tower.com/learn/git/ebook/en/command-line/appendix/command-line-101#:~:text=To%20change%20this%20current%20working,%24%20cd%20..
# https://support.apple.com/guide/terminal/manage-files-apddfb31307-3e90-432f-8aa7-7cbc05db27f7/mac#:~:text=Go%20to%20the%20Terminal%20app,it%20in%20the%20new%20location.
# Referenced the bCourses page on these topics and the class lecture recordings.

# HW3 Review
# 2.1 Data Types
def checkDataType(x):
    info = type(x)
    x = str(x)
    return info
checkDataType(True)
checkDataType(3.14)

# 2.2 Conditionals
def evenOrOdd(int):
    if int % 2 == 0:
        return "Even"
    else:
        return "Odd"
evenOrOdd(7)
evenOrOdd(10)

# 3. Loops
numbers = [1, 2, 3, 4, 5]
def sumWithLoop(numbers):
    total = 0
    for i in numbers:
        total += i
    return total
sumWithLoop(numbers)
#Source: https://stackoverflow.com/questions/13909052/how-do-i-add-together-integers-in-a-list-sum-a-list-of-numbers-in-python





