# Watch & Unlock

**OTT rewarded-advertising concept · Wireframe checkpoint · 13 September 2026**

Viewers earn platform tokens by finishing eligible episodes, choosing to watch sponsor ads, and optionally completing a short sponsor demo. They can redeem tokens for viewing benefits, starting with skipping one eligible ad break.

[Full case study and Figma brief](CASE-STUDY.md) · [28-screen gallery](SCREENS.md) · [Wireframe notes](WIREFRAMES.md) · [Verification](VERIFICATION.md)

![Episode-completion offer](prototype/screens/tv-01.svg)

## What is saved

- Detailed product concept, proposed token economy, and screen-by-screen design instructions.
- 28 grayscale vector screens: eight core TV screens, four mobile states, ten recovery and wallet states, and six playback states.
- An offline click-through prototype with review controls for simulated completion and cross-device handoff.
- Verification notes covering the main journey, balance transitions, recovery paths, and layout checks.

## The value exchange

**Episode complete: 5 tokens → Ad complete: 20 → Sponsor demo complete: 25 → Redeem one ad-break skip: 0.**

The viewer can continue watching without accepting the optional ad. Scanning a QR code alone does not earn the follow-up bonus. Redemption identifies the exact episode and one eligible ad break; it does not promise an entire ad-free episode.

## Review the prototype

Download or clone the repository, then open [`prototype/index.html`](prototype/index.html) in a browser. No installation or server is required. GitHub displays this file as source; it is not a hosted live-preview link.

Click product controls to follow the journey. Use the labeled review controls to simulate ad completion, mobile handoff, and reward confirmation. Tab moves through controls, Enter or Space selects, and Escape returns. Production TV directional-focus behavior is annotated rather than implemented.

## Figma handoff

TV frames are 1920 × 1080; mobile frames are 390 × 844. Import files from [`prototype/screens/`](prototype/screens/) and follow the [design instructions](WIREFRAMES.md#import-into-figma).

A [Figma draft](https://www.figma.com/design/R6I5AHFaQCs4r7FltVYoi6) was created, but its Starter-plan connector limit prevented adding design nodes. The SVG screens are in this repository; the Figma draft remains blank. SVG import does not create native Auto Layout, component variants, or prototype links, and imported text behavior depends on Figma and available fonts.

## Evidence and limitations

This is a concept and storyboard prototype. Token values, advertiser economics, and viewer motivations are hypotheses. No user study, production trial, advertiser partnership, or measured commercial outcome is claimed. Media, QR claims, sign-in, transactions, and synchronization are simulated; no real accounts or reward services are connected.

Next steps: create native Figma components and links, validate TV remote navigation, test reward comprehension with viewers, and assess the unit economics of rewards.

[← Return to the design portfolio](../../README.md) · [GitHub profile](https://github.com/Eskstrom)
