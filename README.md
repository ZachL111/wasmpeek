# wasmpeek

`wasmpeek` is a focused JavaScript codebase around inspect WebAssembly text fragments for imports and exports. It is meant to be easy to inspect, run, and extend without a hosted service.

## Wasmpeek Walkthrough

I would read the project from the outside in: command, fixture, model, then roadmap. That keeps the developer tools idea grounded in files that can be checked locally.

## Reason For The Project

The goal is to capture the core behavior in code and make the surrounding assumptions obvious. A reader should be able to run the verifier, open the fixtures, and understand why each decision was made.

## Data Notes

`degraded` is the first example I would inspect because it lands on the `review` path with a score of -38. The broader file also keeps `degraded` at -38 and `surge` at 227, which gives the model a useful low-to-high spread.

## How It Is Put Together

The interesting part is the boundary between accepted and reviewed scenarios. Extended examples sit near that boundary so future edits can show whether the model became more permissive or more cautious. The JavaScript version uses native modules and a small Node test path.

## Capabilities

- Models code shape with deterministic scoring and explicit review decisions.
- Uses fixture data to keep diagnostics changes visible in code review.
- Includes extended examples for safe defaults, including `surge` and `degraded`.
- Documents repeatable output tradeoffs in `docs/operations.md`.
- Runs locally with a single verification command and no external credentials.

## Command Examples

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/verify.ps1
```

This runs the language-level build or test path against the compact fixture set.

## Check The Work

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/audit.ps1
```

The audit command checks repository structure and README constraints before it delegates to the verifier.

## Where Things Live

- `src`: primary implementation
- `tests`: verification harness
- `fixtures`: compact golden scenarios
- `examples`: expanded scenario set
- `metadata`: project constants and verification metadata
- `docs`: operations and extension notes
- `scripts`: local verification and audit commands
- `package.json`: Node package scripts

## Possible Extensions

- Add a short report command that prints the score breakdown for a single scenario.
- Add malformed input fixtures so the failure path is as visible as the happy path.
- Split the scoring constants into a typed configuration object and validate it before use.
- Add one more developer tools fixture that focuses on a malformed or borderline input.

## Tradeoffs

The scoring model is simple by design. More domain-specific behavior should be added through explicit adapters or extra fixture classes rather than hidden constants.

## Getting It Running

The only required setup is the local JavaScript toolchain. After cloning, stay in the repo root so fixture paths resolve correctly.
