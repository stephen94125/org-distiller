# Confidence Levels

Use exactly these labels across all artifacts.

## Labels

| Label | Meaning | Typical evidence |
|---|---|---|
| High | Repeated evidence across multiple events or independent sources | several events, different channels, corroborating interview or observation |
| Medium | Multiple hints but limited source diversity or incomplete context | repeated messages in one channel, two related incidents, one strong source plus partial support |
| Low | Plausible but weak, partial, ambiguous, or based on few observations | one incident, indirect evidence, unclear participant intent |
| Unknown | Not enough evidence to infer | missing data, conflicting evidence, no event support |

## Upgrade Criteria

Raise confidence only when:

- event count increases
- source diversity improves
- alternative explanations become less plausible
- the same pattern appears across time or contexts
- direct evidence replaces indirect evidence

## Downgrade Criteria

Lower confidence when:

- data comes from one person or one channel
- the event is ambiguous
- the claim depends on tone or inferred motive
- offline context is likely missing
- evidence is stale
- contradictory evidence appears
- the claim could harm a real person if wrong

## Required Phrasing

High:

- "Across E003, E011, and E014..."
- "The available evidence consistently shows..."

Medium:

- "The pattern appears in multiple events, but source diversity is limited..."
- "This may indicate..."

Low:

- "A plausible interpretation is..."
- "This should be treated as a hypothesis..."

Unknown:

- "The available evidence does not support a conclusion..."
- "This should remain an open question..."

## False Precision Guardrail

Do not use numeric scores unless the dataset includes enough structured data to justify them. Prefer qualitative labels and event IDs. If network metrics are available, state the data source and sampling limits.
