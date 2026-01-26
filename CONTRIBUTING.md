Calling all developers who want to join the primelib module development.

# 🤝 Contribution Guidelines
Thank you for your willingness to contribute code and documentation to the primelib project! 
This guide outlines the contribution process and standards to enable more efficient collaboration.

# 📌 Before Contributing
1. This project is open source under the MIT License(see [Official License](LICENSE.md)), and all contributed code shall be licensed in accordance with this License.

2. The scope of contributions includes: bug fixes, performance optimizations, new feature development, documentation improvements, supplementary test cases, and more.

3. For first-time contributors, it is recommended to start with simple bug fixes / documentation improvements and submit complex features after familiarizing yourself with the process.

## 🧪 Testing Requirements
- All code changes must ensure all existing test cases pass.
- New features must cover at least **normal scenarios + boundary scenarios** for testing:
  Example (Prime Iterator):
  - Normal scenario: Generating prime numbers up to 20 returns correct results.
  - Boundary scenarios: `max_num=2` (the smallest prime number), `max_num=1` (raises an exception), `max_num=10000` (no obvious performance lag).

## ❓ Frequently Asked Questions
1. **How long does PR review take?**
   Reviews are generally completed within 1-3 business days. If no response is received after 3 days, you may leave a reminder under the relevant Issues/PR.
2. **Will contributed code be rejected?**
   Contributions may be rejected in the following cases:
   - Violates PEP 8 standards with no corrections made;
   - The new feature is inconsistent with the project's positioning;
   - No test cases are added or the test cases fail to pass;
   - The code has potential security risks or performance issues.
3. **What about non-code contributions (e.g., document translation, bug feedback)?**
   Submit them directly in Issues without going through the PR process.

## 📬 Communication Methods
- Bug feedback / Feature requests: Submit via GitHub Issues;
- Urgent issues / Collaborative communication: Leave your contact information (e.g., email) in Issues, and the project maintainers will reply in a timely manner.