import pandas as pd, json
df = pd.read_csv('data/ola_bookings_clean.csv')
days = sorted(df.Date.unique()); di = {d:i for i,d in enumerate(days)}
def codes(col):
    vals = sorted(df[col].dropna().unique()); m = {v:i for i,v in enumerate(vals)}
    return vals, df[col].map(m).fillna(-1).astype(int).tolist()
vt, v = codes('Vehicle_Type'); st, s = codes('Booking_Status'); pm, p = codes('Payment_Method')
cr, c = codes('Canceled_Rides_by_Customer'); dr, r = codes('Canceled_Rides_by_Driver'); ir, i = codes('Incomplete_Rides_Reason')
succ = df.Booking_Status.eq('Success')
cust = sorted(df[succ].Customer_ID.unique()); cm = {x:k for k,x in enumerate(cust)}
rows = dict(d=df.Date.map(di).tolist(), v=v, s=s, p=p, c=c, r=r, i=i,
  inc=df.Incomplete_Rides.eq('Yes').astype(int).tolist(),
  val=df.Booking_Value.fillna(0).astype(int).tolist(), km=df.Ride_Distance.fillna(0).astype(int).tolist(),
  dr=(df.Driver_Ratings*10).round().fillna(-1).astype(int).tolist(), cr=(df.Customer_Rating*10).round().fillna(-1).astype(int).tolist(),
  cu=df.Customer_ID.map(cm).fillna(-1).astype(int).tolist())
D = dict(days=days, vt=vt, st=st, pm=pm, cr=cr, dr=dr, ir=ir, cust=cust, rows=rows)
html = open('dashboard/template.html', encoding='utf-8').read().replace('/*DATA*/null', json.dumps(D, separators=(',',':')))
open('dashboard/index.html','w',encoding='utf-8').write('<!doctype html>\n<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">\n'+html.replace('<title>','<title>',1)+'\n</html>')
open('dashboard/artifact.html','w',encoding='utf-8').write(html)
print(len(html)/1e6,'MB', st, pm, ir)
