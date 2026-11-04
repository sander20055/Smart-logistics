# FreshWay Outbound project brief

Prepared 4 November 2026. Repository snapshot: sander20055/Smart-logistics, main, a6d4b67b62b1b75b78ad039312a58158dbcc8ad1. 144 files downloaded. 120 non-image source files extracted for review, including two duplicate helper copies; data profiles cover all supplied CSVs/workbooks. Images indexed and brand assets visually reviewed. Original files remain unchanged. Actual submitted SA4 was additionally read from the prior saved report/presentation because the repository SA4 folder contains partial contributions.

## Purpose and scope
Design an integrated future logistics solution for the fictional FreshWay supermarket chain. Outbound handles store replenishment from three DCs to 120 stores and the EFC shuttle. SA5 builds on window-aware planning/live ETA proposals in SA3 and arrival-risk/unloading prediction with human approval in submitted SA4.

## Agreed vision
One shared company AI server/platform hosts separately governed departmental applications. Outbound's models predict arrival risk and unloading time. No other department's model is specified. Shared infrastructure is the team's design direction; purchase, integration and rollout are not approved or implemented merely because the team agreed it.

## SA5 design
Proposed partial self-organisation in a planning workspace: trip agents choose and revise tentative options, exchange feasibility/slack and resolve competing provisional reservations. Planners approve every actual operational change. Demonstrate local cooperation/adaptation before calling the implementation self-organising. Pure prediction or central alerts remain decision support.

## Evidence and constraints
19,242 unique deliveries, 14 October 2024–11 January 2025. Supplied on_time: ZE87.47%, other98.38%; inclusive-window calculation88.56%/94.08%. 58 end-boundary disagreements require definition confirmation. ZE appointments30min, others60min; planned arrivals always opening+15min. 45min is non-ZE remaining margin. No required-versus-accepted quantities/POD/departure logs, so full OTIF and causal replay unavailable. Team CSV includes488 appended analysis rows.

Case OTIF97.2%/target98.5%, cost~EUR7.73/target7.00, cages/route45.4/target52 are case references and norms. Sample allocated cost/cageEUR7.1237 and route-specific utilisation73.19% are separate calculations. No measured AI gains, planner45→10min reduction, binding95% ZE norm or guaranteed savings.

C03: subcontract store trucks diesel-only, booking cutoffs and ZE fine liability unresolved. C10:20of22ZE stores lack trailer-compatible docks;37 stores have pre07:00 noise conditions, IDs unresolved. C11: TMS Routiq cloud paid position API; contract31Mar2027, WMS renewal notice31Dec2026, BI cloud roadmap2027. C09: price interfaces, test peak volume, check power/space/cooling and operating continuity before procurement. Storage owns Energy & Capacity; Incoming owns Compliance; E-commerce owns Customer Promise.

Fixed counterparties: Orderpicking, Inventory & SCM, Delivery to consumers. Include the latter for agreed shared constraints without inventing vehicle sharing or live van training data.

## Humans and deliverables
Authors: Sander van de Pol; Quinten Poppinga; Made Bhisma Satya Nugraha (roster spelling, confirm against preferred spelling); Scholte van Ringelestijn; Francesco Gatteschi. Lecturers: Frits Coers and Wilbur Hage.

SA5 requires recent academic literature, technology→behaviour→effect→value impact map, system coordination/adaptation, bounded decision handover/reclaim, cross-delivery and receiver's own usable-receipt response. Report and maximum3slides, Board Memo, APA7, honest AI declaration. Final portfolio also needs rubric map/evidence appendix. Planned2November deadline is past on preparation date4November; actual Brightspace state unverified.

## Reading order
Study Guide v2; Lesson6slides20–25 and lesson page; Company dossier A2/A4/A5; Outbound department file; submitted SA3/SA4; current SA5 contributions; relevant board cards; dictionaries and raw datasets; rubric/checklist. Review receipts/Decision Log separately: no confirmations were supplied. See Work/ for specialist reviews and reproducible calculations.
