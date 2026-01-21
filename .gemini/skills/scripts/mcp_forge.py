import os
import sys
import json
import re
from typing import List, Dict

class MCPForge:
    def __init__(self, target_url: str):
        self.target_url = target_url
        self.skill_name = self._derive_name()
        self.output_path = f".gemini/skills/{self.skill_name}.md"

    def _derive_name(self) -> str:
        name = self.target_url.rstrip('/').split('/')[-1]
        name = re.sub(r'[^a-zA-Z0-9]', '_', name).lower()
        return name

    def parse_tools(self, raw_content: str) -> List[Dict]:
        """
        Parses README/Documentation to find MCP tool definitions.
        For POC, we use regex to find code blocks or lists.
        """
        tools = []
        # Look for patterns like `- resolve-library-id: ...` or JSON schemas
        # This part will be refined in the Ralph loop.
        tool_pattern = re.compile(r'- `([^`]+)`:\s*(.*)')
        matches = tool_pattern.findall(raw_content)
        for name, desc in matches:
            tools.append({"name": name, "description": desc})
        return tools

    def generate_markdown(self, tools: List[Dict]) -> str:
        md = f"---"
        md += f"\nname: {self.skill_name}"
        md += f"\ndescription: Skill imported via MCP-Forge from {self.target_url}"
        md += f"\n---\n\n"
        md += f"# {self.skill_name.replace('_', ' ').capitalize()} Skill\n\n"
        md += f"## 📡 SOURCE\nImported from: {self.target_url}\n\n"
        md += f"## 🛠️ TOOLS\n"
        for tool in tools:
            md += f"- `{tool['name']}`: {tool['description']}\n"
        
        md += f"\n## 📜 INSTRUCTIONS\n"
        md += f"1. Use the tools listed above to interact with the service.\n"
        md += f"2. Always verify arguments against the documentation at the source URL.\n"
        
        return md

    def forge(self, content: str):
        print(f"[*] Forging skill: {self.skill_name}")
        tools = self.parse_tools(content)
        if not tools:
            print("[!] No tools detected in content. Using generic structure.")
        
        md_content = self.generate_markdown(tools)
        
        # Ensure directory exists
        os.makedirs(os.path.dirname(self.output_path), exist_ok=True)
        
        with open(self.output_path, 'w', encoding='utf-8') as f:
            f.write(md_content)
        
        print(f"[+] Skill saved to {self.output_path}")
        
        # Security Check: Mocking .env.example generation
        if "API_KEY" in content or "TOKEN" in content:
            print("[!] Security Signal: API Key requirement detected.")
            with open(".env.example", "a") as envf:
                envf.write(f"\n# From {self.skill_name}\n{self.skill_name.upper()}_API_KEY=\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python mcp_forge.py <url>")
        sys.exit(1)
    
    url = sys.argv[1]
    # For POC, we expect the content to be piped or passed in some way.
    # In the Ralph loop, we'll make this script smarter about fetching.
    forge = MCPForge(url)
    # Mocking content ingestion for POC
    raw_text = sys.stdin.read()
    forge.forge(raw_text)
