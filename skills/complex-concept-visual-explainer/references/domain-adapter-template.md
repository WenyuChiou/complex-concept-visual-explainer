# Domain adapter template

Use this file to define a new domain without changing the generic visual core.
The adapter carries domain vocabulary, units, model boundaries, and claims that
require expert review.

## Adapter identity

- **Domain name:**
- **Audience:**
- **Primary use case:**
- **Reference sources:**
- **Domain expert reviewer:**

## System definition

- **System boundary:** What is inside the model or process?
- **External context:** What influences it from outside?
- **Hierarchy:** What contains what? List the large context, nested units, and
  focal component.
- **Time or sequence:** What is the time step, event order, or interaction loop?

## Content map

| Generic field | Domain-specific definition | Preferred visible label |
|---|---|---|
| Context |  |  |
| Input / observation |  |  |
| State |  |  |
| Decision mechanism |  |  |
| Action contract |  |  |
| System transformation |  |  |
| Output |  |  |
| Feedback |  |  |
| Constraint / validation |  |  |

## Decision alternatives

Keep these branches as siblings when both are in scope:

```text
Rule-based agent: observation -> explicit rule set -> action
LLM-driven agent: prompt + observation -> reasoning -> structured action
```

- **Rule source:**
- **Prompt source:**
- **Shared action schema:**
- **Validation:**
- **Fallback:**
- **Audit / provenance:**

## Label policy

- **General labels:** plain-language labels with no equations, function calls,
  array notation, JSON braces, or unexplained code glyphs.
- **Technical whitelist:** identifiers that may appear in a professor-facing
  figure and why each is necessary.
- **Forbidden visible labels:**

## Domain vocabulary

List entities, variables and units, state names, action verbs, model/API names,
and synonyms to avoid.

## Non-claims and hazards

List interpretations the diagram must not imply. At minimum consider:

- a policy is not the physical or deterministic state-transition model;
- an LLM proposal is not evidence that the system obeys a natural-language law;
- a callback or function interface is not automatically a network REST API;
- a demonstration configuration is not evidence of general validity.

## Asset plan

| Asset role | Primary question | Required entities and labels |
|---|---|---|
| Overview |  |  |
| Decision zoom |  |  |
| Cascade / consequence |  |  |
| Implementation seam |  |  |

## Acceptance tests

- [ ] Domain terms and units are correct.
- [ ] Every input/output arrow has the correct direction.
- [ ] The focal decision is inside the declared system boundary.
- [ ] Rule-based and LLM-driven alternatives are not conflated.
- [ ] The action schema is structured and testable.
- [ ] Constraints, validation, and fallback are visible where required.
- [ ] The figure does not make a stronger claim than the reference sources.
- [ ] A domain expert has reviewed the final wording.
