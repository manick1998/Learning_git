"""

🔥 MODULE 2: Git Installation & Configuration – Part 2
🎯 Topic: git config --global user.name, user.email, git config --list
✅ Postmortem (A to Z, Spoonfeeding, Real-life, Story Based)
✅ No English, only Tanglish
✅ Kulanthaikum puriyum maadhiri



🧒 Oru Git Kathai – Part 2: “Yaar enna panra-nu theriyanuma?”
Arjun Git install panni, git --version check pannitaan.
Ippo project ku code commit panna ready-aa irukaan.

Aana Git oru question kekum…

"Dai Arjune... Nee yaaru da?
Yaaroda peru la commit podanum-nu enakku theriyuma?"

Idhukku thaana... First-time configuration!
(Like namma phone la name save panradhu maadhiri)

🧪 Step 1: Name & Email set panna
🧔 Arjun sollra maadhiri neeyum sollu Git-kitta:

git config --global user.name "Unga Name"


🔍 Example:

git config --global user.name "Arjun Kumar"



🧑‍💻 Git sollum:
"OK Arjune! Ippo naan therinjukitten nee yaaru-nu!"


💌 Step 2: Email set panna

git config --global user.email "ungamail@example.com"


git config --global user.email "arjunkumar@gmail.com"


🤔 Why email?
GitHub-ku connect aagum bodhu,
Email la dhan identify pannum.
(Mail ID = Aadhaar Card in Git world!)

📋 Step 3: Namma settings laam correct-a irukkaa-nu check panna
git config --list


🟢 Output:
user.name=Arjun Kumar
user.email=arjunkumar@gmail.com


👉 Ithu varudhu-na, ✅ Correct-a set pannirukkeenga.


🎯 Deep Detail – --global naa enna?
🧠 --global na whole system-ku apply aagum.
Namma laptop/PC la ella Git projects-ku same name/email use aagum.

📝 Specific project-ku maattum name/email venaam-na:

git config user.name "Project Name"
git config user.email "projectmail@example.com"




👨‍👦 Real Life Example (Kulanthayum Puriyara Madhiri)
🔷 Cricket Example:
Dhoni team la irundhu match podraru.

Scorer-ukku theriyanum: Yaar boundary adicharu, yaar out aanaanga.

So each player-oda ID card venum.

✅ Git config = Scorer-kitta ID kodukradhu!


🔷 Family Example:
Appa, Amma, Thambi – Moonu perum shopping list la item add pannanga.

Aana later appa sonnaaru:
“Yaar enna item add panranga-nu theriyala!” 😅

✅ Git config = Appa theriyara maadhiri signature vechiradhu!


🔷 Technical Example:
Company la 4 developer irukanga.

Oru repo-le ella perum commit panranga.

GitHub la commit history paartha udane:

Ravi sonna line

Priya delete panna file

Arjun update panna bug fix

✅ Git config = History full-a transparent-a kaattum!



🔚 Summary Table:

| Step      | Command                                                 | Explanation                       |
| --------- | ------------------------------------------------------- | --------------------------------- |
| Name set  | `git config --global user.name "Unga Name"`             | Yaaru-nu Git kitta sollradhu      |
| Email set | `git config --global user.email "ungamail@example.com"` | GitHub-ku connect panna use aagum |
| Check     | `git config --list`                                     | Set panna values check pannradhu  |



"""