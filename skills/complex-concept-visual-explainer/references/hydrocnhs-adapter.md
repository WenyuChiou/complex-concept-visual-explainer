# HydroCNHS domain adapter

Use this adapter with `complex-concept-visual-explainer` for the HydroCNHS
watershed and reservoir feasibility case.

## Framework role

HydroCNHS is a research and educational hydrological modeling framework. In
this work it is used with a small synthetic configuration as a feasibility demo
for integrating an LLM into a reservoir policy. The synthetic case does not
mean the framework itself is only a demo model.

## Natural-system pathway

Use this physical story:

```text
climate or rainfall forcing -> rainfall-runoff -> subbasins and tributaries
-> river routing -> reservoir storage and control -> downstream flow
```

The large watershed can be divided into smaller catchments with multiple
reservoirs. After routing, an upstream reservoir output becomes the input to a
downstream reservoir. Local tributary inflow may enter between reservoirs.

Avoid claims of fully distributed routing, real-time operational control, or
deployment unless the selected configuration and documentation support them.

## Agent and decision layers

Examples include:

- **Dam Agent / Reservoir Agent:** the ABM software decision-maker that owns a
  reservoir observation, policy, and release action.
- **River-diversion agent:** changes water withdrawn from a river.
- **Urban-water agent:** represents urban demand or use.

Not every agent is an LLM. For the reservoir integration, rule-based and
LLM-driven decisions are alternative mechanisms used by the Dam Agent. They are
not parent and child agents and should not be shown as simultaneously active
unless the experiment explicitly runs both.

For a comparison visual, use two separated lanes:

```text
upper lane: Existing Rule-based Dam Agent
lower lane: LLM-driven Dam Agent integration path
shared right side: Reservoir Decision Interface -> HydroCNHS routing
```

Mark the actual agent boundary with `ABM AGENT`. Label decision mechanisms
inside that boundary as `Rule-based Decision` and `LLM-driven Decision`.

## Reservoir interface seam

The existing Dam interface is an in-process Python callback, not automatically
a REST service. Use `Reservoir Decision Interface` as the plain-language visual
label and retain `Dam API` only as a technical alias when the audience needs
repository terminology. Neither label denotes an agent.

At the conceptual level, use:

```text
upstream water flow -> Dam Agent decision -> reservoir decision interface
-> release amount -> reservoir outlet -> downstream routing -> downstream flow
```

For a professor-facing engineering visual, the following identifiers may be
used when they are needed to explain the contract: `release_cms`, `Dam API`,
and `Gemma 4:12B`. Do not put function calls, time-indexed arrays, or JSON
syntax in a general explanatory visual.

The LLM integration replaces only the policy implementation behind the
interface. The outer Dam Agent remains the ABM component:

```text
Dam Agent -> typed observation -> LLM-driven decision -> structured action
-> deterministic validator -> bounded release amount
```

HydroCNHS retains state transition, water balance, pseudo-outlet insertion, and
routing. Include fallback, replay, and audit logging when the audience needs
implementation detail.

## External policy knowledge and RAG

Treat an operating manual as an external knowledge source, not as an agent or
as model training data. Use this visual path:

```text
operating manual -> RAG retriever -> policy context -> LLM-driven decision
```

Keep the path in the LLM integration lane. Mark it as a future extension when
retrieval is not implemented. If a dynamic reservoir observation selects the
retrieved rule, describe that behavior in the technical record; omit the query
arrow from a professor-facing figure when it makes the diagram ambiguous.

The feasibility contract supports context injection and a fixed release action,
but it does not by itself prove that a manual has been retrieved or that all
manual conditions are enforced. Do not depict RAG as a replacement for
deterministic operating-rule validation.

## Recommended wording

Prefer:

- `Dam Agent / Reservoir Agent`
- `LLM replaces the reservoir policy`
- `same interface; different decision mechanism`
- `Reservoir Decision Interface`
- `HydroCNHS retains water balance and routing`
- `synthetic feasibility case`
- `in-process API callback`

Avoid:

- `LLM replaces HydroCNHS`
- `LLM performs routing`
- `Dam API` as the name of an agent
- `REST API` unless a network service is actually implemented
- `every agent is an LLM`
- `fully distributed routing` without configuration-level evidence
- `RAG controls release directly` without a deterministic guard

## Asset and acceptance plan

For the professor-facing comparison, prefer one wide two-lane figure:

```text
upper: Existing Rule-based Dam Agent
lower: LLM-driven Dam Agent with optional RAG and validator
right: shared Reservoir Decision Interface -> HydroCNHS Routing
```

Verify the following before accepting the figure:

- [ ] Domain terms and units are correct.
- [ ] Every input/output arrow has the correct direction.
- [ ] `Dam Agent / Reservoir Agent` is visibly distinct from `Dam API`.
- [ ] Rule-based and LLM-driven decisions are separate alternatives.
- [ ] RAG is shown as knowledge support and only enters the LLM lane.
- [ ] Existing, MVP, and future extension status are explicit.
- [ ] The action schema is structured and testable.
- [ ] Constraints, validation, and fallback are visible where required.
- [ ] The figure does not imply that the LLM performs routing.
- [ ] A domain expert has reviewed the final wording.

## References

Use these primary project sources when a visual makes implementation-specific
claims. The links below are pinned to HydroCNHS integration commit
`d7484fadda609a314528f6d6ab8c5e4e9a4b0c73`; the upstream repository remains
the authoritative source for framework behavior.

- Framework scope and the four integration APIs: [`README.md`](https://github.com/WenyuChiou/HydroCNHS/blob/d7484fadda609a314528f6d6ab8c5e4e9a4b0c73/README.md#supporting-apis-for-incorporating-humanagent-components)
- ABM agent base and configuration concepts: [`src/hydrocnhs/abm.py`](https://github.com/WenyuChiou/HydroCNHS/blob/d7484fadda609a314528f6d6ab8c5e4e9a4b0c73/src/hydrocnhs/abm.py#L55-L63)
- Agent initialization: [`src/hydrocnhs/hydrocnhs.py`](https://github.com/WenyuChiou/HydroCNHS/blob/d7484fadda609a314528f6d6ab8c5e4e9a4b0c73/src/hydrocnhs/hydrocnhs.py#L208-L385)
- Dam action callback and routing update: [`src/hydrocnhs/hydrocnhs.py`](https://github.com/WenyuChiou/HydroCNHS/blob/d7484fadda609a314528f6d6ab8c5e4e9a4b0c73/src/hydrocnhs/hydrocnhs.py#L789-L815)
- Routing configuration and upstream outlet relationships: [`src/hydrocnhs/model_builder.py`](https://github.com/WenyuChiou/HydroCNHS/blob/d7484fadda609a314528f6d6ab8c5e4e9a4b0c73/src/hydrocnhs/model_builder.py#L196-L216)
- Fixed observation/action contract and mock evidence: [`llm_integration_review/`](https://github.com/WenyuChiou/HydroCNHS/tree/codex/llm-reservoir-agent/llm_integration_review)

The external visual skill is generic; these links are a domain adapter, not a
claim that every HydroCNHS configuration has the same topology or agent set.
The `llm_integration_review` link is a mutable development-branch evidence
link, not a pinned release reference.
