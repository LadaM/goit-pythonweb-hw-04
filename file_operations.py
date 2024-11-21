import logging
from aiopath import AsyncPath


async def async_copytree_custom(source_folder: str, target_folder: str):
    source_path = AsyncPath(source_folder)
    target_path = AsyncPath(target_folder)

    if not await source_path.is_dir():
        raise ValueError(f"Source folder '{source_folder}' does not exist or is not a directory.")

    await target_path.mkdir(parents=True, exist_ok=True)

    async for item in source_path.glob("**/*"):
        relative_path = item.relative_to(source_path)
        target_item = target_path / relative_path

        if await item.is_dir():
            await target_item.mkdir(parents=True, exist_ok=True)
        else:
            try:
                await async_copy_file(item, target_item)
            except Exception as e:
                logging.error(f"Failed to copy file {item} to {target_item}: {e}")


async def async_copy_file(source_file: AsyncPath, target_file: AsyncPath):
    """Asynchronously copy a file."""
    await target_file.parent.mkdir(parents=True, exist_ok=True)
    async with source_file.open("rb") as src, target_file.open("wb") as dst:
        while chunk := await src.read(1024 * 1024):
            await dst.write(chunk)
