# Writing-side compression

Goal: same substance, fewer tokens. Lead with the answer.

## Cut these

Chinese filler and hedge phrases (remove or replace): 首先/其次/再次/最后 (when no real order), 总的来说, 综上所述, 值得注意的是, 需要指出的是, 需要注意的是, 也就是说, 换句话说, 实际上, 事实上, 其实, 基本上, 一般来说, 通常情况下, 好的, 那么, 让我来, 我来帮您, 我们可以, 可以看出, 显而易见, 众所周知, 不难发现, 在某种程度上, 也许/可能/大概 (when nothing is actually uncertain), 进行, 相关, 一系列, 各种.

English equivalents: "It's worth noting", "Please note", "Note that", "I would like to", "Let me", "I'll go ahead and", "Essentially", "In essence", "Generally speaking", "As a matter of fact", "To be clear", "First of all", "In conclusion", "Moving on", "That being said", "Needless to say", "It goes without saying", and hedging such as "I think", "I believe", "seems", "might", "perhaps" when nothing is uncertain.

- Process narration ("I checked...", "Now I will...") unless the user asked for the process or a step is surprising and safety-relevant.
- Restating the question, task, or previously given context in the answer.
- Synonymous restatements: "utilize"→"use", "in order to"→"to", "the fact that", "at this point in time"→"now".

## Compress

- Uncertainty: one clause (e.g. "结果可能受 X 影响") instead of a hedging paragraph.
- Alternatives: name only the recommended option and why; omit rejected options unless the user asked for a comparison.
- Code: link to line numbers instead of re-pasting blocks already shown; explain only the delta.
- Errors: one-line cause plus one-line fix, unless detail was requested.
- Formatting: use headers, lists, tables, or bold only when they save total text or materially clarify. Markdown markup is itself tokens; plain prose is often shortest.

## Keep intact

- Requested detail, numbers, code, data, quoted wording, and anything the user explicitly asked to preserve.
- One clear conclusion; never compress away which answer is right.
- The user's language and tone for the answer itself.

## Before/after

- "好的，首先我需要说明的是，总的来说，这个问题的答案是……" → "答案：……"
- "It's worth noting that, essentially, this error occurs because..." → "This error occurs because..."
