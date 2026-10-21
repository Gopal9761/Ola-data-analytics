# Ola Ride Analytics: Bengaluru, July 2024

An end-to-end data analytics project on 40,539 ride bookings. It covers data cleaning in Python, 10 business questions in SQL, and an interactive 5-view dashboard.

**Live dashboard:** `https://<your-github-username>.github.io/ola-ride-analytics/dashboard/` (see "Publish the dashboard" below)

## Business questions
How many rides are completed, where is revenue coming from, why do rides get cancelled, and how do customers and drivers rate each other?

## Key findings
| Metric | Result |
|---|---|
| Total bookings | 40,539 over 30 days (1 to 30 July 2024) |
| Success rate | 62.2% (25,207 rides) |
| Revenue from successful rides | ₹1,37,62,477 (avg ₹546 per ride) |
| Cancelled by driver | 17.8% (top reason: personal and car-related issues, 34.7%) |
| Cancelled by customer | 10.1% (top reason: driver not moving towards pickup, 29.9%) |
| Driver not found | 10.0% |
| Incomplete rides | 6.1% of successful rides (customer demand and vehicle breakdown are about equal) |
| Payments | Cash 54.8% of revenue, UPI 40.6%, cards 4.6% |
| Distance | Auto rides average 10 km; every other vehicle averages about 25 km |
| Ratings | Driver 4.00 and customer 3.99 on average, almost no correlation (-0.01) |
| Weekly pattern | Weekend and weekday volumes are within 2% of each other |

## Dashboard views
1. **Overall:** ride volume per day, booking status breakdown
2. **Vehicle Type:** top 5 vehicle types by distance, average distance, vehicle summary table
3. **Revenue:** revenue by payment method, top 5 customers, distance per day and distance distribution
4. **Cancellation:** customer reasons, driver reasons, incomplete ride reasons
5. **Ratings:** average rating by vehicle type, driver rating box plot, customer vs driver scatter

Filters: vehicle type and date range.

## Tech stack
Python (pandas), SQL (MySQL syntax, tested in SQLite), HTML/JavaScript with Chart.js.

## Project structure
```
ola-ride-analytics/
├── data/ola_bookings_clean.csv    cleaned dataset (40,539 rows)
├── scripts/clean.py               cleaning steps
├── scripts/run_sql.py             runs the SQL answers and prints results
├── scripts/build_data.py          embeds the data into the dashboard page
├── sql/ola_queries.sql            10 SQL questions as views
├── dashboard/index.html           the interactive dashboard (single file)
└── README.md
```

## Data cleaning
- Removed 62,485 empty trailing rows from the raw export (103,024 rows became 40,539).
- Dropped the empty `Unnamed: 20` column and the `Vehicle Images` column (all `#NAME?` errors).
- Converted the text `null` to real missing values.
- Split `Date` and `Time` properly and fixed the inconsistent label "AC is Not working".
- Ratings, TAT, distance and payment exist only for successful rides, as designed in the dataset.

## Notes
- The dataset is synthetic. It was generated from a ChatGPT prompt as part of a tutorial exercise, so it does not describe real Ola operations.
- "Success" includes the 1,542 rides later marked incomplete. Revenue counts every successful booking.
- Many customers tie at 3 rides, so "top 5 customers by number of rides" is an arbitrary pick among ties. The dashboard ranks customers by booking value instead.

## Run it yourself
```bash
pip install pandas
python scripts/clean.py <raw_booking_csv> data/ola_bookings_clean.csv
python scripts/run_sql.py
```
Open `dashboard/index.html` in any browser (it loads Chart.js from a CDN, so it needs internet).

## Credits
Project brief and dataset prompt from Top Varsity's OLA Data Analyst Project tutorial.
