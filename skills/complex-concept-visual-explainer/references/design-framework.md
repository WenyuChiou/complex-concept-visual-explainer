# Generic visual design framework

Use this reference to convert a complex system into a small, auditable visual
story. Keep domain-specific vocabulary and scientific claims in a domain
adapter; keep the role grammar and layout rules here.

## Story spine

Start from the causal sequence:

```text
context -> process or environment -> component -> observation/state
-> decision mechanism -> structured action -> interface
-> deterministic transformation -> downstream consequence -> feedback
```

State one speaker sentence for every asset. A figure should answer one primary
question, not summarize an entire project. Split a crowded story into a
connected family only when the audience must move between scales.

## Role taxonomy

Classify nodes before selecting a visual form. Do not infer role from an icon.

| Role | Required question | Typical visual boundary |
|---|---|---|
| Context / source | Where does the process happen or where does knowledge originate? | context field or source card |
| Observation / state | What enters the focal component? | input card or state node |
| Agent | Which software decision-maker owns the policy and action? | outer agent boundary with an explicit agent label |
| Decision mechanism | How does the agent choose an action? | sibling policy cards inside the agent |
| Action / contract | What structured value crosses the interface? | action card or shared contract |
| Interface | How does another component call or receive the action? | boundary gate or interface card |
| Knowledge support | Which documents, data, or retrieved evidence inform a decision? | dashed external knowledge group |
| Validator / constraint | Which rule or bound checks the proposal? | red gate or shield |
| Deterministic model | Which physical or system transformation remains outside policy? | teal model boundary |
| Outcome / feedback | What is produced downstream or returned at the next step? | output card and feedback arrow |

Use explicit labels when roles can be confused. For example, label a reservoir
decision callback as `Reservoir Decision Interface` and annotate `Dam API` as
`Interface, not an agent` when the audience might read the API as a component
that makes decisions.

## Status taxonomy

Keep implementation status separate from semantic role:

| Status | Meaning | Recommended treatment |
|---|---|---|
| Existing | Present in the original system | solid boundary, neutral color, `Existing` badge |
| MVP | Added and testable in the current integration | colored boundary, `MVP` badge |
| Future extension | Designed but not implemented or not selected | dashed boundary, `Future extension` badge |
| Optional | Available only for selected deployments | dashed connector and explicit note |

Use shape, line style, and labels in addition to color so the visual remains
interpretable in grayscale.

## Layout patterns

Choose the smallest pattern that answers the speaker sentence.

### Overview

Show system boundary, hierarchy, focal component, upstream cause, downstream
consequence, and the next feedback point. Use when the audience first needs
context before a technical seam.

### Decision comparison

Use two separated lanes when comparing an existing implementation with a new
decision mechanism:

```text
upper lane: Existing decision path
lower lane: New or replacement decision path
left: shared observation
right: shared action interface and deterministic model
```

Give sibling alternatives equal visual status. Do not nest the old policy
inside the new policy or show both as simultaneously active unless the model
actually runs both.

### Decision zoom

Show shared observation/state, sibling decision mechanisms, shared action
contract, validation, and the deterministic consumer. Use when the audience
already understands the system context.

### Cascade

Show repeated components connected by causal arrows. Label an upstream output
and downstream input when an interface or routing step changes meaning.

### Implementation seam

Show the stable interface, replaceable policy, validation, fallback, audit log,
and unchanged simulator. Use for engineering discussions about integration.

### Density and pipeline layout

Do not compress a long sequential chain into a narrow horizontal strip. When a
shared action is followed by three or more downstream stages, allocate a
dedicated pipeline band, a second row, or a separate implementation-seam
figure. Give each stage a readable card width, internal padding, and visible
gaps; preserve the causal order with orthogonal, non-crossing arrows. Keep
downstream outcome cards in a separate right-side column when they would
otherwise compete for space with the pipeline. If the labels only remain
legible by shrinking type, change the layout rather than shrinking the text.

### Directional continuity and convergence

Choose one primary reading direction before routing arrows. When sibling
decision branches produce a shared action, place that action at an explicit
convergence point before the downstream chain. Connect each branch directly to
the convergence point; do not route a branch through another branch or panel,
and do not land a branch arrow in the middle of a later stage. Continue the
downstream chain in the same direction. If a turn is necessary, use one
deliberate clockwise or counter-clockwise orthogonal turn rather than several
competing reading paths.

## External knowledge and RAG

Represent document grounding as a knowledge-support path:

```text
operating document -> retriever -> policy context -> intended decision branch
```

Keep the path outside the agent boundary unless retrieval is explicitly part
of the agent implementation. Connect it only to the LLM-driven branch when
comparing rule-based and LLM-driven alternatives. Treat a document as an
external source, an embedding as a retrieval representation, and retrieved
text as context; never imply that RAG writes the document into model weights.

If a dynamic observation is used as a retrieval query, draw a dashed query or
coupling arrow to the retriever, not to the source document. Omit that arrow
in a professor-facing figure when it creates visual ambiguity; record the
query behavior in the technical label map instead.

## Arrow and color semantics

| Mark | Meaning |
|---|---|
| Thick solid arrow | material, state, or causal system movement |
| Thin solid arrow | ordinary process sequence |
| Dashed arrow | observation, feedback, coupling, query, or zoom relation |
| Bounded gate | validation, constraint, approval, or safety check |

| Role | Color |
|---|---|
| Observation, natural flow, or data movement | Blue |
| Deterministic transformation or model | Teal |
| Agent, policy, or LLM-driven mechanism | Purple |
| Action or intervention | Orange |
| Validation, risk, or constraint | Red |
| Existing neutral path | Gray |

Never use color as the only carrier of meaning.

## Icon and label discipline

- Use icons only as secondary cues; keep the exact text label primary.
- Use one consistent icon family across a visual family.
- Avoid icons that imply agency for interfaces, models, retrievers, or
  validators.
- Keep labels short, exact, and readable at slide scale.
- Use plain-language labels for general audiences.
- Use only domain-adapter-whitelisted identifiers in technical figures.
- Do not add function calls, equations, JSON braces, array notation, or code
  glyphs merely to make a figure look technical.

## Semantic quality checklist

Before accepting a visual, verify:

1. Can the reader identify the actual agent without relying on color or icon?
2. Are policy mechanisms siblings rather than parent and child?
3. Is the interface visibly different from the agent and the model?
4. Are input, state, decision, action, output, and feedback distinct?
5. Does every arrow have one direction and one interpretable meaning?
6. Are existing, MVP, and future elements visibly distinguished?
7. Does any RAG path enter only the intended decision mechanism?
8. Does the deterministic model remain outside the policy boundary?
9. Can the shared interface support the alternative policy implementation?
10. If three or more stages follow the shared action, are they given a
    dedicated band or second row instead of a compressed strip?
11. Do sibling branches converge before the downstream chain, with one obvious
    primary reading direction and no branch arrow entering a later stage?
12. Does the figure avoid claims stronger than the domain sources support?

## Handoff record

Store a compact record with every project-bound figure:

- speaker intent;
- audience level;
- content map;
- exact visible label map;
- alt text describing the causal relationship;
- existing/MVP/future status map;
- domain assumptions and non-claims;
- semantic and visual QA result;
- source image provenance when generated by an image tool.
