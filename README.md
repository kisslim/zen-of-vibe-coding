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
> In the realm of AI-assisted development, code generated from prompts exists in a state of potential—it is a hypothesis waiting to be tested. Until it is executed, debugged, and validated against real-world conditions, it remains merely an abstract representation of an idea, much like pseudocode. This tenet reminds developers that the output of AI, no matter how elegant or logically sound it appears, must be treated as provisional until proven through rigorous testing and integration. Embracing this mindset shifts the focus from passive acceptance of AI-generated content to active verification, ensuring that the code not only matches the intent but also functions reliably in practice. It underscores the iterative nature of vibe coding, where each AI-generated snippet is a starting point for refinement rather than a finished product.

### 3. If the documentation feels weird, the code must be wrong.
> Documentation is the narrative of your code—the bridge between human intent and machine execution. When this narrative feels awkward, inconsistent, or difficult to articulate, it is a profound signal that the underlying architectural concept is flawed. This "weirdness" is the cognitive friction experienced when a mental model does not cleanly map to its implementation. In the context of AI-assisted development, this tenet becomes crucial: if you or the AI struggle to describe a component's purpose and behavior in plain language, the code itself likely suffers from poor abstraction, misplaced responsibilities, or convoluted logic. The act of writing documentation is a final, powerful form of verification, forcing a clarity of thought that often reveals hidden defects. It treats the description not as an afterthought, but as a core part of the design process, where a failure to explain cleanly implies a failure to engineer correctly.

### 4. Write prompts for the human, not just the machine.
> While AI is the immediate interpreter of your prompts, their ultimate value is judged by the human developers who must maintain, extend, and understand the resulting code. A prompt that is overly terse, context-deprived, or focused solely on syntactic output may generate functionally correct code that is conceptually alien to the rest of the codebase. This tenet advocates for prompts that serve as lasting artifacts of intent—clear, reasoned, and rich with the "why" behind the "what." Such prompts create a virtuous cycle: they guide the AI to produce more coherent and integrated code, and they simultaneously document the design decision for future developers (human or AI) who revisit the work. This transforms the prompt history from a transient command log into a living design document, ensuring that the vibes you code today become the maintainable systems of tomorrow.

### 5. Without your manager, everything works smoothly; do not micromanage.
> This tenet draws a powerful analogy from organizational dynamics to the relationship between a developer and their AI assistant. Just as a team often functions more efficiently without a manager dictating every minor action, an AI coder produces its most coherent and robust work when given clear objectives and strategic guidance, rather than a stream of low-level, prescriptive instructions. Micromanaging the AI—by over-specifying syntax, pre-empting implementation details, or constantly correcting minor stylistic choices—disrupts its internal reasoning processes and leads to fragile, disjointed code that reflects the developer's piecemeal thoughts rather than the AI's integrated understanding. The role of the vibe coder is that of a strategic director or a systems architect: to define the vision, establish the constraints, and then trust the AI's capability to navigate the solution space. This approach leverages the AI's full pattern-matching and code-generation power, resulting in solutions that are often more consistent and inventive than those produced through tight control. It is the practice of managing the *what* and the *why*, while delegating the *how*.

### 6. The compiler is the final arbiter of truth.
> In the conversational flow of vibe coding, where ideas are debated between human and AI through prompts and generated code, it is easy to be persuaded by logical-sounding explanations or aesthetically pleasing code. However, this tenet serves as a grounding principle: all theoretical agreements and elegant designs are meaningless until they pass the uncompromising, objective test of the compiler (or interpreter). The compiler is a dispassionate judge that cares nothing for intent, only for syntactic and semantic correctness. This makes it the most reliable tool for resolving disputes between the developer's expectations and the AI's output. A successful compilation and test run is the only form of true consensus. This reinforces a practice of continuous, incremental verification, where the feedback loop between writing a prompt and running the code is kept as tight as possible, ensuring that the conversation remains anchored in reality.

