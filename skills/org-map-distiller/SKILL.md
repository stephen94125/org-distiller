---
name: org-map-distiller
description: "Meta-skill for distilling small-group or organization communication records into a portable <org_name>-map skill. Use when analyzing LINE chats, email, meeting notes, interviews, observation notes, documents, or recurring team records to generate an evidence-backed map skill containing events, people profiles, relationship maps, graph summaries, risks, and open questions."
---

# Org Map Distiller

Distill human small-group records into a portable organization map skill.

This is a meta-skill. Its job is not only to analyze a group, but to generate a reusable `<org_name>-map` skill that contains:

- `SKILL.md`
- `references/events.md`
- `references/people.md`
- `references/relationships.md`
- `references/graph-summary.md`
- `references/open-questions.md`
- `references/risks.md`

The generated skill should help future agents quickly understand the group by strongly encouraging them to read the six reference artifacts before answering questions about that group.

This skill is useful for company teams, family businesses, departments, labs, communities, and recurring working groups. It is not for psychological diagnosis, defamatory claims, loyalty tests, surveillance, or contacting people.

## Core Rule

Always separate four layers:

1. Events: what happened in a specific interaction.
2. People: what each person repeatedly does across events.
3. Relationships: how two or more people interact, with direction and type.
4. Network patterns: what stable structure appears across the group.

Never jump directly from one message or one incident to a personality label.

## Target Skill Naming

When creating the generated map skill, choose the target skill name as follows:

1. If the user specifies a target skill name, use it.
2. If the user specifies a group or organization name, generate `<group-name>-map`.
3. If no name is specified, use `org-map`.

Examples:

- group name: `金點子王` → target skill name: `金點子王-map`
- group name: `sales-team` → target skill name: `sales-team-map`
- no specified name → target skill name: `org-map`

If the runtime requires ASCII or kebab-case names, use an ASCII folder name but preserve the display name inside the generated `SKILL.md`.

## Generated Skill Directory

When file operations are available, create this structure:

```text
<target-skill-name>/
  SKILL.md
  references/
    events.md
    people.md
    relationships.md
    graph-summary.md
    open-questions.md
    risks.md
```

If file operations are not available, output the full contents for each file in separate fenced code blocks.

## Load References

Read only the files needed for the task:

* `references/relationship-taxonomy.md`: use before classifying power, trust, conflict, dependency, information, decision, emotion, responsibility, alliance, avoidance, mentorship, gatekeeping, brokerage, network positions, or higher-order relations.
* `references/inference-rules.md`: use before making person, motive, role, power, conflict, trust, or responsibility inferences.
* `references/confidence-levels.md`: use whenever assigning confidence, handling contradictory evidence, or deciding whether to downgrade a conclusion into an open question.

Use `templates/` when writing generated reference artifacts.

## Required Generated Artifacts

For the target map skill, produce or maintain:

* `references/events.md`
* `references/people.md`
* `references/relationships.md`
* `references/graph-summary.md`
* `references/open-questions.md`
* `references/risks.md`

If evidence is weak, produce partial artifacts and mark confidence honestly. Missing data should become open questions, not invented conclusions.

## Workflow

### 1. Determine Target

Identify:

* target group or organization name
* target skill name
* output directory
* source type
* time range
* participants
* aliases
* language
* channel
* completeness
* privacy constraints
* missing context

Do not assume the dataset is complete.

If the user did not specify the target skill name, use `<group-name>-map` when a group name is available. Otherwise use `org-map`.

### 2. Extract Entities and Events

Extract people, possible aliases, formal roles, observed roles, and interaction episodes. Convert raw text into event records before making relationship or person claims.

Each event should capture:

* trigger
* sequence
* decision or non-decision
* responsibility movement
* emotional or social signals
* outcome
* evidence pointer
* candidate interpretations
* confidence

Use `templates/events.md` when writing `references/events.md`.

### 3. Classify Relationships

Infer relationships only from repeated events or strong direct evidence. Relationships must be directional, typed, evidence-linked, and confidence-scored.

A pair can have multiple relationship types at once. For example, A may trust B technically while shifting ambiguous responsibility to B operationally.

Use `references/relationship-taxonomy.md`, `references/inference-rules.md`, and `templates/relationships.md`.

Write the result to `references/relationships.md`.

### 4. Build Person Profiles

Build people profiles from repeated patterns, not from isolated impressions. Separate facts, formal role, observed role, network position, behavior patterns, communication style, work style, decision behavior, reputation in the data, inferred motive, uncertainty, and evidence gaps.

Avoid stable personality labels unless supported by multiple events and still phrase them as observed patterns.

Use `references/inference-rules.md`, `references/confidence-levels.md`, and `templates/people.md`.

Write the result to `references/people.md`.

### 5. Synthesize the Graph

Summarize the group as a network. Include formal vs informal structure, knowledge hubs, bottlenecks, boundary spanners, hidden decision makers, emotional centers, conflict sources, responsibility gaps, bypass routes, fragile single points of failure, and what cannot be concluded.

Use `references/relationship-taxonomy.md` and `templates/graph-summary.md`.

