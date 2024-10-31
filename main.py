import pygame
import random
from typing import Set, Tuple, List, Optional
from dataclasses import dataclass

# Constants
@dataclass
class Colors:
    BLACK: Tuple[int, int, int] = (0, 0, 0)
    GREY: Tuple[int, int, int] = (128, 128, 128)
    YELLOW: Tuple[int, int, int] = (255, 255, 0)
    GREEN: Tuple[int, int, int] = (0, 255, 0)
    RED: Tuple[int, int, int] = (255, 0, 0)

@dataclass
class GameConfig:
    WIDTH: int = 800
    HEIGHT: int = 800
    TILE_SIZE: int = 20
    FPS: int = 60
    MIN_SPEED: int = 1
    MAX_SPEED: int = 10
    DEFAULT_SPEED: int = 5

class GameOfLife:
    def __init__(self, config: GameConfig = GameConfig()):
        pygame.init()
        self.config = config
        self.colors = Colors()
        
        # Calculate grid dimensions
        self.GRID_WIDTH = self.config.WIDTH // self.config.TILE_SIZE
        self.GRID_HEIGHT = self.config.HEIGHT // self.config.TILE_SIZE
        
        # Initialize pygame
        self.screen = pygame.display.set_mode((self.config.WIDTH, self.config.HEIGHT))
        pygame.display.set_caption("Conway's Game of Life")
        self.clock = pygame.time.Clock()
        
        # Game state
        self.positions: Set[Tuple[int, int]] = set()
        self.running: bool = True
        self.playing: bool = False
        self.speed: int = self.config.DEFAULT_SPEED
        self.generation: int = 0
        self.population: int = 0
        
        # UI elements
        self.font = pygame.font.Font(None, 36)

    def generate_random_cells(self, density: float = 0.3) -> Set[Tuple[int, int]]:
        """Generate random initial state with specified density (0.0 to 1.0)"""
        total_cells = int(self.GRID_WIDTH * self.GRID_HEIGHT * density)
        return set([(random.randrange(0, self.GRID_HEIGHT), 
                    random.randrange(0, self.GRID_WIDTH)) 
                   for _ in range(total_cells)])

    def get_neighbors(self, pos: Tuple[int, int]) -> List[Tuple[int, int]]:
        """Get valid neighbors for a given position"""
        x, y = pos
        neighbors = []
        
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                    
                new_x, new_y = x + dx, y + dy
                
                # Implement wrapping around edges
                new_x = new_x % self.GRID_WIDTH
                new_y = new_y % self.GRID_HEIGHT
                
                neighbors.append((new_x, new_y))
                
        return neighbors

    def update_grid(self) -> Set[Tuple[int, int]]:
        """Update the grid according to Conway's Game of Life rules"""
        new_positions = set()
        candidates = set()
        
        # Add all neighbors of live cells to candidates
        for pos in self.positions:
            candidates.add(pos)
            candidates.update(self.get_neighbors(pos))
        
        # Check each candidate
        for pos in candidates:
            neighbors = self.get_neighbors(pos)
            live_neighbors = sum(1 for n in neighbors if n in self.positions)
            
            # Apply Conway's rules
            if pos in self.positions:
                if live_neighbors in [2, 3]:
                    new_positions.add(pos)
            else:
                if live_neighbors == 3:
                    new_positions.add(pos)
        
        return new_positions

    def draw_grid(self) -> None:
        """Draw the game grid and cells"""
        self.screen.fill(self.colors.GREY)
        
        # Draw live cells
        for position in self.positions:
            col, row = position
            top_left = (col * self.config.TILE_SIZE, row * self.config.TILE_SIZE)
            pygame.draw.rect(self.screen, self.colors.YELLOW, 
                           (*top_left, self.config.TILE_SIZE, self.config.TILE_SIZE))
        
        # Draw grid lines
        for row in range(self.GRID_HEIGHT + 1):
            pygame.draw.line(self.screen, self.colors.BLACK, 
                           (0, row * self.config.TILE_SIZE), 
                           (self.config.WIDTH, row * self.config.TILE_SIZE))
        
        for col in range(self.GRID_WIDTH + 1):
            pygame.draw.line(self.screen, self.colors.BLACK, 
                           (col * self.config.TILE_SIZE, 0), 
                           (col * self.config.TILE_SIZE, self.config.HEIGHT))

    def draw_ui(self) -> None:
        """Draw UI elements including status and controls"""
        # Draw status bar
        status_text = f"Generation: {self.generation} | Population: {len(self.positions)} | Speed: {self.speed}x"
        status = self.font.render(status_text, True, self.colors.BLACK)
        self.screen.blit(status, (10, 10))
        
        # Draw controls help
        controls = [
            "Space: Play/Pause",
            "C: Clear",
            "R: Random",
            "Up/Down: Speed",
            "Click: Toggle Cell"
        ]
        
        for i, text in enumerate(controls):
            control = self.font.render(text, True, self.colors.BLACK)
            self.screen.blit(control, (10, 50 + i * 30))

    def handle_events(self) -> None:
        """Handle pygame events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                col = x // self.config.TILE_SIZE
                row = y // self.config.TILE_SIZE
                pos = (col, row)
                
                if pos in self.positions:
                    self.positions.remove(pos)
                else:
                    self.positions.add(pos)
                    
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.playing = not self.playing
                    
                elif event.key == pygame.K_c:
                    self.positions.clear()
                    self.playing = False
                    self.generation = 0
                    
                elif event.key == pygame.K_r:
                    self.positions = self.generate_random_cells()
                    
                elif event.key == pygame.K_UP:
                    self.speed = min(self.speed + 1, self.config.MAX_SPEED)
                    
                elif event.key == pygame.K_DOWN:
                    self.speed = max(self.speed - 1, self.config.MIN_SPEED)

    def run(self) -> None:
        """Main game loop"""
        update_counter = 0
        
        while self.running:
            self.clock.tick(self.config.FPS)
            self.handle_events()
            
            if self.playing:
                update_counter += self.speed
                
                if update_counter >= self.config.FPS // 10:
                    update_counter = 0
                    self.positions = self.update_grid()
                    self.generation += 1
            
            self.draw_grid()
            self.draw_ui()
            pygame.display.update()
        
        pygame.quit()

if __name__ == "__main__":
    game = GameOfLife()
    game.run()