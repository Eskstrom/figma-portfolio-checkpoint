[← Project overview](README.md)

# Watch & Unlock — Wireframes v1

Wireframe package based on the [Watch & Unlock case study](CASE-STUDY.md). **28 vector screens** in the verified milestone.

## Open and review

After cloning or downloading this repository, open [`prototype/index.html`](prototype/index.html) in a browser. GitHub’s file view displays HTML source instead of running the prototype. It works offline and contains every screen. Click product buttons to follow the flow; use the labeled review controls to simulate ad completion, mobile handoff, and cross-device confirmation. Use Tab / Enter / Space for accessible selection and Escape to go back. This is a click-through prototype; production TV directional-focus handling is not implemented.

The canonical balance is **5 → 20 → 25 → 0**. Restart the journey from the toolbar. The sidebar also opens individual screen states for review; jumping via the sidebar is not a real transaction.

## Import into Figma

1. Open the [created Figma file](https://www.figma.com/design/R6I5AHFaQCs4r7FltVYoi6).
2. Drag the SVGs from [`prototype/screens/`](prototype/screens/) onto the canvas. TV artboards are 1920 × 1080; mobile artboards are 390 × 844.
3. Group TV-01 through TV-08 in order. Put mobile screens beneath the QR handoff and edge states in a separate row.
4. The SVGs contain vector shapes and text. Depending on Figma’s importer and installed fonts, text may be outlined; inspect it before editing. SVG import does not create Auto Layout, component variants, or prototype connections.
5. Recreate shared buttons, balance pills, notices, and cards as native Figma components using the specifications in the [case study](CASE-STUDY.md). Use Inter if available; the preview falls back to Arial offline.
6. Wire the main path: TV-01 → TV-02 → TV-03 → TV-04 → M-01 → M-02 → M-03 → TV-05 → TV-06 → TV-07 → Play-reserved → Play-applied.

The Figma file was created successfully, but the connector hit its Starter-plan MCP tool limit before design nodes could be added. **The wireframes are included in this repository; they have not been added to that Figma file.**

## What is simulated

All artwork, ads, video playback, QR codes, authentication, sponsor destinations, rewards, and synchronization. No credentials are collected. No network services are required by the prototype. Token prices and eligibility rules are concept assumptions, not validated commercial terms.

## Saved progress

| Local checkpoint | Saved contents |
| --- | --- |
| 01-tv | First eight TV screens |
| 02-complete | TV, mobile handoff, and recovery states |
| 03-verified | Final 28-screen set and verification notes |

This repository contains the latest verified screen set. Historical checkpoint folders remain in the local working package; they are not Git commits or Figma version-history entries.

Read the [verification notes](VERIFICATION.md) for completed checks and limitations, or [browse the screen gallery](SCREENS.md).

## Screen inventory

| Screen | Purpose | Spendable tokens |
| --- | --- | ---: |
| tv-01 | Episode complete | 5 |
| tv-02 | Optional sponsor ad | 5 |
| tv-03 | Ad reward confirmed | 20 |
| tv-04 | Continue on your phone | 20 |
| tv-05 | Wallet and rewards | 25 |
| tv-06 | Confirm redemption | 25 |
| tv-07 | Reward activated | 0 |
| tv-08 | Token activity | 0 |
| m-01 | Confirm account on phone | 20 |
| m-02 | Watch sponsor demo | 20 |
| m-03 | Mobile bonus confirmed | 25 |
| m-signin | Sign in to claim tokens | 20 |
| edge-wallet-20 | Wallet · more tokens needed | 20 |
| edge-wallet-5 | Wallet · more tokens needed | 5 |
| edge-wallet-0 | Wallet · more tokens needed | 0 |
| edge-exit | Leave ad | 5 |
| edge-pending | Reward pending | 5 |
| edge-pending-activity | Pending activity | 5 |
| edge-expired | QR code expired | 20 |
| edge-unavailable | No reward ads | 5 |
| edge-refund | Reward refunded | 25 |
| edge-failed | Activation failed | 25 |
| play-0 | Episode 4 playback | 0 |
| play-5 | Episode 4 playback | 5 |
| play-20 | Episode 4 playback | 20 |
| play-25 | Episode 4 playback | 25 |
| play-reserved | Episode 4 playback · reserved | 0 |
| play-applied | Episode 4 playback · applied | 0 |

## Source and regeneration

[`prototype/build_wireframes.py`](prototype/build_wireframes.py) uses Python’s standard library. Run commands from `projects/watch-and-unlock/prototype/`. Run `python build_wireframes.py tv` for the TV milestone, `python build_wireframes.py full` for the full package, or `python build_wireframes.py verified` for the verified milestone. Screens use named groups, reusable drawing helpers, and a consistent grayscale style. The generator preserves milestone directories and creates a ZIP for sharing.
