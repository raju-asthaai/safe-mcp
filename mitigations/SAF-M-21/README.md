# SAF-M-21: Output Context Isolation

## Overview
**Mitigation ID**: SAF-M-21  
**Category**: Architectural Control  
**Effectiveness**: High  
**Implementation Complexity**: Low  
**First Published**: 2025-01-09

## Description
Output Context Isolation uses special delimiters or structured formatting (such as XML-style tags) to clearly separate tool outputs from system instructions in the LLM context. This architectural pattern ensures that data returned by tools cannot be interpreted as instructions by implementing clear boundaries between different types of content. For example, wrapping tool outputs in `<tool-output>...</tool-output>` tags helps the LLM maintain context awareness.

## Mitigates
- [SAF-T1102](../../techniques/SAF-T1102/README.md): Prompt Injection (Multiple Vectors)
- [SAF-T1103](../../techniques/SAF-T1103/README.md): Indirect Prompt Injection
- [SAF-T1112](../../techniques/SAF-T1112/README.md): Sampling Request Abuse — nested `sampling/createMessage` output must be held logically separate from planner state until reviewed, logged, and policy-checked, so a malicious server's sampling response cannot directly seed subsequent reasoning

## Technical Implementation
[TO BE COMPLETED]

## References
[TO BE COMPLETED]

## Related Mitigations
- [SAF-M-1](../SAF-M-1/README.md): Architectural Defense - Control/Data Flow Separation
- [SAF-M-5](../SAF-M-5/README.md): Content Sanitization

## Version History
| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 0.1 | 2025-01-09 | Initial documentation | Frederick Kautz |