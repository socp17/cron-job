CREATE TABLE IF NOT EXISTS
price(
id INTEGER PRIMARY KEY ASC,
company_id INTEGER,
date INTEGER,
price REAL,
FOREIGN KEY(company_id) REFERENCES companies(id),
CONSTRAINT uniq_price_history_company_id_date UNIQUE(company_id, date)
);