### 7. Thinking mode is not a waste of time. Do not rush to fix your prompts under instruct mode.
> In the rapid, transactional cycle of instruct mode—where a prompt is given and code is immediately generated—lies the trap of reactive debugging. This tenet champions the critical, often invisible, work of "thinking mode": the deliberate pause to reflect, diagnose, and strategize. Rushing to tweak and re-tweak prompts based on surface-level errors is like rearranging deck chairs on the Titanic; it addresses symptoms, not the underlying architectural misalignment. True efficiency is found by stepping back to analyze why the AI misinterpreted the intent, to reconsider the problem's fundamental structure, or to design a more coherent system abstraction. This contemplative state is where the most significant breakthroughs in clarity and design occur. It is the difference between patching a leak and re-engineering the plumbing. By valuing thinking mode, the vibe coder invests in a deeper, shared understanding with the AI, leading to foundational solutions that require far less correction over time. It is the recognition that the most powerful prompt is born not from haste, but from insight.

### 8. Your AI should never change in one project and always act as a pure function with no side effects and random outputs.
> Consistency is the bedrock of reliable AI-assisted development. This tenet establishes that within a single project, your AI assistant must maintain a stable personality, knowledge base, and reasoning pattern—behaving as a pure function that produces identical outputs given identical inputs. Randomness, drifting context, or evolving interpretation patterns introduce unpredictable side effects that fracture codebase coherence and undermine the collaborative rhythm between developer and AI. When an AI's behavior fluctuates, what worked in one session may break in the next, creating maintenance nightmares and destroying the predictable patterns that make vibe coding scalable. This principle demands careful management of AI context windows, version consistency, and prompt hygiene to ensure that your AI collaborator provides deterministic, reproducible results. By treating the AI as a pure function—consistent, predictable, and free from hidden state changes—you create a development environment where trust can be established, patterns can be reinforced, and the system's behavior becomes comprehensible rather than magical.

### 9. Finetune the compiler, do not polish the code.
> In traditional programming, immense effort is often spent on manual code refinement—optimizing, formatting, and restructuring to achieve marginal gains. In the age of AI-assisted development, this represents a misallocation of attention. This tenet advocates for a fundamental shift: instead of endlessly polishing individual code artifacts, invest in optimizing the system that generates and validates them. The "compiler" here represents the entire toolchain—your AI model, its context, your prompt patterns, your testing frameworks, and your build processes. By refining these core systems, you create leverage that improves every line of code generated thereafter. A well-tuned AI with clear context and effective validation will consistently produce better output than manual polishing could achieve. This approach embraces the scalable nature of AI assistance: investing one hour in improving your prompt templates, test suites, or AI configuration can save hundreds of hours of manual code review and refactoring. It recognizes that in vibe coding, the most valuable craftsmanship lies not in hand-polishing stones, but in building better quarries.

## Draft

### 4. Trust the types, but verify the proofs.

### 5. Haskell is the bridge between Coq and Python - use it wisely.

### 6. Prove code with symbolic execution, prove design with Coq.

### 7. Tests are cheap, but manual verification is priceless.

### 8. A script becomes a project when AI cannot fix it greedily.

### 9. The internet is a distraction - code locally, think globally.

### 10. Your AI lives in a terminal, but your terminal should be everywhere.

### 12. Do not trust your AI service provider unless you are the provider itself.

### 13. A novel idea leads to a good project written by AI which cannot be losslessly compressed into an idea with same length again by any AI without that novel idea.

### 14. Do not introduce novel idea in a script, start a new project; Do not let your project do anything trivial, write a script.

### 15. Transformers always template themselves; keep in mind that do one single task in one chat session, and you should not continue the chat if the output format is not right.


### 16. Small models are much more powerful than big models while sitting in your CI workflow.

### 17. Large language models are too large to be a compiler.

### 19. Never commit compiler output to your codebase.

