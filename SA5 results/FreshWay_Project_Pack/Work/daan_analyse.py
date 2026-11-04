from pathlib import Path
import json, hashlib
import pandas as pd

import sys
B=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path(__file__).resolve().parents[1]
O=Path(__file__).parent
files=[B/'FreshWay/store_replenishment.csv',B/'Data/Outbound/store_replenishment.csv',B/'Outbound-teams/store_replenishment (1).csv']
frames=[pd.read_csv(p,sep=None,engine='python') for p in files]
d=frames[0].copy()
for c in ['date','planned_arrival','actual_arrival']: d[c]=pd.to_datetime(d[c])
for c in ['window_start','window_end']:d[c+'_dt']=pd.to_datetime(d['date'].dt.strftime('%Y-%m-%d')+' '+d[c])
d['window_min']=(d.window_end_dt-d.window_start_dt).dt.total_seconds()/60
d['planned_offset_min']=(d.planned_arrival-d.window_start_dt).dt.total_seconds()/60
d['planned_margin_min']=(d.window_end_dt-d.planned_arrival).dt.total_seconds()/60
d['delay_from_plan_min']=(d.actual_arrival-d.planned_arrival).dt.total_seconds()/60
d['recalc_by_close']=d.actual_arrival<=d.window_end_dt
d['inside_slot']=(d.actual_arrival>=d.window_start_dt)&d.recalc_by_close
d['early']=d.actual_arrival<d.window_start_dt
d['early_gt5']=d.actual_arrival<d.window_start_dt-pd.Timedelta(minutes=5)
d['late_min']=((d.actual_arrival-d.window_end_dt).dt.total_seconds()/60).clip(lower=0)
d['cages']=d[['rc_ambient','rc_chilled','rc_frozen']].sum(axis=1)
def summarize(x):
 return dict(n=len(x),stores=x.store_id.nunique(),routes=x.route_id.nunique(),supplied_on_time_n=int(x.on_time.sum()),supplied_on_time_pct=100*x.on_time.mean(),recalc_by_close_n=int(x.recalc_by_close.sum()),recalc_by_close_pct=100*x.recalc_by_close.mean(),inside_slot_n=int(x.inside_slot.sum()),inside_slot_pct=100*x.inside_slot.mean(),early_n=int(x.early.sum()),early_gt5_n=int(x.early_gt5.sum()),early_gt5_pct=100*x.early_gt5.mean(),flag_mismatch_n=int((x.on_time!=x.recalc_by_close).sum()),window_minutes=x.window_min.value_counts().sort_index().to_dict(),planned_offset_minutes=x.planned_offset_min.value_counts().sort_index().to_dict(),planned_margin_minutes=x.planned_margin_min.value_counts().sort_index().to_dict(),mean_deviation_min=x.delay_from_plan_min.mean(),mean_unloading_min=x.unloading_time_min.mean(),median_unloading_min=x.unloading_time_min.median(),unloading_p90_min=x.unloading_time_min.quantile(.9),late_n=int((x.late_min>0).sum()),late_minutes_total=x.late_min.sum(),cages=int(x.cages.sum()),cost_total_eur=x.cost_trip_eur.sum(),cost_per_cage_eur=x.cost_trip_eur.sum()/x.cages.sum())
