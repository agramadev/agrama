"""
Ollama client wrapper for summarisation
"""

import os
import httpx
from typing import Dict, List, Optional, Any


class OllamaClient:
    """Ollama client wrapper for summarisation."""

    def __init__(self, url: Optional[str] = None, model: str = "qwen3:1.7b"):
        """Initialize the Ollama client.

        Args:
            url: The Ollama URL. If not provided, uses the OLLAMA_URL environment variable.
            model: The model to use for summarisation.
        """
        self.url = url or os.environ.get("OLLAMA_URL", "http://localhost:11434")
        self.model = model

    async def generate(
        self, prompt: str, system_prompt: Optional[str] = None, stream: bool = False
    ) -> Dict[str, Any]:
        """Generate text using Ollama.

        Args:
            prompt: The prompt to generate text from.
            system_prompt: The system prompt to use.
            stream: Whether to stream the response.

        Returns:
            The response from Ollama.
        """
        url = f"{self.url}/api/generate"

        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": stream,
        }

        if system_prompt:
            payload["system"] = system_prompt

        async with httpx.AsyncClient() as client:
            response = await client.post(url, json=payload)
            response.raise_for_status()
            return response.json()

    async def chat(
        self,
        messages: List[Dict[str, str]],
        system_prompt: Optional[str] = None,
        stream: bool = False,
    ) -> Dict[str, Any]:
        """Chat with Ollama.

        Args:
            messages: The messages to chat with.
            system_prompt: The system prompt to use.
            stream: Whether to stream the response.

        Returns:
            The response from Ollama.
        """
        url = f"{self.url}/api/chat"

        payload = {
            "model": self.model,
            "messages": messages,
            "stream": stream,
        }

        if system_prompt:
            payload["system"] = system_prompt

        async with httpx.AsyncClient() as client:
            response = await client.post(url, json=payload)
            response.raise_for_status()
            return response.json()

    async def summarise(self, text: str, max_tokens: int = 8000) -> str:
        """Summarise text using Ollama.

        Args:
            text: The text to summarise.
            max_tokens: The maximum number of tokens to use.

        Returns:
            The summarised text.
        """
        # Truncate the text if it's too long
        if len(text) > max_tokens * 4:  # Rough estimate of 4 characters per token
            text = text[: max_tokens * 4]

        system_prompt = "Summarise the following text for future retrieval. Be concise but comprehensive."

        response = await self.generate(text, system_prompt=system_prompt)

        return response.get("response", "")
