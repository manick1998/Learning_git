"""😵‍💫 Real-time Situation
Situation 1:

🚶‍♂️ Nee oru code la work pannitu iruka.
💬 Suddenly Team Lead vandhu:

“Inime immediate-ah main branch la oru bug fix pananum da!”

😨 Aana un current work complete illa.
Commit panna mudiyala. Aana switch-aagavum vendiyadhu 😰




❓ Solution: git stash 😍
🔐 "Temporary-ah un changes safe-a oru locker la stash pannuvom!"
Later use panlam!

✅ 1. git stash – Temporary Save

git stash


💡 Modified & Staged files temporary-ah hide pannidum.
Working directory clean aagidum 😮‍💨


🎭 Comedy Example:
👦 Thambi: Code write panra mathiyila amma sollanga,

“Poi kada-la vaangu!” 🍅🧄

Aana code-a save panna mudiyala!
So:
git stash

✅ 2. git stash list – All Stashed Changes

🎯 Un stash pannina list ellam show aagum:

stash@{0}: WIP on main: abc123 – Added login page
stash@{1}: WIP on dev: def456 – Fixed navbar issue


🧠 stash@{0} is the latest one.

✅ 3. git stash apply – Restore from Locker

git stash apply

🎯 Latest stash restore pannum (but locker-la irukum still).


✅ 4. Specific Stash Apply:

git stash apply stash@{1}

🎯 Old stash-um apply panna mudiyum 👌


✅ 5. Apply & Delete (Pop):

git stash pop


🎯 Restore pannum plus locker-la irundhu remove pannidum.



✅ 6. Delete Specific Stash:

git stash drop stash@{0}


🎯 Oru stash-a delete pannuvom.

✅ 7. Delete All Stashes:

git stash clear

🎯 All stash lockers empty 😮‍💨


💕 Kadhal Example:
👦 Boy proposal page code ezhuthitu irukaan
💬 Girl: “Enakku oru help panna mudiyuma?”
👦: git stash
(Proposal page safe-a locker la)

git stash
# goes to help
git stash apply
# continues proposal ❤️

👨‍👩‍👧 Family Example:
👩 Amma: Kitchen recipe code panra
👧 Baby: “Amma coloring help pannunga!”
👩 Amma


git stash


Color help mudinjadhu appuram:

git stash apply

Recipe thirumbi continue 💪


🧑‍💻 Technical Example:
🧑‍💻 Dev staging branch la new feature code panra
Suddenly Production issue vandhuchu
Switch panna vendiyadhu:

git stash
git checkout main
# fix issue
git checkout staging
git stash apply


🔥 All safe – both sides!


🔚 Summary Table:

| Action                 | Command                     |
| ---------------------- | --------------------------- |
| Temporary save         | `git stash`                 |
| View stashes           | `git stash list`            |
| Restore latest stash   | `git stash apply`           |
| Restore & delete stash | `git stash pop`             |
| Restore specific stash | `git stash apply stash@{1}` |
| Delete specific stash  | `git stash drop stash@{0}`  |
| Clear all stashes      | `git stash clear`           |


🚦 Bonus: When to use git stash?

| Situation                                    | Use?                               |
| -------------------------------------------- | ---------------------------------- |
| Half-finished work – want to switch branches | ✅ Yes                              |
| Changes needed later – not ready for commit  | ✅ Yes                              |
| Want clean working directory temporarily     | ✅ Yes                              |
| Want to save changes permanently             | ❌ No    → Use `git commit` instead |


🧠 Final Recap with Emoji:
🔐 git stash – Locker la podu

📋 git stash list – Locker open & view

🛠️ git stash apply – Changes restore

🧹 git stash pop – Restore & remove

🗑️ git stash clear – All locker empty!




"""