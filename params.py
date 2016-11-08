PARAMS = {
    'PRICE': {
        'Price': {
            'type': 'REAL',
            'columnName': 'price'
        }
    },
    'INFO': {
        'Sector': {
            'type': 'TEXT',
            'columnName': 'sector'
        },
        'Industry': {
            'type': 'TEXT',
            'columnName': 'industry'
        },
        'Full Time Employees': {
            'type': 'INTEGER',
            'columnName': 'full_time_employees'
        }
    },
    'KEY_STATS': {
        'Beta': {
            'columnName': 'beta',
            'type': 'REAL'
        },
        'Book Value Per Share (mrq)': {
            'columnName': 'book_to_value_per_share',
            'type': 'REAL'
        },
        'Current Ratio (mrq)': {
            'columnName': 'current_ratio',
            'type': 'REAL'
        },
        'Diluted EPS (ttm)': {
            'columnName': 'diluted_eps',
            'type': 'REAL'
        },
        'EBITDA (ttm)': {
            'columnName': 'ebitda',
            'type': 'REAL'
        },
        'Enterprise Value/EBITDA (ttm)': {
            'columnName': 'enterprise_value_to_ebitda',
            'type': 'REAL'
        },
        'Enterprise Value/Revenue (ttm)': {
            'columnName': 'enterprise_value_to_revenue',
            'type': 'REAL'
        },
        'Fiscal Year Ends': {
            'columnName': 'fiscal_year_ends',
            'type': 'REAL'
        },
        'Float': {
            'columnName': 'floating',
            'type': 'REAL'
        },
        'Forward P/E': {
            'columnName': 'forward_pe',
            'type': 'REAL'
        },
        'Gross Profit (ttm)': {
            'columnName': 'gross_profit',
            'type': 'REAL'
        },
        'Held by Insiders': {
            'columnName': 'held_by_investors',
            'type': 'REAL'
        },
        'Held by Institutions': {
            'columnName': 'held_by_institutions',
            'type': 'REAL'
        },
        'Levered Free Cash Flow (ttm)': {
            'columnName': 'levered_free_cash_flow',
            'type': 'REAL'
        },
        'Market Cap (intraday)': {
            'columnName': 'market_cap', 'type': 'REAL'
        },
        'Most Recent Quarter (mrq)': {
            'columnName': 'most_recent_quarter',
            'type': 'REAL'
        },
        'Net Income Avl to Common (ttm)': {
            'columnName': 'net_income_available',
            'type': 'REAL'
        },
        'Operating Cash Flow (ttm)': {
            'columnName': 'operating_cash_flow',
            'type': 'REAL'
        },
        'Operating Margin (ttm)': {
            'columnName': 'operating_margin',
            'type': 'REAL'
        },
        'PEG Ratio (5 yr expected)': {
            'columnName': 'peg_ratio',
            'type': 'REAL'
        },
        'Price/Book (mrq)': {
            'columnName': 'price_to_book',
            'type': 'REAL'
        },
        'Price/Sales (ttm)': {
            'columnName': 'price_to_sales',
            'type': 'REAL'
        },
        'Profit Margin (ttm)': {
            'columnName': 'profit_margin',
            'type': 'REAL'
        },
        'Profitability': {
            'columnName': 'profitability',
            'type': 'REAL'
        },
        'Qtrly Earnings Growth (yoy)': {
            'columnName': 'quarterly_earnings_growth',
            'type': 'REAL'
        },
        'Qtrly Revenue Growth (yoy)': {
            'columnName': 'quartery_revenue_growth',
            'type': 'REAL'
        },
        'Return on Assets (ttm)': {
            'columnName': 'return_on_assets',
            'type': 'REAL'
        },
        'Return on Equity (ttm)': {
            'columnName': 'return_on_equity',
            'type': 'REAL'
        },
        'Revenue (ttm)': {
            'columnName': 'revenue',
            'type': 'REAL'
        },
        'Revenue Per Share (ttm)': {
            'columnName': 'revenue_per_share',
            'type': 'REAL'
        },
        'Shares Short': {
            'columnName': 'shares_short',
            'type': 'REAL'
        },
        'Short Ratio': {
            'columnName': 'short_ratio',
            'type': 'REAL'
        },
        'Total Cash (mrq)': {
            'columnName': 'total_cash',
            'type': 'REAL'
        },
        'Total Cash Per Share (mrq)': {
            'columnName': 'total_cash_per_share',
            'type': 'REAL'
        },
        'Total Debt (mrq)': {
            'columnName': 'total_debt',
            'type': 'REAL'
        },
        'Total Debt/Equity (mrq)': {
            'columnName': 'total_debt_to_equity',
            'type': 'REAL'
        },
        'Trailing P/E (ttm, intraday)': {
            'columnName': 'trailing_pe',
            'type': 'REAL'
        }
    },
    'REPORTS': {
        'Accounts Payable': {
            'columnName': 'accounts_payable',
            'type': 'REAL',
            'report': 'bs'
        },
        'Accumulated Amortization': {
            'columnName': 'accumulated_amortization',
            'type': 'REAL',
            'report': 'bs'
        },
        'Adjustments To Net Income': {
            'columnName': 'adjustments_to_net_income',
            'type': 'REAL',
            'report': 'cf'
        },
        'Capital Expenditures': {
            'columnName': 'capital_expenditures',
            'type': 'REAL',
            'report': 'cf'
        },
        'Capital Surplus': {
            'columnName': 'capital_surplus',
            'type': 'REAL',
            'report': 'bs'
        },
        'Cash And Cash Equivalents': {
            'columnName': 'cash_and_cash_equivalents',
            'type': 'REAL',
            'report': 'bs'
        },
        'Change In Cash and Cash Equivalents': {
            'columnName': 'change_in_cash_and_cash_equivalents',
            'type': 'REAL',
            'report': 'cf'
        },
        'Changes In Accounts Receivables': {
            'columnName': 'changes_in_accounts_receivables',
            'type': 'REAL',
            'report': 'cf'
        },
        'Changes In Inventories': {
            'columnName': 'changes_in_inventories',
            'type': 'REAL',
            'report': 'cf'
        },
        'Changes In Liabilities': {
            'columnName': 'changes_in_liabilities',
            'type': 'REAL',
            'report': 'cf'
        },
        'Changes In Other Operating Activities': {
            'columnName': 'changes_in_other_operating_activities',
            'type': 'REAL',
            'report': 'cf'
        },
        'Common Stock': {
            'columnName': 'common_stock',
            'type': 'REAL',
            'report': 'bs'
        },
        'Cost of Revenue': {
            'columnName': 'cost_of_revenue',
            'type': 'REAL',
            'report': 'is'
        },
        'Deferred Long Term Asset Charges': {
            'columnName': 'deferred_long_term_asset_charges',
            'type': 'REAL',
            'report': 'bs'
        },
        'Deferred Long Term Liability Charges': {
            'columnName': 'deferred_long_term_liability_charges',
            'type': 'REAL',
            'report': 'bs'
        },
        'Depreciation': {
            'columnName': 'depreciation',
            'type': 'REAL',
            'report': 'cf'
        },
        'Discontinued Operations': {
            'columnName': 'discontinued_operations',
            'type': 'REAL',
            'report': 'is'
        },
        'Dividends Paid': {
            'columnName': 'dividends_paid',
            'type': 'REAL',
            'report': 'cf'
        },
        'Earnings Before Interest And Taxes': {
            'columnName': 'earnings_before_interest_and_taxes',
            'type': 'REAL',
            'report': 'is'
        },
        'Effect Of Accounting Changes': {
            'columnName': 'effect_of_accounting_changes',
            'type': 'REAL',
            'report': 'is'
        },
        'Effect Of Exchange Rate Changes': {
            'columnName': 'effect_of_exchange_rate_changes',
            'type': 'REAL',
            'report': 'cf'
        },
        'Extraordinary Items': {
            'columnName': 'extraordinary_items',
            'type': 'REAL',
            'report': 'is'
        },
        'Goodwill': {
            'columnName': 'goodwill',
            'type': 'REAL',
            'report': 'bs'
        },
        'Gross Profit': {
            'columnName': 'gross_profit',
            'type': 'REAL',
            'report': 'is'
        },
        'Income Before Tax': {
            'columnName': 'income_before_tax',
            'type': 'REAL',
            'report': 'is'
        },
        'Income Tax Expense': {
            'columnName': 'income_tax_expense',
            'type': 'REAL',
            'report': 'is'
        },
        'Intangible Assets': {
            'columnName': 'intangible_assets',
            'type': 'REAL',
            'report': 'bs'
        },
        'Interest Expense': {
            'columnName': 'interest_expense',
            'type': 'REAL',
            'report': 'is'
        },
        'Inventory': {
            'columnName': 'inventory',
            'type': 'REAL',
            'report': 'bs'
        },
        'Investments': {
            'columnName': 'investments',
            'type': 'REAL',
            'report': 'cf'
        },
        'Long Term Debt': {
            'columnName': 'long_term_debt',
            'type': 'REAL',
            'report': 'bs'
        },
        'Long Term Investments': {
            'columnName': 'long_term_investments',
            'type': 'REAL',
            'report': 'bs'
        },
        'Minority Interest': {
            'columnName': 'minority_interest',
            'type': 'REAL',
            'report': 'bs'
        },
        'Misc Stocks Options Warrants': {
            'columnName': 'misc_stocks_options_warrants',
            'type': 'REAL',
            'report': 'bs'
        },
        'Negative Goodwill': {
            'columnName': 'negative_goodwill',
            'type': 'REAL',
            'report': 'bs'
        },
        'Net Borrowings': {
            'columnName': 'net_borrowings',
            'type': 'REAL',
            'report': 'cf'
        },
        'Net Income Applicable To Common Shares': {
            'columnName': 'net_income_applicable_to_common_shares',
            'type': 'REAL',
            'report': 'is'
        },
        'Net Income From Continuing Ops': {
            'columnName': 'net_income_from_continuing_ops',
            'type': 'REAL',
            'report': 'is'
        },
        'Net Receivables': {
            'columnName': 'net_receivables',
            'type': 'REAL',
            'report': 'bs'
        },
        'Net Tangible Assets': {
            'columnName': 'net_tangible_assets',
            'type': 'REAL',
            'report': 'bs'
        },
        'Non Recurring': {
            'columnName': 'non_recurring',
            'type': 'REAL',
            'report': 'is'
        },
        'Other Assets': {
            'columnName': 'other_assets',
            'type': 'REAL',
            'report': 'bs'
        },
        'Other Cash Flows from Financing Activities': {
            'columnName': 'other_cash_flows_from_financing_activities',
            'type': 'REAL',
            'report': 'cf'
        },
        'Other Cash flows from Investing Activities': {
            'columnName': 'other_cash_flows_from_investing_activities',
            'type': 'REAL',
            'report': 'cf'
        },
        'Other Current Assets': {
            'columnName': 'other_current_assets',
            'type': 'REAL',
            'report': 'bs'
        },
        'Other Current Liabilities': {
            'columnName': 'other_current_liabilities',
            'type': 'REAL',
            'report': 'bs'
        },
        'Other Items': {
            'columnName': 'other_items',
            'type': 'REAL',
            'report': 'is'
        },
        'Other Liabilities': {
            'columnName': 'other_liabilities',
            'type': 'REAL',
            'report': 'bs'
        },
        'Other Stockholder Equity': {
            'columnName': 'other_stockholder_equity',
            'type': 'REAL',
            'report': 'bs'
        },
        'Preferred Stock': {
            'columnName': 'preferred_stock',
            'type': 'REAL',
            'report': 'bs'
        },
        'Property Plant and Equipment': {
            'columnName': 'property_plant_and_equipment',
            'type': 'REAL',
            'report': 'bs'
        },
        'Redeemable Preferred Stock': {
            'columnName': 'redeemable_preferred_stock',
            'type': 'REAL',
            'report': 'bs'
        },
        'Research Development': {
            'columnName': 'research_development',
            'type': 'REAL',
            'report': 'is'
        },
        'Retained Earnings': {
            'columnName': 'retained_earnings',
            'type': 'REAL',
            'report': 'bs'
        },
        'Sale Purchase of Stock': {
            'columnName': 'sale_purchase_of_stock',
            'type': 'REAL',
            'report': 'cf'
        },
        'Selling General and Administrative': {
            'columnName': 'selling_general_and_administrative',
            'type': 'REAL',
            'report': 'is'
        },
        'Short Term Investments': {
            'columnName': 'short_term_investments',
            'type': 'REAL',
            'report': 'bs'
        },
        'Short/Current Long Term Debt': {
            'columnName': 'short/current_long_term_debt',
            'type': 'REAL',
            'report': 'bs'
        },
        'Total Assets': {
            'columnName': 'total_assets',
            'type': 'REAL',
            'report': 'bs'
        },
        'Total Cash Flow From Operating Activities': {
            'columnName': 'total_cash_flow_from_operating_activities',
            'type': 'REAL',
            'report': 'cf'
        },
        'Total Cash Flows From Investing Activities': {
            'columnName': 'total_cash_flows_from_investing_activities',
            'type': 'REAL',
            'report': 'cf'
        },
        'Total Current Assets': {
            'columnName': 'total_current_assets',
            'type': 'REAL',
            'report': 'bs'
        },
        'Total Current Liabilities': {
            'columnName': 'total_current_liabilities',
            'type': 'REAL',
            'report': 'bs'
        },
        'Total Liabilities': {
            'columnName': 'total_liabilities',
            'type': 'REAL',
            'report': 'bs'
        },
        'Total Operating Expenses': {
            'columnName': 'total_operating_expenses',
            'type': 'REAL',
            'report': 'is'
        },
        'Total Other Income/Expenses Net': {
            'columnName': 'total_other_income/expenses_net',
            'type': 'REAL',
            'report': 'is'
        },
        'Total Revenue': {
            'columnName': 'total_revenue',
            'type': 'REAL',
            'report': 'is'
        },
        'Total Stockholder Equity': {
            'columnName': 'total_stockholder_equity',
            'type': 'REAL',
            'report': 'bs'
        },
        'Treasury Stock': {
            'columnName': 'treasury_stock',
            'type': 'REAL',
            'report': 'bs'
        }
    }
}
