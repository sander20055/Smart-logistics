# Milan — architecture review for FreshWay SA5

Status: source-based architecture review. The source extracts listed below were read. The generated final report was not inspected because the local execution connection failed during this agent's turn. This memo therefore validates the proposed architecture and states the material conditions the final report must preserve.

## Validated direction and continuity

The shared AI platform is a proposed company-wide infrastructure decision. Outbound's two models are proposed departmental applications: arrival/window-risk prediction and unloading-duration prediction. The platform does not imply that the other six departments use these same models, grant unrestricted data access, or already have approved model requirements. The user has chosen the shared-platform direction; implementation and expenditure approval have not been evidenced.

Retain the existing TMS, WMS and board computers. SA3's corrected data-flow presentation proposes delivery-window-aware planning and ETA monitoring using existing systems and a paid export API; it reserves route decisions for the planner. The SA4 concept section and slide likewise describe predictive decision support, with every operational route change approved by the planner. The root agent has additionally identified the submitted SA4 report from Library as the authoritative prior version; use that version in the final report rather than treating every repository contribution as an approved final design.

## Existing landscape versus proposed additions

Company dossier A5 (pp. 11–13) states that the TMS has an API to the WMS and a batch connection to ERP. Its existence does not prove that route release, picking sequence, departure readiness or reliable events are already exchanged. The dossier explicitly says route planning and pick sequence are not linked. Board computers exist in all 54 tractors. Position data sits in the TMS vendor's cloud. The BI warehouse has nightly loading and provides no real-time source. An IoT platform exists, with MQTT ingestion, but that does not establish an available live feed for this application.

Proposed additions are an authenticated API/event adapter, validation and event history, isolated Outbound model services, provisional coordination services, a planner review console, a release interface, and monitoring. The shared platform supplies identity, role permissions, model registry/versioning, audit logs, scheduling and support. It must keep departmental data and operational write permissions separate. A model must not acquire TMS/WMS write privileges merely because it can read data.

Hosting remains an unresolved deployment decision. C11 shows a mixture of cloud and on-premise systems and a funded cloud-data-platform move in 2027. Compare an extension aligned with that roadmap against new managed capacity before buying a physical server. Do not prescribe GPU count, CPU/RAM, capacity, availability percentage or euro cost without model benchmarks, concurrent departmental workloads, event frequency, retention, security and recovery requirements. Training and bulk analytics can consume spare capacity or run on separate queues; operational predictions require a protected priority and an agreed degradation policy. These are proposed requirements, not existing capabilities.

## Bounded self-organisation that preserves human route approval

Prediction, alerts and publishing data alone do not demonstrate self-organisation. The scoped proposal can demonstrate it in provisional planning: individual trip services select and revise feasible candidate options under a common policy, while a reservation/readiness service represents shared loading-resource constraints and conflict decisions. A trip service responds to new ETA or readiness evidence, requests a tentative reservation, receives acceptance or conflict information, and adjusts its own candidate. Other trip services also respond to changed availability. The repeated local interactions adapt the set of provisional plans rather than merely refreshing one central prediction.

This is partial self-organisation of planning coordination. It is not evidence of deployed self-organising transport. It is first tested in shadow mode, with simulated or provisional reservations and no actual effect on picking priorities, drivers, charging or route release. If the implementation is actually a single central optimiser producing all candidates, describe it as central adaptive planning instead of claiming decentralised self-organisation.

The proposed policy must define authorised candidate choices, validated time/access/vehicle/capacity constraints, reservation lifetime and conflict rule, maximum iterations or coordination deadline, required data freshness, escalation conditions, and cancellation/rollback behaviour. Their numerical values and operational authorisation remain to be agreed. No agent invents or learns its own permission envelope.

### Decision rights

