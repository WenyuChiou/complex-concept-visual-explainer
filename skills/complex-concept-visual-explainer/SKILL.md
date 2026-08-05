---
name: complex-concept-visual-explainer
description: This skill should be used when the user asks to "explain a complex system visually", "create a workflow diagram", "compare rule-based and LLM-driven decisions", "design a presentation visual", or requests an overview-to-zoom diagram, infographic, or architecture visual for hydrology, urban water, consumer behavior, or another coupled system.
compatibility: Requires Codex built-in image generation, local image inspection, and filesystem access. Use project-local assets and Markdown documentation; no external network is required.
version: 0.2.0
---

# Complex Concept Visual Explainer

Use this skill to turn a complex idea into a small, coherent visual story that
a non-specialist can follow. The output is an auditable mapping from context to
observation, decision, action, system consequence, and feedback - not a
decorative collection of unrelated images.

## Semantic-first workflow

Treat visual design as a compilation pipeline rather than a style exercise:

```text
message -> concept map -> role/status map -> layout template
-> rendered visual -> semantic quality check -> handoff record
```

State one sentence describing what the audience must understand. Build the
concept map before choosing icons or colors. Classify every visible node using
the generic role taxonomy below:

| Role | Question answered |
|---|---|
| Context / source | Where does the process happen or what supplies knowledge? |
| Observation / state | What does the focal component receive or know? |
| Agent | Which software decision-maker owns the policy and action? |
| Decision mechanism | How is the agent's action selected? |
| Knowledge support | Which document or retrieved context informs a decision? |
| Action / contract | What structured output crosses the boundary? |
| Interface | How does another component call or receive the action? |
| Deterministic model | Which physical or system transformation remains outside policy? |
| Outcome / feedback | What changes downstream or returns to the next step? |
| Constraint / validator | What is bounded, checked, or safety-critical? |

Assign implementation status independently from role. Use explicit labels such
as `Existing`, `MVP`, `Future extension`, and `Optional`; do not rely on color
alone to communicate status.

## Core method

Use the generic causal spine:

`system context -> nested component -> observation/state -> decision mechanism -> structured action -> deterministic transformation -> downstream consequence -> feedback`

Keep two layers separate:

1. **Generic visual core:** system boundary, hierarchy, causal direction,
   overview-to-zoom composition, sibling decision branches, shared interface,
   label discipline, and quality control.
2. **Domain adapter:** entities, states, inputs, actions, units, model
   boundaries, vocabulary, and claims that require expert review.

Load the relevant file in `references/` before introducing specialized terms.
Never let the generic core invent domain facts.

## Audience and label policy

Choose the audience level before designing the figure.

### General explanatory visuals

Use plain-language noun phrases and action verbs. Do not place function calls,
array subscripts, equations, JSON braces, code glyphs, or mathematical symbols
in the visible diagram. For the HydroCNHS case, prefer labels such as:

- `Upstream water flow`
- `Reservoir storage level`
- `Reservoir decision interface`
- `Common action: release amount`
- `Output: downstream flow`

This rule is for the visible figure, not for the technical notes or source
mapping behind it.

### Professor-facing or engineering visuals

Keep the same plain-language structure, but allow a small, explicit whitelist
of identifiers when they clarify a real contract. For the current case the
whitelist is normally `release_cms`, `Dam API`, and `Gemma 4:12B`. Do not add
function-call syntax or time-indexed arrays by default; use them only when the
user explicitly asks for implementation notation.

The label map must record which audience level was used. Never mix technical
identifiers into a general visual merely because they are available in source
code.

## Decision mechanisms and comparison layout

When comparing policies, show them as two parallel alternatives with equal
visual status:

```text
Rule-based agent: observation -> explicit rule set -> action
LLM-driven agent: prompt + observation -> reasoning -> structured action
```

Both converge at the same action contract:

```text
rule-based agent OR LLM-driven agent -> shared action contract -> system model
```

For an existing-versus-replacement comparison, prefer two separated lanes:

```text
upper lane: Existing rule-based path
lower lane: LLM integration path
shared right side: interface -> deterministic model -> downstream outcome
```

Put the ABM agent boundary around the decision mechanism and its action
handling. Label the policy, interface, validator, knowledge retriever, and
physical model separately. A `Dam API`, callback, or interface is not an agent.
Do not draw the rule-based policy as a child of the LLM. Do not imply that an
LLM is the physical solver, state-transition model, routing engine, or safety
validator. The LLM proposes a policy action; the deterministic system applies
and validates it.

