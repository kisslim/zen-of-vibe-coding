# The Zen of Vibe Coding

> *A modern interpretation of programming principles for the age of AI-assisted development*

**Vibe Coding** is an emerging software development practice where developers use natural language prompts to guide AI in generating, refining, and debugging code. [Coined by AI researcher Andrej Karpathy](https://x.com/karpathy/status/1886192184808149383) in early 2025, it represents a shift from writing code line-by-line to directing an AI assistant through a conversational process. This approach allows the developer to focus on the overarching goal and application design, while the AI handles the implementation details.

The following principles adapt the timeless wisdom of the Zen of Python for this new paradigm.

## The Core Principles

### Beautiful is better than ugly, but runnable is better than beautiful.
> While aesthetically pleasing code is valuable, the primary goal is a functioning application. An elegantly structured function is useless if it doesn't run, whereas a working—if imperfect—program provides immediate value and a foundation for improvement.

### Explicit is better than implicit, but verified is better than explicit.
> Clearly stated code and prompts help both humans and AI understand intent. However, explicit instructions are not enough; the generated code must be verified through execution and testing to ensure it behaves as expected, catching errors that explicit instructions might have missed.

### Simple is better than complex, but correct is better than simple.
> Simplicity should be a key aim, as it often leads to more maintainable and understandable code. However, correctness is the non-negotiable foundation. A simple but incorrect solution is worse than a more complex one that works properly.

### Complex is better than complicated, but proven is better than complex.
> Some problems are inherently complex and require sophisticated solutions. A "complex" solution can be well-structured and logical, whereas a "complicated" one is unnecessarily convoluted. When complexity is necessary, it should be backed by proofs or rigorous testing to ensure its reliability.

## The Guiding Tenets

### 1. Duplication is good. Dependency is disaster.
> What appears as duplication to humans is pattern reinforcement to AI. When AI generates code, it creates consistent templates across your codebase—this "duplication" actually maintains architectural coherence and makes the system more predictable for future AI assistance. Dependencies, however, introduce unpredictable templating and fragile abstraction layers that disrupt AI's pattern recognition. Embrace AI's natural tendency toward consistent patterns through strategic repetition, as dependencies create complexity that neither humans nor AI can reliably manage.

### 2. All unverified code is pseudocode.
> Treat all code—whether AI-generated or human-written—as speculative until proven functional. Assume nothing works until you've seen it execute successfully and produce the expected results. This mindset prevents false confidence and ensures thorough validation.

### 3. If the documentation feels weird, the code must be wrong.
> When explaining your code feels awkward or convoluted, this often reveals underlying design flaws. Clear, straightforward documentation typically emerges from clean, well-structured code. If you struggle to describe what the code does simply, reconsider the implementation itself.

### 4. Trust the types, but verify the proofs.
> Static type checking provides valuable early error detection and enhances code robustness. However, type safety alone cannot guarantee logical correctness. Complement types with comprehensive testing and other verification methods to establish behavioral proofs.

### 5. Haskell is the bridge between Coq and Python - use it wisely.
> Programming languages exist on a spectrum from formal verification to practical development. Coq represents the rigorous end for machine-checked proofs, while Python emphasizes rapid development. Haskell occupies the middle ground, offering strong type guarantees and functional purity without the full overhead of formal methods.

### 6. Prove code with symbolic execution, prove design with Coq.
> Apply appropriate verification techniques to different concerns. Use symbolic execution to thoroughly analyze code paths and runtime behavior. Reserve formal proof assistants like Coq for validating fundamental algorithms and critical design specifications where mathematical certainty is required.

### 7. Tests are cheap, but manual verification is priceless.
> Automated testing provides inexpensive, repeatable validation and should be used extensively. However, human review offers irreplaceable value—manual inspection catches subtle security issues, logical flaws, and requirement mismatches that automated tests might miss, while deepening the reviewer's understanding.

### 8. A script becomes a project when AI cannot fix it greedily.
> The distinction between script and project lies in AI's ability to comprehend and modify the code in one pass. A script is small enough for AI to understand and fix completely in a single attempt. When changes require architectural awareness, multiple file contexts, or historical understanding, you're dealing with a project that demands more sophisticated approaches.

### 9. The internet is a distraction - code locally, think globally.
> While online resources and AI services are essential, constant web browsing disrupts the focused mental state crucial for effective programming. Maintain a local development environment that supports deep concentration, minimizing context switches that break productive flow.

### 10. Your AI lives in a terminal, but your terminal should be everywhere.
> Command-line interfaces provide the most efficient access to AI coding assistants, offering speed and scriptability. Ensure your terminal setup is portable and consistent across devices and platforms, making your AI tools universally accessible regardless of your working environment.

### 11. Your AI should never change in one project and always act as a pure function with no side effects and random outputs.
> Maintain consistent AI behavior throughout a project's lifecycle. The assistant should function deterministically, producing identical outputs for identical inputs. Avoid random variations in AI responses, as reproducibility is essential for stable development and reliable results.

### 12. Do not trust your AI service provider unless you are the provider itself.
> Recognize that external AI services may alter their offerings—changing models, adjusting pricing, or modifying features—in ways that could disrupt your workflow. For critical projects, consider self-hosted solutions to maintain control over your development environment.

### 13. A novel idea leads to a good project written by AI which cannot be losslessly compressed into an idea with same length again by any AI without that novel idea.
> Truly innovative concepts generate AI-assisted projects that contain emergent complexity and insights beyond the original prompt. The resulting implementation embodies knowledge and structure that cannot be perfectly reverse-engineered back into the initial idea's concise form without losing essential value—the project becomes greater than the sum of its prompting.

### 14. Do not introduce novel idea in a script, start a new project; Do not let your project do anything trivial, write a script.
> Maintain clear boundaries between different scales of work. Keep scripts focused on simple, single-purpose tasks. When implementing novel or complex functionality, create a proper project with appropriate architecture. Conversely, avoid burdening projects with trivial operations that belong in separate, focused scripts.

### 15. Transformers always template themselves; keep in mind that do one single task in one chat session, and the format should be right with first attempt.
> AI models naturally structure responses based on learned patterns. Approach each interaction with a single, well-defined objective. Craft your initial prompt to be sufficiently clear and comprehensive that the AI produces correctly formatted, complete output immediately, avoiding iterative formatting corrections.

### 16. Small models are much more powerful than big models while sitting in your CI workflow.
> Large language models excel at broad, creative tasks like generating novel code from a vague prompt, but this strength becomes a critical weakness in an automated Continuous Integration (CI) environment. A CI system requires deterministic, fast, and reliable operations. Small, finely-tuned models, specialized for tasks like linting, security scanning, or identifying simple logical errors, provide consistent and predictable results. Their "power" lies not in creative breadth, but in their focused precision, speed, and low cost, making them the superior tool for enforcing quality gates automatically. In the context of the Zen, this embodies "verified is better than explicit"—a small model's specialized verification is more valuable than a large model's potentially brilliant but non-deterministic and expensive analysis.

### 17. Large language models are too large to be a compiler.
> Compilers operate through deterministic, rule-based transformations with guaranteed correctness and predictable performance. Large language models, by contrast, are probabilistic systems that generate outputs through statistical pattern matching rather than formal logic. Their immense size and architectural complexity make them unsuitable for the precise, reliable code transformation that compilation requires. While LLMs can simulate compilation-like behaviors, they lack the mathematical rigor and consistent output guarantees of true compilers, making them fundamentally mismatched for this role. This echoes the principle that "proven is better than complex"—the proven, deterministic nature of traditional compilers outweighs the complex but unreliable approximation offered by LLMs for critical compilation tasks.
