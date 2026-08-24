---
title: "Slides 02: Git"
description: "Unix Programming Environment"
author: Peter Bui
keywords: lecture,sos,git
url: https://pnutz.h4x0r.space/courses/cse.20589.fa26/slides02.html
theme: domer-slides
---

<!-- _class: lead -->

# CSE 20589

## Git

---

# Warm-up Questions

<div class="font-large">

1. How do you currently keep track of <strong class="success">multiple
   versions</strong> of a file?

2. How do you <strong class="caution">share</strong> files with others?

3. What is <strong class="primary">Git</strong> and how does it help us with the
   two situations above?

</div>

---

<!-- _class: lead -->

# Git: <strong class="gold">Concepts</strong>

---

# Concepts: <strong class="gold">Overview</strong>

<strong class="primary">Git</strong> is a free and open source <strong
class="hljs-comment">distributed version control system</strong> designed to
handle everything from small to very <strong class="danger">large projects
</strong>with speed and efficiency.

<br>

<div class="columns-3-2">

<div>

- <strong class="success">Journal</strong>

- <strong class="caution">Time Machine</strong>

- <strong class="special">Shared Space</strong>

</div>

<div class="centered">

<br>

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Git-logo.svg/330px-Git-logo.svg.png">

</div>

</div>

---

# Concepts: <strong class="gold">Journal</strong>

As a <strong class="success">journal</strong>, <strong
class="primary">Git</strong> allows us to **keep track** of our work by
annotating it:


- With <strong class="primary">Git</strong>, we keep our work in a <strong
  class="caution">repository</strong> that contains our data and the <strong
  class="success">journal</strong> that describes the history of changes to our
  data.

- We periodically **record** our progress by storing <strong
  class="hljs-comment">commits</strong> or entries to the <strong
  class="success">journal</strong> (<strong class="success">*commit
  log*</strong>)

- At any time, we can view the current <strong class="danger">changes</strong>
  and our past work, along with descriptions of what was done and who did it!

---

# Concepts: <strong class="gold">Time Machine</strong>

Because of the <strong class="success">journal</strong>, <strong
class="primary">Git</strong> can serve as a <strong class="caution">time
machine</strong> and allow us to revisit **previous versions** of our data:

- We can easily <strong class="caution">throw away</strong> our current
  changes.

- We can <strong class="danger">revert</strong> to a previous project state.

- We can selectively <strong class="special">checkout</strong> **previous
  versions** of a file.

- We can <strong class="danger">modify</strong> our history!

---

# Concepts: <strong class="gold">Shared Space</strong>

Because of the <strong class="success">journal</strong>, <strong
class="primary">Git</strong> allows multiple people to work on the same data
set and:

- Allow us to easily <strong class="special">share</strong> work done on the
  project from multiple people.

- Allow us to <strong class="danger">merge</strong> in changes from different
  folks.

- Tell us if there are <strong class="caution">conflicting</strong> changes.

---

<!-- _class: lead -->

# Git: <strong class="gold">Mental Model</strong>

---

# Model: <strong class="gold">Upstream Repository</strong>

<div class="centered margin-top-0-5">

<img src="static/img/slides02-model-upstream.png">

</div>

Each project is stored in a <strong class="primary">primary repository
</strong>called the <strong class="warning">upstream</strong> that can usually
be found on a code hosting platform such as [GitHub], [GitLab], or [Codeberg].

<br>

#### Example Upstream Repository

