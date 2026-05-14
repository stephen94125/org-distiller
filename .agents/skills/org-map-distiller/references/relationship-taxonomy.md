# Relationship Taxonomy

Use directional relationships wherever possible: `A -> B`. If the relation is reciprocal, record both directions or explicitly mark reciprocity.

## Core Relationship Types

| Type | Definition | Observable evidence | Common false inference | Useful sources |
|---|---|---|---|---|
| Power / authority | A can direct, approve, veto, evaluate, or constrain B | commands, approvals, escalations, compliance, vetoes, resource control | assuming formal title equals real influence | org chart, chat, email, meeting notes, interviews |
| Trust | A relies on B, shares sensitive information, or consults B before action | consultation, delegation of important work, early information sharing, reliance in uncertainty | mistaking frequent contact for trust | chat, email, interviews, advice network |
| Conflict | A and B show disagreement, opposition, avoidance, status contest, or resource tension | objections, delays, blame, repeated escalation, side channels, refusal, repair attempts | calling all disagreement personal conflict | meetings, chat, incident logs, interviews |
| Dependency | A needs B for completion, information, permission, expertise, emotional support, or political cover | repeated requests, blockers, handoffs, approval dependency, rescue behavior | treating dependency as weakness | workflow records, chat, project logs |
| Information flow | A sends, withholds, filters, translates, or routes information to B | FYI patterns, summaries, forwarding, delayed disclosure, gatekeeping | assuming sender understands or endorses content | email, chat, documents |
| Decision flow | A proposes, B approves, C vetoes, D executes, or no one decides | decision statements, approvals, deferrals, ambiguous ownership | mistaking execution for authority | meeting notes, approvals, chat |
| Emotional support | A calms, reassures, validates, or protects B emotionally | reassurance, mediation, empathy, repair, de-escalation | overreading politeness as support | chat, observation, interviews |
| Emotional burden | A repeatedly absorbs B's anxiety, anger, ambiguity, face-saving, or blame | pressure messages, reassurance demands, emotional cleanup, conflict mediation | pathologizing normal teamwork | chat, interviews, observation |
| Responsibility shifting | A moves ambiguous, risky, or unrewarded work to B without clear authority or support | vague delegation, non-decisions, post-failure blame, unclear ownership transfer | confusing normal delegation with dumping | incidents, chat, meetings |
| Collaboration | A and B jointly coordinate work with mutual information and shared ownership | joint plans, mutual updates, shared decisions, peer repair | calling sequential handoff collaboration | project logs, chat |
| Informal alliance | A and B coordinate outside formal channels or support each other in group decisions | side-channel alignment, mutual defense, repeated co-voting, shared framing | inventing factions from two incidents | chat, interviews, meetings |
| Avoidance / bypass | A avoids B, routes around B, or uses alternate channels to reduce friction or delay | missing direct contact, repeated intermediaries, backchannel escalation | assuming malicious intent for all routing | communication traces, interviews |
| Mentorship / sponsorship | A advises, develops, protects, or promotes B | coaching, recommendation, advocacy, skill transfer, career support | mistaking friendliness for sponsorship | interviews, chat, performance context |
| Gatekeeping / brokerage | A controls access to people, information, decisions, or resources between groups | routing control, introductions, translation, selective forwarding, approval chokepoints | equating all brokers with blockers | network data, chat, org context |

## Network Positions

Use these as structural labels, not personality labels:

- Knowledge hub: receives and answers many information requests.
- Bottleneck: many flows require this person and slow down when they are absent.
- Broker: bridges otherwise disconnected people or groups.
- Boundary spanner: connects different departments, communities, or role worlds.
- Coordinator: aligns tasks, timing, responsibilities, and dependencies.
- Decision node: proposals or disputes converge here for approval or veto.
- Peripheral actor: appears rarely or only through intermediaries.
- Emotional center: many affective signals, reassurance, complaints, or conflict repairs route here.
- Conflict source: repeated events show conflict starts, escalates, or becomes unresolved around this person.
- Responsibility sink: ambiguous or unrewarded work repeatedly lands here.

## Higher-Order Relations

Some patterns are not pairwise:

- Triads: A routes through B to influence C.
- Coalitions: A and B repeatedly align against or around C.
- Cliques: a subgroup repeatedly communicates internally more than with others.
- Factions: stable subgroups compete over resources, direction, recognition, or status.
- Hyperedges: one event binds multiple participants into one decision, conflict, or responsibility movement.

Record higher-order relations in `graph-summary.md` and cite the events that connect the participants.
