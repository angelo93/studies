CREATE TABLE customer
  (customer_num      NUMBER(3)   CONSTRAINT customer_num_pk PRIMARY KEY,
   fname             VARCHAR2(15),
   lname             VARCHAR2(15),
   company           VARCHAR2(20),
   address1          VARCHAR2(20),
   address2          VARCHAR2(20),
   city              VARCHAR2(15),
   state             CHAR(2),
   zipcode           CHAR(5),
   phone             VARCHAR(18)
  )
  
 