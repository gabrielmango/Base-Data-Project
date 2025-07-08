# Git Branching and Commit Standards

## Branch Naming Convention
`<type>/<issue-id>-<short-description>`

### Branch Types
| Type        | Description                                     | Example                          |
|-------------|------------------------------------------------|----------------------------------|
| `feat/`     | New features or functionality                  | `feat/PROJ-123-add-mongo-loader` |
| `fix/`      | Bug fixes                                      | `fix/PROJ-456-handle-null-dates` |
| `refactor/` | Code restructuring without behavior change     | `refactor/PROJ-789-optimize-sql` |
| `docs/`     | Documentation updates                          | `docs/PROJ-101-update-readme`    |
| `test/`     | Test-related changes                           | `test/PROJ-202-add-pipeline-test`|
| `chore/`    | Maintenance tasks, config changes              | `chore/PROJ-303-update-poetry`   |
| `hotfix/`   | Critical production fixes                      | `hotfix/PROJ-404-urgent-db-fix`  |

### Rules
- Use lowercase with hyphens
- Keep descriptions concise (3-5 words)
- Include issue tracker ID if available
- Separate words with hyphens

## Commit Message Convention
```
<type>[optional scope]: <description>

[optional body]

[optional footer]
```

### Commit Types
| Type     | Description                           |
|----------|---------------------------------------|
| `feat`   | A new feature                         |
| `fix`    | A bug fix                             |
| `docs`   | Documentation changes                 |
| `style`  | Formatting, white-space               |
| `refactor`| Code change without functional change |
| `test`   | Test additions/corrections            |
| `chore`  | Maintenance tasks                     |
| `build`  | Build system changes                  |
| `ci`     | CI configuration changes              |
| `perf`   | Performance improvements              |
| `revert` | Reverts a previous commit             |

### Commit Structure
1. **Header** (required)
   - Format: `<type>(<scope>): <short description>`
   - Max 72 characters
   - Imperative mood ("Add" not "Added")

2. **Body** (optional)
   - Explain what and why
   - Wrap at 72 characters
   - Blank line after header

3. **Footer** (optional)
   - Reference issue tracker IDs
   - BREAKING CHANGE notices

### Examples
**Simple feature:**
```
feat(loaders): add MongoDB bulk insert
```

**Fix with issue reference:**
```
fix(extractors): handle website timeouts

Resolves: PROJ-456
```

**Breaking change:**
```
feat(config)!: migrate to YAML configuration

BREAKING CHANGE: .env files no longer supported
```

## Workflow Process
1. Start from updated `main` branch:
   ```bash
   git checkout main
   git pull origin main
   ```

2. Create new branch:
   ```bash
   git checkout -b feat/PROJ-123-add-postgres-conn
   ```

3. Make atomic commits:
   ```bash
   git add path/to/file.py
   git commit -m "feat(connections): implement connection pool"
   ```

4. Push and create PR:
   ```bash
   git push -u origin feat/PROJ-123-add-postgres-conn
   ```

## Best Practices
1. **Atomic Commits**: Each commit = single logical change
2. **Frequent Commits**: Small, regular commits
3. **Meaningful Messages**: Focus on why, not just what
4. **Pre-commit Checks**:
   ```bash
   poetry run task format
   poetry run task test
   ```

## Commit Message Validation
Create `.git/hooks/commit-msg`:
```bash
#!/bin/sh

MESSAGE=$(cat $1)
PATTERN="^(feat|fix|docs|style|refactor|test|chore|build|ci|perf|revert)(\(.+\))?: .{1,72}$"

if ! echo "$MESSAGE" | head -1 | grep -qE "$PATTERN"; then
  echo "ERROR: Invalid commit message" >&2
  echo "Format: <type>[scope]: <description>" >&2
  exit 1
fi
```
Make executable: `chmod +x .git/hooks/commit-msg`

## Cheat Sheet
| Element          | Pattern                                         |
|------------------|-------------------------------------------------|
| **Branch**       | `type/issue-short-description`                  |
| **Commit Type**  | `feat`, `fix`, `docs`, `refactor`, etc.         |
| **Commit Scope** | Component in parentheses `(connections)`        |
| **Commit Desc**  | Imperative mood, <72 chars, first letter caps  |