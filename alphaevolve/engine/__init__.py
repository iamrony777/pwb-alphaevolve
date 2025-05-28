from __future__ import annotations

"""High-level evolution interface."""

import asyncio
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Optional

from alphaevolve.store.sqlite import ProgramStore
from alphaevolve.evolution.controller import Controller

__all__ = ["AlphaEvolve", "Strategy"]


@dataclass
class Strategy:
    """Simple container for strategy code and metrics."""

    id: str
    code: str
    metrics: Dict[str, Any]


class AlphaEvolve:
    """Convenience wrapper for running the evolution loop."""

    def __init__(
        self,
        initial_program_path: str,
        evaluation_file: str,
        config_path: str,
        *,
        store: Optional[ProgramStore] = None,
    ) -> None:
        # For now we simply ignore the paths but keep them for future use.
        self.initial_program_path = Path(initial_program_path)
        self.evaluation_file = Path(evaluation_file)
        self.config_path = Path(config_path)
        self.store = store or ProgramStore()
        self.controller = Controller(self.store)

    async def run(self, iterations: int = 1) -> Strategy:
        """Run the evolution loop for a fixed number of iterations."""
        for _ in range(iterations):
            await self.controller._spawn(None)  # type: ignore[attr-defined]
            await asyncio.sleep(0.01)
        best = self.store.top_k(k=1)
        if not best:
            raise RuntimeError("No strategies generated")
        row = best[0]
        return Strategy(id=row["id"], code=row["code"], metrics=row["metrics"])
