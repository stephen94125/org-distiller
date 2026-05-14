---
name: org-map-distiller
description: "Distill small-group or organization communication records into evidence-backed events, people profiles, relationship maps, graph summaries, risks, and open questions. Use when analyzing LINE chats, email, meeting notes, interviews, observation notes, documents, or recurring team records to understand roles, power, trust, conflict, dependency, information flow, decision flow, responsibility flow, informal organization, and stable interaction patterns without jumping to unsupported personality judgments."
---

# Organization Relationship Map

Analyze human small-group records as an interaction system, not as gossip or one-person persona extraction. Use events as the evidence unit, then derive people profiles, directed relationships, network patterns, risks, and actionable open questions.

This skill is useful for company teams, family businesses, departments, labs, communities, and recurring working groups. It is not for psychological diagnosis, defamatory claims, loyalty tests, surveillance, or contacting people.

## Core Rule

Always separate four layers:

1. Events: what happened in a specific interaction.
2. People: what each person repeatedly does across events.
3. Relationships: how two or more people interact, with direction and type.
4. Network patterns: what stable structure appears across the group.

Never jump directly from one message or one incident to a personality label.

## Load References

Read only the files needed for the task:

- `references/relationship-taxonomy.md`: use before classifying power, trust, conflict, dependency, information, decision, emotion, responsibility, alliance, avoidance, mentorship, gatekeeping, brokerage, network positions, or higher-order relations.
- `references/inference-rules.md`: use before making person, motive, role, power, conflict, trust, or responsibility inferences.
- `references/confidence-levels.md`: use whenever assigning confidence, handling contradictory evidence, or deciding whether to downgrade a conclusion into an open question.

Use `templates/` when writing final artifacts.

## Required Artifacts

When enough source material exists, produce or maintain:

- `events.md`
- `people.md`
- `relationships.md`
- `graph-summary.md`
- `open-questions.md`
- `risks.md`

If evidence is weak, produce partial artifacts and mark confidence honestly. Missing data should become open questions, not invented conclusions.

## Workflow

### 1. Intake and Boundaries

Identify source type, time range, participants, aliases, language, channel, completeness, privacy constraints, and missing context. Distinguish real names from aliases. Do not assume the dataset is complete.

### 2. Extract Entities and Events

Extract people, possible aliases, formal roles, observed roles, and interaction episodes. Convert raw text into event records before making relationship or person claims.

Each event should capture trigger, sequence, decision or non-decision, responsibility movement, emotional or social signals, outcome, evidence pointer, candidate interpretations, and confidence.

Use `templates/events.md` when writing `events.md`.

### 3. Classify Relationships

Infer relationships only from repeated events or strong direct evidence. Relationships must be directional, typed, evidence-linked, and confidence-scored.

A pair can have multiple relationship types at once. For example, A may trust B technically while shifting ambiguous responsibility to B operationally.

Use `references/relationship-taxonomy.md`, `references/inference-rules.md`, and `templates/relationships.md`.

### 4. Build Person Profiles

Build people profiles from repeated patterns, not from isolated impressions. Separate facts, formal role, observed role, network position, behavior patterns, communication style, work style, decision behavior, reputation in the data, inferred motive, uncertainty, and evidence gaps.

Avoid stable personality labels unless supported by multiple events and still phrase them as observed patterns.

Use `references/inference-rules.md`, `references/confidence-levels.md`, and `templates/people.md`.

### 5. Synthesize the Graph

Summarize the group as a network. Include formal vs informal structure, knowledge hubs, bottlenecks, boundary spanners, hidden decision makers, emotional centers, conflict sources, responsibility gaps, bypass routes, fragile single points of failure, and what cannot be concluded.

Use `references/relationship-taxonomy.md` and `templates/graph-summary.md`.

### 6. Check Contradictions and Risks

Check for conflicting evidence, alternative explanations, low-confidence claims, privacy risk, defamation risk, power asymmetry, confirmation bias, missing offline context, and weaponization risk.

Use `references/inference-rules.md`, `references/confidence-levels.md`, and `templates/risks.md`.

### 7. Create Open Questions

Open questions should be actionable:

- ask whom
- ask what
- why it matters
- what evidence would confirm it
- what evidence would disconfirm it
- what artifact would change if answered

Use `templates/open-questions.md`.

### 8. Incremental Merge

When new data arrives, append new events first, then update people, relationships, graph summary, risks, and open questions. Preserve older conclusions unless new evidence contradicts them. Record contradictions explicitly and never silently overwrite prior interpretations.

## Confidence Labels

Use exactly these labels:

- High: repeated evidence across multiple events or independent sources.
- Medium: multiple hints but limited source diversity or incomplete context.
- Low: plausible but weak, partial, or based on few observations.
- Unknown: not enough evidence to infer.

Never present low-confidence inference as fact. Promote strong claims only when supported by event IDs and alternative explanations have been considered.

## Output Constraints

Write evidence-first and keep interpretation separate from evidence.

Prefer:

- "In the available events, A repeatedly..."
- "This may indicate..."
- "Alternative explanation..."
- "Needs confirmation..."
- event IDs and source pointers
- tables for people and relationships

Do not write:

- "A is a bad person"
- "B has narcissistic personality"
- "C definitely manipulates everyone"
- "D is loyal/disloyal" without evidence
- private psychological diagnosis
- claims about motive without event support
- hidden relationship claims without source evidence

## Minimum Quality Bar

Before finalizing, verify:

- Events exist before people and relationship claims.
- Every relationship has direction, type, evidence, confidence, and alternatives.
- Every negative person inference has an alternative explanation or is downgraded.
- Formal role, observed role, behavior, reputation, motive, and network position are not conflated.
- Claims about power, trust, conflict, emotion, and responsibility cite events.
- Missing context is visible in `open-questions.md`.
- Risks are explicit when the output could be used against real people.
