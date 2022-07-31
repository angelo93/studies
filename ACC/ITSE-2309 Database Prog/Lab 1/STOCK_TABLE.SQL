CREATE TABLE stock
  (stock_num      NUMBER(2),
   manu_code      CHAR(3),
   description    VARCHAR2(15),
   unit_price     NUMBER(8,2),
   unit           CHAR(4),
   unit_descr     VARCHAR2(15),
   PRIMARY KEY (stock_num,manu_code),
   FOREIGN KEY (manu_code)
      REFERENCES manufact (manu_code))
   