-- Keep a log of any SQL queries you execute as you solve the mystery.
.schema

-- Get an overview of all available info before diving in.
SELECT * FROM crime_scene_reports;

-- Get all crime_scene reports from Humphrey Street that took place on July 28, 2023
SELECT * FROM crime_scene_reports
 WHERE street = 'Humphrey Street'
   AND year = 2023
   AND month = 7
   AND day = 28;

-- Note Duck Theft id is 295 & all three witnesses mentioned the Humphrey Street bakery. Time was 10:15.
SELECT * FROM interviews
 WHERE year = 2023
   AND month = 7
   AND day = 28;

SELECT license_plate FROM bakery_security_logs
 WHERE year = 2023
   AND month = 7
   AND day = 28
   AND hour > 9
   AND hour < 11
   AND minute > 14
   AND minute < 30
   AND activity = 'exit';

-- Owners of license plates that left within 10 mins of theft.
SELECT name, license_plate FROM people
 WHERE license_plate IN (
SELECT license_plate FROM bakery_security_logs
 WHERE year = 2023
   AND month = 7
   AND day = 28
   AND hour > 9
   AND hour < 11
   AND minute > 14
   AND minute < 30
   AND activity = 'exit'
);

-- ATM queries.
SELECT account_number FROM atm_transactions
 WHERE atm_location = 'Leggett Street'
   AND transaction_type = 'withdraw'
   AND year = 2023
   AND month = 7
   AND day = 28;

SELECT * FROM people
  JOIN bank_accounts ON people.id = bank_accounts.person_id
 WHERE license_plate IN (
SELECT license_plate FROM bakery_security_logs
 WHERE year = 2023
   AND month = 7
   AND day = 28
   AND hour > 9
   AND hour < 11
   AND minute > 14
   AND minute < 30
   AND activity = 'exit'
)
   AND account_number IN (
SELECT account_number FROM atm_transactions
 WHERE atm_location = 'Leggett Street'
   AND transaction_type = 'withdraw'
   AND year = 2023
   AND month = 7
   AND day = 28
);

-- Shortlisted suspects: [Bruce, Diana, Iman, Luca]
SELECT * FROM people
  JOIN bank_accounts ON people.id = bank_accounts.person_id
 WHERE license_plate IN (
SELECT license_plate FROM bakery_security_logs
 WHERE year = 2023
   AND month = 7
   AND day = 28
   AND hour > 9
   AND hour < 11
   AND minute > 14
   AND minute < 30
   AND activity = 'exit'
)
   AND account_number IN (
SELECT account_number FROM atm_transactions
 WHERE atm_location = 'Leggett Street'
   AND transaction_type = 'withdraw'
   AND year = 2023
   AND month = 7
   AND day = 28
)
   AND phone_number IN (
SELECT caller FROM phone_calls
 WHERE year = 2023
   AND month = 7
   AND day = 28
   AND duration < 60
);

-- Shortlisted suspects: [Bruce, Diana]
SELECT * FROM flights
 WHERE year = 2023
   AND month = 7
   AND day = 29;

-- Flight id 36 left earliest at 08:20

SELECT * FROM passengers
  JOIN flights ON passengers.flight_id = flights.id
 WHERE passport_number = '5773159633' OR passport_number = '3592750733';

SELECT * FROM people
  JOIN bank_accounts ON people.id = bank_accounts.person_id
 WHERE license_plate IN (
SELECT license_plate FROM bakery_security_logs
 WHERE year = 2023
   AND month = 7
   AND day = 28
   AND hour > 9
   AND hour < 11
   AND minute > 14
   AND minute < 30
   AND activity = 'exit'
)
   AND account_number IN (
SELECT account_number FROM atm_transactions
 WHERE atm_location = 'Leggett Street'
   AND transaction_type = 'withdraw'
   AND year = 2023
   AND month = 7
   AND day = 28
)
   AND phone_number IN (
SELECT caller FROM phone_calls
 WHERE year = 2023
   AND month = 7
   AND day = 28
   AND duration < 60
)
   AND passport_number IN (
SELECT passport_number FROM passengers
  JOIN flights ON passengers.flight_id = flights.id
 WHERE flights.id = 36
);

-- So far, Bruce has matched all the criteria provided by the interviewers.
SELECT name FROM people
 WHERE people.phone_number = (
SELECT receiver FROM phone_calls
 WHERE caller = '(367) 555-5533'
   AND phone_calls.id = 233
);

SELECT * FROM flights
 WHERE id = 36;

SELECT * FROM airports
 WHERE id = 4;

-- Bruce escaped to New York City with the help of Robin.


