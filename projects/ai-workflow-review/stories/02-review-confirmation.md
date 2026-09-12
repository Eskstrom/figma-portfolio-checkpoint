# Story 2: Separating review completion from a positive decision

[Project overview](../README.md) · [Full case study](../CASE-STUDY.md) · [Next story](03-verification-recovery.md)

## Situation

The qualification workflow asked reviewers to assess supporting documentation against individual requirements and confirm an overall result. That decision affected the handoff to subsequent work.

## Observation

An accurate Not Qualified result could still create hesitation at an action labeled Everything looks right. The reviewer needed to know whether the action confirmed the assessment or approved the referral.

The ambiguity exposed two separate meanings: the review was correct, and the referral met the requirements.

## Design decision and collaboration

I kept individual criteria and the overall qualification result explicit, and treated review completion as a separate decision. A reviewer could confirm an accurate negative assessment.

The confirmation refinement used task-specific language such as Confirm assessment and explained the next step. Technology and operations partners needed a shared understanding of what confirmation meant and which outcome the downstream workflow received.

![Qualification screen showing the earlier confirmation wording](../assets/09-preview.png)

## Outcome

Reviewers understood that confirming their work did not automatically qualify the referral. The interaction made the meaning of completion clearer while retaining the negative business outcome.

## Learning

Success has several meanings in a workflow. The interface must distinguish completing a task correctly from reaching a positive business result, particularly when confirmation triggers additional work.

## Artifact note

The gallery preserves the captured Everything looks right state. It illustrates the original ambiguity and the separation between criteria, final outcome, and completion. The confirmation-language refinement described above is not shown in that captured state.
