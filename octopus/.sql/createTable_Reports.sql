CREATE TABLE IF NOT EXISTS
reports(
 id INTEGER PRIMARY KEY ASC,
 company_id INTEGER,
 date INTEGER,
 total_revenue REAL,
 cost_of_revenue REAL,
 gross_profit REAL,
 research_development REAL,
 selling_general_and_administrative REAL,
 non_recurring REAL,
 total_operating_expenses REAL,
 total_other_income_to_expenses_net REAL,
 earnings_before_interest_and_taxes REAL,
 interest_expense REAL,
 income_before_tax REAL,
 income_tax_expense REAL,
 minority_interest_income REAL,
 net_income_from_continuing_ops REAL,
 discontinued_operations REAL,
 extraordinary_items REAL,
 effect_of_accounting_changes REAL,
 other_items REAL,
 net_income_applicable_to_common_shares REAL,
 cash_and_cash_equivalents REAL,
 short_term_investments REAL,
 net_receivables REAL,
 inventory REAL,
 other_current_assets REAL,
 total_current_assets REAL,
 long_term_investments REAL,
 property_plant_and_equipment REAL,
 goodwill REAL,
 intangible_assets REAL,
 accumulated_amortization REAL,
 other_assets REAL,
 deferred_long_term_asset_charges REAL,
 total_assets REAL,
 accounts_payable REAL,
 short_to_current_long_term_debt REAL,
 other_current_liabilities REAL,
 total_current_liabilities REAL,
 long_term_debt REAL,
 other_liabilities REAL,
 deferred_long_term_liability_charges REAL,
 minority_interest REAL,
 negative_goodwill REAL,
 total_liabilities REAL,
 misc_stocks_options_warrants REAL,
 redeemable_preferred_stock REAL,
 preferred_stock REAL,
 common_stock REAL,
 retained_earnings REAL,
 treasury_stock REAL,
 capital_surplus REAL,
 other_stockholder_equity REAL,
 total_stockholder_equity REAL,
 net_tangible_assets REAL,
 depreciation REAL,
 adjustments_to_net_income REAL,
 changes_in_accounts_receivables REAL,
 changes_in_liabilities, REAL,
 changes_in_inventories REAL,
 changes_in_other_operating_activities REAL,
 total_cash_flow_from_operating_activities REAL,
 capital_expenditures REAL,
 investments REAL,
 other_cash_flows_from_investing_activities REAL,
 total_cash_flows_from_investing_activities REAL,
 dividends_paid REAL,
 sale_purchase_of_stock REAL,
 net_borrowings REAL,
 other_cash_flows_from_financing_activities REAL,
 effect_of_exchange_rate_changes REAL,
 change_in_cash_and_cash_equivalents REAL,
 report_type INTEGER,
 FOREIGN KEY(company_id) REFERENCES companies(id),
 CONSTRAINT uniq_report_stats_company_id_date UNIQUE(company_id, date, report_type)
);