Apply a downstream-density rule: when the shared action is followed by three
or more sequential stages, give those stages a dedicated pipeline band or a
second row. Do not squeeze validation, deterministic transformation,
downstream process, and outcome cards into a narrow strip. Preserve readable
card widths, internal padding, visible gaps, and orthogonal non-crossing arrows;
move outcome cards to a separate right-side column when needed. Change the
layout before reducing text size.

Apply a directional-convergence rule: establish one primary reading direction
before placing arrows. When sibling decision branches produce a shared action,
place that action at a visible convergence point before the downstream chain.
Route each branch directly to that point; never route a branch through a sibling
branch or panel, and never let a branch arrow land in the middle of a later
downstream stage. Continue the deterministic chain in the same direction. If a
turn is necessary, use one deliberate clockwise or counter-clockwise
orthogonal turn rather than several competing reading paths.

## External knowledge and RAG

Represent document-grounded decisions as a knowledge-support path, not as a
second agent:

```text
operating document -> retriever -> policy context -> LLM-driven decision
```

Keep the path connected only to the LLM-driven branch when rule-based and
LLM-driven alternatives are being compared. Show a current observation as a
retrieval query only when the arrow can be routed unambiguously to the
retriever. Treat embedding as a retrieval implementation detail; do not imply
that the document is written into model weights. Mark document version,
effective date, or evidence identifiers in technical handoff notes when they
matter to the claim.

## Smallest useful visual family

Use one asset when one relationship is enough. Use a connected family only
when the idea needs more than one scale:

1. **Overview:** system boundary, large context, nested units, focal component,
   upstream causes, and downstream consequences.
2. **Decision zoom:** shared observation/state, parallel decision mechanisms,
   shared action contract, and the deterministic system that consumes it.
3. **Cascade:** repeated components showing how one output becomes the next
   input after the relevant process or routing step.
4. **Implementation seam:** stable interface, replaceable policy, validation,
   fallback, and unchanged surrounding simulator.

Choose the minimum set needed for the speaker's narrative. Keep names, arrow
semantics, and color roles stable across the family.

## Workflow

### 1. Establish the communication target

Write one sentence:

> After viewing this figure or slide sequence, the audience should understand
> **[one relationship or decision]**.

Record the audience's assumed background. Define the physical or operational
context before introducing ABM, API, LLM, or model names.

### 2. Set boundary, hierarchy, roles, and status

Identify the environment, largest context, nested units, focal component,
upstream causes, downstream consequences, and external constraints. Assign
each node a generic role and implementation status before drawing. Show the
focal component with a stable anchor such as a halo or dashed zoom box.

### 3. Build the content map

Before prompting, fill these fields:

| Field | Question |
|---|---|
| Context | Where does the process happen? |
| Input / observation | What does the component receive or observe? |
| State | What internal condition changes over time? |
| Decision mechanism | How is an action selected? |
| Action contract | What structured output crosses the interface? |
| System transformation | What deterministic model or physics acts on it? |
| Output | What leaves the component and who receives it next? |
| Feedback | Which result or constraint returns at the next step? |
| Constraint | What is bounded, validated, or safety-critical? |

List exact visible labels verbatim. Do not ask the image generator to invent
scientific labels, equations, identifiers, or API names.

### 4. Select a layout and generate or edit

Use the built-in image-generation tool for bitmap or cartoon diagrams. Make a
separate call for each asset with one primary message. For a revision, inspect
the local target first and use it as the edit reference. State the causal
order, arrow semantics, palette, exact labels, and forbidden implications in
the prompt.

Select the smallest layout that answers the communication target. Use a
two-lane comparison for existing-versus-new behavior, a decision zoom for
parallel policies, a cascade for repeated upstream/downstream units, and an
implementation seam for a replaceable policy behind a stable interface.

Use an editable text-native diagram when the user requests editable shapes or
precise text. Preserve the same content map and visual grammar.

### 5. Inspect and iterate

Inspect every output at full resolution and at intended slide scale. Check
composition, spelling, arrow direction, branch structure, label legibility,
domain claims, and the boundary between policy and simulator. Make targeted
revisions rather than accepting an attractive but semantically wrong figure.

### 6. Promote and document

For project-bound assets:

