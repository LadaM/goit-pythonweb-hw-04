import argparse
import asyncio
import logging
import time
from file_operations import async_copytree_custom
from aioshutil import copytree as aioshutil_copytree

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def parse_args():
    parser = argparse.ArgumentParser(description="Async folder copy performance comparison.")
    parser.add_argument("--source", required=True, help="Source folder path.")
    parser.add_argument("--target", required=True, help="Base target folder path.")
    return parser.parse_args()

async def main():
    args = parse_args()
    source = args.source
    target1 = args.target
    target2 = f"{args.target}_shutil"  # Append "_shutil" to the target path for the second copy

    # Copy using the custom method
    logging.info(f"Starting copy process (custom method) from {source} to {target1}")
    start_time_custom = time.monotonic()
    await async_copytree_custom(source, target1)
    elapsed_time_custom = time.monotonic() - start_time_custom

    # Copy using the aioshutil method
    logging.info(f"Starting copy process (aioshutil method) from {source} to {target2}")
    start_time_aioshutil = time.monotonic()
    await aioshutil_copytree(source, target2, dirs_exist_ok=True)
    elapsed_time_aioshutil = time.monotonic() - start_time_aioshutil

    print("\n==== Performance Comparison ====")
    print(f"Custom Method: {elapsed_time_custom:.3f} seconds")
    print(f"Aioshutil Method: {elapsed_time_aioshutil:.3f} seconds")
    print("================================")

if __name__ == "__main__":
    asyncio.run(main())
