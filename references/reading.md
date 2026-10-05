# Reading-side compression

Goal: acquire only the tokens needed to answer correctly, in the fewest reads.

## Locate before reading

- Search first: `rg` for symbols, errors, function names, and config keys; `rg --files` to list candidates. Never dump whole files to "get oriented".
- Before reading diffs: `git diff --stat`, then read only the changed hunks; `git status --short` first.
- Before reading logs: filter with `rg -i "error|warn|fatal|fail|<user keyword>"`, then widen only if the filtered view is insufficient.

## Read windows, not whole files

- For long files, read a targeted window first: the head, tail, or the section around a match. Use `Get-Content -TotalCount` / `Select-Object -Skip N -First M` on Windows, or `sed -n` / `head` / `tail` elsewhere.
- Expand to a full read only when the task needs whole-file semantics: full rewrite, cross-cutting refactor, or a config whose parts interact.

## Re-read incrementally

- If a file was read earlier in the conversation, do not dump it again. Re-open only what changed: `git diff -- <path>` for modified work, or re-run the earlier search to confirm state.
- Trust prior reads and summaries unless the user reports drift; verify only the changed region.

## Summarize long context

- For long transcripts, histories, or paste dumps: compress into a compact intermediate summary of facts, decisions, open questions, and key values. Work from the summary; open the original only for exact wording, quotes, or data.
- Use the most compact format that stays accurate: a table or key-value list for repetitive fields, short prose for relationships.

## Keep working notes lean

- Do not copy large blocks into notes or intermediate messages. Record line numbers, identifiers, and conclusions.
- Trim stale notes once they no longer affect the remaining work.

## When not to compress reads

- Correctness-critical verification: exact configs, schemas, sensitive text.
- The user asked to review a whole file or produce full-file output.
- Search or summarization cannot faithfully replace the raw text.
