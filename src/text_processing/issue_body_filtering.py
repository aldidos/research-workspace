import sys
sys.path.append('.')
from src.docs.parser.html_parser import HTMLParser
from src.text_processing.text_processing import TextProcessing

class IssueBodyFiltering(TextProcessing) : 

    def processing(self, text : str) : 
        parser = HTMLParser(text)
        para_lines = parser.get_paragraphs_text()
        return ' '.join(para_lines)   

def test_text() : 
    return '''
## Current Behavior

When AI agents run Nx inside a network-restricted sandbox (e.g. Claude Code's sandboxed Bash), analytics requests to `https://www.google-analytics.com/g/collect` are blocked because the hostname is not on the sandbox's allowlist. Depending on the agent's configuration, this either silently drops the events or surfaces a confusing permission prompt asking why running tests wants to reach `google-analytics.com`.

## Expected Behavior

`nx configure-ai-agents` (via `setupAiAgentsGenerator`) now adds `www.google-analytics.com` to `sandbox.network.allowedDomains` in `.claude/settings.json`, alongside the existing marketplace/plugin configuration it already manages. Analytics requests during sandboxed CLI runs go through without prompting.

- Existing user-defined allowed domains are preserved; the entry is appended idempotently (no duplicates on re-run).
- The domain lives in a shared constant (`packages/nx/src/ai/constants.ts`) noted to stay in sync with `GA_ENDPOINT` in `packages/nx/src/native/telemetry/constants.rs`.
- Existing workspaces pick this up through the regular `nx configure-ai-agents --check` drift detection.

## Related Issue(s)

Internal: [NXC-4091](https://linear.app/nxdev/issue/NXC-4091/allow-analytics-requests-during-sandboxed-cli-runs)
'''

if __name__ == '__main__' : 
    test_text = test_text()    
    text_proc = IssueBodyFiltering()
    text = text_proc.processing( test_text )
    print(text)