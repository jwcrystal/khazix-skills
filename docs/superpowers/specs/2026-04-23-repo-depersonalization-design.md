# Repo Depersonalization Design

## Goal

Convert this repository from a branded public distribution into a neutral, personal-use skill repository with reusable methodology, no embedded persona branding in skill bodies, and explicit migration notes where names change, while keeping the repository name unchanged.

## Success Criteria

- Remove `Khazix` / `數字生命卡茲克` / `KKKKhazix` branding from skill bodies, prompts, and repository-facing docs unless kept in a short attribution note.
- Rename skill-facing names and human-facing labels so the resulting repository is suitable for personal/private use rather than a mirror of someone else's brand.
- Preserve the useful methodology and technical behavior of the skills.
- Keep a minimal migration note so renamed skills and paths remain understandable.
- Avoid unrelated refactors.

## Scope

### In Scope

- `README.md`
- `CLAUDE.md`
- `hv-analysis/SKILL.md`
- `hv-analysis/scripts/md_to_pdf.py`
- `longform-writer/SKILL.md`
- `longform-writer/references/content_methodology.md`
- `longform-writer/references/style_examples.md`
- `prompts/橫縱分析法.md`
- Any repo paths, titles, labels, and usage text directly tied to persona branding

### Out of Scope

- Rewriting the underlying research or writing methodologies from scratch
- Adding new features to the skills
- Packaging, release, or publish automation changes beyond text/path updates required by renaming

## Approach

Use a full depersonalization pass with renaming and a small compatibility note:

1. Replace brand-bound prose with neutral, method-focused language.
2. Rename human-facing and technical names that still carry the old brand.
3. Keep one concise attribution/migration section in `README.md` only.
4. Preserve skill triggers, structure, and technical behavior unless branding is part of the behavior.

## Naming Strategy

### Repository

- Keep the repository name as-is, but replace descriptive copy with neutral personal-use wording.
- Remove account, workspace, and publishing identity from repo docs.

### Skills

- `longform-writer/` is the neutral replacement for the former `khazix-writer/` skill.
- The skill frontmatter `name`, title, examples, and references should use the new neutral naming.
- `hv-analysis/` may keep its methodology-oriented name because it describes the framework rather than the persona, but its body text should remove author-persona framing.

### Prompts

- Keep prompt names only if they are methodology-based.
- Remove author attribution from prompt body text except for a short README note.

## Content Strategy

### README.md

- Change the descriptive copy while keeping the repo name unchanged.
- Update any skill table entries that still describe skills as persona-specific.
- Add a short attribution/migration section.
- Keep installation/use text generic rather than tied to a branded account identity.

### CLAUDE.md

- Remove mirror/publishing instructions tied to account and platform identity.
- Reframe it as a local repository guidance file.
- Preserve only instructions still useful for maintaining this repo.

### hv-analysis/SKILL.md

- Keep the framework and process.
- Remove lines that frame the method as belonging to a specific persona.
- Replace style guidance such as persona readability references with neutral descriptions like「高可讀性、敘事性、非學術腔研究寫法」.
- Remove author-name examples from command snippets.

### hv-analysis/scripts/md_to_pdf.py

- Change the default author from `數字生命卡茲克` to a neutral default such as `作者未指定`.
- Keep CLI override support unchanged.

### longform-writer Skill Family

- Rename the folder and skill name to a neutral equivalent.
- Rewrite the skill description so it targets long-form article generation in a specified authorial style rather than persona imitation.
- Rewrite reference materials to describe reusable style dimensions instead of persona worship or identity-specific imitation.
- For examples that are too identity-specific, either rewrite them into neutral examples preserving the writing principle, or replace them with distilled rules.

### prompts/橫縱分析法.md

- Keep the framework explanation.
- Remove explicit founder attribution from the prompt body.
- If needed, move attribution to README only.

## Migration Note

`README.md` should include a small section covering:

- old skill name → new name
- note that branding was removed for personal-use neutrality
- where attribution is retained

This is documentation-only compatibility, not a requirement to keep old filenames around.

## Risks and Mitigations

### Risk: Over-renaming breaks discoverability or existing local references

Mitigation:
- keep a clear old→new mapping in README
- preserve methodology terms where they are not brand-specific

### Risk: Writing skill loses its useful style signal after depersonalization

Mitigation:
- replace persona labels with explicit style characteristics
- keep concrete editorial checks and examples where they still work generically

### Risk: Repo docs still contain hidden account-specific references

Mitigation:
- run a final grep for brand/account names after edits

## Verification Plan

- Search the repo for remaining occurrences of `Khazix`, `數字生命卡茲克`, `KKKKhazix`, and similar identifiers.
- Review renamed skill metadata and paths for consistency.
- Check that README migration notes match actual renamed paths.
- Confirm code/script defaults still work after text changes.

## Implementation Order

1. Keep the repo name unchanged and use `longform-writer` as the replacement for `khazix-writer`.
2. Update repo docs (`README.md`, `CLAUDE.md`).
3. Update `hv-analysis` body text and script defaults.
4. Rewrite the `longform-writer` skill and references.
5. Update prompt text.
6. Run final repo-wide search for leftover branding.

## Finalized Naming Decision

- keep the repository name unchanged
- rename `khazix-writer` to `longform-writer`
