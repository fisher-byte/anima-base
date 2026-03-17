---
title: Feature Prioritization Decision Framework
author: Lenny Rachitsky
topic: Product Management, Prioritization, Startups, PMF
tags: [prioritization, product-management, pmf, startups]
last_updated: 2026-03-17
verification_status: verified
---

# Feature Prioritization Decision Framework

> Most prioritization advice is for large companies with established features. For early-stage pre-PMF startups, different frameworks apply.

## Overview

**Lenny's Core Insight**: Startup prioritization ≠ Large company prioritization

**Startup reality**:
- You're like a newly lit fire: exciting but fragile
- Make a few wrong moves, and it dies
- You have no PMF, no growth flywheel, no margin for error
- You can't afford to be "data-driven"—you don't have enough data

**Large company reality**:
- You have momentum and fuel
- You're optimizing what already works, not creating something new
- You have room for error—big wins make up for many mistakes

**The goal**: Make 10 customers **very** happy (not 100 customers lukewarm).

---

## The Startup Prioritization Framework

### Pre-PMF Decision Hierarchy

**At pre-PMF stage**, every decision should serve this single goal:

> **Make 10 customers very happy**

**Decision criteria**:
1. Does this make a customer happier?
2. Is this customer in our target segment (ICP)?
3. Is this the most important problem for them?
4. Can we deliver this quickly?
5. Does this increase retention?

**If yes to all**: Do it.
**If no to any**: Defer or skip.

---

## Common Prioritization Pitfalls

### ❌ Pitfall 1: Solving "Vitamin" Problems

**Problem**: Building nice-to-have features that make life slightly easier

**Examples of vitamins**:
- Email templates (can't use them if product doesn't solve email overload)
- UI polish (users don't stay if core value isn't there)
- Convenience features (nice to have but not critical)

