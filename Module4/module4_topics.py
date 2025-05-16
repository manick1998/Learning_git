"""🔥 MODULE 4: Git File Lifecycle – Working Dir ➡ Staging ➡ Commit
3 zone iruku:

Working Directory (actual files)

Staging Area (prepare panra files)

Git Repository (commit pannadhudhaan)

Command flow:

git add ➡ git commit

Real-time story: Pasanga project la edit panra files laam final ah commit aagara level

======================================================================================

📦 Staging Area – Enna Idhu?
🔊 “Staging Area na, commit panna ready-a irukkura files oda pakkathu room.”
Git-ku sollanum: “Ithu naan commit panna ready da! 🫡”


”

🧠 Simple Definition:
Nee edit panna files → Working Directory

Adha git add use pannitu → Staging Area

Apram dhaan git commit panni Git repo-kku move aagum.


🎭 Realtime Example 1 – Lover Story 💕:
Scenario:
Boyfriend letter ezhudhuraan (proposal letter) – Working Directory

Adha review pannitu neat-a rewrite panraan – Staging Area

Final ah kadhal letter post pannraan – Git Repository

Staging Area la irukkudhu dhaan final commit panna ready-a irukkura kadhal ❤️ letter 😄



🏏 Realtime Example 2 – Cricket Team Selection:
Scenario:
All players practice pannuraanga → Working Directory

Coach shortlist pannuraanga → Staging Area

Captain final 11 announce pannuraar → Git Repo

Practice pannuna podhum illa, Staging ku select aaganum dhan commit aagalam! 



😂 Realtime Example 3 – Comedy Scene:
Scenario:
Goundamani 5 jokes ezhudhuraar → Working Directory

Senthil 2 jokes pick pannitu final script prepare pannuraar → Staging Area

Director approve pannitu cinema-la add pannuraar → Git Repo

Joke vettiya adichu final script-ku prepare panradhu dhan Staging Area 😂


💻 Technical Examples
💻 Tech Example 1:
bash
Copy
Edit


touch hello.py
Pudhu file create pannina → Untracked file
Git-ku innum sollala “Ithu enaku venum nu”


git add hello.py

Ippo Git-kku sonna: “Ithu commit panna ready da!”
hello.py → Staging Area move aayiduchu ✅

🔄 Commands Summary:

| Command             | Use Panradhu                                               |
| ------------------- | ---------------------------------------------------------- |
| `git add file.py`   | File-ai staging area ku anupuradhu 📤                      |
| `git status`        | Staging-la irukka files status check                       |
| `git reset file.py` | Staging-la irukkura file-ai thirumba working-la anupuradhu |


🧪 Status Variations – Git Status Output la:

| File Status               | Meaning                             |
| ------------------------- | ----------------------------------- |
| `Untracked file`          | Git-ku pudhusa therinjidhu          |
| `Modified file`           | Nee edit pannirukka, but not staged |
| `Changes to be committed` | Staged and ready for commit         |


🪄 Story Recap Table:
| Git Zone     | Action Example                        | Lover / Cricket / Comedy             |
| ------------ | ------------------------------------- | ------------------------------------ |
| Working Dir  | File edit / create                    | Letter write / Practice / Joke write |
| Staging Area | File select for commit (`git add`)    | Letter neat aakradhu / Shortlist     |
| Git Repo     | Final commit pannradhu (`git commit`) | Post / Final Team / Movie release    |
===========================================================================


"""