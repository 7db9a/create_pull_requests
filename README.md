

## Setup

Create `env.list` file with the following:

```
GITHUB_TOKEN=YOUR_GITHUB_TOKEN
```

Run

```
docker run -it --env-file env.list create-pull-requests \
python create_pull_requests.py "7db9a" "demo" "master" "pullRequest1" "refactor(lsp): remove redundant client cleanup" "auto pull request"
```

```
docker build -t create-pull-requests .
```