| Decision | Proposed authority | Boundary and revocation |
|---|---|---|
| Refresh arrival-risk/unloading forecasts | Outbound model service | Only validated inputs and approved model versions; stop or mark unavailable on stale/invalid data |
| Select/revise a provisional route option | Trip coordination service | Only inside approved candidate envelope; no TMS release |
| Accept/reject tentative loading reservation | Reservation/readiness service | Agreed capacity and conflict rules; tentative only in shadow phase; expiry and cancellation required |
| Alter actual route, departure, driver instruction or picking priority | Responsible human planner/department owner | Explicit approval and release; rejected proposals have no operational effect |
| Allocate charging capacity | Storage's authorised process | Outbound requests feasibility; it cannot override Storage's Energy & Capacity File |
| Commit spend/platform scope | Board/company governance | No approval inferred from the student vision or a draft memo |
| Disable coordination or withdraw delegation | Authorised Outbound manager/platform operator | Kill switch invalidates pending proposals/reservations; operate last approved plan manually |

Released routes need an explicit version and acknowledgement from the TMS/driver workflow. Reject stale proposals if the underlying plan or constraint version changed. On platform, feed or model failure, continue the last approved plan and manual exception handling. Do not send cached predictions as if current. Cancel tentative reservations when a proposal expires, a planner rejects it, or automation is disabled. Outage recovery should reconcile event and plan versions before coordination resumes.

## Interface requirements to agree

The TMS feed needs route/stop/delivery IDs, current plan version, vehicle, planned arrivals/windows, trustworthy departure and progress timestamps, event timestamp and receipt timestamp. Paid API access, latency, licence scope and outage behaviour need confirmation. Outbound historical CSV data is not a live interface.

Orderpicking owns the operational readiness data it supplies. Agree the meaning and timeliness of cage quantities/readiness and the join key before using them. The supplied daily picking summary is too coarse to prove individual trip readiness. Any loading-reservation exchange is proposed and requires its own interface/acceptance agreement. Do not infer readiness from scan counts without a confirmed definition.

Retail/store constraints include dock type, permitted vehicle, agreed receiving window, street/noise rules and unloading conditions. C10 does not provide the store-level list of all noise-restricted permits. Unknown restrictions must remain unresolved feasibility inputs, not default to permission. Inventory & SCM receives confirmed actual quantities and arrival information. GPS alone cannot prove quantities delivered or OTIF. Storage supplies charging/resource constraints through its authorised interface; no Outbound charging controller is introduced.

Every interface needs owner/consumer, fields and keys, units and timestamp/timezone, event and freshness semantics, quality checks, permitted purpose/access, retention, change/version policy, support and fallback, and receiving-department confirmation. No receiver signature or usable cross-delivery is claimed without their actual response.

## New board-card implications

