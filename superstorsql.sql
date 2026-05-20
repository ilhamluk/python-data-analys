select * from public.sample_superstore ss 
where "Category" = 'furniture' or "Sub-Category" = 'Tables'

select * from public.sample_superstore ss 
where "Discount" != 0`

select * from public.sample_superstore ss 
where "Quantity" in (2,3,5)

select * from public.sample_superstore ss 
where "Quantity" not in (2,3,5)

select "Customer Name"
from public.sample_superstore ss 
where "City" in ('Albany', 'Houston')

select 
SUM ("Sales") as total_profit
from public.sample_superstore ss 
where "State" = 'Texas' or "Region" = 'South';


select AVG ("Profit") 
from public.sample_superstore ss 
where "Category" != 'Office Supplies'

select distinct "Customer Name" from public.sample_superstore ss
where "Ship Mode" != 'Standard Class' and
"Segment" = 'Consumer' and
"Customer Name" not in ('Ted Butterfield', 'Karl Braun') and 
"State" in ('Delaware', 'Ohio')

 