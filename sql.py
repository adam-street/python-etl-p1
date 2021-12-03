test_select = ('''
  SELECT *
  FROM public.test_table;
''')

test_insert = ('''
  INSERT INTO public.test_table
  VALUES(%s);
''')
