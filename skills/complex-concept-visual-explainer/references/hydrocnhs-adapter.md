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

## Agent layer

Examples include:

- **Dam agent:** controls a reservoir release.
- **River-diversion agent:** changes water withdrawn from a river.
- **Urban-water agent:** represents urban demand or use.

An agent is a software decision-maker with observations, a policy, and an
action. Not every agent is an LLM. Rule-based and LLM-driven agents are sibling
alternatives, not parent and child components.

## Reservoir interface seam

The existing Dam interface is an in-process Python callback, not automatically
a REST service. At the conceptual level it is:

```text
upstream water flow -> reservoir decision interface -> release amount
-> reservoir outlet -> downstream routing -> downstream flow
```

For a professor-facing engineering visual, the following identifiers may be
used when they are needed to explain the contract: `release_cms`, `Dam API`,
and `Gemma 4:12B`. Do not put function calls, time-indexed arrays, or JSON
syntax in a general explanatory visual.

The LLM integration replaces only the policy implementation behind the
interface:

```text
typed observation -> Gemma 4:12B policy -> structured action
-> deterministic validator -> bounded release amount
```

HydroCNHS retains state transition, water balance, pseudo-outlet insertion, and
routing. Include fallback, replay, and audit logging when the audience needs
implementation detail.

## Recommended wording

Prefer:

- `LLM replaces the reservoir policy`
- `HydroCNHS retains water balance and routing`
- `synthetic feasibility case`
- `in-process API callback`
- `same interface; different decision mechanism`

Avoid:

- `LLM replaces HydroCNHS`
- `LLM performs routing`
- `REST API` unless a network service is actually implemented
- `every agent is an LLM`
- `fully distributed routing` without configuration-level evidence

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
- This feasibility case's fixed observation/action contract and mock evidence: [`llm_integration_review/`](https://github.com/WenyuChiou/HydroCNHS/tree/d7484fadda609a314528f6d6ab8c5e4e9a4b0c73/llm_integration_review)

The external visual skill is generic; these links are a domain adapter, not a
claim that every HydroCNHS configuration has the same topology or agent set.
