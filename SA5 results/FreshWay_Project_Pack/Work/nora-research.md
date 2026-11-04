# Nora: academic research and source verification

## Verified source and read scope

Reviewed Quinten's SA5 research/concept text and SA4 AI concept/use-case text in the repository extractions. Reviewed the actual course deployment-evidence ladder in Lesson 2, slides 49–50, with corroborating examples in Lesson 5. Opened the complete Wiley full-text article URL (1,798 retrieved lines) and the University of Twente full PDF URL (6,766 retrieved lines), inspected their introductory and bibliographic content, and verified the publisher/university metadata. The retrieval exposed full text, but I did not complete a sequential reading of all 66 article pages before this handoff. A local download/extraction attempt was interrupted. Do not describe my work as a complete full-paper reading. The coordinator separately checked the article's Table 7 and the simulation/deployment counts.

Verified reference:

Gerrits, B., van Heeswijk, W., & Mes, M. (2024). Towards self-organizing logistics in transportation: A literature review and typology. *International Transactions in Operational Research, 31*(3), 1309–1374. https://doi.org/10.1111/itor.13408

Publisher full text: https://onlinelibrary.wiley.com/doi/full/10.1111/itor.13408

University record: https://research.utwente.nl/en/publications/towards-self-organizing-logistics-in-transportation-a-literature-/

University-hosted PDF: https://research.utwente.nl/files/349276501/Int_Trans_Operational_Res_-_2023_-_Gerrits_-_Towards_self_organizing_logistics_in_transportation_a_literature_review_and.pdf

The article first appeared online on 2 December 2023. Its final issue date is May 2024. APA 7 should use 2024 for the final volume/issue/page reference, as Quinten does. The PDF's early-publication header shows 2023 and pages 1–66, which should not replace the final metadata.

## Material corrections

1. Quinten's Tier 1 classification is incorrect under this course's criteria. The course uses deployment maturity, not an academic-quality hierarchy. Peer review does not establish a Tier 1 implementation, nor does it prove that a paper's method or conclusions are necessarily sound.
2. Lesson 2 slide 49: Tier 1 means an implementation running in production with quantified results in accountable investor/audited reporting and independent journalistic examination. Tier 2 means a dated company-announced deployment with named partner/site scale and independent trade reporting.
3. Lesson 2 slide 50: Tier 3 means pilot, proof of concept, or plan; identify it as such. Tier 4 means vendor marketing or untraceable figures, suitable only for labelled illustration. The assignment post asks for Tier 1/2/3, but course criteria also include Tier 4, so do not hide the latter when assessing weak evidence.
4. Gerrits et al. is credible academic synthesis, not one identifiable deployed implementation with one overall deployment tier. Describe its research role and the maturity of reviewed applications separately. FreshWay case documents are authoritative within the teaching case, not real-company Tier 1 deployment proof. The proposed FreshWay platform/agents belong to concept or pilot maturity (Tier 3), with no operational benefits established.
5. Do not confuse validation method with maturity: the coordinator verified that 115 studies have simulation maturity, while the validation-method simulation count is 92. Five are classified as deployed. Phrase the counts using the exact column and avoid implying that every simulation-maturity study uses the same validation method.
6. Quinten's phrase that peer review 'proves the method was sound' should be removed. Peer review is a screening process, not proof of correctness or deployment.
7. Quinten's working description of the FreshWay SA5 pilot still leaves every plan-changing action to a planner. Automatic prediction, alerting, and publishing alone do not demonstrate that logistics decisions are delegated. The report must identify the precise bounded coordination decision delegated to the system, distinguish a proposed later design from the current validation pilot, and avoid claiming full self-organisation already exists.
8. Platform centralisation and control centralisation are different. A shared host can support distinct software decision rights, but merely naming per-trip software modules 'agents' does not establish autonomy or cooperative adaptation. The interaction protocol and delegated decision must be explicit.
9. Placement in the article's autonomy/cooperativeness framework is a FreshWay design interpretation, not a measured or externally validated score. Quinten already warns that boundaries are not rigid; retain that qualification and avoid certainty about a quadrant.

## Usable short research synthesis

Gerrits et al. (2024) connect self-organising transport logistics with delegated decisions and interactions between autonomous actors. Their typology distinguishes the control structure from intelligence, information location and cooperation. This supports describing precisely which actor may decide, which other actors constrain that decision, and how coordination adapts when conditions change. It does not prove a benefit from FreshWay's proposed platform. The study synthesises literature rather than testing FreshWay's grocery replenishment process. Its deployment evidence remains limited, so service, workload and cost effects require a pilot comparison.

## FreshWay design implications (our proposal)

Retain SA4's arrival-risk and unloading-duration predictions and planner approval for departure changes, stop-order changes and driver instructions. Distinguish the shared company infrastructure decision from Outbound's own models and rules. Within approved interfaces, a narrow future system decision could coordinate and revise a provisional readiness proposal or reservation against counterparties' declared capacity, then present the feasible option to the planner. A proposal message becomes a confirmed operational commitment only through the agreed receiving process. The exact decision rights need genuine counterpart confirmation.

Keep early-arrival risk, downstream store windows, charging/vehicle availability and data freshness in feasibility checks. These are FreshWay requirements and design choices, not findings tested by Gerrits et al. Model retraining and authority-boundary changes need separate controls: a model may update predictions without acquiring new decision rights.

## Other references and unresolved verification

Quinten's SA5 section cites one academic article: Gerrits et al.; its identity and metadata are verified. SA4's multiple supporting articles were inventoried from Quinten's text but not independently checked in this review. Do not present them as newly verified here. The coordinator identified a Schulte/Voss citation in another teammate contribution as suspect; I did not verify that reference or DOI. Exclude it until the exact title/authors/DOI and relevant full text are checked. Do not call it fabricated without conclusive evidence.

## Traceable course/source locations

- `Lessons/2026_Lesson 2 - Smart logistics and business intelligence.pptx`, slides 49–50: deployment evidence tiers.
- `Lessons/2026_Lesson 5 - AI in logistics.pptx`, slides 17–19: practical Tier 1/2/2–3 examples and independent-source caveats.
- `Outbound-teams/SA5/SA5 Outbound – Research and concept (Quinten).docx`, sections 1.3, Sources and Table 5: incorrect working tier definition; sections 2.1–2.2 and Table 2: proposal versus actual decision delegation.
- `Outbound-teams/SA4/SA4 Outbound – AI concept and use cases (Quinten).docx`, sections 1.1 and 1.6: predictive support and human approval boundaries.

No source files were modified. This is a research handoff, not a statement of operational approval, submission, counterpart acceptance or full-article reading completion.
