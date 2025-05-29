# Logic Gate Simulator

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Pygame](https://img.shields.io/badge/pygame-2.1+-green.svg)
![License](https://img.shields.io/badge/license-MIT-orange.svg)

**Logic Gate Simulator** is an educational GUI-based application built with Python and Pygame. This interactive tool helps beginners understand fundamental logic gates through visual experimentation. Users can connect virtual logic gates, toggle inputs, and observe real-time output behavior.

## Screenshot Gallery
| Basic Gate Operations | Interactive Simulation |
|------------------------|------------------------|
| ![Basic Operations](https://github.com/TechnicalCoderji/GUI-Project/blob/50a801267a7f3c2dd151c220dd5f99f4c6686624/Logic%20Gate/img/s2.png) | ![Interactive Simulation](https://github.com/TechnicalCoderji/GUI-Project/blob/50a801267a7f3c2dd151c220dd5f99f4c6686624/Logic%20Gate/img/s1.png) |
| *Testing basic gate configurations* | *Real-time output visualization* |

## Features
- 🖱️ Interactive UI using Pygame
- 💡 Visual input/output indicators (LED-style)
- 📚 Educational design focused on learning logic concepts

## Supported Gates
The simulator currently supports these 7 fundamental logic gates:
- AND
- OR
- NOT
- NAND
- NOR
- XOR
- XNOR

## Installation
1. Ensure you have Python 3.8+ installed
2. Install Pygame:
   ```bash
   pip install pygame
   ```
3. Clone the repository:
   ```bash
   git clone https://github.com/TechnicalCoderji/GUI-Project/Logic Gate.git
   ```
4. Run the simulator:
   ```bash
   cd Logic Gate
   python main.py
   ```

## Usage Instructions
1. **Select gates**: Click on any gate from the menu at the bottom
2. **Toggle inputs**: Click on input pins (left side) to switch between 0 (OFF) and 1 (ON)
3. **Observe outputs**: Output pins (right side) automatically update with LED indicators:
   - 🔴 Red: 0 (False)
   - 🟢 Green: 1 (True)

## Project Structure
```
logic-gate-simulator/
├── main.py          # Main application and GUI logic
├── gate.py          # Logic gate implementations and classes
├── img/             # Screenshots and graphical assets
├── README.md        # Project documentation (this file)
└── requirements.txt # Python dependencies
```

## Future Plans
- 🔊 Sound effects for user interactions
- 📊 Integrated truth table display for current configurations

## License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
