This is a simulation that mimics market events that occurred between 2025 and 2026 for the ticker symbol: MSTY. The simulation is modified to apply to a separate group of 7 ETFs (exchange-traded funds) to model how economic declines and business uncertainty can result in a reverse stock split, on top of a decline in share values.



Write a program at /app/solve.py that takes the input file titled "Portfolio for Schwab Investments - Test.xlsx" from the /app/solution directory and populates the model calculations side-by-side, and then creates an output file containing the calculations explained below in the /app/solution/outputfile directory, titled "Portfolio for Schwab Investments - Solved.xlsx".



Ignore any other files in these folders and add data in the input file workbook under each of the columns with the header "Model Figure".



These inputs are provided to you for you to utilize:



\- BAB:  Price = $27.20, Annual Dividend = $0.094     Distributions: Monthly

\- BKLN: Price = $21.00, Annual Dividend = $0.103     Distributions: Monthly

\- HYBL: Price = $28.44, Annual Dividend = $0.168     Distributions: Monthly

\- PGHY: Price = $19.90, Annual Dividend = $0.12169   Distributions: Monthly

\- VRP:  Price = $24.33, Annual Dividend = $0.21      Distributions: Monthly

\- VYMI: Price = $90.00, Annual Dividend = $0.939     Distributions: Quarterly

\- AMDY: Price = $38.05, Annual Dividend = $0.412     Distributions: Weekly



Updated market values (in a separate column) for this operation are in Table 2:



\- BAB:  Price = $23.12

\- BKLN: Price = $17.85

\- HYBL: Price = $24.17

\- PGHY: Price = $16.91

\- VRP:  Price = $20.68

\- VYMI: Price = $76.50

\- AMDY: Price = $19.03



Two tables are present in the worksheet. There is an initial investment table. Below that there is a table simulating a reverse stock split. In both tables, $50,000 should be considered the initial investment for AMDY, with the remaining $200,000 invested into all other ETFs spread equally, for a total investment of $250,000.



The reverse stock split causes AMDY to have 50% of the total quantity of shares as before and 85% of the total quantity of shares as before for the other 6 ETFs. For the first table, this does not apply. In the second table, assume that some time has passed after the reverse stock split, and economic decline has caused the share prices to drop to the level specified above.



There are 6 columns labeled as "Model Figure". In the same order of these columns from left to right, you will have to compute the:

* Cost Basis Total Dollars Invested
* Total quantity of shares
* Total ETF Dividend/Share per Year
* Gross Total ETF Dividend per Year
* Gross Total ETF Dividend per Month
* The Total ETF Dividend per Month (Net of the standard qualified dividend tax deducted)



You have 28800 seconds to complete this task.

