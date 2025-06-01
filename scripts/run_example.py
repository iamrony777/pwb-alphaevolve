import asyncio

from alphaevolve import AlphaEvolve

# Initialize the system
evolve = AlphaEvolve(initial_program_paths=["examples/sma_momentum.py"])


# Run the evolution
async def main() -> None:
    best_strategy = await evolve.run(iterations=10)
    print("Best strategy metrics:")
    for name, value in best_strategy.metrics.items():
        print(f"  {name}: {value:.4f}")


if __name__ == "__main__":
    asyncio.run(main())
