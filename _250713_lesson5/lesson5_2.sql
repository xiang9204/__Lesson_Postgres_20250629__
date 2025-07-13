-- 刪除 employee TABLE
-- CASCADE 是將所有級連，即所有有關聯的資料表，皆刪除。
DROP TABLE IF EXISTS employee CASCADE;

-- 創建 employee TABLE
CREATE TABLE employee(
	emp_id SERIAL,
	name VARCHAR(20),
	birth_date DATE,
	sex VARCHAR(1),
	salary INT,
	branch_id INT,
	sup_id INT,
 	PRIMARY KEY(emp_id)
);

-- 創建 branch TABLE，並將 branch 的 manager_id 參照進 employee 的 emp_id
CREATE TABLE branch(
	branch_id INT,
	branch_name VARCHAR(20),
	manager_id INT,
	PRIMARY KEY(branch_id),
	FOREIGN KEY(manager_id)
	REFERENCES employee(emp_id) ON DELETE SET NULL
);

-- 增加 FOREIFN KEY
ALTER TABLE employee ADD FOREIGN KEY(branch_id)
REFERENCES branch(branch_id) ON DELETE SET NULL;

ALTER TABLE employee ADD FOREIGN KEY(sup_id)
REFERENCES employee(emp_id) ON DELETE SET NULL;