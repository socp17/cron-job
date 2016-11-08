CREATE OR REPLACE FUNCTION add_company( ticker text) RETURNS boolean AS $$ DECLARE did_insert boolean := false;
