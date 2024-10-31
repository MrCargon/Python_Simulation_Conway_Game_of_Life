# Conway's Game of Life

A Python implementation of Conway's Game of Life using Pygame, featuring an interactive interface and customizable settings.

![Game of Life Preview](/api/placeholder/800/400)

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Rules of the Game](#rules-of-the-game)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Controls](#controls)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Overview

Conway's Game of Life is a cellular automaton devised by mathematician John Conway in 1970. It's a zero-player game, meaning its evolution is determined by its initial state, requiring no further input. The game takes place on a grid of cells, where each cell can be either alive or dead, and evolves according to a set of rules based on the states of neighboring cells.

## Features

- Interactive grid with clickable cells
- Adjustable simulation speed
- Generation and population counters
- Random pattern generation
- Grid wrapping (edges connect to opposite sides)
- Customizable grid size and colors
- On-screen controls help
- Status display showing key metrics

## Rules of the Game

### For Living Cells:
1. Any live cell with fewer than two live neighbors dies (underpopulation)
2. Any live cell with two or three live neighbors lives on to the next generation
3. Any live cell with more than three live neighbors dies (overpopulation)

### For Dead Cells:
1. Any dead cell with exactly three live neighbors becomes a live cell (reproduction)

## Requirements

- Python 3.7+
- Pygame 2.0+

## Installation

1. Clone the repository:
```bash
git clone ##
cd game-of-life
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

Run the game using Python:
```bash
python main.py
```

## Controls

- **Left Mouse Button**: Toggle cell state (alive/dead)
- **Space**: Play/Pause simulation
- **C**: Clear the grid
- **R**: Generate random pattern
- **↑/↓**: Adjust simulation speed
- **ESC** or close window: Quit game

## Configuration

The game can be customized by modifying the `GameConfig` class in `main.py`:

```python
@dataclass
class GameConfig:
    WIDTH: int = 800          # Window width
    HEIGHT: int = 800         # Window height
    TILE_SIZE: int = 20       # Size of each cell
    FPS: int = 60            # Frame rate
    MIN_SPEED: int = 1       # Minimum simulation speed
    MAX_SPEED: int = 10      # Maximum simulation speed
    DEFAULT_SPEED: int = 5   # Starting simulation speed
```

Colors can be customized in the `Colors` class:

```python
@dataclass
class Colors:
    BLACK: Tuple[int, int, int] = (0, 0, 0)
    GREY: Tuple[int, int, int] = (128, 128, 128)
    YELLOW: Tuple[int, int, int] = (255, 255, 0)
    GREEN: Tuple[int, int, int] = (0, 255, 0)
    RED: Tuple[int, int, int] = (255, 0, 0)
```

## Project Structure

```
game-of-life/
│
├── main.py              # Main game implementation
├── requirements.txt     # Project dependencies
└── README.md           # Project documentation
```

## Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a Pull Request

### Areas for Improvement

- Add pattern saving/loading functionality
- Implement different cell colors for age visualization
- Add more complex pattern generation algorithms
- Create a pattern library
- Add sound effects and animations
- Implement statistics tracking

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- John Conway for creating the Game of Life
- The Pygame community for their excellent library
- All contributors to this project

## Contact

For questions, suggestions, or issues, please open an issue in the GitHub repository.