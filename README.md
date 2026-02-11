# First-Year-Project-Minesweeper-Game-Development-and-Comparative-ChatGPT-Study
# 🎮 Minesweeper Game Development & ChatGPT Performance Analysis
# 🎮 First-Year Computer Science Projects — Minesweeper & Dungeon Crawler

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![LaTeX](https://img.shields.io/badge/Report-LaTeX-green.svg)](https://www.latex-project.org/)
[![University](https://img.shields.io/badge/University-ULB-red.svg)](https://www.ulb.be/)
[![Course](https://img.shields.io/badge/Course-INFO--F--106-orange.svg)]()

---

## 📋 Description

This repository contains the work completed for the **INFO-F-106: Computer Science Project** course at the **Université Libre de Bruxelles (ULB)**.

The course consists of **three main components**:

| # | Project | Description |
|---|---------|-------------|
| 1 | **Minesweeper** | Classic Minesweeper game implementation in Python |
| 2 | **Dungeon Crawler** | Interactive maze/labyrinth exploration game |
| 3 | **ChatGPT Report** | Scientific analysis of ChatGPT's capabilities in programming |

---

## 🎯 Projects Overview

### 🧨 Project 1: Minesweeper

A fully functional implementation of the classic **Minesweeper** game in Python.

**Features:**
- Grid-based gameplay with customizable dimensions
- Random mine placement
- Recursive cell revealing (propagate click)
- Win/loss detection
- Clean terminal-based interface

---

### 🏰 Project 2: Dungeon Crawler (Interactive Maze)

An **interactive labyrinth exploration game** where the player navigates through a dungeon.

**Features:**
- Procedurally generated or predefined maze
- Player movement (up, down, left, right)
- Obstacles, traps, and collectibles
- Goal: reach the exit or complete objectives
- Terminal-based interactive gameplay

---

### 📊 Project 3: ChatGPT Performance Analysis

A **scientific report** evaluating the capabilities and limitations of ChatGPT in assisting software development.

**Research Questions:**
- Can ChatGPT generate functional code without detailed instructions?
- Is it more effective on specific tasks than general ones?
- Does it actually save development time?
- What are its main advantages and limitations?

**Conclusion:**  
ChatGPT is a powerful assistant but **does not replace** the programmer. Its effectiveness depends heavily on the user's expertise and the precision of instructions provided.

---

## 📁 Repository Structure


## 📁 Repository Structure
```
├── 📄 README.md # This file
│
├── 📂 doc/ # Documentation
│ ├── 📄 project_guidelines.pdf # Project specifications (partial)
│ └── 📄 report_guidelines.pdf # Report instructions (partial)
│
├── 📂 project1_minesweeper/ # Minesweeper game
│ ├── 🐍 minesweeper.py # Main game code
│ └── 📄 README.md # Project-specific instructions
│
├── 📂 project2_dungeon_crawler/ # Dungeon Crawler game
│ ├── 🐍 dungeon.py # Main game code
│ └── 📄 README.md # Project-specific instructions
│
├── 📂 report/ # ChatGPT analysis report
│ ├── 📄 rapport.tex # LaTeX source
│ ├── 📄 rapport.pdf # Compiled report
│
└── 
```


## 🛠️ Technologies Used

| Component | Technology |
|-----------|------------|
| Game | Python 3.x |
| Report | LaTeX |
| Version Control | Git & GitHub |

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed
- LaTeX distribution (for compiling the report)

### Running the Game

```bash
cd minesweeper
python main.py

cd report
pdflatex rapport.tex
