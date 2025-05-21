"""git checkout use panni

🎭 Branch switch

🔙 Old commit-kupoi files restore

🧻 Specific file restore from previous commit or branch panlaam.



🔧 git checkout – 3 Main Usage Types:

| Use Case                    | Example                       |
| --------------------------- | ----------------------------- |
| 1. 🔀 Branch switch         | `git checkout feature-branch` |
| 2. 🕒 Go back to old commit | `git checkout <commit_id>`    |
| 3. 🧻 Restore specific file | `git checkout main file.txt`  |


💘 Lovers Example:
👩‍❤️‍👨 Love Git Repo:

Commit 1: “Hi Darling”

Commit 2: “I Miss You”

Commit 3: “We broke up”

Boyfriend sad 😢
But he wants to re-read old messages (Commit 2)

git checkout <commit_id_2>


➡️ Avan commit 2 view panra mathiri poi paakalam ❤️
(Note: Avan HEAD detached la iruppan. Temporary visit 😅)


🏏 Cricket Example:
Captain’s Git:

Branch 1: main → Playing 11

Branch 2: ipl-t20 → Experimental team

Captain wants to switch to T20 team:

git checkout ipl-t20


➡️ T20 team branch la shift aagiduchu 🧢🔥

👪 Family Example:
👩 Amma Git Repo:

File: menu.txt

Main branch: “Idli, Dosa, Sambar”

Branch party-menu: “Pizza, Pasta, Coke”

Now Amma wants regular menu:


git checkout main


➡️ Amma back to healthy menu 🍲


🤣 Comedy Example:
Goundamani Git:

File: joke.txt

Main: “Sir, tea kudunga”

Mistake: “Sir, coffee poison ah!”

Boss: “Adha delete panra”


git checkout main joke.txt


➡️ Old clean joke file restore aagiduchu 😆


🎓 Technical A to Z Explanation:

✅ 1. Branch Switch:

git checkout <branch-name>


🧠 HEAD apdiye new branch-kku shift aagum.
Old files, new files pathu switch aagidum.

Example:

git checkout develop


🗣️: "Develop branch-kku shift aachu boss!"

🔁 2. Go to Old Commit:

git checkout <commit-id>


⚠️ Ithu detached HEAD mode-a irukkum. Temporary view only.

git checkout 4537dff


🧠: You’re just viewing history, not editing it.
If changes pannanumna, new branch create pannanum.

git checkout -b old-version 4537dff


➡️ Ithu new branch-a open pannum from old state.

🧻 3. Restore File from Another Branch:

git checkout <branch-name> -- <filename>


Example:

git checkout main -- index.html

💡 Ithu current working dir la main branch-la iruntha file-a restore pannum.
Very useful when one file got changed/messed.


💥 Realtime Developer Mistake Example:
🤖 Case 1: File Mess\

git checkout main -- README.md


➡️ Main branch la iruntha README.md current working directory la overwrite aagum.

⚠️ Caution – Detached HEAD?
If you do:

git checkout 123abc


🧠 You’ll be in detached HEAD – safe illa to do commits here directly.
If you want to continue from here:

git checkout -b temp-fix


🔁 Difference Summary:

| Action        | Command                         | Result                         |
| ------------- | ------------------------------- | ------------------------------ |
| Branch switch | `git checkout <branch>`         | Moves HEAD to that branch      |
| Commit view   | `git checkout <commit-id>`      | HEAD detached                  |
| File restore  | `git checkout main -- file.txt` | File replaced from main branch |


🧠 Memory Tip:
🗂️ checkout = Check + Out
→ Enna thevaiyo adha check out panrom:

Branch-a?

File-a?

Commit snapshot-a?

🧘 Final Recap:

| Use Case                         | What Happens                 |
| -------------------------------- | ---------------------------- |
| 🔀 `git checkout <branch>`       | Move to another branch       |
| ⏳ `git checkout <commit>`        | View old snapshot (detached) |
| 🧻 `git checkout branch -- file` | File restore from branch     |


"""