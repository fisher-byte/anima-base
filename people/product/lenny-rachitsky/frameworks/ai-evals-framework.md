---
title: "AI Evals Framework"
subtitle: "Systematic approach to measuring and improving AI applications"
persona: lenny-rachitsky
source: "Hamel Husain & Shreya Shankar — Why AI evals are the hottest new skill for product builders"
source_url: "https://www.youtube.com/watch?v=BsWxPI9UM4c"
source_type: podcast
publish_date: 2025-09-25
categories:
  - AI Product Development
  - Quality Assurance
  - Product Iteration
tags:
  - ai-evals
  - llm-applications
  - product-quality
  - systematic-improvement
  - data-analytics
verification_status: verified
confidence_level: high
---

# AI Evals Framework

## Core Definition

**AI Evals** = Systematic way to measure and improve AI application quality through data analytics and feedback loops.

> "To build great AI products, you need to be really good at building evals. It's the highest ROI activity you can engage in." — Hamel Husain

## Why Evals Matter

### The Problem Without Evals
- **Guessing game**: No systematic way to know if changes improve or break things
- **Vibe checks only**: Fine for prototypes, unmanageable at scale
- **Blind iteration**: Changing prompts/models without confidence in outcomes
- **Hidden regressions**: Fixing one issue while unknowingly breaking another

### The Value Proposition
1. **Confidence in iteration**: Know whether changes improve your product
2. **Systematic measurement**: Data-driven insights replace guesswork
3. **Faster debugging**: Identify specific failure modes quickly
4. **Quality assurance**: Catch regressions before they reach users
5. **Team alignment**: Shared metrics for product quality

## The Evals Spectrum

Evals exist on a continuum from simple to sophisticated:

### 1. Unit Tests (Deterministic)
- **What**: Binary pass/fail checks for non-negotiable functionality
- **When**: Core features that must always work
- **Example**: "Does the real estate agent extract property address correctly?"

### 2. Heuristic Checks (Rule-Based)
- **What**: Automated checks based on rules and patterns
- **When**: Well-defined quality criteria
- **Example**: "Does email response contain required sections?"

### 3. LLM-as-Judge (Qualitative)
- **What**: Using AI to evaluate AI outputs on subjective criteria
- **When**: Open-ended, ambiguous quality dimensions
- **Example**: "Is the tone professional and empathetic?"

### 4. Human Evaluation (Ground Truth)
- **What**: Expert review for nuanced judgment
- **When**: Establishing baselines, validating LLM judges
- **Example**: Domain expert reviews generated content

## Core Process: Open Coding Method

**Goal**: Build a measurement system that captures real product quality

### Phase 1: Collect Representative Data
```
1. Gather 50-100 real examples from production
2. Ensure diverse coverage of:
   - Common use cases
   - Edge cases
   - Known failure modes
   - Different user types
3. Prioritize recent data (reflects current behavior)
```

**Key Insight**: "Quality > Quantity. 50 well-chosen examples > 1000 random ones."

### Phase 2: Open Coding (The Critical Step)
```
1. Appoint ONE domain expert (avoid committee approach)
   → Usually the PM or engineer with best product taste
   
2. Review each example with critical eye:
   - What's working well?
   - What's problematic?
   - Why is this good/bad?
   
3. Develop taxonomy of quality dimensions naturally:
   - Patterns emerge from repeated observations
   - Categories crystallize through iteration
   - Don't force predetermined rubrics
```

**Anti-Pattern**: "Starting with a rubric before looking at data. Let categories emerge."

### Phase 3: Create Rubric
```
Transform observations into measurable criteria:

Example for Email Assistant:
✓ Addresses customer question directly
✓ Professional tone (no casual slang)
✓ Includes next steps
✓ Proper formatting
✗ Hallucinates information
✗ Overly verbose (>200 words)
```

### Phase 4: Build Automated Evals
```
1. Start simple: Heuristics first
   - Length checks
   - Keyword presence
   - Format validation
   
2. Add LLM-as-Judge for subjective criteria
   - Use rubric as prompt context
   - Ask for yes/no + brief reasoning
   - Validate against human labels
   
3. Create regression test suite
   - Save examples that broke in past
   - Run evals on every change
```

### Phase 5: Iterate & Monitor
```
1. Run evals continuously (CI/CD integration)
2. Track metrics over time
3. Update evals as product evolves
4. Add new failure modes to test suite
```

## Best Practices & Principles

### ✅ DO

**1. Start Small & Iterate**
- "The goal is not to do evals perfectly, it's to actionably improve your product"
- One person can build initial evals (avoid committee paralysis)
- Ship imperfect evals > Perfect evals that never ship

**2. Trust Domain Expertise**
- Appoint the person with best product taste
- Usually PM or engineer closest to users
- One expert > Committee consensus

**3. Use Representative Data**
- Sample from production (real user behavior)
- Include edge cases and known failures
- Refresh dataset as product evolves

**4. Build on Success**
- Most products need this process once
- Then iterate and refine
- Each eval session builds on previous work

**5. Make it Fun & Addictive**
- "Everyone that does this immediately gets addicted to it"
- Rapid feedback loops
- Visible product improvements

