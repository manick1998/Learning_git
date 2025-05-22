"""💡 1. Pull Request-na enna?
GitHub-la fork/cloned repo-la edutha changes ah, original repo owner kitta submit panni 
“Ithu correctaa? Merge pannalama?” nu request podradhu dhaan Pull Request (PR) 🙏


🧠 2. Pull Request Flow – 6 Easy Steps:
✅ Step 1: Fork Original Repo
👉 Public repo vaanga – fork click pannu
📌 Now unakku own copy ready


✅ Step 2: Clone Forked Repo

git clone https://github.com/unname/my-forked-repo.git
cd my-forked-repo


📂 Local-la work panna setup ready


✅ Step 3: New Branch Create Pannu

git checkout -b bugfix/logo-align


🌱 Fresh branch → changes safe-a nadakkum
🚫 Direct main branch la work panna kudathu


✅ Step 4: Change Code + Commit

# Code change pannitu
git add .
git commit -m "Fixed logo alignment issue"

💡 Change panni commit panna ready


✅ Step 5: Push to Your Forked Repo


git push origin bugfix/logo-align

🌐 GitHub forked repo-ku branch send pannirukom


✅ Step 6: GitHub la Pull Request Create Pannu
🖥 GitHub → Compare & pull request button click
✍️ Description ezhuthu:

Enna fix pannina?

Enna purpose?

Screenshot / Example attach panna better

➡️ Create Pull Request button click


❤️ 3. Kadhal Example – Lover Letter PR 💌
👧 Girl: Original letter repo la “proposal.md” file

👦 Boy: Fork pannitu, roses-added branch create pannitu:


git commit -m "Added roses and chocolate lines 💐🍫"
git push origin roses-added


➡️ GitHub la PR podraan:

"Please accept my changes 💖 Pull pannalama?" 😍


👨‍👩‍👧 4. Family Example – Amma’s Recipe Pull Request 🍲
👦 Paiyan: Amma recipe fork pannitu extra-spice branch la kodum


git commit -m "Added 2 tsp pepper 🔥"


➡️ Amma kitta PR podraan:

"Amma, idhu unga original recipe ku nalla twist 🙏 Merge pannalama?"


😂 5. Comedy Example – Team Memes PR 😆
👨‍💻 Dev A: funny-memes repo la irukkararu
👨‍💻 Dev B: Fork pannitu “Monday-meme” nu add panraan

git commit -m "Added Monday Office Struggle meme 😩"


➡️ PR: “Boss, ithu daily pain ah capture pannuthu. Merge pannunga 😜”



👨‍💻 6. Technical Example – Bug Fix PR 🐞
🎯 Repo: weather-app
👨‍💻 You: Fork pannitu
🌱 Branch: fix-temperature-unit


git commit -m "Fixed Fahrenheit to Celsius conversion"
git push origin fix-temperature-unit


➡️ GitHub la Pull Request → main branch ku

📌 Maintainer review pannuvaanga
✅ Nallaa irundha → Merge
❌ Issue irundha → Comments varum


🔁 7. Merge Types in PR:

| Merge Type            | Description                     |
| --------------------- | ------------------------------- |
| Create a merge commit | History maintain pannum         |
| Squash and merge      | Multiple commits → 1 merge      |
| Rebase and merge      | Clean history – like re-writing |


👉 Mostly maintainers decide pannuvaanga


🧩 8. What Happens After PR?

| Action             | Result                           |
| ------------------ | -------------------------------- |
| Maintainer accepts | Merge into main                  |
| Maintainer rejects | Comment pottu return pannuvaanga |
| You fix & resend   | PR update agidum (same PR id-la) |


🔧 9. PR Summary Table:

| Step                | Command / Action                       |
| ------------------- | -------------------------------------- |
| Fork Repo           | GitHub UI → Fork                       |
| Clone Repo          | `git clone <your-repo>`                |
| Create Branch       | `git checkout -b my-feature`           |
| Code + Commit       | `git add . && git commit -m "message"` |
| Push Branch         | `git push origin my-feature`           |
| Create Pull Request | GitHub UI → Compare & Pull Request     |
| Wait Review/Merge   | Maintainer action                      |


🧘‍♂️ 10. Final Analogy Summary:

| Life Example | GitHub PR Flow                            |
| ------------ | ----------------------------------------- |
| Love Letter  | Proposal changes sent for approval 💌     |
| Amma Recipe  | Twist add panni recipe submit pannuvom 🍛 |
| Meme Comedy  | Own version add panni LOL kodupom 🤣      |
| Team Bug Fix | Code fix pannitu submit panrom 🛠         |

"""