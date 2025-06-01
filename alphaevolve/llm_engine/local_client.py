from __future__ import annotations

from typing import Any

from .base_client import LLMClient


class LocalClient(LLMClient):
    """Placeholder local LLM client. Currently unimplemented."""

    async def chat(self, messages: list[dict[str, str]], **kw) -> Any:
        raise NotImplementedError("Local LLM backend not implemented")
