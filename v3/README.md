## Refactored Code from v2
After learning object-oriented programming (OOP) about a week ago, I decided to refactor the entire codebase.  
The next goal is to develop a GUI version after I finish learning it.

## Features
- Mid thread validation (top, mid, bottom input)
- Calculate elevation & height difference automation
- Distance input between points
- Automatic status check (RISE, FALL, FLAT)
- Export result to Excel .xlsx 
- CSV backup if Excel export fails
- Neatly formatted table output in terminal
- make graphic (profile, bar chart, scatter plot)
- combine the graphic with excel result

## How It Works
1. User enters number of points, initial AMSL elevation and distance between each points.
2. For each point pair:
   - Input backsight and foresight using thread readings
   - Mid-thread is validated automatically
   - Elevation difference is calculated
   - Status is shown (RISE, FALL, FLAT)
3. the result can be shown with table in terminal
4. Final result can be exported to Excel, make graphic, and send graphic with final result