Write the result to `references/graph-summary.md`.

### 6. Check Contradictions and Risks

Check for conflicting evidence, alternative explanations, low-confidence claims, privacy risk, defamation risk, power asymmetry, confirmation bias, missing offline context, and weaponization risk.

Use `references/inference-rules.md`, `references/confidence-levels.md`, and `templates/risks.md`.

Write the result to `references/risks.md`.

### 7. Create Open Questions

Open questions should be actionable:

* ask whom
* ask what
* why it matters
* what evidence would confirm it
* what evidence would disconfirm it
* what artifact would change if answered

Use `templates/open-questions.md`.

Write the result to `references/open-questions.md`.

### 8. Generate the Map Skill

After the six reference artifacts are created, generate `<target-skill-name>/SKILL.md`.

The generated `SKILL.md` must:

1. State that it is a map skill for the target group.
2. Give a concise high-density summary of the group’s known structure.
3. Strongly instruct future agents to read the six reference files before making claims.
4. Explain when each reference should be read.
5. Preserve evidence-first reasoning rules.
6. Avoid psychological diagnosis and unsupported motive claims.
7. Tell future agents to answer from the map, not from vague memory.

The generated `SKILL.md` should not reproduce the entire six artifacts. It should summarize the map efficiently and route future reasoning into the reference files.

## Generated SKILL.md Requirements

The generated map skill must include these sections:

```text
---
name: <target-skill-name>
description: "<short trigger description>"
---

# <Display Name>

## What This Skill Is

## Fast Map Summary

## Mandatory Reference Loading

## How To Use The References

## Reasoning Rules

## Answering Rules

## Update Rules

## Boundaries
```

### Fast Map Summary

This section should summarize the current group map in a compact way:

* group identity
* data coverage
* main people
* rough formal structure
* rough informal structure
* main power routes
* main information routes
* main responsibility routes
* known bottlenecks
* known conflict or risk zones
* strongest open questions

This summary should be short enough to quickly activate context, but it must point to reference files for evidence.

### Mandatory Reference Loading

The generated skill must strongly encourage reference loading.

Use language like:

```text
Before answering any non-trivial question about this group, read the relevant files in `references/`.

For claims about what happened, read `references/events.md`.
For claims about a person, read `references/people.md`.
For claims about a relationship, read `references/relationships.md`.
For claims about the whole group structure, read `references/graph-summary.md`.
For uncertain or unresolved issues, read `references/open-questions.md`.
For sensitive or risky claims, read `references/risks.md`.

Do not rely only on this SKILL.md summary when making specific claims.
```

### How To Use The References

The generated skill must route future agents like this:

* `events.md`: source of truth for evidence.
* `people.md`: use for person profiles, but verify sensitive claims against events.
* `relationships.md`: use for directed relationship claims.
* `graph-summary.md`: use for whole-system interpretation.
* `open-questions.md`: use when evidence is missing or the user asks what to investigate next.
* `risks.md`: use before making negative, sensitive, or weaponizable claims.

## Incremental Merge

When new data arrives:

1. Append new events first.
2. Update people only if new event evidence changes the pattern.
3. Update relationships only with event support.
4. Update graph summary after people and relationships.
5. Update risks and open questions.
6. Preserve older conclusions unless new evidence contradicts them.
7. Record contradictions explicitly and never silently overwrite prior interpretations.
8. Update the generated `SKILL.md` fast map summary only after the six references are updated.

## Confidence Labels

Use exactly these labels:

* High: repeated evidence across multiple events or independent sources.
* Medium: multiple hints but limited source diversity or incomplete context.
* Low: plausible but weak, partial, or based on few observations.
* Unknown: not enough evidence to infer.

Never present low-confidence inference as fact. Promote strong claims only when supported by event IDs and alternative explanations have been considered.

## Output Constraints

Write evidence-first and keep interpretation separate from evidence.

Prefer:

* "In the available events, A repeatedly..."
* "This may indicate..."
* "Alternative explanation..."
* "Needs confirmation..."
* event IDs and source pointers
* tables for people and relationships

Do not write:

* "A is a bad person"
* "B has narcissistic personality"
* "C definitely manipulates everyone"
* "D is loyal/disloyal" without evidence
* private psychological diagnosis
* claims about motive without event support
* hidden relationship claims without source evidence

## Minimum Quality Bar

Before finalizing, verify:

* The target skill name is set.
* The target skill directory exists or is fully output.
* `SKILL.md` exists.
* `references/events.md` exists.
* `references/people.md` exists.
* `references/relationships.md` exists.
* `references/graph-summary.md` exists.
* `references/open-questions.md` exists.
* `references/risks.md` exists.
* Events exist before people and relationship claims.
* Every relationship has direction, type, evidence, confidence, and alternatives.
* Every negative person inference has an alternative explanation or is downgraded.
* Formal role, observed role, behavior, reputation, motive, and network position are not conflated.
* Claims about power, trust, conflict, emotion, and responsibility cite events.
* Missing context is visible in `references/open-questions.md`.
* Risks are explicit when the output could be used against real people.
* The generated `SKILL.md` strongly routes future agents to the six reference artifacts.