[https://github.com/nd-cse-20589-fa26/assignments]()

[GitHub]: https://github.com
[GitLab]: https://gitlab.com
[Codeberg]: https://codeberg.org

---

# Model: <strong class="gold">Origin Repository</strong>

<div class="centered margin-top-0-5">

<img src="static/img/slides02-model-origin.png">

</div>

We <strong class="hljs-comment">fork</strong> the <strong
class="warning">upstream repository</strong> to create a <strong
class="caution">remote copy</strong> of the project called the <strong
class="info">origin</strong> in our own account.

<br>

#### Example Fork

[https://github.com/nd-cse-20589-fa26/assignments-pbui]()

---

# Model: <strong class="gold">Local Repository</strong>

<div class="centered margin-top-0-5">

<img src="static/img/slides02-model-local.png">

</div>

We <strong class="hljs-comment">clone</strong> the <strong class="info">remote
origin repository</strong> to our <strong class="caution">local
machine</strong> to create a <strong class="success">local copy</strong> of the
project:

$ **git** <strong class="hljs-comment">clone</strong> git@github.com:nd-cse-20589-fa26/assignments-pbui

---

# Model: <strong class="gold">Working Directory</strong>

<div class="centered margin-top-0-5">

<img src="static/img/slides02-model-working-directory.png">

</div>

We <strong class="hljs-comment">checkout</strong> the project files from our
<strong class="success">local repository</strong> to populate our <strong
class="special">working directory</strong>.  This is usually done automatically
when we <strong class="hljs-comment">clone</strong>.

---

# Model: <strong class="gold">Staging Area</strong>

<div class="centered margin-top-0-5">

<img src="static/img/slides02-model-staging-area.png">

</div>

We <strong class="hljs-comment">add</strong> files to the <strong
class="danger">staging area</strong> to have <strong
class="primary">Git</strong> track our changes.

$ **git** <strong class="hljs-comment">add</strong> file

---

# Model: <strong class="gold">Commit</strong>

<div class="centered margin-top-0-5">

<img src="static/img/slides02-model-commit.png">

</div>

We <strong class="hljs-comment">commit</strong> changes to permanently record
the staged data.

$ **git** <strong class="hljs-comment">commit</strong> -m "Summary of changes"

---

# Model: <strong class="gold">Push</strong>

<div class="centered margin-top-0-5">

<img src="static/img/slides02-model-push.png">

</div>

We <strong class="hljs-comment">push</strong> to send the recorded data from
the <strong class="success">local repository</strong> to the <strong
class="info">origin</strong>.

$ **git** <strong class="hljs-comment">push</strong>

---

# Model: <strong class="gold">Pull</strong>

<div class="centered margin-top-0-5">

<img src="static/img/slides02-model-pull.png">

</div>

We <strong class="hljs-comment">pull</strong> to <strong
class="caution">fetch</strong> changes from the <strong
class="info">origin</strong> and <strong class="warning">merge</strong> them
into our <strong class="success">local repository</strong>.

$ **git** <strong class="hljs-comment">pull</strong>

---

<!-- _class: lead -->

# Git: <strong class="gold">Branches</strong>

---

# Branches: <strong class="gold">Overview</strong>

Internally, the recorded <strong class="success">commits</strong> in a <strong
class="primary">repository</strong> form a <strong class="caution">directed
acyclic graph (DAG)</strong>.

<div class="centered">

<br>

<img src="static/img/slides02-branches.png">

</div>

- Each <strong class="success">commit</strong> is a node with a unique <strong
  class="special">hash identifier</strong>.

- The last <strong class="success">commit</strong> is referred to as the
  <strong class="warning">HEAD</strong>.

- A <strong class="primary">branch</strong> is a pointer to the last <strong
  class="success">commit</strong> in a line of development.

- The default <strong class="primary">branch</strong> is called the <strong
  class="danger">master</strong> or <strong class="danger">main</strong>.

---

# Branches: <strong class="gold">Creating</strong>

When we <strong class="hljs-comment">branch</strong>, we create an alternative path or line of
development:

<div class="centered">

<br>

<img src="static/img/slides02-branches-creating.png">

</div>

$ **git** <strong class="hljs-comment">branch</strong> reading01

Since <strong class="success">commits</strong> belong to the <strong
class="primary">branch</strong> where they are recorded, the data in the
<strong class="special">working directory</strong> will depend on which <strong
class="primary">branch</strong> we are currently working on.

---

# Branches: <strong class="gold">Switching</strong>

Because our <strong class="special">working directory</strong> can only show
one <strong class="primary">branch</strong> at a time, we must <strong
class="hljs-comment">switch</strong> to the <strong
class="primary">branch</strong> we want to work on.

<div class="centered">

<br>

<img src="static/img/slides02-branches-creating.png">

</div>

$ **git** <strong class="hljs-comment">switch</strong> reading01

Each <strong class="hljs-comment">switch</strong> performs a <strong
class="hljs-comment">checkout</strong> that updates the files in the <strong
class="special">working directory</strong> to match the changes in the <strong
class="primary">branch</strong>.

To both create a new <strong class="primary">branch</strong> and <strong
class="hljs-comment">checkout</strong> its changes:

$ **git** <strong class="hljs-comment">switch</strong> -c reading01

---

# Branches: <strong class="gold">Merging / Rebasing</strong>

To integrate changes from one <strong class="primary">branch</strong> into
another, we perform a <strong class="hljs-comment">merge</strong> or <strong
class="hljs-comment">rebase</strong>.

<div class="centered">

<br>

<img src="static/img/slides02-branches-merging.png">

</div>

- During a <strong class="hljs-comment">merge</strong>, we create a new <strong
  class="success">commit</strong> that represents the combining of both <strong
  class="primary">branches</strong>.

- During a <strong class="hljs-comment">rebase</strong>, we copy the unique
  <strong class="success">commits</strong> from one <strong
  class="primary">branch</strong> and replay them onto another.

---

# Branches: <strong class="gold">Resolving Conflicts</strong>

During a <strong class="hljs-comment">merge</strong> or <strong
class="hljs-comment">rebase</strong>, there may be <strong
class="danger">conflicting changes</strong> between the two <strong
class="primary">branches</strong>.  In this situation, the user must <strong
class="success">resolve</strong> the <strong class="danger">conflicts</strong>
before the <strong class="hljs-comment">merge</strong> or <strong
class="hljs-comment">rebase</strong> can continue:

1. Edit files with <strong class="danger">conflicts</strong>.

2. <strong class="hljs-comment">add</strong> resolved files to <strong
   class="danger">staging area</strong>.

3. <strong class="hljs-comment">commit</strong> the new changes.
