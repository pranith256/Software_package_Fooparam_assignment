import argparse
from .core import complex_volume_calculation

def main():
    parser = argparse.ArgumentParser(description="Perform complex volume calculations.")
    parser.add_argument('radius', type=float, help='Radius of the sphere')
    args = parser.parse_args()

    try:
        volume = complex_volume_calculation(args.radius)
        print(f"The calculated volume of the sphere is: {volume} cubic units.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()