CREATE TABLE items
  (item_num       NUMBER(2),
   order_num      NUMBER(4),
   stock_num      NUMBER(2),
   manu_code      CHAR(3),
   quantity       NUMBER(3),
   total_price    NUMBER(8,2),
   PRIMARY KEY (item_num,order_num),
   FOREIGN KEY (stock_num, manu_code)
      REFERENCES stock (stock_num, manu_code))
   