| Source | Verified case finding | Consequence for SA5 |
|---|---|---|
| C03, p. 1 | Store haulier has refrigerated Euro VI diesel vehicles, no electric units; booking by 14:00 day before (Monday by Saturday noon); guaranteed up to 120 trucks/day, above best effort; contract unclear on ZE fines | A subcontractor candidate is not automatically ZE-feasible. Vehicle suitability/access and contractual limits must be hard constraints. Same-day capacity cannot be assumed. C03 does not explain the fixed +15-minute scheduling offset. |
| C09, pp. 1–2 | FreshFlow stopped after average-volume sizing failed at December peaks, late-priced closed integration, power limits and unbudgeted operating continuity | Benchmark peak workload; agree interface scope and quote before purchase; obtain power/cooling/space evidence for on-premise hosting; budget support, migration and coexistence. Do not claim staff savings before peak and baseline tests. |
| C10, p. 1 | 100 trailer-dock stores (2 ZE), 14 rigid-only (all ZE), 6 street-level (all ZE); 37 residential stores require quiet cages/no reversing alarm before 07:00; leased changes require consent | Model unload time with vehicle/dock/load context. Earlier arrival options must respect verified local permits and receiving windows. ZE effects are confounded by dock/access mix. C10 does not identify why every historic planned arrival is window_start +15 minutes. Building changes are a separate consent requirement, not part of this initial prediction/coordination proposal. |
| C11, pp. 1–2 | Routiq TMS is cloud, contract ends 31 Mar 2027, paid position API; WMS on-premise expires 30 Jun 2027, notice by 31 Dec 2026; WCS closed paid changes; cloud data platform planned in 2027 | Reuse and align procurement with actual renewal decisions. Routiq is the case TMS; PTV examples must not be attributed to Routiq. Existing EUR 0.45m TMS annual cost is not the incremental AI investment. The server/platform is not funded merely because a data-platform project is already committed. |
| C12, pp. 1–2 | Case assigns cold-chain responsibility and evidence obligations, with limits for subcontracted recovery | Treat temperature and cold-chain controls as hard operational boundaries. ETA improvement cannot waive them. The incident register is not a measured benefit from this proposal. Do not expand SA5 into an autonomous food-safety controller. |
| C05, p. 1; Storage dept pp. 3–4 | Storage owns Energy & Capacity File; existing 8 electric tractors differ from hypothetical 54-truck electrification; grid and night-window constraints are distinct | Request current constraints for affected routes. Do not claim all trucks electric or invent shared charging availability. Server power/cooling needs belong in hosting feasibility, with no unbenchmarked demand figure. |
| C06, pp. 1–2; C07, p. 1 | Promotion accuracy differs sharply by period; attributable promotion shrink lacks method; shrink kg and euro measures differ | Pilot and training validation should cover peak context; no claim that ETA models directly improve demand forecasting or deliver shrink savings. Other departments own those requirements. |

## Proposed gates

1. Validate sources, timestamps, definitions and actual store/vehicle/contract constraints; resolve permissions and interface semantics.
2. Agree/price adapters and hosting options, load-test normal and peak scenarios, establish support/fallback and approve the coordination envelope.
3. Test forecasts against simple historical store/load baselines with chronological evaluation. Test coordination in shadow mode for conflicts, expiry, data loss and operator stop.
4. Have the relevant owners review evidence and authorise a limited operational pilot. Every actual route or picking change retains its human release owner. Compare effects on pilot and nonpilot deliveries and cost/workload guardrails.
5. Scale only after measured evidence and a separate implementation decision. SA5 does not claim any gate complete.

## Material corrections for the final report

- Use “proposed partial self-organisation in provisional planning” while reservations remain shadow-only. Define actual mutual adaptation, not just a prediction-refresh loop.
- State clearly that thresholds, priority rules, interface permission and deployment approval are pending; do not imply a live delegated operational decision already exists.
- Preserve the distinction between current WMS–TMS API and proposed loading/readiness coordination. Existing connectivity does not prove required event semantics or write operations.
- Replace any “C03/C10 missing” statement with “now reviewed, with store-level permit detail and reason for +15-minute offset still unresolved.”
- Correct unrestricted early-arrival proposals: C10 adds noise/access conditions, and C03's diesel subcontractor cannot be assumed ZE-admissible.
- Retain human approval for every operational route change. No invented Orderpicking priority changes, charging authority, other-department models, completed pilot, savings or signatures.

## Source pointers read

FreshWay/Company dossier.pdf, A2–A5; FreshWay/Dataset guide.pdf, pp. 1–5; FreshWay/Department file — Outbound transport.pdf, pp. 1–4; Data/C1 TM C12/Board cards C03, C09, C10, C11, C12, all pages; Data/Storage/Board card C05, all pages; Data/Storage/Department file — Storage.pdf, all pages; Data/SCM/C06 and C07, all pages; Outbound-teams/SA3/FreshWay_Outbound_SA3_Data_Flow.pptx, slides 1–3 and notes; repository SA4 Quinten concept/slide and SA5 Tech slide text. Earlier multi-file output also exposed parts of the corrected SA3 support report but did not establish a complete review of that report. No claim is made here that the generated final SA5 report was inspected.
