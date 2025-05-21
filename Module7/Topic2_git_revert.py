"""
🎯 Goal: Mistake commit-a safe-ah undo panna git revert use panrom.
Ithu reset madhiri past-ku poi delete panradhillai…
Ithu new commit create pannidum which undo the effect of previous commit.



🔁 Basic Idea:
🧠 git reset → Time machine → Delete past
🧠 git revert → Hero madhiri → Undo pannitu new scene create pannuvom

git revert <commit_id>


💡 Example: git revert abc123


🎭 Real-Time Story:
Example Situation:

echo "line 1" > notes.txt
git add .
git commit -m "Add line 1"

echo "line 2" >> notes.txt
git add .
git commit -m "Add line 2"

echo "line 3" >> notes.txt
git add .
git commit -m "Add line 3"


Now file content:

line 1
line 2
line 3

Oops! Line 2 commit mistake. Now we want to undo that. But we don’t want to delete history, just safely revert it.


git log --oneline

Output:

c3d9f0c Add line 3
6f7e1aa Add line 2  ← Mistake!
4f6a123 Add line 1


Now we run:

git revert 6f7e1aa


🔄 Difference Between reset vs revert

| Feature            | `git reset`              | `git revert`                           |
| ------------------ | ------------------------ | -------------------------------------- |
| History            | Erase panrum             | History preserve panrum                |
| Commit Undo Style  | Past-ku poi adikka       | New commit create pannitu adikkum      |
| Team Safety        | Unsafe for team projects | **Safe for shared repos (team use)** ✅ |
| File Delete Option | Yes (hard)               | No delete. Only reverse                |



💘 Lovers Example:
👦 Boyfriend Git repo:

Commit 1: “Hi baby”

Commit 2: “I love u”

Commit 3: “I hate you” (😱 fight aayiduchu)

Now avaru sorry sollanum. But adha delete panna mudiyadhu, trace venum.

git revert HEAD


➡️ New commit create aagum → “Undo: I hate you”
➡️ Apdiye history la irukkum, but patch fix aagidum 💖



🏏 Cricket Example:
Captain’s Git:

Commit 1: “MS Dhoni added”

Commit 2: “Remove Dhoni” (mistake!)

But reset panna teamku confusion 😵‍💫

git revert <remove dhoni commit id>


➡️ New commit: “Undo Remove Dhoni”
➡️ Dhoni returns 🔁 crowd ku happy 🧢🔥



👪 Family Example:
👩 Amma Git Repo:

Commit 1: “Made Dosa”

Commit 2: “Add Paneer Pizza”

Commit 3: “Remove Sambar” (Mistake!!)

git revert <sambar remove commit>


➡️ Sambar comeback! 🍲
➡️ Amma’s menu log is intact 😍


🤣 Comedy Example:
Goundamani Git:

Commit 1: “Welcome Sir”

Commit 2: “Serve Coffee”

Commit 3: “Take Payment”

Now Sir didn’t pay 😆


git revert <payment commit>


➡️ Goundamani: "Cancel pannunga bill-a!" 😂
➡️ Tea served free!


⚙️ Technical Real-Life Example:
👨‍💻 Example 1 – Developer Mistake:

git revert f6a2de


➡️ Safe undo
➡️ Code history intact
➡️ Teams will know what got reverted


👨‍💻 Example 2 – Production Fix:
Last commit caused bug in production ❌
Instead of deleting commit:

git revert HEAD


➡️ Rollback aagidum
➡️ Jira ticket ku safe commit trace ready irukkum



💥 Final Recap:


| Concept          | Explanation                                                |
| ---------------- | ---------------------------------------------------------- |
| `git revert`     | Mistake commit-ku **safe undo** by creating **new commit** |
| Usage            | `git revert <commit_id>`                                   |
| Advantage        | History preserve pannum, teamwork-ku safe ✅                |
| Common Use Cases | Lovers, family menu, cricket captain, production bug, etc. |
| Danger Level     | ❌ ZERO! Very safe command                                  |


💡 Always remember:

Reset – risky, clean slate (past delete)

Revert – safe, traceable, teamwork-friendly ❤️


"""