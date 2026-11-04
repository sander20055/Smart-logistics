# Daan — data and KPI review for SA5

Review date: 4 November 2026. All results below are calculations from supplied teaching-case data, not observations of a deployed FreshWay AI system. Reproduction: run `daan_analyse.py` with the bundled Python interpreter. Detailed values and source inventory are in `daan-metrics.json`.

## Sources inspected and their meaning

- Full transaction files: `FreshWay/store_replenishment.csv`, its identical copy under `Data/Outbound/`, and the team copy `Outbound-teams/store_replenishment (1).csv`. Master records: stores, vehicles, sites, products and suppliers.
- Complete relevant data dictionaries across FreshWay, Outbound, Orderpicking, Storage, E-commerce and D2C. Data-domain CSV schema inventory and row counts appear in the JSON. Spreadsheet extraction covers all supplied workbooks; D2C workbook sheets were reviewed as contextual evidence, not used to claim an Outbound operational result.
- `FreshWay/Dataset guide.pdf`, pp. 1–4; `FreshWay/Department file — Outbound transport.pdf`, pp. 1–3; `FreshWay/Company dossier.pdf`, A2, A4 and A5.
- `Outbound-teams/SA3/FreshWay_Outbound_SA3_Report_Costs_Corrected.pdf`, pp. 1–5. It already accurately flags missing departure times, required quantities, 58 flag mismatches and inconsistent consecutive-stop timings.
- Francesco's SA4/SA5 Section3 reports and corresponding supplied SA4/SA5 presentations. These contributions contain usable evaluation ideas but numerous unsupported baseline/target and benefit claims.
- C03 and C10, now supplied: C03 describes subcontracted diesel double-deck vehicles and booking constraints. C10 describes dock constraints and 37 noise-conditioned permits without naming the affected store IDs. Neither explains why every planned arrival is +15 minutes after window opening.
- Team Data log workbook: requested complete-roll-cage data were marked incomplete/not available on 23 September; later handover lines lack completion/receipt confirmation. This is evidence of a dependency, not proof a live interface exists.

## Authoritative source selection and duplicate handling

The raw FreshWay and Data/Outbound CSVs are identical after parsing: **19,242 rows and 25 fields**. Use the FreshWay raw CSV as the calculation source.

The semicolon-delimited team copy contains **19,730 physical parsed rows**, but only **19,242 valid delivery IDs**. Its first 19,242 rows match the raw source in every cell when read as strings. The remaining **488 rows are appended spreadsheet-style analysis, blank rows and notes**, without delivery IDs. Do not count them as deliveries or train a model on them. Parse with the correct delimiter, retain raw files unchanged and require a nonmissing unique delivery_id.

The delivery period is **14 October 2024 to 11 January 2025**, over **76 operating dates**, 120 stores and **11,513 distinct route IDs**. Dataset Guide's stated overall calendar ends 12 January 2025, a Sunday; that is compatible with this six-day store-delivery file ending on Saturday. All original 25 fields are nonmissing in the raw D1 file; this does not establish completeness of unrecorded business events.

## Verified punctuality and timing baselines

| Measure | ZE stores | Other stores | Overall |
|---|---:|---:|---:|
| Store count | 22 | 98 | 120 |
| Deliveries | 3,847 | 15,395 | 19,242 |
| Supplied on_time TRUE | 3,365 | 15,146 | 18,511 |
| Supplied flag percentage | 87.47% | 98.38% | 96.20% |
| Recalculated arrival at/before closing, inclusive | 88.59% | 98.48% | 96.50% |
| Arrival inside both inclusive delivery-window bounds | 88.56% | 94.08% | 92.97% |
| Supplied-flag vs inclusive-close mismatches | 43 | 15 | 58 |
| Delivery-window length | 30 min | **60 min** | varies |
| Planned arrival after opening | +15 min | +15 min | +15 min |
| Remaining planned margin before closing | 15 min | **45 min** | varies |
| Mean actual minus planned arrival | +7.14 min | +10.46 min | +9.80 min |
| Early arrivals before opening | 1 | 678 | 679 |
| Arrivals more than five minutes before opening | 0 | 321 | 321 |
| Recorded unloading mean | 41.13 min | 40.61 min | 40.71 min |
| Recorded unloading median | 40 min | 37 min | 38 min |

All **58 flag mismatches occur exactly at the recorded window-end minute**, where the supplied flag is false but actual_arrival <= window_end is true. This may reflect timestamp rounding or the underlying generation/comparison rule. Do not silently replace the source flag or claim the supplied percentages are inclusive-window punctuality. State the rule, preserve both results and obtain data-owner confirmation before setting a pilot baseline.

The 87.47%/98.38% pair from SA3 remains valid **only as the supplied flag baseline**. For a provisional transparent operational definition, use inside both inclusive bounds, reporting ZE **3,407/3,847 = 88.56%** alongside the earlier supplied figure. Changing definitions creates an apparent improvement without any process change; the same rule must apply to control and intervention.

