"""🔥 MODULE 7: Undoing Changes – git reset – Go Back (A to Z Postmortem in Tanglish)
🎯 Purpose:
git reset na time machine madiri. Mistake pannitom-na, back button press panradhudhaan 😄
Old state-ku marubadiyum povom. But adhuvum 3 mode irukku.

🧠 Basic Concept:
git reset = Commit / Stage / File status ah marakka use panrom.
3 major types irukku:


| Command             | Use                                                            |
| ------------------- | -------------------------------------------------------------- |
| `git reset --soft`  | Commit-a than back pannum, staging la irukkum                  |
| `git reset --mixed` | Commit + staging back, working dir la file irukkum             |
| `git reset --hard`  | Commit + staging + working dir ellam delete! (Use carefully ❌) |


🎯 Real-Time Kathai:
💻 Story Setup:


echo "line 1" > story.txt
git add .
git commit -m "1st line"
echo "line 2" >> story.txt
git add .
git commit -m "2nd line"
echo "line 3" >> story.txt
git add .
git commit -m "3rd line"


Now total 3 commits irukku.


💔 Real-Time Example: Lover Mistake
Boyfriend git repo:

Commit 1: "Love letter start"

Commit 2: "I like you"

Commit 3: "I love you" (Oops! Too early confession 😱)

Ippadi mistake pannitaaru... apdiye back button-a press panna:


🛠 git reset --soft HEAD~1
"Love you" commit-a remove pannuvom, but still staging la irukkum
Like: Undo commit, but keep file ready


git reset --soft HEAD~1


🧠 HEAD~1 na → last commit-ku munnadi poi vidu

Now:

git log la "I love you" illai 😌

But git status la file stage la ready irukkum



🛠 git reset --mixed HEAD~1
Undo commit + staging-aum remove pannuvom
File mattum working directory la irukkum


git reset --mixed HEAD~1


Now:

File unstaged (add panna mathiri)

git status la modified ah kaatum

Useful when: "Oops! Add panna thevai illa!"



🛠 git reset --hard HEAD~1
🔥 Danger Zone!
Commit + staging + file in working dir – ellathayum delete panrum ❌


git reset --hard HEAD~1


Ithu panna:

"I love you" line-um poidum

File-leyum illa 😨

Unstage aagum

Undo + delete thaan

🛑 Use only if you are 100% sure. No undo for this undo!


🏏 Cricket Example:
Captain strategy repo:

Commit 1: Team list

Commit 2: Add Dhoni

Commit 3: Remove Dhoni (mistake 😭)

Undo dhoni remove panradhukku:

git reset --soft HEAD~1


Dhoni comeback confirmed 🧢🔥

👪 Family Example:
Mom:

Commit 1: Idly

Commit 2: Vada

Commit 3: Pizza (Kids force panniya 😆)

Now she wants to go back:

git reset --mixed HEAD~1


Pizza cancel... back to Vada life 💛


💬 Comedy Example:
Goundamani:

Commit 1: Vaanga sir vaanga

Commit 2: Tea kudunga

Commit 3: Bill vaangunga (Aiyo, unpaid 🤣)

Now he wants to remove bill:

git reset --hard HEAD~1

Tea free, no bill! 😆


⚠️ Important Note:

| Mode      | Safe? | What happens?                          |
| --------- | ----- | -------------------------------------- |
| `--soft`  | ✅     | Only commit removed, file still staged |
| `--mixed` | ✅     | Commit + stage removed, file stays     |
| `--hard`  | ❌     | Everything erased. No mercy.           |



🔚 Final Recap:
git reset --soft HEAD~1
🧠 Undo commit only, stage la file irukkum

git reset --mixed HEAD~1
🤹 Undo commit + stage, file working la irukkum

git reset --hard HEAD~1
💀 Ellameyum poidum — RIP files 🪦










































































































"""