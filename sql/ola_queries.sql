-- Ola ride bookings (Bengaluru, July 2024): 10 business questions in SQL
-- Table: bookings (load data/ola_bookings_clean.csv). Works in MySQL and SQLite.
-- Note: 'Success' bookings include the rides later flagged Incomplete_Rides = 'Yes'.

-- 1. All successful bookings
CREATE VIEW Successful_Bookings AS
SELECT * FROM bookings WHERE Booking_Status = 'Success';

-- 2. Average ride distance for each vehicle type (successful rides)
CREATE VIEW ride_distance_for_each_vehicle AS
SELECT Vehicle_Type, ROUND(AVG(Ride_Distance), 2) AS avg_distance
FROM bookings WHERE Booking_Status = 'Success' GROUP BY Vehicle_Type;

-- 3. Total rides cancelled by customers
CREATE VIEW cancelled_rides_by_customers AS
SELECT COUNT(*) AS cancelled_by_customer FROM bookings WHERE Booking_Status = 'Canceled by Customer';

-- 4. Top 5 customers by number of rides
CREATE VIEW Top_5_Customers AS
SELECT Customer_ID, COUNT(Booking_ID) AS total_rides
FROM bookings GROUP BY Customer_ID ORDER BY total_rides DESC, Customer_ID LIMIT 5;

-- 5. Rides cancelled by drivers for personal and car-related issues
CREATE VIEW Rides_cancelled_by_Drivers_P_C_Issues AS
SELECT COUNT(*) AS personal_car_issue_cancellations
FROM bookings WHERE Canceled_Rides_by_Driver = 'Personal & Car related issue';

-- 6. Max and min driver rating for Prime Sedan
CREATE VIEW Max_Min_Driver_Rating AS
SELECT MAX(Driver_Ratings) AS max_rating, MIN(Driver_Ratings) AS min_rating
FROM bookings WHERE Vehicle_Type = 'Prime Sedan';

-- 7. All rides paid by UPI
CREATE VIEW UPI_Payment AS
SELECT * FROM bookings WHERE Payment_Method = 'UPI';

-- 8. Average customer rating per vehicle type
CREATE VIEW AVG_Cust_Rating AS
SELECT Vehicle_Type, ROUND(AVG(Customer_Rating), 2) AS avg_customer_rating
FROM bookings GROUP BY Vehicle_Type;

-- 9. Total booking value of successful rides
CREATE VIEW total_successful_ride_value AS
SELECT SUM(Booking_Value) AS total_successful_ride_value
FROM bookings WHERE Booking_Status = 'Success';

-- 10. Incomplete rides with the reason
CREATE VIEW Incomplete_Rides_Reason AS
SELECT Booking_ID, Incomplete_Rides_Reason FROM bookings WHERE Incomplete_Rides = 'Yes';
