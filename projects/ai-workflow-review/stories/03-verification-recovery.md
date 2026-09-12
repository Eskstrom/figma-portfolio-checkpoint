# Story 3: Recovering when an integration cannot provide an answer

[Project overview](../README.md) · [Full case study](../CASE-STUDY.md) · [First story](01-evidence-review.md)

## Situation

Insurance verification sat within a broader authorization workflow. Staff depended on external information, while the process also needed to accommodate incomplete inputs, unsuccessful lookups, and manual verification.

## Observation

Operations partners described leaving the platform to verify information elsewhere after a lookup failed. Technology partners understood the integration issue, but the reviewer-facing state needed to distinguish a negative coverage result from missing information or an unsuccessful retrieval.

Those situations required different next steps, even when they initially appeared similar on screen.

## Design decision and collaboration

I separated the status of verification from the coverage result. Unable to verify represented an unresolved check; a completed check displayed its substantive result separately.

The recovery path supported correcting missing information, retrying where appropriate, or recording manual verification with its source and time. Operations partners defined what staff needed to continue working. Technology partners clarified available system states and recovery actions. My role was to express those distinctions in a way reviewers could act on.

![Eligibility review workspace](../assets/07-preview.png)

## Outcome

Staff could understand why a case remained unresolved and choose an appropriate next step. The next person handling the case could see whether verification had occurred and where the result came from, reducing repeated investigation.

## Learning

An unavailable answer should remain visibly unresolved. Distinguishing an integration problem from a negative result preserves the meaning of the next handoff in an automated workflow.

## Artifact note

The gallery shows the verified eligibility state, providing the workspace context for this story. It does not include the failure and manual-recovery states described here. Records and document illustrations are synthetic; outcomes are qualitative.
