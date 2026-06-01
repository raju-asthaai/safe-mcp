# SAF-M-22: Semantic Output Validation

## Overview
**Mitigation ID**: SAF-M-22  
**Category**: Input Validation  
**Effectiveness**: Medium-High  
**Implementation Complexity**: Medium  
**First Published**: 2025-01-09

## Description
Semantic Output Validation analyzes tool outputs before they reach the LLM to ensure they match expected formats and don't contain instruction-like patterns. This mitigation goes beyond simple pattern matching by understanding the semantic content and context of outputs, validating that data conforms to expected schemas, and detecting anomalous content that may indicate injection attempts.

## Mitigates
- [SAF-T1102](../../techniques/SAF-T1102/README.md): Prompt Injection (Multiple Vectors)
- [SAF-T1103](../../techniques/SAF-T1103/README.md): Indirect Prompt Injection

## Technical Implementation
[TO BE COMPLETED]

## References
[TO BE COMPLETED]

## Related Mitigations
- [SAF-M-5](../SAF-M-5/README.md): Content Sanitization
- [SAF-M-10](../SAF-M-10/README.md): Automated Scanning

## Version History
| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 0.1 | 2025-01-09 | Initial documentation | Frederick Kautz |