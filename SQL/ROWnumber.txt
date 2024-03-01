# ROW_NUMBER()

select column1, column2,
ROW_NUMBER() over (ORDER BY column1) AS row_number
from Table_name
WHERE <condition>

# ROW_NUMBER using PARTITION

select column1, column2,
ROW_NUMBER() over (PARTITION by column2 ORDER BY column1) AS row_number
from Table_name
WHERE <condition>