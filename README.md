# micro-passangers
Microservice for see passangers information and update it

# Dependencies
install:

```
pip install fastapi uvicorn sqlalchemy asyncpg databases psycopg2-binary python-dotenv pytest httpx pytest-asyncio aiosqlite
```

# Database

Generate database:

```sql
create database "reservations";

create table passengers( id serial primary key, name varchar not null, last_name varchar not null, birthdate date not null);

create table travel(id serial primary key, code varchar not null, travel_from varchar not null, travel_to varchar not null, departure_date timestamp not null );

create table reservations(id serial primary key, passenger_id INT, travel_id INT, CONSTRAINT fk_passenger FOREIGN KEY(passenger_id)REFERENCES passengers, CONSTRAINT fk_travel FOREIGN KEY(travel_id) REFERENCES travels, register_time timestamp default current_timestamp);
```