routes=d.groupby('route_id').agg(cages=('cages','sum'),stops=('delivery_id','size'),vehicle=('vehicle_id','first'),date=('date','first'),cost=('cost_trip_eur','sum'))
v=pd.read_csv(B/'FreshWay/vehicles.csv');s=pd.read_csv(B/'FreshWay/stores.csv')
capacity_col=[c for c in v if 'capacity' in c and ('cage' in c or 'rc' in c)]
consecutive=d.sort_values(['route_id','stop_sequence']).copy()
consecutive['prev_arrival']=consecutive.groupby('route_id').actual_arrival.shift()
consecutive['prev_unload']=consecutive.groupby('route_id').unloading_time_min.shift()
consecutive['minimum_arrival']=consecutive.prev_arrival+pd.to_timedelta(consecutive.prev_unload+consecutive.driving_time_min,unit='min')
bad=consecutive[consecutive.actual_arrival<consecutive.minimum_arrival]
mismatch=d[d.on_time!=d.recalc_by_close]
astr=pd.read_csv(files[0],dtype=str); bstr=pd.read_csv(files[2],sep=';',dtype=str)
comparison=dict(freshway_vs_data_outbound_identical=frames[0].equals(frames[1]),team_physical_rows=len(bstr),team_valid_delivery_rows=int(bstr.delivery_id.notna().sum()),team_extra_analysis_rows=int(bstr.delivery_id.isna().sum()),team_valid_rows_match_source=astr.equals(bstr[bstr.delivery_id.notna()].reset_index(drop=True)))
result=dict(source_files=[str(p.relative_to(B)) for p in files],source_comparison=comparison,period=dict(first=str(d.date.min().date()),last=str(d.date.max().date()),operating_dates=d.date.nunique(),duplicate_delivery_ids=int(d.delivery_id.duplicated().sum()),missing=d.isna().sum().to_dict()),overall=summarize(d),ze=summarize(d[d.ze_zone]),nonze=summarize(d[~d.ze_zone]),routes=dict(n=len(routes),mean_cages=routes.cages.mean(),median_cages=routes.cages.median(),mean_stops=routes.stops.mean(),max_cages=int(routes.cages.max()),over66_n=int((routes.cages>66).sum())),mismatch_examples=mismatch[['delivery_id','actual_arrival','window_end_dt','on_time']].head(8).astype(str).to_dict('records'),all_mismatches_exactly_window_close=bool((mismatch.actual_arrival==mismatch.window_end_dt).all()),consecutive_stop_issues=dict(n=len(bad),out_of_possible=int(consecutive.prev_arrival.notna().sum()),examples=bad[['delivery_id','route_id','actual_arrival','minimum_arrival']].head(5).astype(str).to_dict('records')),master_stores=dict(n=len(s),ze_n=int(s.ze_zone.sum()),unloading_windows=s.groupby(['ze_zone','unloading_window_start','unloading_window_end']).size().to_dict()),vehicle_columns=v.columns.tolist(),vehicle_capacity_columns=capacity_col)
if capacity_col:
 rc=routes.merge(v,left_on='vehicle',right_on='vehicle_id',how='left'); cap=capacity_col[0];result['capacity']=dict(by_vehicle=v[v.vehicle_id.isin(routes.vehicle)][['vehicle_id',cap]].to_dict('records'),overcapacity_n=int((rc.cages>rc[cap]).sum()),weighted_utilization=rc.cages.sum()/rc[cap].sum(),mean_route_utilization=(rc.cages/rc[cap]).mean())
result['data_domain_inventory']=[]
for p in B.rglob('*.csv'):
 try:
  t=pd.read_csv(p,sep=None,engine='python')
  result['data_domain_inventory'].append(dict(path=str(p.relative_to(B)),rows=len(t),columns=t.columns.tolist()))
 except Exception as e:result['data_domain_inventory'].append(dict(path=str(p.relative_to(B)),error=str(e)))
# Hypothetical timestamp translations only: no causal claim and no feasible route rescheduling.
result['ze_timestamp_translation_sensitivity']={str(shift):dict(by_close_pct=100*((d[d.ze_zone].actual_arrival-pd.Timedelta(minutes=shift))<=d[d.ze_zone].window_end_dt).mean(),inside_slot_pct=100*(((d[d.ze_zone].actual_arrival-pd.Timedelta(minutes=shift))>=d[d.ze_zone].window_start_dt)&((d[d.ze_zone].actual_arrival-pd.Timedelta(minutes=shift))<=d[d.ze_zone].window_end_dt)).mean()) for shift in [0,5,10,15]}
def clean(o):
 if isinstance(o,dict):return {str(k):clean(v) for k,v in o.items()}
 if isinstance(o,list):return [clean(x) for x in o]
 if hasattr(o,'item'):return o.item()
 return o
(O/'daan-metrics.json').write_text(json.dumps(clean(result),indent=2),encoding='utf-8')
print(json.dumps(clean({k:v for k,v in result.items() if k not in ['capacity','period','mismatch_examples','master_stores']}),indent=2))
