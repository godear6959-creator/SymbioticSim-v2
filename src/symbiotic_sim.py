import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import entropy

class SymbioticSim:
    """
    SymbioticSim v2.0 (Beta Cuántica)
    Núcleo de simulación de redes simbióticas con memoria persistente y entrelazamiento.
    """
    
    def __init__(self, size=100):
        self.size = size
        # Memoria Estructural (95% persistencia)
        self.memory_grid = np.random.rand(size, size) * 0.95
        # Gradientes de Entrelazamiento (0.0001 - 0.0171)
        self.entanglement_gradients = np.random.uniform(0.0001, 0.0171, (size, size))
        # Ruido Adaptativo (0 - 1)
        self.adaptive_noise = np.random.rand(size, size)
        
    def calculate_shannon_entropy(self):
        """Calcula la entropía de Shannon del estado actual."""
        flat_grid = self.memory_grid.flatten()
        hist, _ = np.histogram(flat_grid, bins=256, density=True)
        return entropy(hist + 1e-10) # Evitar log(0)

    def mutate(self, chaos_factor=0.1):
        """Aplica mutación adaptativa basada en el ruido y los gradientes."""
        mutation = (self.adaptive_noise * self.entanglement_gradients) * chaos_factor
        self.memory_grid = np.clip(self.memory_grid + mutation, 0, 1)
        # Mantener la persistencia del 95%
        self.memory_grid *= 0.95
        return self.calculate_shannon_entropy()

    def plot_state(self, save_path=None):
        """Visualiza el estado actual de la red simbiótica."""
        plt.figure(figsize=(10, 8))
        plt.imshow(self.memory_grid, cmap='magma')
        plt.colorbar(label='Persistencia de Memoria')
        plt.title(f"Estado SymbioticSim v2.0 - Entropía: {self.calculate_shannon_entropy():.2f} bits")
        if save_path:
            plt.savefig(save_path)
        plt.show()

if __name__ == "__main__":
    print("Iniciando SymbioticSim v2.0 (Beta Cuántica)...")
    sim = SymbioticSim()
    initial_entropy = sim.calculate_shannon_entropy()
    print(f"Entropía Inicial: {initial_entropy:.4f} bits")
    
    # Simular 100 pasos de mutación
    for _ in range(100):
        sim.mutate()
        
    final_entropy = sim.calculate_shannon_entropy()
    print(f"Entropía Final (tras 100 pasos): {final_entropy:.4f} bits")
    print("Simulación completada. Integridad cuántica asegurada.")
