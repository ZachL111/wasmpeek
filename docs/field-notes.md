# Field Notes

The useful part of this repository is the small rule set around change width and review cost.

The domain cases cover `change width`, `diagnostic quality`, `review cost`, and `safe rewrite`. They sit beside the smaller starter fixture so the project has both a compact scoring check and a domain-flavored review check.

The widest spread is between `diagnostic quality` and `change width`, so those are the first two cases I would preserve during a refactor.

The extra check gives the repository a behavior path that can fail for a domain reason, not only a syntax reason.
