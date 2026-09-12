# Designing human review across an AI workflow

[Back to project](README.md) · [Screen gallery](SCREENS.md)

## Context and ownership

I designed this workflow review experience as the sole designer. The product context was healthcare operations: documents move through tasks involving patient separation, document classification, information extraction, insurance verification, and qualification.

I conducted focused testing and shadowing with technical workers, and brought experience from my previous Firstsource BPO role. That background informed my attention to operational exceptions and the practical work surrounding an automated result.

## The central problem

An extracted answer alone is not enough for a reviewer to act on. They need to understand which person or document it belongs to, inspect supporting information, correct it when necessary, and know what confirming the task means.

The screen set suggests three connected design responsibilities:

| Responsibility | Interface response |
|---|---|
| Make an interpretation inspectable | Keep the document beside the extracted fields, with source-link and refocus controls |
| Match the controls to the decision | Use page grids for assignment, fields for extraction, and criteria for qualification |
| Keep the work operationally visible | Show queue counts, processing times, workflow membership, and reviewer status |

These responsibilities provide a coherent interpretation of the design artifacts. They are not presented as verbatim findings from a research report.

## Decision 1: Keep source evidence beside editable output

The extraction workspace places the source document on the left and editable patient, document, and diagnosis information on the right. Source-link icons and a refocus control give the reviewer a way to return to the evidence while examining the structured interpretation.

The design intent is to reduce the work of navigating between evidence and answer. Highlighting helps indicate where to inspect; it should not be read as proof that an extracted value is correct.

![Extraction workspace](assets/03-preview.png)

The same task also includes a lower contact-details state. This matters because reviewing the first visible fields does not mean the entire record has been checked. The screenshots establish that additional fields exist; they do not establish automatic validation or a completion-blocking rule.

## Decision 2: Make document ownership spatial

Patient splitting uses selectable page thumbnails and a patient list showing page ranges. The selected patient and selected pages are visible together, with an explicit Save action during editing. The key relationship is between a person and a set of pages, so the interaction exposes that relationship directly.

This accommodates a packet that contains more than one patient, a case that a simple one-document/one-person model would miss. Document tagging uses a related grid but changes the assignment target to document type.

![Page assignment to patients](assets/05-preview.png)

The original screenshot includes a loading state in the completion action. This reconstruction preserves that visible state. Cancellation, retry, and duplicate-assignment behavior would need additional specification before implementation; they cannot be inferred from a static image.

## Decision 3: Separate review completion from business outcome

The qualification interface presents individual criteria, a final decision, and the action **Everything looks right**. Some criteria pass and others fail while the overall result is **Not Qualified**.

The important distinction is that the reviewer can confirm an accurate negative assessment. Treating every completion as a positive approval would collapse two different meanings into one action.

![Qualification criteria and final decision](assets/09-preview.png)

This is the strongest end-to-end interaction to discuss in a portfolio interview: evidence, individual judgments, the overall outcome, and confirmation are visible in one workspace. The current label also creates a useful design critique: task-specific wording such as “Confirm review” could make that distinction clearer. That wording is a future refinement, not a claim about the original shipped interface.

## Decision 4: Preserve task differences within a shared structure

Eligibility uses grouped patient, payer, subscriber, and plan information with an explicit verification status. Benefits review includes a completion/failure choice. Medication extraction groups dates, schedule, route, units, and dose in repeated sections.

The shared structure creates familiarity, while the right-hand controls adapt to the shape of the task. These screens support a story about designing a family of review experiences across many entities rather than forcing every result into one generic form.

## Decision 5: Connect individual review to team operations

The workflow dashboard exposes pending work and processing-time patterns. The people view adds membership, active status, completed counts, and an Add People search state. Together, these screens show that the product includes both doing the work and managing who can handle it.

![Workflow dashboard](assets/01-preview.png)

The displayed metrics describe interface content. They are not evidence of a measured project outcome.

## Research and evidence boundaries

**Established context:** original authorship, sole design ownership, focused testing, shadowing with technical workers, and prior Firstsource experience.

**Visible in the artifacts:** the screen structure, controls, field groupings, source references, page-selection states, criteria-level statuses, and queue/people views.

**Not established in this public record:** participant counts, interview quotations, a precise before/after iteration tied to observation, rollout history, engineering collaboration anecdotes, or measured impact. Those details should be added only from the original project records.

## What I would evaluate next

For a future evaluation, I would measure whether reviewers locate the relevant evidence, identify deliberately introduced errors, preserve page-to-patient assignments, and distinguish a confirmed negative result from a failed review. Task completion time would be considered alongside correction accuracy and unintended confirmations.

These are proposed evaluation criteria, not results from the original testing.

## Deliverable status

This portfolio reconstruction contains ten static screen states. Public document illustrations and identities are synthetic. Editable SVG geometry is included, with approximate icons and typography. It does not include production code, model integration, a reusable Figma component library, or a connected prototype.
