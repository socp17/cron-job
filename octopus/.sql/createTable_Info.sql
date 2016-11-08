CREATE TABLE IF NOT EXISTS
info(
id INTEGER PRIMARY KEY ASC,
company_id INTEGER,
date INTEGER,
full_time_employees INTEGER,
industry TEXT,
sector TEXT,
FOREIGN KEY(company_id) REFERENCES companies(id),
CONSTRAINT uniq_key_stats_company_id_date UNIQUE(company_id, date)
);
