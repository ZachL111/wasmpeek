# wasmpeek

`wasmpeek` keeps a focused JavaScript implementation around developer tools. The project goal is to inspect WebAssembly text fragments for imports and exports.

## Why It Exists

The project exists to keep a narrow engineering decision visible and testable. For this repo, that decision is how change width and review cost should influence a review result.

## Wasmpeek Review Notes

Start with `diagnostic quality` and `change width`. Those cases create the widest score spread in this repo, so they are the best quick check when the model changes.

## Features

- `fixtures/domain_review.csv` adds cases for change width and diagnostic quality.
- `metadata/domain-review.json` records the same cases in structured form.
- `config/review-profile.json` captures the read order and the two review questions.
- `examples/wasmpeek-walkthrough.md` walks through the case spread.
- The JavaScript code includes a review path for `diagnostic quality` and `change width`.
- `docs/field-notes.md` explains the strongest and weakest cases.

## Architecture Notes

The fixture data drives the tests. The code stays thin, while `metadata/domain-review.json` and `config/review-profile.json` explain what each case is meant to protect.

The added JavaScript path is deliberately direct, with fixtures doing most of the explaining.

## Usage

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/verify.ps1
```

## Tests

The verifier is intentionally local. It should fail if the fixture score math, lane assignment, or language-specific test drifts.

## Limitations And Roadmap

This remains a local project with deterministic fixtures. It does not depend on credentials, hosted services, or live data. Future work should add richer malformed inputs before widening the public API.
