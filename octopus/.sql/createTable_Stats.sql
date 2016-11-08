CREATE TABLE IF NOT EXISTS
key_stats(
 id INTEGER PRIMARY KEY ASC,
 company_id INTEGER,
 date INTEGER,
 market_cap REAL,
 trailing_pe REAL,
 forward_pe REAL,
 peg_ratio REAL,
 price_to_sales REAL,
 price_to_book REAL,
 enterprise_value_to_revenue REAL,
 enterprise_value_to_ebitda REAL,
 fiscal_year_ends TEXT,
 most_recent_quarter TEXT,
 profitability REAL,
 profit_margin REAL,
 operating_margin REAL,
 return_on_assets REAL,
 return_on_equity REAL,
 revenue REAL,
 revenue_per_share REAL,
 quartery_revenue_growth REAL,
 gross_profit REAL,
 ebitda REAL,
 net_income_available REAL,
 diluted_eps REAL,
 quarterly_earnings_growth REAL,
 total_cash REAL,
 total_cash_per_share REAL,
 total_debt REAL,
 total_debt_to_equity REAL,
 current_ratio REAL,
 book_to_value_per_share REAL,
 operating_cash_flow REAL,
 levered_free_cash_flow REAL,
 floating REAL,
 held_by_investors REAL,
 held_by_institutions REAL,
 shares_short REAL,
 short_ratio REAL,
 beta REAL,
FOREIGN KEY(company_id) REFERENCES companies(id),
CONSTRAINT uniq_key_stats_company_id_date UNIQUE(company_id, date)
);