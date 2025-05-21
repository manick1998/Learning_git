"""🔥 git branch – A to Z Postmortem (Tanglish-la Deep, Spoonfeeding Explanation)
🎯 git branch = Namma project ku vera vera “story line” create panni work panna use panra tool 😄




🧠 Basic Concept:
Oru movie la multiple versions irukku-nu nenachu paathuko:

Hero one path la software engineer

Inoru path la IPS officer

Inoru path la villain 😈

Ithu thaan branching concept!

Namma Git-la, main (master) branch irukkum default-a.
Namma venumna new branch create panni, experiment, test, features laam separate-a try panni later merge panna mudiyum.



✅ Common Commands:


| Command                       | Meaning                  |
| ----------------------------- | ------------------------ |
| `git branch`                  | Existing branch list     |
| `git branch branch_name`      | Pudhu branch create      |
| `git checkout branch_name`    | Branch switch            |
| `git checkout -b branch_name` | Create + switch together |
| `git branch -d branch_name`   | Branch delete            |


🔥 Step-by-Step A to Z:

🪜 Step 1: git branch


git branch



Current repo-la irukkura ella branches um kaamikkum
Current-a irukkura branch green star la kaamikkum.


💬 Family Example:
Amma veetla Soru Plan Repo maintain panraanga 🍛

main branch → Amma usual rasam-sambar

diet-plan branch → Appa ku special sugar-less food

festival-special → Deepavali samayal

git branch



* main
  diet-plan
  festival-special



🏏 Cricket Example:
Captain Git repo-la match planning panrar:

main → Regular team

ipl → IPL strategy

wc2025 → World Cup squad

git branch


* main
  ipl
  wc2025


Captain decide panrar: “WC 2025 la strategy maathanum”
So switch:


git checkout wc2025




❤️ Lovers Example:
Boyfriend oru Love Plan Repo maintain panrar:

main → Usual texts

impress-plan → Gift + Poem

apology-plan → Sorry messages

git branch

* main
  impress-plan
  apology-plan


Enna panraru?

git checkout -b impress-plan

New branch create + switch to impress-plan


💻 Technical Example:
Step-by-Step

mkdir git-demo
cd git-demo
git init
echo "hi" > index.txt
git add .
git commit -m "initial commit"


Create branch:

git branch dev


List branches:

git branch


Output:

* main
  dev

  
 Switch to dev:

git checkout dev


🤓 Deep Note:
Git-la, branch nu oru “pointer” thaan.
Adhu oru specific commit ID ah point pannuthu.

Namma branch create pannomna, Git:

Current commit ID ah copy panni

Pudhu branch-ku assign pannum



🤩 Comedy Example:
Goundamani Script Repo:

main → Original jokes

senthil-mock → Mock version

dubbed-version → Hindi comedy dubbing


git branch



* main
  senthil-mock
  dubbed-version


Goundamani: “Senthil comedy laam side branch-la irukkanum da!”


🧠 git branch Flags Summary:

| Command                  | Use                          |
| ------------------------ | ---------------------------- |
| `git branch`             | List all branches            |
| `git branch <name>`      | New branch create            |
| `git checkout <name>`    | Switch branch                |
| `git checkout -b <name>` | Create + Switch              |
| `git branch -d <name>`   | Delete branch                |
| `git branch -a`          | List local + remote branches |




🎯 Why Branching?
Experiment panna

Multiple developer work isolate panna

Main code clean-a irukka


🔚 Final Kathai:
Git Branch = Namma project oda multiple worlds
Namma oru line-la error panni affect pannama vera line-la try pannalam
Last-la correct-a irundha merge panlaam 💪
"""