**Examples of painkillers** (what to build instead):
- Email overload (Superhuman—product is literally solving this)
- Compliance burden (Vanta—can't operate without it)
- Payment processing (Stripe—core to business)

**Decision test**:
> "Can your users do their job well WITHOUT your product?"

- **No**: Painkiller (build this)
- **Yes**: Vitamin (deprioritize this)

### ❌ Pitfall 2: Trying to Be "Data-Driven"

**Problem**: You don't have enough data for meaningful insights

**Lenny's calculation**:
If you want to increase conversion by 10% (from 20% to 22%), you need **5,000+ users** to experience that change to have statistical significance.

**Startup reality**: You have 10-100 users, not 5,000.

**Decision rule**: Use data for direction, not proof. In early stages:
- **Use**: User interviews, observation, qualitative feedback
- **Don't use**: A/B testing (not enough sample size), statistical analysis

### ❌ Pitfall 3: Too Much Theory, Not Enough Building

**Problem**: Founders (particularly ex-PMs) with incredibly detailed strategy docs and beautiful decks who don't ship often enough

**Symptoms**:
- 50-page strategy documents
- Quarterly roadmaps when you haven't shipped anything this month
- Perfect plans that never execute

**Decision rule**: If you're holding back because you're not sure which direction to go, **just ship something**.

**Lenny's insight from Airbnb**:
> While I was at Airbnb, I'm pretty sure majority of our experiments had zero (or negative) impact. But we continued to grow because we had strong PMF, a word-of-mouth flywheel, and a growing market, and we found enough big wins to make up for many mistakes. You have none of these advantages at an early-stage startup.

**Translation**: In early stage, ship fast to find what works. You don't have PMF to protect you from mistakes.

### ❌ Pitfall 4: Doing Everything Your Users Ask

**Problem**: Users will (unknowingly) deceive you about what they need

**Why users deceive**:
- They diagnose problems (wrongly)
- They prescribe solutions (wrongly)
- They don't know what's possible
- They optimize for their job, not your business

**Example**:
- User says: "I need feature X"
- Real problem: "I can't accomplish goal Y efficiently"
- Your solution: Feature Z (simpler, better for many users)

**Julianna Lamb (Stytch CTO)**:
> "We have a philosophy when it comes to building product that we shouldn't just build either what competitors are doing or take at face value what customers are asking for. Rather, we dig deeper to understand problem they're trying to solve and what optimal solution could be. Maybe someone thinks that x is a solution to problem y—but if you just build x without understanding problem y, you often shortchange yourself. There's actually a more elegant or better solution to problem y that you'll only find if you understand the root issue first."

**Decision rule**: Focus on **pain points**, not feature requests. Then design the best solution to that pain.

---

## Evidence-Based Prioritization: Confidence Meter + LNO

### The Confidence Meter Framework

**From Itamar Gilad (via Lenny)**

**For each idea**, rate confidence 1-10 on:
- User validation (interviews, surveys)
- Problem clarity (do we understand it?)
- Market signals (are people looking for this?)
- Execution capability (can we build it?)
- Technical risk (will it work?)

**Decision thresholds**:
- **1-3**: Don't pursue yet (not enough validation)
- **4-6**: Consider with caution, test with 5-10 users
- **7-8**: Prioritize and build
- **9-10**: Top priority, full investment

**When to build**:
- Confidence 7+ AND
- Solves real pain (not nice-to-have) AND
- Fits ICP (target segment) AND
- Fits within runway

**Example**: Adding social features to email client
- Confidence: 4/10 (users haven't asked for it)
- Pain: Low (email is productivity tool, not social)
- ICP: Doesn't fit (high-frequency, speed-obsessed users)
- Decision: Don't build, deprioritize

### The LNO Framework

**From Shreyas Doshi (via Lenny)**

**Three types of work**:
- **L (Low-hanging fruit)**: Quick wins, visible impact, fixes bugs
- **N (New opportunities)**: Innovation, differentiation, new growth areas
- **O (Optimization)**: Improving existing value

**Decision rule**: Maintain balance across L-N-O categories

**Pre-PMF bias**:
- Focus on **L** (fix critical bugs, show users you're responsive)
- Focus on **N** (find PMF through innovation)
- Avoid **O** (don't optimize product that doesn't fit yet)

**Example decision matrix**:

| Initiative | Type | Confidence | Pain Level | ICP Fit | Decision |
|-----------|-----|-----------:|----------:|--------:|--------:|
| Fix critical bug | L | 10/10 | High | ✅ | Do now |
| Add social features | N | 4/10 | Low | ❌ | Skip |
| Improve onboarding | O | 8/10 | High | ✅ | After critical bugs |
| Explore new market | N | 3/10 | Unknown | ❌ | Skip |
| Optimize database | O | 7/10 | Medium | ⚠️ | Later |

---

## The GIST Model for Roadmapping

**From Itamar Gilad**

**What is GIST?**
- **G**oals: High-level outcomes
- **I**deas: Features/initiatives
- **S**teps: Tactical tasks
- **T**asks: Individual work items

**How to use**:
1. Start with **Goals** (e.g., "Increase retention to 50%")
2. Brainstorm **Ideas** to achieve goals (e.g., "Improve onboarding", "Add feature X")
3. Break ideas into **Steps** (e.g., "Research user drop-off", "Design new onboarding")
4. Create **Tasks** for each step (e.g., "Interview 5 users", "Wireframe new flow")

**Decision benefits**:
- Links every task to strategic goals
- Makes trade-offs explicit (which goals matter most?)
- Enables rapid iteration (move tasks around without rebuilding roadmap)
- Separates "what" (goals/ideas) from "how" (steps/tasks)

---

## Prioritization Decision Flow

### For Pre-PMF Startups

```
Idea comes up
    ↓
[Decision: Does this solve real pain?]
    ↓ No → Skip
    ↓ Yes
[Decision: Is this for our ICP?]
    ↓ No → Deprioritize
    ↓ Yes
[Decision: What's confidence level?]
    ↓ 1-3 → Need more validation
    ↓ 4-6 → Test with 5-10 users
    ↓ 7-10 → Consider building
    ↓
[Decision: What type of work?]
    ↓ L (quick fix) → Do now
    ↓ N (innovation) → Prioritize if >7 confidence
    ↓ O (optimization) → Deprioritize until PMF
    ↓
[Decision: Can we deliver in < 2 weeks?]
    ↓ No → Break down or skip
    ↓ Yes → Build and ship
    ↓
Measure: Retention, happiness, NPS
    ↓
[Decision: Did this make users happier?]
    ↓ Yes → Double down
    ↓ No → Learn and adjust
```

### For Post-PMF Companies

**After PMF**, additional factors apply:
- **Impact size**: Will this affect many users?
- **Strategic alignment**: Does this support long-term goals?
- **Resource efficiency**: What's the ROI of engineer time?
- **Market opportunity**: Does this create differentiation?

**Decision matrix**:

| Factor | Pre-PMF Weight | Post-PMF Weight |
|--------|--------------:|--------------:|
| Pain level | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| ICP fit | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| Confidence | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| Impact | ⭐⭐ | ⭐⭐⭐⭐⭐ |
| Strategic value | ⭐ | ⭐⭐⭐⭐ |
| Resource efficiency | ⭐ | ⭐⭐⭐⭐ |

---

## Practical Decision Rules

### Rule 1: Never Prioritize Based on Competitors

**Problem**: "Competitor has this feature, so should we"

**Lenny's insight**: Don't compare feature lists. Competitors may have built features users don't actually want.

**Decision rule**: Build features your **users actually use** and derive value from, not what competitors have.

**How to check**:
- Look at your usage data
- Interview users about what they value
- If nobody's using a feature, kill it (even if competitor has it)

### Rule 2: Prioritize for Retention, Not Acquisition

**Problem**: Building features to attract new users at expense of existing users

**Lenny's insight**: In early stage, retention > acquisition. If you can't keep users, don't waste resources acquiring them.

**Decision rule**: Prioritize features that:
- Increase Day 7/30 retention
- Increase usage depth
- Increase NPS (users recommend product)

**Deprioritize**:
- Features that bring vanity metrics (page views, downloads)
- Features that don't increase retention
- Features that complicate product without value

### Rule 3: The "10 Happy Customers" Test

**For every decision**, ask:
> "Will this make our best 10 customers happier or more successful?"

- **Yes**: Prioritize
- **No**: Deprioritize
- **Don't know**: Talk to those 10 customers first

**Why this works**: Early stage, you don't have PMF. Your early adopters are your path to PMF. Making them very happy is your only job.

### Rule 4: Avoid "Feature Checklist" Thinking

**Problem**: Building everything competitors have

**Lenny's insight**: "I see startups comparing feature lists. They're like: 'Competitor has features A, B, C, D, so we need A, B, C, D, and E (to differentiate). They build features nobody uses."

**Decision rule**: Focus on:
- What features do users actually use?
- What features increase retention?
- What features users pay for?
- What features create differentiation?

**Kill features** that:
- Nobody uses
- Don't increase retention
- Don't align with positioning
- Create bloat/confusion

---

## Case Example: Startup Prioritization

### Scenario: B2B SaaS in pre-PMF stage

**Context**:
- 50 users
- Product: Developer tool
- No PMF yet (retention 30%)
- Runway: 9 months

**Idea backlog**:
1. Add social features (users asked for it)
2. Improve documentation (onboarding friction)
3. Add API integrations (competitor has it)
4. Fix critical bug (users complaining)
5. Redesign dashboard (looks dated)

**Prioritization decisions**:

| Idea | Pain Level | ICP Fit | Confidence | Type | Decision |
|------|----------|---------|-----------|-----|---------|
| Fix critical bug | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | 10/10 | L | ✅ Do now |
| Improve documentation | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | 8/10 | O | ✅ After bug |
| Add social features | ⭐ | ⭐ | 4/10 | N | ❌ Skip |
| Add API integrations | ⭐⭐ | ⭐⭐ | 3/10 | N | ❌ Not yet |
| Redesign dashboard | ⭐⭐ | ⭐⭐⭐ | 6/10 | O | ⚠️ Later |

**Rationale**:
- Fix bug: Makes users happier immediately (L)
- Documentation: Reduces onboarding friction (O, but high confidence + pain)
- Social features: Nice-to-have, doesn't solve core pain (N, but low confidence)
- API integrations: Competitor has it, but users not asking (N, low confidence)
- Dashboard: Looks matter, but not critical to success (O, medium confidence)

**Execution**:
1. Fix bug (1 week)
2. Measure: Did retention improve?
3. Improve documentation (2 weeks)
4. Measure: Did onboarding improve?
5. Reassess backlog

---

## Related Resources

- [Prioritizing at Startups - Lenny](/people/product/lenny-rachitsky/articles/prioritizing-at-startups.md)
- [Becoming Evidence-Guided - Itamar Gilad](https://www.lennysnewsletter.com/p/becoming-evidence-guided-itamar-gilad)
- [Shreyas Doshi Interview - LNO + Pre-Mortems](/people/product/lenny-rachitsky/podcasts/2022-06-07-shreyas-doshi.md)
- [Lenny's Decision Frameworks Collection](/people/product/lenny-rachitsky/articles/lenny-decision-frameworks-comprehensive.md)
- [PMF Decision Scenarios](/people/product/lenny-rachitsky/articles/pmf-decision-scenarios.md)

---

**Key insight**: In early stage, simplicity beats sophistication. Focus on making 10 customers very happy through solving real pain they have. Every decision should serve this single goal. Everything else is distraction.