- save the selected file in the project asset directory with a stable name;
- update the slide-label map with the exact visible labels and audience level;
- update the design record with the speaker message and non-claims;
- retain generated source references only as provenance, not as the project
  runtime path.

Never leave a project-referenced image only in a generation cache.

### 7. Run the semantic and visual quality gate

Confirm:

- the system boundary and focal node are identifiable;
- the actual agent is explicitly identifiable and is not confused with its
  policy, interface, validator, retriever, or deterministic model;
- upstream-to-downstream or causal direction is unambiguous;
- input, state, decision mechanism, action, output, and feedback are distinct;
- rule-based and LLM-driven branches are siblings;
- the action contract is shared and structured;
- the deterministic model or physical process remains separate from policy;
- a downstream chain with three or more stages has a dedicated band or second
  row rather than compressed cards;
- one primary reading direction is obvious, sibling branches route directly to
  the convergence point, and no branch arrow enters a later stage;
- existing, MVP, and future components are explicitly distinguishable;
- any RAG path enters only the intended decision mechanism and does not imply
  model retraining or physical control by the language model;
- every visible label appears in the label map and is spelled correctly;
- the selected audience level is respected;
- a general visual has no function calls, equations, array notation, JSON
  braces, or unexplained code glyphs;
- the image is readable at presentation scale;
- no unsupported scientific or software claim was introduced.

For a technical visual, verify that every non-plain identifier is on the
explicit whitelist and is necessary for the stated contract.

## Visual grammar

Use a wide presentation layout unless the user specifies another format.

- Read left to right for time, causality, or upstream-to-downstream flow.
- Use thick solid arrows for material, state, or system movement.
- Use dashed arrows for observation, feedback, coupling, or zoom links.
- Use cards for modules and agents; use a shared boundary for interfaces.
- Use one bottom callout for the main takeaway.
- Use line style, shape, and labels in addition to color.

Suggested semantic roles:

| Role | Color |
|---|---|
| Natural, material, or data flow | Blue |
| Deterministic transformation or model | Teal |
| Agent, policy, or LLM | Purple |
| Action or intervention | Orange |
| Validation, risk, or constraint | Red |

Do not use color as the only carrier of meaning.

## Prompt template

```text
Use case: scientific-educational infographic-diagram
Asset type: wide English presentation visual
Primary request: one explanatory question
Audience level: general explanatory OR professor-facing engineering
System boundary: what remains inside the deterministic model
Causal order: context -> observation/state -> decision -> structured action
-> deterministic transformation -> output -> feedback
Style: flat vector, modular GitHub learning-project style, generous whitespace
Composition: overview, zoom, cascade, or implementation seam
Text (verbatim): exact labels only; do not invent identifiers
Color semantics: blue flow, teal model, purple policy, orange action, red validation
Constraints: keep policy separate from physics; preserve arrow direction
Avoid: clutter, tiny text, unsupported claims, function calls, equations, code glyphs
```

## Domain adapters

Use `references/domain-adapter-template.md` for a new domain. For the current
case, use `references/hydrocnhs-adapter.md`. A consumer-behavior adapter can
map:

```text
market or social context -> consumer state -> observation or stimulus
-> rule-based OR LLM-driven decision -> purchase/action -> outcome -> feedback
```

Do not copy hydrological terms into another domain unless the domain genuinely
uses them.

## Additional resources

Consult the following files progressively rather than loading all references by
default:

- **`references/design-framework.md`** - generic role taxonomy, layout
  patterns, visual grammar, and semantic review checklist.
- **`references/domain-adapter-template.md`** - template for adding a new
  domain without changing the generic visual core.
- **`references/hydrocnhs-adapter.md`** - HydroCNHS vocabulary, interface
  boundary, non-claims, and reservoir-specific acceptance checks.
- **`examples/hydrocnhs/`** - reviewed two-lane reference artifact and handoff
  record for the HydroCNHS rule-based versus LLM decision case.
- **`evals/`** - dependency-free text smoke tests for the reusable principles.

## Minimal deliverable

When a user asks for a visual explanation, return:

1. the narrative and asset roles;
2. the content map and parallel decision branches;
3. generated or revised visuals at absolute project paths when requested;
4. a label map, alt text, and design record;
5. the semantic and visual quality-gate result;
6. unresolved domain assumptions or limitations.

Do not call a visual family paper-ready solely because it looks polished;
domain experts must review scientific interpretation and terminology.
