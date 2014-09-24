def convert(value):
	if vale.startwith('~'):
		return value.strip('~')
	if not value:
		value = '0'
		return float(value)
	conn = sqlite3.connect('food.db')
	curs = conn.cursor()
	curs.execute('''
         create table food(
         id   TEXT     PRIMARY KEY,
         desc TEXT,
         water FLOAT,
         kcal   FLOAT,
         protein FLOAT,
         fat     FLOAT,
         ash      FLOAT,
         carbs    FLAOT,
         fiber    FLOAT,
         sugar    FLOAT
         )
         ''')
	query = 'INSERT INTO food VALUES (?,?,?,?,?,?,?,?,?,?)'
	for line in open(r'c:/ABBREV.txt'):
		fields = line.split('^')
		vals = [convert(f) for f in fields[:field_count]]
		curs.execute(query,vals)
		conn.commit()
		conn.close()
		
