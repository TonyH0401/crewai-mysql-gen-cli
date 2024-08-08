CREATE TABLE employees (
    emp_no      INT             NOT NULL AUTO_INCREMENT,
    birth_date  DATE            NOT NULL,
    first_name  VARCHAR(14)     NOT NULL,
    last_name   VARCHAR(16)     NOT NULL,
    gender      ENUM ('M','F')  NOT NULL,
    hire_date   DATE            NOT NULL,
    PRIMARY KEY (emp_no)
);

CREATE TABLE departments (
    dept_no     CHAR(4)         NOT NULL,
    dept_name   VARCHAR(40)     NOT NULL,
    PRIMARY KEY (dept_no),
    UNIQUE  KEY (dept_name)
);

CREATE TABLE dept_emp (
    emp_no      INT         NOT NULL,
    dept_no     CHAR(4)     NOT NULL,
    from_date   DATE        NOT NULL,
    to_date     DATE        NOT NULL,
    KEY         (emp_no),
    KEY         (dept_no),
    FOREIGN KEY (emp_no) REFERENCES employees (emp_no) ON DELETE CASCADE,
    FOREIGN KEY (dept_no) REFERENCES departments (dept_no) ON DELETE CASCADE,
    PRIMARY KEY (emp_no, dept_no, from_date)
);

CREATE TABLE dept_manager (
    dept_no      CHAR(4)  NOT NULL,
    emp_no       INT      NOT NULL,
    from_date    DATE     NOT NULL,
    to_date      DATE     NOT NULL,
    KEY         (emp_no),
    KEY         (dept_no),
    FOREIGN KEY (emp_no)  REFERENCES employees (emp_no) ON DELETE CASCADE,
    FOREIGN KEY (dept_no) REFERENCES departments (dept_no) ON DELETE CASCADE,
    PRIMARY KEY (emp_no, dept_no, from_date)
);

CREATE TABLE titles (
    emp_no      INT          NOT NULL,
    title       VARCHAR(50)  NOT NULL,
    from_date   DATE         NOT NULL,
    to_date     DATE,
    KEY         (emp_no),
    FOREIGN KEY (emp_no) REFERENCES employees (emp_no) ON DELETE CASCADE,
    PRIMARY KEY (emp_no, title, from_date)
);

CREATE TABLE salaries (
    emp_no      INT    NOT NULL,
    salary      INT    NOT NULL,
    from_date   DATE   NOT NULL,
    to_date     DATE   NOT NULL,
    KEY         (emp_no),
    FOREIGN KEY (emp_no) REFERENCES employees (emp_no) ON DELETE CASCADE,
    PRIMARY KEY (emp_no, from_date)
);

-- Insert data into employees
INSERT INTO employees (birth_date, first_name, last_name, gender, hire_date) VALUES
('1985-01-01', 'John', 'Doe', 'M', '2020-01-01'),
('1990-02-02', 'Jane', 'Smith', 'F', '2019-02-01'),
('1988-03-03', 'Jim', 'Brown', 'M', '2021-03-01'),
('1992-04-04', 'Jake', 'White', 'M', '2018-04-01'),
('1987-05-05', 'Jill', 'Black', 'F', '2017-05-01'),
('1986-06-06', 'Jack', 'Green', 'M', '2016-06-01'),
('1991-07-07', 'Jenny', 'Blue', 'F', '2015-07-01'),
('1989-08-08', 'Joe', 'Red', 'M', '2022-08-01'),
('1993-09-09', 'Jessica', 'Yellow', 'F', '2023-09-01'),
('1994-10-10', 'Jerry', 'Purple', 'M', '2014-10-01');

-- Insert data into departments
INSERT INTO departments (dept_no, dept_name) VALUES
('d001', 'Marketing'),
('d002', 'Finance'),
('d003', 'HR'),
('d004', 'IT'),
('d005', 'Sales'),
('d006', 'Legal'),
('d007', 'Operations'),
('d008', 'R&D'),
('d009', 'Admin'),
('d010', 'Support');

-- Insert data into dept_emp
INSERT INTO dept_emp (emp_no, dept_no, from_date, to_date) VALUES
(1, 'd001', '2020-01-01', '2023-01-01'),
(2, 'd002', '2019-02-01', '2022-02-01'),
(3, 'd003', '2021-03-01', '2024-03-01'),
(4, 'd004', '2018-04-01', '2021-04-01'),
(5, 'd005', '2017-05-01', '2020-05-01'),
(6, 'd006', '2016-06-01', '2019-06-01'),
(7, 'd007', '2015-07-01', '2018-07-01'),
(8, 'd008', '2022-08-01', '2025-08-01'),
(9, 'd009', '2023-09-01', '2026-09-01'),
(10, 'd010', '2014-10-01', '2017-10-01');

-- Insert data into dept_manager
INSERT INTO dept_manager (emp_no, dept_no, from_date, to_date) VALUES
(1, 'd001', '2020-01-01', '2023-01-01'),
(2, 'd002', '2019-02-01', '2022-02-01'),
(3, 'd003', '2021-03-01', '2024-03-01'),
(4, 'd004', '2018-04-01', '2021-04-01'),
(5, 'd005', '2017-05-01', '2020-05-01'),
(6, 'd006', '2016-06-01', '2019-06-01'),
(7, 'd007', '2015-07-01', '2018-07-01'),
(8, 'd008', '2022-08-01', '2025-08-01'),
(9, 'd009', '2023-09-01', '2026-09-01'),
(10, 'd010', '2014-10-01', '2017-10-01');

-- Insert data into titles
INSERT INTO titles (emp_no, title, from_date, to_date) VALUES
(1, 'Manager', '2020-01-01', '2023-01-01'),
(2, 'Analyst', '2019-02-01', '2022-02-01'),
(3, 'Consultant', '2021-03-01', '2024-03-01'),
(4, 'Developer', '2018-04-01', '2021-04-01'),
(5, 'Salesperson', '2017-05-01', '2020-05-01'),
(6, 'Lawyer', '2016-06-01', '2019-06-01'),
(7, 'Operations Manager', '2015-07-01', '2018-07-01'),
(8, 'Researcher', '2022-08-01', '2025-08-01'),
(9, 'Administrator', '2023-09-01', '2026-09-01'),
(10, 'Support Specialist', '2014-10-01', '2017-10-01');

-- Insert data into salaries
INSERT INTO salaries (emp_no, salary, from_date, to_date) VALUES
(1, 60000, '2020-01-01', '2021-01-01'),
(1, 65000, '2021-01-01', '2022-01-01'),
(1, 70000, '2022-01-01', '2023-01-01'),
(2, 50000, '2019-02-01', '2020-02-01'),
(2, 55000, '2020-02-01', '2021-02-01'),
(2, 60000, '2021-02-01', '2022-02-01'),
(3, 45000, '2021-03-01', '2022-03-01'),
(3, 50000, '2022-03-01', '2023-03-01'),
(3, 55000, '2023-03-01', '2024-03-01'),
(4, 70000, '2018-04-01', '2019-04-01');