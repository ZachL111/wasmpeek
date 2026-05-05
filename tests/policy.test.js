import assert from "node:assert/strict";
import { classify, score } from "../src/policy.js";

const cases = [
  {
    "name": "case_1",
    "demand": 55,
    "capacity": 105,
    "latency": 18,
    "risk": 11,
    "weight": 11,
    "score": 168,
    "decision": "review"
  },
  {
    "name": "case_2",
    "demand": 75,
    "capacity": 80,
    "latency": 20,
    "risk": 9,
    "weight": 11,
    "score": 193,
    "decision": "accept"
  },
  {
    "name": "case_3",
    "demand": 90,
    "capacity": 96,
    "latency": 17,
    "risk": 19,
    "weight": 13,
    "score": 187,
    "decision": "accept"
  }
];

for (const item of cases) {
  const signal = {
    demand: item.demand,
    capacity: item.capacity,
    latency: item.latency,
    risk: item.risk,
    weight: item.weight
  };
  assert.equal(score(signal), item.score);
  assert.equal(classify(signal), item.decision);
}
