# Threshold Policy Engine

Select a binary score threshold that meets requested precision/recall constraints and minimizes simple false-positive plus false-negative count.

```bash
cat scores.json | python tool.py
python -m unittest -v
```

Costs are intentionally unweighted. Calibrate business costs and validate policies on appropriate held-out data before use.
