# Complex Concept Visual Explainer

A reusable Codex-compatible skill for explaining complex systems through a
coherent visual sequence: overview, decision zoom, downstream consequence, and
implementation seam.

The generic core is domain-neutral. Domain adapters provide the vocabulary,
units, model boundary, decision semantics, and non-claims for a specific case.
The repository currently includes a HydroCNHS adapter and is designed to
support future urban-water, consumer-behavior, and other coupled-system cases.

## Install for Codex or compatible agents

Use the portable skill directory:

```text
skills/complex-concept-visual-explainer/SKILL.md
```

With the Vercel Skills CLI:

```bash
npx skills add WenyuChiou/complex-concept-visual-explainer \
  --skill complex-concept-visual-explainer --agent codex --yes
```

Manual installation copies `skills/complex-concept-visual-explainer/` to the
agent's configured skills directory, preserving the directory name
`complex-concept-visual-explainer` and its `references/` subdirectory.

## Design principles

- Keep context, observation, decision, action, system transformation, output,
  and feedback visually distinct.
- Show rule-based and LLM-driven policies as parallel alternatives, using
  separated lanes when comparing an existing path with an integration path.
- Identify the actual ABM agent separately from its decision mechanism,
  interface, validator, retriever, and deterministic model.
- Mark implementation status explicitly as Existing, MVP, Future extension, or
  Optional.
- Represent document grounding as operating document -> retriever -> policy
  context -> intended LLM decision branch.
- Keep the LLM at the policy boundary; the deterministic model retains state
  transition, safety validation, and physical or system propagation.
- Use plain-language labels for general audiences. Technical identifiers are
  allowed only when the domain adapter explicitly whitelists them.
- Include concise alt text or a text equivalent for every generated visual.

## Reference artifact

The HydroCNHS example includes a two-lane professor-facing comparison showing
the existing rule-based Dam Agent above the LLM integration path, with a shared
reservoir decision interface and unchanged HydroCNHS routing:

- [`two-lane-llm-integration.png`](skills/complex-concept-visual-explainer/examples/hydrocnhs/two-lane-llm-integration.png)
- [`two-lane-llm-integration.md`](skills/complex-concept-visual-explainer/examples/hydrocnhs/two-lane-llm-integration.md)

## Repository layout

- `skills/complex-concept-visual-explainer/SKILL.md`: core instructions.
- `skills/complex-concept-visual-explainer/references/`: design framework and
  domain adapters.
- `skills/complex-concept-visual-explainer/examples/`: reviewed domain examples
  that ship with the portable skill package.
- `skills/complex-concept-visual-explainer/evals/`: evaluation prompts and the
  dependency-free token-check runner (`evaluate_outputs.py`).

To run a text smoke test after generating an eval response:

```bash
python skills/complex-concept-visual-explainer/evals/evaluate_outputs.py \
  skills/complex-concept-visual-explainer/evals/evals.json 1 output.txt
```

Run the complete dependency-free fixture suite with:

```bash
python skills/complex-concept-visual-explainer/evals/run_all.py
```

The HydroCNHS research case, presentation, mock test, and generated visual
assets are maintained in the separate HydroCNHS integration fork:

https://github.com/WenyuChiou/HydroCNHS/tree/codex/llm-reservoir-agent

## Provenance

The repository keeps the BSD 3-Clause attribution from HydroCNHS because the
HydroCNHS adapter documents and links to that upstream project. The generic
skill instructions and non-domain-specific references are authored for this
repository. See [`NOTICE.md`](NOTICE.md) for the boundary.