### ❌ DON'T

**1. "Can't AI Just Eval Itself?"**
- Myth: LLMs can automatically create perfect evals
- Reality: Requires human judgment to define quality
- AI assists, humans direct

**2. Over-Engineer Too Early**
- Don't build complex ML pipelines upfront
- Start with simple heuristics
- Add sophistication only when needed

**3. Let Committees Slow You Down**
- Open coding doesn't need group consensus
- One expert moves faster than ten reviewers
- Get feedback after, not during

**4. Rely Only on Vibe Checks**
- Good for prototypes, breaks at scale
- Can't track improvements systematically
- No confidence in changes

**5. Ignore Past Failures**
- Always add regression tests for fixed bugs
- Build institutional memory
- Prevent repeat mistakes

## Common Misconceptions

### Myth 1: "Evals Need Perfect Ground Truth"
**Reality**: Directional improvement > Perfect accuracy
- 80% confidence is actionable
- Better than zero measurement

### Myth 2: "Evals Are Only for AI Labs"
**Reality**: Any AI product needs evals
- Real estate agents
- Customer support bots
- Content generation tools
- All benefit from systematic measurement

### Myth 3: "Evals Are Expensive & Time-Consuming"
**Reality**: Highest ROI activity
- One person, one week → Initial eval system
- Saves weeks of blind debugging
- Prevents costly production failures

### Myth 4: "We Burned By Evals Before"
**Reality**: Bad evals ≠ Evals are bad
- Common anti-patterns exist
- Learn from mistakes
- Modern tools make it easier

## Getting Started: First Steps

### Week 1: Foundation
1. **Day 1-2**: Collect 50-100 production examples
2. **Day 3-4**: Open coding session (critical step!)
3. **Day 5**: Create initial rubric

### Week 2: Implementation
1. **Day 1-2**: Build simple heuristic checks
2. **Day 3-4**: Add LLM-as-Judge for 2-3 key dimensions
3. **Day 5**: Integrate into development workflow

### Week 3: Iteration
1. Run evals on current system (baseline)
2. Make one improvement
3. Measure impact
4. Repeat

## Measuring Success

### Key Metrics
- **Pass rate**: % of outputs meeting quality bar
- **Regression catch rate**: Issues caught before production
- **Iteration velocity**: Time from idea → validated improvement
- **Confidence level**: Team trust in making changes

### Leading Indicators
- Engineers reference eval results in PRs
- Evals run automatically in CI/CD
- Eval failures block deployments
- Team adds new test cases proactively

## Skill Development

**Why This Is The Hottest New Skill**
1. **Emergent requirement**: Didn't exist 2 years ago
2. **Universal need**: Every AI product needs it
3. **High leverage**: Small investment, huge impact
4. **Competitive advantage**: Teams with evals ship faster

**Who Needs This Skill**
- Product Managers (define quality criteria)
- Engineers (implement eval systems)
- AI researchers (validate model improvements)
- QA teams (expand test coverage)

## Real-World Impact

### Before Evals
- Prompt changes → Hope for the best
- User complaints → Reactive fixes
- Slow iteration → Fear of breaking things
- No metrics → Unclear if improving

### After Evals
- Systematic measurement → Confidence in changes
- Proactive quality → Catch issues early
- Fast iteration → Data-driven decisions
- Clear metrics → Track progress

## Advanced Topics

### LLM-as-Judge Deep Dive
```python
# Simplified concept
rubric = """
Evaluate email quality on:
1. Addresses question: Yes/No
2. Professional tone: Yes/No
3. Has next steps: Yes/No

Output: JSON with scores + reasoning
"""

score = llm.evaluate(
    output=generated_email,
    rubric=rubric
)
```

### Continuous Eval Pipeline
```
User Request → AI Application → Eval System → Metrics Dashboard
                    ↓                          ↑
                Production                  Feedback
                    ↓                          ↑
              Logging System ←→ Regression Suite
```

## Resources

### Learn More
- **Maven Course**: Hamel Husain & Shreya Shankar's AI Evals course
  - 2,000+ students trained
  - Teams from OpenAI, Anthropic, major AI labs
  - #1 course on Maven

### Community
- Trained 500+ companies
- Active sharing of best practices
- Rapidly evolving field

## Key Takeaways

1. **Evals = Data analytics for AI products**
   - Systematic measurement replaces guessing
   - Highest ROI activity for AI builders

2. **Start simple, iterate fast**
   - Open coding → Rubric → Automated evals
   - One person can start, team can scale

3. **Domain expertise > Perfection**
   - Trust your product taste
   - Actionable > Perfect

4. **Make it systematic**
   - Run continuously
   - Track over time
   - Build institutional knowledge

5. **New essential skill**
   - Required for competitive AI products
   - Separates good from great teams
   - Career differentiator

---

**Course**: Taught by Hamel Husain & Shreya Shankar  
**Scale**: 2,000+ PMs/engineers across 500 companies  
**Testimonial**: "The number one course on Maven"  

*"This is the deepest yet most understandable primer you'll find on the world of evals."* — Lenny Rachitsky
