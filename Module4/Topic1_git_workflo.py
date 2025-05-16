"""

🔥 Git File Lifecycle – 3 Important Zones:


| Zone                  | Enna nadakum?                          |
| --------------------- | -------------------------------------- |
| 🗃️ Working Directory | Actual files irukkura place (local la) |
| 📦 Staging Area       | Prepare panra files stage pannuvom     |
| 🏛️ Git Repo          | Final snapshot save agum place         |



🎯 Today Focus: Working Directory (WD)
— "Idhu dhaan unga veedu, unga ellaa file-um ippo inga dhan irukku 😎"


🔎 Working Directory na enna?
🟢 Git project folder-le irukkura actual files and folders
🟢 Git init pannina apram create aagura repo ku veliye irukkura nadagam
🟢 Changes ellam inga dhan nadakkum


📁 Example Folder Structure:

/my-project        <-- 🔥 Working Directory
├── index.html
├── app.py
└── readme.md

Intha folder-la nadakra changes ellam Working Directory la irukkura actions.

🧪 Technical Meaning:
Unmodified file → untouched file

Modified file → edit aana file

New file → pudhusa create pannirukka


💡 Analogy: Oru Kalyana Veedu Example 🏠
🎭 Kalyanam Example:

| Git Lifecycle     | Real Life Equivalent                              |
| ----------------- | ------------------------------------------------- |
| Working Directory | Amma kitchen-la samayal panra stage 🍛            |
| Staging Area      | Samayal saaptuku table-la arrange panra stage 🍽️ |
| Git Repository    | Saapadu photo vachu memory save panra stage 📸    |


🎮 Realtime Example 1 – Cricket Practice:
🏏 Cricket Ground la Pasanga Practice:
Net practice la batting panra boys → Working Directory

Select aana best players → Staging Area

Final team announce aana list → Git Repository

🧠 Git-ku munnadi ellarum practice dhan.
Practice pannra stage dhaan Working Directory! 😎


🏡 Realtime Example 2 – Family Project:
Thambi drawing board-la design panraan → Working Directory

Appa check pannitu select panra files → Staging Area

Amma final frame la potutu veetla display panraanga → Git Repository

🤹 Thambi oda rough version Working Directory la dhan 😄


🎭 Realtime Example 3 – Comedy Scene:
Sivakarthikeyan Script Example 😆
Comedy punch panra idea paper-la ezhudhura → Working Directory

Director-ku send panra scene → Staging Area

Cinema-la final edit panni release panra scene → Git Repo

🧪 Technical Example 1 – Python Dev:

touch script.py


Pudhu file create pannina, innum Git-ku theriyadhu

Ithu Working Directory la irukkura untracked file



🧪 Technical Example 2 – Web Dev:

code index.html


Edit panni save pannina

Git-ku “Nee change pannirukka!” nu theriyum

But Git innum track pannala

So idhu Modified in Working Directory



🔁 What Happens in WD:

🔁 What Happens in WD:



| Action                  | Status in Git                   |
| ----------------------- | ------------------------------- |
| Pudhu file create       | `Untracked file`                |
| File edit               | `Modified file`                 |
| Git-ku file add pannala | `Changes not staged for commit` |
| `git add` pannina       | Moves to → **Staging Area** ✅   |



🎯 Commands Involved:


git status        # WD-la enna changes irukku nu kaatuthu
git diff          # WD & Staging compare pannum
git checkout .    # WD changes-a revert pannum


🧠 Summary Tabl

| Git Zone          | Enna?                                  | Real Life Example         |
| ----------------- | -------------------------------------- | ------------------------- |
| Working Directory | Nee edit, create, delete panra stage   | Amma samayal panra veedu  |
| Staging Area      | Git-ku “Ready” nu sonna stage          | Plate-la saapadu vechadhu |
| Git Repository    | Commit pannitu permanent save panradhu | Saapadu photo memory 📸   |



🧵 Moral of the Story:
🔊 “Working Directory na — Git la oru file life start agra place.
File yaarum track pannala, intha stage la than namba design, edit ellam pannuvom.”



🔥 git commit – Enna Idhu?
“Oru file-ai staging area la irundhu permanent Git repository ku send pannradhu dhaan git commit.”

💡 Simple-a solna:
Working Directory – Edit panra place

Staging Area – “Ready bro!” nu sollra place

Git Repository – Final safe locker 🧳

🔁 Command Format:

git commit -m "Unna nenacha daan naan commit pannunen 🥹"



❤️ Lover Example:
Scenario:
Boyfriend kadhal letter ezhudhuvaar – Working Directory

Neat-a type pannuvaar, spelling check – Staging Area

Envelope la potu post office ku anupuvaar – Git Repository

🔊 git commit = “Letter-ai post pannitten da, idha thirumba edhavadhu maathave mudiyathu!” 💌


🏏 Cricket Example:
Scenario:
Players practice panraanga – Working

Coach shortlist panraanga – Staging

Captain final 11 team announce panraar – Commit

🔊 git commit = “Team list press release aagiduchu da, ippo yaaraiyum add/remove panna mudiyadhu!” 🏏



😂 Comedy Example:
Scenario:
Goundamani 5 jokes solla ezhudhuvaar – Working

Senthil 2 pick panni prepare panraar – Staging

Director final script approve panni shoot pannuvaar – Git Repo

🔊 git commit = “Camera roll aayiduchu da! Script lock 🔒!” 🎬

💻 Technical Example 1:

touch hero.py
nano hero.py
# Type panren: print("Thalaivar entry 🎉")

File create + edit – Working Directory

git add hero.py
Staging-ku anupinaachu ✅

git commit -m "Thalaivar intro ready 🚀"


Permanent Git Repository la commit aagiduchu.
Ippo hero.py oru version ah Git safe-a vachirukku 🔐


💻 Technical Example 2:
Undo panna mudiyuma?

git log

Commit history paarunga – version no, message laam.

Commit history paarunga – version no, message laam.

🧠 Once committed, adhu snapshot aagiduchu.
Maathuradhu, delete panradhukku special steps venum (not like editing working files).

🎭 Emotions-Based Examples:
😍 Kadhalan:
git add → Kadhal letter type pannaachu
git commit → Letter post pannitten 😭

🏏 Dhoni:
git add → Practice match ready
git commit → “Final World Cup team aayiduchu da!”

😂 Vadivelu:
git add → Kattikitu comedy plan panraan
git commit → “Adhuvum naan panren! Release pannaachu!” 😂

🧪 Commit Best Practices:

| 🔧 Action              | 🧠 Best Practice                                 |
| ---------------------- | ------------------------------------------------ |
| `git commit -m "msg"`  | Message should be short & meaningful 📝          |
| `git commit -am "msg"` | Add + Commit in one shot (only tracked files) 🚀 |
| `git log`              | Previous commits view panna 💻                   |

✅ Summary – Git Zones:

| Zone           | Action       | Example                                 |
| -------------- | ------------ | --------------------------------------- |
| Working Dir    | File edit    | Ezudhura place                          |
| Staging Area   | `git add`    | Neat-a prepare panra place              |
| Git Repository | `git commit` | Final official memory / snapshot locker |


🧵 Simple Analogy Table:

| Scenario        | Working Dir        | Staging Area    | Git Repo            |
| --------------- | ------------------ | --------------- | ------------------- |
| Love Letter     | Type panrathu      | Check panrathu  | Post pannathu       |
| Cricket Team    | Practice           | Shortlist       | Final team announce |
| Vadivelu Script | Idea type panrathu | Filter panrathu | Shoot pannathu      |


🤖 Real Use Example:

git init
echo "print('Hello Raja')" > raja.py
git add raja.py
git commit -m "Raja intro scene completed 🫡"

Ithu dhaan complete basic Git flow 🔁


"""