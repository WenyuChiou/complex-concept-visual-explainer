# Generic visual design framework

## Story spine

Use this sequence when teaching a complex system:

```text
context -> process or environment -> component -> observation/state
-> decision -> action -> system transformation -> downstream consequence
-> feedback or next step
```

Split it into an overview, zoom, cascade, or seam view when one canvas becomes
crowded. Give each asset one sentence of speaker intent.

## Layout patterns

- **Overview:** system boundary, hierarchy, focal component, upstream causes,
  and downstream consequences.
- **Decision zoom:** shared observation/state, sibling decision branches,
  shared action contract, and deterministic consumer.
- **Cascade:** repeated components connected by causal arrows; label upstream
  output and downstream input when the interface matters.
- **Implementation seam:** stable interface, replaceable policy, validation,
  fallback, and unchanged simulator.

## Arrow and color semantics

| Mark | Meaning |
|---|---|
| Thick solid arrow | material, state, or causal system movement |
| Thin solid arrow | ordinary process sequence |
| Dashed arrow | observation, feedback, coupling, or zoom relation |
| Bounded gate | validation, constraint, approval, or safety check |

| Role | Color |
|---|---|
| Natural, material, or data flow | Blue |
| Deterministic transformation or model | Teal |
| Agent, policy, or LLM | Purple |
| Action or intervention | Orange |
| Validation, risk, or constraint | Red |

Use shape, line style, and labels as well as color so the figure remains
interpretable in grayscale.

## Label and accessibility rules

- Keep labels short, exact, and large enough for slide-scale reading.
- Use plain-language labels for general audiences.
- In technical figures, use only identifiers named in the domain adapter's
  whitelist; never add code notation for decoration.
- Do not let an image generator invent equations, identifiers, or domain terms.
- Keep the main message in one callout, not in tiny footer text.
- Provide alt text that describes the causal relationship, not just colors.

## Review questions

1. What is inside and outside the system boundary?
2. Can the reader identify input, state, decision, action, output, and feedback?
3. Does each arrow have one interpretable direction and meaning?
4. Is an LLM shown as a policy/proposal rather than unsupported physical truth?
5. Does the downstream consequence connect to the next input or feedback?
6. Can the shared interface support another policy implementation?
7. Which claims require domain-expert review?
