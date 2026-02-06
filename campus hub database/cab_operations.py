from db import get_connection

def add_trip():
    driver = input("Driver ID: ")
    destination = input("Destination: ")
    time = input("Departure time (YYYY-MM-DD HH:MM:SS): ")
    seats = input("Seats: ")
    price = input("Price per seat: ")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO cab_pool
        (driver_id, destination, departure_time, seats_available, price_per_seat)
        VALUES (%s, %s, %s, %s, %s)
    """, (driver, destination, time, seats, price))

    conn.commit()
    print("Trip added.")
    cursor.close()
    conn.close()
