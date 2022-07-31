CREATE TABLE orders
  (order_num      NUMBER(4)    CONSTRAINT order_num_pk PRIMARY KEY,
   order_date     DATE         CONSTRAINT order_date_nn NOT NULL,
   customer_num   NUMBER(3)    CONSTRAINT order_cust_num_fk 
       REFERENCES CUSTOMER(customer_num),
   ship_instruct  VARCHAR2(40),
   backlog        CHAR(1),
   po_num         VARCHAR(10),
   ship_date      DATE,
   ship_weight    NUMBER(8,2),
   ship_charge    NUMBER(6,2),
   paid_date      DATE)