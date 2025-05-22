"""🧠 1. Git Merge-na enna da?
🔁 Rendu branches-a oru branch-la serthu combine panradhudhaan merge.
Mostly, side branch (feature branch) la work pannitu main la merge pannuvom.


🧊 Real-time Situation:
👨‍💻 Developer Boy:

main – Production

login-feature – New login screen design

Work complete aayiduchu… Ippo login-feature → main la serthu release panna venum.



✅ 2. Merge Syntax:

git checkout main
git merge login-feature

💡 First main branch ku poitu, login-feature la irundha changes ellam main ku merge pannuvom.



🤖 Extra Commit Aaguma?
✅ Yes!
Merge Commit nu oru new commit create aagum:

Merge branch 'login-feature' into main

🧠 This is why Git Merge is called:

“Easy But Adds Extra Commit” ✍️


📌 3. git merge Flow with Diagram:

main:        A---B---C
                   \
login-feature:      D---E

# after merge:
main:        A---B---C-------F
                        \   /
                        D---E

                        
🎯 F = Merge Commit – Connects both branches together.


🎭 Comedy Example:
👦 Thambi – dev branch la "Sambar" vechaanga 🍛
👧 Akka – main la "Poriyal" vechaanga 🥦

Now 👨‍🍳 Amma:

“Rendu combine panni saapadra sappadu venum!” 🤤


git checkout main
git merge dev


Sambar + Poriyal = Merge Commit Ready! 😋


❤️ Kadhal Example:
👦 Boy: Love Letter type pannitu love-letter branch la vachirukaan
👧 Girl: Final read panna main branch la iruka

So:


git checkout main
git merge love-letter


Proposal final aagiduchu 💌


💻 Technical Story:
👨‍💻 Dev bugfix-001 branch la production fix panna
Now main la merge panna:


git checkout main
git merge bugfix-001


✅ Bugfix main la merge aagiduchu.
🆕 Merge Commit visible in history.



⚠️ 4. Merge Conflict-na enna?
🎯 Rendu branch la same file, same line modify panna irundha, Git confused aagum 😵‍💫
So Merge Conflict nu message kudukkum



🤕 Example Conflict:
main branch la:


print("Hello World")


feature branch la:


print("Vanakkam Ulagam")


Ippo merge panna Git sollum:

“Enna print pannanum? Decide pannu da!” 🤯



✅ Conflict Resolve Panrathu:
Open the file:

<<<<<<< HEAD
print("Hello World")
=======
print("Vanakkam Ulagam")
>>>>>>> feature


Nee edhu venum nu decide pannu:

print("Vanakkam Ulagam")


Save the file

Then run:

git add filename.py
git commit

🎉 Conflict resolved!


🔚 Summary Table:


| Action                        | Command                         |
| ----------------------------- | ------------------------------- |
| Merge branch                  | `git merge branchname`          |
| Switch to main before merge   | `git checkout main`             |
| Resolve conflict              | Edit → `git add` → `git commit` |
| Check if merge conflict there | Git will show during `merge`    |


💡 Git Merge vs Rebase?


| Feature        | `merge`                     | `rebase`                  |
| -------------- | --------------------------- | ------------------------- |
| Commit History | Extra commit created        | Linear, no extra commit   |
| Easy?          | ✅ Yes                       | ❌ Bit advanced            |
| Conflict risk  | Moderate                    | Higher during rebase      |
| Use when       | Team work, preserve history | Clean solo commit history |


🧠 Final Recap:
🔀 git merge – Combine branches

🆕 Creates new commit (merge commit)

⚠️ May cause conflicts – resolve manually

🧽 Useful when feature complete → main ku merge


"""