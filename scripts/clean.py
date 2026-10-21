import pandas as pd, sys
src, out = sys.argv[1], sys.argv[2]
df = pd.read_csv(src, na_values=['null'], encoding='utf-8-sig', low_memory=False)
df = df.dropna(how='all')                         # trailing empty rows
df = df.drop(columns=[c for c in df.columns if c.startswith('Unnamed') or c=='Vehicle Images'])
df = df.dropna(subset=['Booking_ID'])
df['Date'] = pd.to_datetime(df['Date'])
df['Time'] = df['Date'].dt.strftime('%H:%M:%S')
df['Date'] = df['Date'].dt.date
df['Canceled_Rides_by_Customer'] = df['Canceled_Rides_by_Customer'].replace({'AC is Not working':'AC is not working'})
df.to_csv(out, index=False)
print(df.shape)
