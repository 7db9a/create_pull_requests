

## Setup

Create `env.list` file with the following:

```
GITHUB_TOKEN=YOUR_GITHUB_TOKEN
```

Run

```
docker run -it --env-file env.list fork-repo node fork-repo.js "turbo-src/demo"
docker run -it --env-file env.list python create_pull_request.py "7db9a" "demo" "master" "pullRequest1" "refactor(lsp): remove redundant client cleanup" "auto pull request"


            /*owner:*/ contributor_name,
            /*repo:*/ "demo",
            /*fork_branch:*/ "pullRequest1",
            /*issue:*/ "issue_1",
            /*title:*/ "refactor(lsp): remove redundant client cleanup",
```

```
docker build -t create-pull-request .
```