"""
🤔 git diff na enna?
"git diff nu solradhu, files la irukkura changes paakradhu."
Edhula irundhu edhuku? → Working Directory ↔ Staging Area, Staging ↔ Last Commit compare pannanum-na use panuvom.




💡 Real Meaning:
Git ku theriyum: “Nee edhavadhu maathuna, naan save panna old version la irundhu evlo difference nu kaamikkaren.


🧠 Structure – git diff Options:

| Command             | Enna kaamikkum?                          |
| ------------------- | ---------------------------------------- |
| `git diff`          | Working dir ↔ Staging area-la difference |
| `git diff --staged` | Staging area ↔ Last commit-la difference |
| `git diff HEAD`     | Working dir ↔ Last commit-la difference  |


❤️ Lover Example:
Situation:
Boyfriend proposal letter ezhudhuraar.

First draft la: "Unnai paarthadhula irundhu naan kaadhalikkiren"

Edit panninaar: "Unna paartha udane kaadhalichiten"


git diff


🔊 Git sonna: “Nee line change pannirukka! Idhu dhaan old, idhu dhaan pudhusa.”

- symbol = Old version (remove)

+ symbol = New version (add)

📌 Boy: “Ithu dhaan naan solla vandha kaadhal difference 😅”


🏏 Cricket Example:
Situation:
Coach team strategy file la modify panninaar.

Old: "Dhoni - Finisher"

New: "Dhoni - Mentor"

git diff


“Unna last commit panni file-la irundhu ippo irukkura file la difference dhaan kaamikka poren!”

🧠 Match strategy maariyirukku nu oru compare report kedakkum.


😂 Comedy Example:
Scenario:
Goundamani script la solli irundhathu:

"Nee than enaku veedu"

Edit panninaar: "Nee veedu than naan thangamudiyala"

git diff


Goundamani: “Script change aayiduchu da! Senthil ah blame panna scene maariyiduchu.”


💻 Technical Example 1:

echo "print('Vanakkam da mapla')" > app.py
git init
git add app.py
git commit -m "first version"

Green = New | Red = Old
Ithu thaan real-time file difference!


💻 Technical Example 2: Staged Difference

git add app.py
git diff --staged


Idhu Staging area vs Last commit difference kaamikku.


👨‍👩‍👧 Family Example:
Scenario:
Amma soru list eludhinaanga.

Old: "Arisi, Thakkali, Vengayam"

New: "Arisi, Thakkali, Milagai"

git diff


📌 Amma sonna:

“Unakku vennilanga venaamnu sollirukken! Nee Milagai add pannirukka!”

Git ku irundha old list & new list la exact-a difference kaamichidum 😄


 Lovers Summary Table:

 
 | Situation              | git command         | Meaning                                 |
| ---------------------- | ------------------- | --------------------------------------- |
| Paadhi letter ezhudhu  | `git diff`          | Unedited vs Edited version kaamikku     |
| Love msg draft compare | `git diff`          | First msg vs second msg difference      |
| Commit pannirukka file | `git diff --staged` | Final commit-ku send panna area compare |


🔥 Recap Quick View:

| Command             | Compares Between                  | Use When?                        |
| ------------------- | --------------------------------- | -------------------------------- |
| `git diff`          | Working Directory vs Staging Area | Just modified but not staged yet |
| `git diff --staged` | Staging Area vs Last Commit       | Already added files check panna  |
| `git diff HEAD`     | Working vs Last Commit directly   | Full file change check panna     |


📦 git diff Summary in 1 Line:
🔍 “Nee enna maathina, naan enna commit pannirundhen – idhula evlo vithyasam nu kaamikkaren!”


"""