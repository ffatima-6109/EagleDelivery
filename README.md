# Eagle Delivery - Project 1

**Name:** Faizah Fatima  
**Course:** COSC 461  
**Project:** Eagle Delivery

## 1. Introduction

In this project, I worked on a simulated delivery robot for Eastern Michigan University. The goal was to help the robot travel from one campus building to another.

I used BFS and A* search to find the shortest routes. I also used Q-learning to train the robot to make decisions through experience. Finally, I created a custom campus map and tested how different exploration rates affect the robot's learning and performance.

## 2. Requirements

- Python 3.9 or newer
- No additional search or reinforcement learning libraries are needed.

## 3. How to Run the Project

Open a terminal inside the project folder.

### Display the campus map

```bash
python3 run_project.py show
```

### Run BFS

```bash
python3 run_project.py search --algorithm bfs --start S --goal W
```

### Run A*

```bash
python3 run_project.py search --algorithm astar --start S --goal W
```

### Run A* on the detour map

```bash
python3 run_project.py search --map maps/emu_detour.txt --algorithm astar --start S --goal W
```

### Run the unit tests

```bash
python3 -m unittest discover -v
```

## 4. Part A: BFS and A*

I compared BFS and A* on two campus maps using six delivery tasks.

Both algorithms found the same shortest path lengths. However, A* usually expanded fewer nodes because it used Manhattan distance to estimate how far the robot was from its destination.

## 5. Part B: Q-learning

For this part, I trained the robot using Q-learning. The robot learned which actions were better by receiving rewards after moving.

I used the following settings:

- Training episodes: 2,000 per seed
- Evaluation episodes: 100 per seed
- Random seeds: 0, 1, and 2
- Maximum steps: 200
- Learning rate (alpha): 0.3
- Discount factor (gamma): 0.95
- Exploration rate (epsilon): 0.2
- Slip probability: 0.0

### Training Commands

```bash
python3 run_project.py train --start S --goal W --output results/baseline_SW

python3 run_project.py train --start L --goal D --output results/baseline_LD

python3 run_project.py train --start H --goal P --output results/baseline_HP

python3 run_project.py train --map maps/emu_detour.txt --start S --goal W --output results/detour_SW
```

All four tasks achieved a 100% evaluation success rate with the settings I used.

## 6. Part C: Custom Campus Map

I used `maps/my_campus.txt` for the custom map experiment.

I tested how the exploration rate affects the robot's learning.

My experiment question was:

**How does changing epsilon affect the robot's learning and delivery performance?**

I used three epsilon values:

- 0.05
- 0.20
- 0.50

I kept the other training settings the same for all three experiments.

### Custom Experiment Commands

```bash
python3 run_project.py train --map maps/my_campus.txt --epsilon 0.05 --output results/custom_005

python3 run_project.py train --map maps/my_campus.txt --epsilon 0.2 --output results/custom_020

python3 run_project.py train --map maps/my_campus.txt --epsilon 0.5 --output results/custom_050
```

### Results

All three epsilon settings achieved a 100% final evaluation success rate. Each had a mean return of 20 and an average of 20 delivery steps.

During the first 100 training episodes, the success rates were approximately 91.33%, 90%, and 89% for epsilon values 0.05, 0.20, and 0.50.

This showed that the three exploration rates had small differences early in training, but all achieved the same final evaluation performance.

## 7. Summarizing Results

I used `summarize_results.py` to calculate the average results across the three random seeds and create learning-curve CSV files.

Example:

```bash
python3 summarize_results.py results/custom_005
```

The other result folders can be summarized using the same command with their respective folder names.

## 8. Project Files

- `agents.py`: BFS, A*, epsilon-greedy, and Q-learning implementations
- `campus.py`: Campus map and delivery environment
- `run_project.py`: Runs the searches and training experiments
- `summarize_results.py`: Summarizes the CSV results
- `maps/`: Original maps and custom campus map
- `tests/`: Tests for the program
- `results/`: Training, evaluation, summary, and learning-curve CSV files
- `EagleDelivery_Report_Faizah_Fatima.pdf`: Final project report

## 9. Conclusion

From this project, I learned how BFS, A*, and Q-learning can be used for robot navigation. A* generally explored fewer nodes than BFS while finding the same shortest paths. Q-learning also helped the robot learn successful delivery routes.

The custom experiment helped me understand how exploration affects learning. All three epsilon settings reached the same final evaluation performance, even though their early training results were slightly different.