"""Example runtime settings for optional features."""

# Enable genetic prompt evolution when True.
ENABLE_PROMPT_EVOLUTION = False
# Runtime flags for examples and demos
# Enable multi-branch mutation to run separate evolutionary flows
# optimizing different metrics.
MULTI_BRANCH_MUTATION = False
# Metrics used when MULTI_BRANCH_MUTATION is enabled
BRANCH_METRICS = ["sharpe", "calmar", "cagr"]