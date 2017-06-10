CREATE TABLE IF NOT EXISTS product(name TEXT, description TEXT, bar_code TEXT, qtd INTEGER);
CREATE TABLE IF NOT EXISTS input_product(id INTEGER, nfe TEXT, datetime TEXT);
CREATE TABLE IF NOT EXISTS product_from_input(input_id INTEGER, product_bar TEXT, qtd INTEGER);
CREATE TABLE IF NOT EXISTS output_product(id INTEGER, nfe TEXT, datetime TEXT);
CREATE TABLE IF NOT EXISTS product_from_output(output_id INTEGER, product_bar TEXT, qtd INTEGER);