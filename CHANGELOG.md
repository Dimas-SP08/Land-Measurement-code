# Changelog

## [v4.0] – 2025-08-08

### Added
- Full GUI interface using **PyQt5**
- Multi-page navigation: Welcome → Input → Thread → Table → Graph → Export
- Dynamic graph rendering (Elevation Profile, Height Difference, Scatter Plot)
- Export options:
  - Save graphs as PNG
  - Export data to CSV
  - Export to Excel with embedded graphs
- `.exe` build for standalone distribution
- Modular UI components (`ui/pages`) and controller logic (`core`)
- Integrated `QStackedWidget` for seamless page transitions

### Changed
- Simplified and clarified docstrings across all modules
- Reorganized project structure for GUI version (`core`, `ui`, `utils`)
- Improved input validation and error handling in GUI
- Replaced CLI prompts with interactive widgets and buttons

---

## [v3.0] – 2025-07-24

### Added
- ‘FLAT’ status when height difference is zero  
- `input_yes_no()` helper for yes/no prompts  
- CSV backup (`csv_backup.py`) if Excel export fails
- Clear screen now works on both Windows and Unix-like terminals 

### Changed
- Full OOP refactor into modules:  
  `survey_point`, `survey_controller`, `survey_cli`,  
  `utils`, `csv_backup`, `excel_tools`, `graphic_tools` 
- Made exception handling more specific (Excel errors now fall back to CSV)
- Improved docstrings in all modules
- Enhanced code organization and readability  
- Streamlined CLI workflow interface 

---

## [v2.0] – 2025-07-13

### Added
- Elevation profile chart (Matplotlib)  
- Height-difference bar chart  
- Scatter plot of elevation vs. distance  
- Automatic embedding of graphs into Excel  

### Changed
- Refactored core functions for improved code efficiency  
- Enhanced input validation and user prompts  

---

## [v1.0] – 2025-07-11

### Added
- Elevation & status (RISE/FALL) calculation  
- Mid-thread validation (top, mid, bottom readings)  
- Distance input between points  
- Export results to Excel (.xlsx)  
- Neatly formatted table output in the terminal  
