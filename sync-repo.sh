# This bash script uses git to synchronize changes between the local and remote GitHub repository.
# Usage: ./sync-repo.sh

# steps:
# 1. stage all changes
# 2. commit changes with message 'Updated'
# 3. pull changes from remote repository on branch 'main'
# 4. push changes to remote repository on branch 'main'.
# 5. check if the push was successful

# 1. Stage all changes
git stage .

# 2. Commit changes with message 'Staged changes Updated'
git commit -m "Staged changes Updated"

# 3. Pull changes from remote repository on branch 'main'
git pull origin main

# 4. Push changes to remote repository on branch 'main'
git push origin main

# 5. Check if the push was successful
if [ $? -eq 0 ]; then
  echo "Push successful"
else
  echo "Push failed"
fi

# Echo a message that the script is complete
echo "Synchronization complete"

