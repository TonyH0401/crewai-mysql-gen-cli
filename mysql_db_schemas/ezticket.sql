CREATE TABLE Category (
        category_id int NOT NULL AUTO_INCREMENT,
        category_name varchar(50) NOT NULL,
        
        PRIMARY KEY (category_id)
    );

    CREATE TABLE User (
        user_id int NOT NULL AUTO_INCREMENT,
        fullname varchar(255) NOT NULL,
        phone char(10) NOT NULL,
        email varchar(30) NOT NULL,
        address varchar(100) NOT NULL,
        level int DEFAULT 1,
        created_at datetime DEFAULT CURRENT_TIMESTAMP,
        last_login datetime DEFAULT CURRENT_TIMESTAMP,
        
        PRIMARY KEY (user_id),
        KEY email_idx (email)
    );

    CREATE TABLE Event (
        event_id int NOT NULL AUTO_INCREMENT,
        event_name varchar(100) NOT NULL,
        occur_date date NOT NULL,
        occur_time varchar(50) NOT NULL,
        location varchar(50) NOT NULL,
        address varchar(255) NOT NULL,
        introduce text,
        banner varchar(255) NOT NULL,
        status varchar(10) NOT NULL CHECK (status IN ('pending', 'published', 'ended')),
        created_at datetime DEFAULT CURRENT_TIMESTAMP,
        updated_at datetime DEFAULT CURRENT_TIMESTAMP,
        author_id int NOT NULL,
        category_id int NOT NULL,
        
        PRIMARY KEY (event_id),
        CONSTRAINT fk_event_author FOREIGN KEY (author_id) REFERENCES User (user_id),
        CONSTRAINT fk_event_category FOREIGN KEY (category_id) REFERENCES Category (category_id)
    );

    CREATE TABLE TicketType (
        ticket_type_id int NOT NULL AUTO_INCREMENT,
        ticket_type_name varchar(100) NOT NULL,
        event_id int NOT NULL,
        price int NOT NULL DEFAULT 0,
        n_sold int NOT NULL DEFAULT 0,
        n_stock int NOT NULL DEFAULT 0,
        is_selling boolean NOT NULL DEFAULT false,
        created_at datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
        updated_at datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
        
        PRIMARY KEY (ticket_type_id),
        CONSTRAINT fk_tickettype_event FOREIGN KEY (event_id) REFERENCES Event (event_id)
    );

    CREATE TABLE Booking (
        booking_id varchar(20) NOT NULL,
        customer_id int NOT NULL,
        payment_method varchar(10) CHECK (payment_method IN ('stripe', 'paypal', 'amazon')),
        temp_cost int NOT NULL,
        status varchar(20) CHECK (status IN ('pending', 'completed', 'canceled')) DEFAULT 'pending',
        created_at datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
        updated_at datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
        
        PRIMARY KEY (booking_id),
        CONSTRAINT fk_booking_user FOREIGN KEY (customer_id) REFERENCES User (user_id)
    );

    CREATE TABLE BookingDetail (
        booking_id varchar(20) NOT NULL,
        ticket_type_id int NOT NULL,
        quantity int NOT NULL,	
        
        PRIMARY KEY (booking_id, ticket_type_id),
        CONSTRAINT fk_bookingdetail_booking FOREIGN KEY (booking_id) REFERENCES Booking (booking_id),
        CONSTRAINT fk_bookingdetail_tickettype FOREIGN KEY (ticket_type_id) REFERENCES TicketType (ticket_type_id)
    );

    CREATE TABLE Checkout (
        checkout_id int NOT NULL AUTO_INCREMENT,
        booking_id varchar(20) NOT NULL,
        tax float NOT NULL,
        total int NOT NULL,
        created_at datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
        updated_at datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
        
        PRIMARY KEY (checkout_id),
        CONSTRAINT fk_checkout_booking FOREIGN KEY (booking_id) REFERENCES Booking (booking_id)
    );

    CREATE TABLE Ticket (
        ticket_id int NOT NULL AUTO_INCREMENT,
        ticket_type_id int NOT NULL,
        ticket_code varchar(20) NOT NULL,
        expiry date NOT NULL,
        status varchar(20) CHECK (status IN ('available', 'sold')),
        created_at datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
        
        PRIMARY KEY (ticket_id),
        CONSTRAINT fk_ticket_tickettype FOREIGN KEY (ticket_type_id) REFERENCES TicketType (ticket_type_id)
    );

    CREATE TABLE Transaction Detail (
        checkout_id int NOT NULL,
        ticket_id int NOT NULL,
        
        PRIMARY KEY (checkout_id, ticket_id),
        CONSTRAINT fk_transactiondetail_checkout FOREIGN KEY (checkout_id) REFERENCES Checkout (checkout_id),
        CONSTRAINT fk_transactiondetail_ticket FOREIGN KEY (ticket_id) REFERENCES Ticket (ticket_id)
    );