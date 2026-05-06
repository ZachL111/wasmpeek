import assert from "node:assert/strict";
import { domainReviewLane, domainReviewScore } from "../src/domainReview.js";

const item = { signal: 56, slack: 41, drag: 32, confidence: 83 };
assert.equal(domainReviewScore(item), 140);
assert.equal(domainReviewLane(item), "ship");
