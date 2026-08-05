# HydroCNHS Two-Lane LLM Integration Reference

## Speaker intent

Show that the existing rule-based Dam Agent and the LLM integration path are
alternative decision mechanisms that use the same reservoir decision interface
and unchanged HydroCNHS routing.

## Audience

Professor-facing engineering discussion; assumes basic familiarity with
HydroCNHS but not with the internal skill or implementation details.

## Content map

| Element | Visible representation |
|---|---|
| Shared observation | `Reservoir Observation` on the left |
| Existing path | Upper `EXISTING PATH` lane |
| Existing agent | `Rule-based Dam Agent` with `ABM AGENT` badge |
| New path | Lower `LLM INTEGRATION PATH` lane |
| New agent | `LLM-driven Dam Agent` with `ABM AGENT` badge |
| LLM stages | `Observation + Context` -> `Reasoning` -> `Release amount` |
| Future knowledge | `Operating Manual` -> `RAG Retriever` -> `Policy Context` |
| Validation | `Safety Validator` on the LLM path |
| Shared interface | `Reservoir Decision Interface`, `Dam API`, `Interface, not an agent` |
| Deterministic model | `HydroCNHS Routing` |
| Downstream result | `Downstream Flow` |

## Alt text

Two horizontally separated lanes receive a shared reservoir observation. The
upper existing lane uses a rule-based Dam Agent. The lower LLM integration lane
uses an LLM-driven Dam Agent with optional future operating-manual retrieval,
policy context, and a safety validator. Both lanes send a release amount to the
same reservoir decision interface, which feeds HydroCNHS routing and downstream
flow.

## Role and status map

- `Rule-based Dam Agent` and `LLM-driven Dam Agent`: ABM agents.
- `Rule-based Decision` and `LLM-driven Decision`: decision mechanisms.
- `RAG Retriever`: future knowledge-support module, not an agent.
- `Safety Validator`: deterministic validation module, not an agent.
- `Reservoir Decision Interface / Dam API`: action interface, not an agent.
- `HydroCNHS Routing`: deterministic hydrological model, not an agent.
- `Existing`: original rule-based path.
- `MVP`: current LLM integration path.
- `Future extension`: optional document-grounded policy context.

## Non-claims

- The LLM does not replace HydroCNHS routing or water balance.
- The diagram does not claim that RAG is already implemented in the runtime.
- The Dam API label denotes an in-process decision interface, not automatically
  a REST service.
- The figure is a feasibility-demo architecture, not proof of hydrological
  validity or operational deployment.

## Visual QA record

- [x] Two lanes are visually separated.
- [x] The ABM agent identity is explicit.
- [x] The interface is marked as not an agent.
- [x] RAG appears only in the LLM lane.
- [x] Shared interface and unchanged HydroCNHS routing are visible.
- [x] Labels remain legible at slide scale.
- [x] No unsupported routing or deployment claim is visible.

## Provenance

Generated as a preview with the Codex built-in image generation tool and copied
into this repository as the reviewed reference artifact. Superseded drafts are
not part of the repository.

- Review date: 2026-08-05
- Reviewer: Codex visual QA plus independent code-reviewer review
- Image dimensions: 1650 x 953 pixels
