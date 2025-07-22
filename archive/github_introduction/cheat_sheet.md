## Github Workflow

---

Use this sheet as a reference if you get stuck during the github process

### Step 1 - Pull Changes from Main

<i>Always do this before creating a new branch, it will save a massive headache later!</i>

```bash
git checkout main       ## switch to main branch
```
```bash
git pull origin main    ## pull merged changes from github
```

---

### Step 2 - Complete New feature/work

```bash
git checkout -b new_branch      ## create and switch to new branch "new_branch"
```

<i>or if you already have work done on an existing branch:</i>

```bash
git checkout existing_branch    ## swtich to existing branch "existing_branch"
```

```bash
git merge main                  ## merge in new changes from main to existing branch
```

---

### Step 3 - Push your new changes to Github

Useful:

```bash
git status      ## overview of current situation (whats changed, whats been committed etc)
```
Run this whenever you need to in order to see what has changed

---

```bash
git add file_thats_changed  ## or git add . to add all changed files
```
```bash
git commit -m "useful message that explains change"   ## commit your changes with a helping message
```
```bash
git push -u origin branch_name      ## push your changes to github
```

<i>Make branch name the same as your current branch name</i>

---

### Step 4 - Make Pull Request on Github

- Best practice is to pull request before merging changes into main
- give a small description of whats changed, and how someone else can test the changes

---

### Step 5 - Pull main changes into your local main

```bash
git checkout main
```
```bash
git pull origin main
```
