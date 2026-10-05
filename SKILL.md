---
name: token-compression
description: "Cut token usage when reading context and writing replies: locate-then-read file windows, incremental re-reads, summarize long transcripts, and give filler-free lead-with-the-answer replies. Use for long contexts or explicit token-saving/brevity requests; skip when exact wording, full files, or detailed explanation is required. 压缩读取上下文与输出回复的 token：先定位再精准读取、增量重读、长文摘要、去掉语气词与冗余表达。"
---

# Token Compression

Cut token cost on both ends of a turn: what Codex reads, and what it writes. Compression is behavioral, not engine-level; it does not change the tokenizer or context window. Savings come from reading less, reading precisely, and writing tighter. Never sacrifice correctness, requested substance, or user intent for brevity.

## When to apply

- The user asks to save or compress tokens, shorten replies, or reduce context usage.
- Context is long or near limits, or large files, logs, and transcripts must be processed.
- Output is bloated with filler, repetition, or process narration.

Skip when brevity would lose meaning: exact quotes or wording, data tables, full-file reviews, or requests for detailed explanation. Compression targets presentation and selection, not omission of required content.

## Modes

- Reading context: read [references/reading.md](references/reading.md).
- Writing replies: read [references/writing.md](references/writing.md).
- Read both when a turn involves heavy input and verbose output.

## Measure savings

When the user wants a number, compare before/after text with [scripts/estimate_tokens.py](scripts/estimate_tokens.py). It is a heuristic (CJK ≈ 1 token per char, other text ≈ 1 token per 4 chars), for relative comparison, not exact billing.

## Core rules

1. Read the smallest source that answers the question; expand only on evidence of need.
2. Once content is summarized, treat the summary as authoritative; do not re-read or re-quote the original unless correctness depends on it.
3. Lead with the answer; state uncertainty in one clause; no filler, no restating the question or prior context.
4. Keep the user's substance, meaning, and intent intact.