The strict five-minute early-arrival guardrail would currently be 0% for ZE and **2.09%** for other stores, or 1.67% overall. Therefore “<2% early arrivals” must specify cohort and be agreed as a proposed threshold. It is not a known company norm.

Do not conflate the transaction-level 30/60-minute appointment windows with the `stores.csv` **morning** acceptance windows, 06:00–08:00 for ZE and 06:00–11:00 for others. D1 also includes afternoon CDC deliveries. Francesco's wording that ZE transaction windows are “predominantly 06:00–08:00” mixes different grains. Any planner must enforce the appropriate verified appointment, store acceptance, permit and noise restrictions together.

## Punctuality is not true OTIF

D1 contains delivered cases/cages and arrival timestamps. It lacks required order quantities, acceptance/receipt confirmation, damaged/short-delivered amounts and explicit completeness flags. Consequently, **none of its arrival percentages measures OTIF**.

The departmental case file prints **97.2% OTIF now / 98.5% target** (p. 2). Treat these as **stated case baseline and company target**, not the recalculated D1 result. The file's measurement framing and the missing full-quantity records warrant reconciliation. The 97.2% number also does not equal D1's 96.20% supplied arrival flag and must never be relabelled an arrival proxy.

True OTIF requires a delivery-keyed agreed required quantity (including accepted changes/cut-offs), actual accepted delivered quantity/POD, damage and shortage handling, and agreed timing semantics. Orderpicking's **sampled** lines have order_ref and error flags but are not a complete delivery-order ledger; daily picking summaries are aggregated by date/site/shift/order type/zone and cannot establish a specific store delivery's completeness. `demand_inventory.csv` is described at store/product-group/day grain and is **not proven to be a delivery_id-level receiving log**. It is not present in this repository. Thus Francesco's proposed direct join “delivery_id to demand_inventory” is unsupported. Propose an Interface Agreement for the missing delivery-level contract/POD data instead of claiming the join works.

## Cost and utilisation: stated figures versus measured ratios

| Measure | Supplied case statement | Recalculated D1 sample | SA5 treatment |
|---|---:|---:|---|
| Cost per delivered cage | approximately EUR 7.73 | **EUR 7.1237** | Label scope difference; reconcile allocation before savings claims |
| ZE cost per delivered cage | not separately stated | EUR 7.8725 | Sample allocated cost ratio |
| Non-ZE cost per cage | not separately stated | EUR 6.9811 | Sample allocated cost ratio |
| Average cages per route | 45.4 | **45.1264** | Case reference and sample are different values |
| Company target cages per route | 52 | no result | Company target, not achieved by AI |
| Company target cost per cage | EUR 7.00 | no AI result | Company norm, not a guaranteed pilot saving |

Calculation uses total allocated `cost_trip_eur` (**EUR 3,701,054.56**) / total rc_ambient+rc_chilled+rc_frozen (**519,540 cages**). The dictionary states cost_trip_eur is a cost allocation **per stop**, including driver time, distance, fixed stop charge and planning overhead. Sum each delivery row once. No need to divide by route count again, and no justification to multiply EUR 7.73 minus EUR 7.00 by an invented 2.1 million yearly volume. Dossier's stated 6,220 cages/day ×312 days is approximately **1.94 million**, and neither extrapolation proves AI savings. Do not annualise a holiday-heavy thirteen-week sample naively.

Actual truck capacities vary: tractor-trailer **66 cages**, city trailer **40**, rigid **30** (`vehicles.csv`, `capacity_rc`). In D1 there are no routes exceeding their joined vehicle cage capacity. Across observed routes, total cages divided by total route-specific capacity is **73.19%**, and the mean route-level cage/capacity ratio is **73.24%**. Dividing every route by 66 understates capacity utilisation for smaller urban vehicles. Keep 45.4/66=69% as a case reference for double-deck framing, not the measured all-vehicle utilisation rate.

Master vehicles contain both own and hired/subcontracted assets: 54 owned trucks and 82 owned vans, plus 261 subcontracted tractor IDs and 184 hired vans. The file's larger row count is not evidence that FreshWay owns that fleet. The truck and van vehicle_id sets are distinct, so D2C and Outbound cannot be joined as one physical fleet through vehicle_id. The same street does not imply transferable unloading times or unrestricted shared data rights.

The mathematical target scenario 45.4/52 gives 12.69% fewer routes **only if volume, vehicle type, service windows, stops and routing feasibility remain constant**. A shared AI prediction service does not establish those conditions. Remove “increases to 52” and “reduces trips by over 12%” as achieved/predicted effects. Instead measure utilisation as a network guardrail while testing the scoped punctuality intervention.

## Additional data-quality and model limitations

