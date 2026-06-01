# SAF-M-7: Content Rendering Parity

## Overview
**Mitigation ID**: SAF-M-7  
**Category**: UI Security  
**Effectiveness**: Medium-High  
**Implementation Complexity**: Low  
**First Published**: 2025-01-03

## Description
Content Rendering Parity ensures that what users see in the UI exactly matches what is sent to the LLM for all types of content (tool descriptions, tool outputs, error messages, and other data). This prevents attacks that exploit differences between displayed and processed content, including hidden instructions in tool outputs or visual deception techniques.

## Mitigates
- [SAF-T1001](../../techniques/SAF-T1001/README.md): Tool Poisoning Attack (TPA)
- [SAF-T1102](../../techniques/SAF-T1102/README.md): Prompt Injection (Multiple Vectors)
- [SAF-T1401](../../techniques/SAF-T1401/README.md): Line Jumping
- [SAF-T1402](../../techniques/SAF-T1402/README.md): Instruction Steganography

## Technical Implementation
[TO BE COMPLETED]

## References
- [UI Security Best Practices](https://owasp.org/www-project-web-security-testing-guide/)

## Related Mitigations
- [SAF-M-8](../SAF-M-8/README.md): Visual Validation
- [SAF-M-4](../SAF-M-4/README.md): Unicode Sanitization and Filtering

## Version History
| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 0.1 | 2025-01-03 | Initial stub | Frederick Kautz |
| 0.2 | 2025-01-09 | Generalized to cover all content types, not just descriptions | Frederick Kautz |