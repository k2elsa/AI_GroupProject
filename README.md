# AI_GroupProject_ARI711S

## Overview
This repository contains the group project for **Artificial Intelligence (ARI711S)** at the Namibia University of Science and Technology (NUST), 2026.  
The project is divided into three parts, each exploring a different area of AI:

1. **Flight Connections (Search Algorithms)** - Finding shortest paths between cities using flight data.  
2. **Hospital Shift Scheduler (Constraint Satisfaction Problem)** - Assigning nurses to shifts while respecting constraints.  
3. **Traffic Sign Recognition (Machine Learning)** - Training a CNN to classify German traffic signs.  



##  Group Members
- **Elsa ** - Part 1 (Data loading + neighbors function), Team Lead, Notebook merge & documentation  
- **Lourena** - Part 1 (Shortest path search)  
- **Juliette** - Part 2 (Node consistency + AC-3 algorithm)  
- **Rejoice** - Part 2 (MRV heuristic + Backtracking with forward checking)  
- **Penduleni** - Part 3 (Traffic sign preprocessing + CNN model)  


##  Repository Structure
AI_GroupProject_ARI711S/
|
|-- part1_flights/          # Flight connections code (Elsa + Lourena)
|-- part2_scheduler/        # Hospital shift scheduler code (Juliette + Rejoice)
|-- part3_traffic_signs/    # Traffic sign recognition code (Penduleni)
|-- notebook/               # Final merged notebook (AI_Project_Final.ipynb)
|-- data/                   # Datasets (CSV files, staff files, GTSRB dataset)
|-- README.md               # Project documentation
|-- LICENSE                 # MIT License



##  Tools & Libraries
- **Python** (main language)  
- **Jupyter Notebook** (final submission format)  
- **GitHub** (collaboration and version control)  
- **Markdown** (documentation inside notebooks)  
- **TensorFlow, OpenCV, Scikit-Learn** (Part 3 - Traffic Sign Recognition)  
- **Standard Python libraries** (csv, collections, queue, etc. for Parts 1 & 2)  



##  How to Run

### Part 1: Flight Connections
```bash
python flights.py data/
Loads cities.csv, flights.csv, airlines.csv.
Finds shortest path between two cities.

Part 2: Hospital Shift Scheduler
bash
python shift_solver.py staff_small.txt
Generates valid weekly schedule using CSP techniques.
Supports node consistency, AC-3, MRV heuristic, and backtracking.

Part 3: Traffic Sign Recognition
bash
python traffic_signs.py gtsrb/ model.h5
Loads and preprocesses GTSRB dataset.
Trains CNN model and saves it as model.h5.
Evaluates accuracy and confusion matrix.

 Deliverables
Final Jupyter Notebook (AI_Project_Final.ipynb) with all three parts merged.

PDF export of the notebook for submission.

GitHub repository link with all code, datasets, and documentation.

 Results
Part 1: Correct shortest path outputs between cities.

Part 2: Valid weekly schedule generated, all constraints satisfied.

Part 3: CNN model trained with accuracy above 95%.

 Notes
Each member contributed code individually and committed separately.

Repository follows best practices with clear structure and documentation.

All outputs are visible in the final notebook.
# AI_GroupProject_ARI711S

## Overview
This repository contains the group project for **Artificial Intelligence (ARI711S)** at the Namibia University of Science and Technology (NUST), 2026.  
The project is divided into three parts, each exploring a different area of AI:

1. **Flight Connections (Search Algorithms)** – Finding shortest paths between cities using flight data.  
2. **Hospital Shift Scheduler (Constraint Satisfaction Problem)** – Assigning nurses to shifts while respecting constraints.  
3. **Traffic Sign Recognition (Machine Learning)** – Training a CNN to classify German traffic signs.  



##  Group Members
- **Elsa Kumwimba** – Part 1 (Data loading + neighbors function), Team Lead, Notebook merge & documentation  
- **Lourena** – Part 1 (Shortest path search)  
- **Juliette** – Part 2 (Node consistency + AC‑3 algorithm)  
- **Rejoice** – Part 2 (MRV heuristic + Backtracking with forward checking)  
- **Penduleni** – Part 3 (Traffic sign preprocessing + CNN model)  


##  Repository Structure
AI_GroupProject_ARI711S/
│
├── part1_flights/          # Flight connections code (Elsa + Lourena)
├── part2_scheduler/        # Hospital shift scheduler code (Juliette + Rejoice)
├── part3_traffic_signs/    # Traffic sign recognition code (Penduleni)
├── notebook/               # Final merged notebook (AI_Project_Final.ipynb)
├── data/                   # Datasets (CSV files, staff files, GTSRB dataset)
├── README.md               # Project documentation
├── LICENSE                 # MIT License



##  Tools & Libraries
- **Python** (main language)  
- **Jupyter Notebook** (final submission format)  
- **GitHub** (collaboration and version control)  
- **Markdown** (documentation inside notebooks)  
- **TensorFlow, OpenCV, Scikit‑Learn** (Part 3 – Traffic Sign Recognition)  
- **Standard Python libraries** (csv, collections, queue, etc. for Parts 1 & 2)  



##  How to Run

### Part 1: Flight Connections
```bash
python flights.py data/
Loads cities.csv, flights.csv, airlines.csv.
Finds shortest path between two cities.

Part 2: Hospital Shift Scheduler
bash
python shift_solver.py staff_small.txt
Generates valid weekly schedule using CSP techniques.
Supports node consistency, AC‑3, MRV heuristic, and backtracking.

Part 3: Traffic Sign Recognition
bash
python traffic_signs.py gtsrb/ model.h5
Loads and preprocesses GTSRB dataset.
Trains CNN model and saves it as model.h5.
Evaluates accuracy and confusion matrix.

 Deliverables
Final Jupyter Notebook (AI_Project_Final.ipynb) with all three parts merged.

PDF export of the notebook for submission.

GitHub repository link with all code, datasets, and documentation.

 Results
Part 1: Correct shortest path outputs between cities.

Part 2: Valid weekly schedule generated, all constraints satisfied.

Part 3: CNN model trained with accuracy above 95%.

 Notes
Each member contributed code individually and committed separately.

Repository follows best practices with clear structure and documentation.

All outputs are visible in the final notebook.