**Consecutive stop timing.** For 3,068 of 7,729 nonfirst stops, actual arrival precedes previous actual arrival + previous unloading_time_min + current driving_time_min. Example: RT-20241014-0002's second store arrives at 15:45 although the preceding arrival, unloading and recorded next-leg drive imply at least 16:05. No departure time is recorded. These values can support descriptive comparisons and candidate model exploration but do not support a faithful causal route replay without correction/interpretation by the data owner.

**Targets and predictors.** Use unloading_time_min as the target for an unloading-duration model, not a predictor for that same stop. Use actual_arrival/on_time/late minutes as evaluation labels, not predispatch inputs. Final driving_time_min, energy_used and cost_trip_eur are postexecution values and leak outcomes into predispatch arrival-risk predictions. A loaded cage count is valid only if it was known at recommendation time; timestamps and event versioning are needed. Previous-stop actual duration can become a live feature only once actually observed.

**Missing live predictors.** Historical D1 does not contain GPS traces, departure/loading readiness timestamps, queue times, weather, traffic observations, model prediction timestamps, charger state of charge, energy schedules, source freshness or model versions. These require proposed interfaces and prospective logging. A common server alone supplies none of them. Do not claim D2C data continuously retrains Outbound ETA models. Validate relevance, coverage, contractual access, refresh latency and performance first.

**Data split.** Train on earlier route-days and evaluate on later unseen days, with all stops of a route in the same split. Fit preprocessing/aggregates using training data only. Test separate ZE/site/vehicle/window and peak-week groups. Compare store/load historical medians or the current planner/TMS estimate against a model using the same prediction horizon and available-at-the-time features. Store-only medians estimated over the entire thirteen weeks leak test outcomes. Arrival-risk metrics should include calibration and precision/recall at an agreed intervention threshold; unloading MAE alone does not evaluate arrival risk or operational improvement.

## Timestamp sensitivity is not a pilot result

Purely subtracting five minutes from all historical ZE actual arrivals yields 96.75% at/before close and 96.13% inside both bounds, versus 88.59%/88.56% without the subtraction. Ten minutes yields 99.04%/94.83%, and fifteen minutes yields 99.38%/84.22%. This illustrates the growing risk of early arrivals. It is **arithmetic sensitivity only**, assuming unchanged travel/unloading and fully feasible earlier departures. It is not a forecast, simulation validation or evidence that FreshWay can achieve 95%. Do not put these figures on the headline SA5 slide unless explicitly labelled as a noncausal sensitivity illustration. A live test must check load readiness, driver hours, vehicle suitability, downstream stops, store/permit limits and Storage constraints.

## Specific corrections to Francesco's Section 3

1. Replace established autonomous fleet/charging orchestration with the proposed scoped shared-platform coordination design. An AI server and dispatch predictions have not been deployed.
2. Remove unsupported causal attribution of punctuality failures to windows. Evidence shows an association and margin constraint, not all individual root causes.
3. “ZE punctuality >=95%”, MAE <5min, <2% early arrivals and four-week duration are proposed pilot choices unless a genuine Board decision confirms them. No ZE company norm is supplied.
4. Remove the invented static baselines (<80% ZE, EUR8.20/cage,40cages), planner45min→10min, seven existing AI silos, guaranteed licence savings, exact GPU contention hours and savings from fines. No measurement/source supports them.
5. Preserve EUR7.73/7.00 and45.4/52 only as case reference/target; show recalculated sample separately where useful.
6. Correct arbitrary references to “empirical grid baseline”: 1.5MVA is a stated contracted limit, not inference from D1. Active-power MW cannot be subtracted from apparent-power MVA without power-factor conditions. Storage owns the applicable Energy & Capacity File and operational headroom. Do not treat approximately0.44MW headroom as a fixed safe charging budget or an inference-server capacity budget.
7. Add required-vs-received quantity and POD dependency for OTIF; do not fabricate SCM receiving logs, implemented IA names or receipt confirmations.
8. Use a staged evaluation: corrected historical baseline, shadow recommendations, limited planner-approved route changes, comparison with matched/control route-days, route-cluster uncertainty and simultaneous guardrails. The study duration/sample size depends on the effect worth detecting and observed variability. Four weeks is a proposal, not evidence of statistical power.

## Recommended SA5 KPI wording

“Outbound will test whether shared-platform arrival-risk and unloading-time predictions support feasible earlier planning for selected ZE deliveries. Historical supplied on_time flags equal87.47% for ZE stops; a recalculation including both recorded window boundaries equals88.56%, and the definition requires data-owner confirmation. The company states OTIF98.5% and cost EUR7.00/cage targets, but the pilot cannot claim OTIF without agreed required-versus-accepted quantity data. The evaluation will compare the same timestamp definition across matched route-days and monitor early arrivals, other-store punctuality, cost per cage, planner time and system availability. Improvements and savings remain hypotheses.”

All necessary ownership, interface and target approvals remain proposed until confirmed by their actual owners. No source or source file was altered.
