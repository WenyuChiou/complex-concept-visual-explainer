---
name: complex-concept-visual-explainer
description: Design, generate, revise, and quality-check coherent visual explanations for complex systems, workflows, agents, decision processes, and model architectures. Use whenever a user asks for an overview-to-zoom diagram, cartoon diagram, infographic, presentation visual, or a comparison of rule-based and LLM-driven behavior, including hydrology, urban water, consumer behavior, and other coupled systems.
compatibility: Requires Codex built-in image generation, local image inspection, and filesystem access. Use project-local assets and Markdown documentation; no external network is required.
---

# Complex Concept Visual Explainer

Use this skill to turn a complex idea into a small, coherent visual story that
a non-specialist can follow. The output is an auditable mapping from context to
observation, decision, action, system consequence, and feedback - not a
decorative collection of unrelated images.

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

## Decision mechanisms

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

Do not draw the rule-based policy as a child of the LLM. Do not imply that an
LLM is the physical solver, state-transition model, routing engine, or safety
validator. The LLM proposes a policy action; the deterministic system applies
and validates it.

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

### 2. Set boundary and hierarchy

Identify the environment, largest context, nested units, focal component,
upstream causes, downstream consequences, and external constraints. Show the
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

### 4. Generate or edit

Use the built-in image-generation tool for bitmap or cartoon diagrams. Make a
separate call for each asset with one primary message. For a revision, inspect
the local target first and use it as the edit reference. State the causal
order, arrow semantics, palette, exact labels, and forbidden implications in
the prompt.

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

### 7. Run the quality gate

Confirm:

- the system boundary and focal node are identifiable;
- upstream-to-downstream or causal direction is unambiguous;
- input, state, decision mechanism, action, output, and feedback are distinct;
- rule-based and LLM-driven branches are siblings;
- the action contract is shared and structured;
- the deterministic model or physical process remains separate from policy;
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

## Minimal deliverable

When a user asks for a visual explanation, return:

1. the narrative and asset roles;
2. the content map and parallel decision branches;
3. generated or revised visuals at absolute project paths when requested;
4. a label map and design record;
5. the quality-gate result and unresolved limitations.

Do not call a visual family paper-ready solely because it looks polished;
domain experts must review scientific interpretation and terminology.
