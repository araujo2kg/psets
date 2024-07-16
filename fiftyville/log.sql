-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Visualize how the information is stored:
SELECT * FROM crime_scene_reports LIMIT 5;

-- Get information from the crime scene
SELECT description
FROM crime_scene_reports
WHERE day = 28
AND month = 7
AND year = 2023
AND street = 'Humphrey Street';
-- Time: 10:15am, Location: Humphrey Street bakery, 3 Witness, 3 interviews with transcripts.

-- Consulting the witnesses interviews information
SELECT name, transcript
FROM interviews
WHERE day = 28
AND month = 7
AND year = 2023;
-- Witnesses: Ruth, Eugene, Raymond.
-- Thief drived off the bakery parking lot within 10 minutes of the robbery
-- Parking lot has cameras (bakery_security_logs)
-- Thief possibly withdrawed money from Leggett Street ATM before 10:15am
-- Thief called accomplice around 10:15 for less than a minute, planning to take earliest flight out of
-- fiftyville TOMORROW, thief asked accomplice to buy the ticket

-- Consulting information of bakery security within timeframe (10:15 to 10:25)
SELECT license_plate, minute
FROM bakery_security_logs
WHERE activity = 'exit'
AND year = 2023
AND month = 7
AND day = 28
AND hour = 10
AND minute > 15
AND minute < 26
ORDER BY minute;

-- Getting the suspects information from the people table based on their license plates:
SELECT name, phone_number, passport_number, license_plate
FROM people
WHERE license_plate IN
(SELECT license_plate
FROM bakery_security_logs
WHERE activity = 'exit' AND year = 2023 AND month = 7 AND day = 28 AND hour = 10 AND minute > 15 AND minute < 26);

-- Suspect list of people exiting bakery on thief timeframe:
-- Vanessa, Bruce, Barry, Luca, Sofia, Iman, Diana, Kelsey

-- Consulting phone calls made by suspects in the timeframe of the robbery and within duration (less than a minute)
SELECT name, caller, receiver, duration
FROM phone_calls
JOIN people ON caller = phone_number
WHERE year = 2023 AND month = 7 AND day = 28 AND duration < 60
AND caller IN
(SELECT phone_number FROM people
WHERE license_plate IN
(SELECT license_plate
FROM bakery_security_logs
WHERE activity = 'exit' AND year = 2023 AND month = 7 AND day = 28 AND hour = 10 AND minute > 15 AND minute < 26));

-- Suspect list based on phone calls made within robbery timeframe and call duration:
-- Sofia, Kelsey, Bruce, Diana

-- Consulting atm transactions in witness timeframe to crossreference suspects:
SELECT bank_accounts.account_number, person_id, creation_year
FROM bank_accounts
JOIN atm_transactions ON bank_accounts.account_number = atm_transactions.account_number
WHERE year = 2023 AND month = 7 AND day = 28 AND atm_location = 'Leggett Street' AND transaction_type = 'withdraw';

-- Consulting people based on id identified by atm transactions to crossreference:
SELECT * FROM people
WHERE id IN
(SELECT person_id
FROM bank_accounts
JOIN atm_transactions ON bank_accounts.account_number = atm_transactions.account_number
WHERE year = 2023 AND month = 7 AND day = 28 AND atm_location = 'Leggett Street' AND transaction_type = 'withdraw');

-- Suspects based on the atm transaction timeframe:
-- Iman, Luca, Diana, Bruce

-- Check earliest flight from the next day (29) for crossreference:
SELECT * from flights
WHERE day = 29
ORDER BY hour;
-- Earliest flight id = 36, destination airport_id = 4.

-- Check thief destination:
SELECT *
FROM airports
WHERE id = 4;
-- Thief destination: LaGuardia Airport(LGA), New York City.

-- Check passengers:
SELECT * FROM people
WHERE passport_number IN
(SELECT passport_number FROM passengers
WHERE flight_id = 36);
-- Suspects in the flight:
-- Sofia, Luca, Kelsey, Bruce.

-- Putting all suspects lists together:
-- Vanessa, Bruce, Barry, Luca, Sofia, Iman, Diana, Kelsey
-- Sofia, Kelsey, Bruce, Diana
-- Iman, Luca, Diana, Bruce
-- Sofia, Luca, Kelsey, Bruce.
-- Bruce is the only one that appears in all suspects lists, so the only possible thief.

-- Identify bruce accomplice:
-- Get bruce phone number:
SELECT phone_number FROM people
WHERE name = 'Bruce';

-- Identify accomplice based on phone call that happened on crime scene:
SELECT * FROM people
WHERE phone_number IN
(SELECT receiver FROM phone_calls
WHERE caller = '(367) 555-5533'
AND day = 28
AND duration < 60);
-- Robin is the accomplice.

-- Thief: Bruce
-- Destination: New York City
-- Accomplice: Robin







