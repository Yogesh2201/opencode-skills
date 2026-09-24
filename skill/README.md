# Skills — source of truth

**Canonical:** `.agents/skills/` (managed via `npx skills` / `skills.sh`). This `.opencode/skill/` folder mirrors the same installs for OpenCode's native loader. `.claude/skills/` is a symlinked mirror.

Do not edit skills in place here — install via:

```bash
npx skills add <repo> --skill <name> -y
```

See `CONTEXT.md` for glossary and `docs/adr/0001-single-canonical-explanations-and-root-minimal.md` for the repo layout decision.
