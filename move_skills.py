import os
import shutil
from pathlib import Path
from typing import List, Tuple

def MoveSkillsFromDirectories(source_directories: List[Path], destination: Path) -> None:
    """
    Move skills from specified source directories to destination directory
    
    Args:
        source_directories: List of source directories, each may contain skill subdirectories or have skills in a 'skills' subdirectory
        destination: Destination directory (current working directory)
    """
    if not destination.exists():
        destination.mkdir(parents=True, exist_ok=True)
        print(f"Created destination directory: {destination}")
    
    moved_count = 0
    skipped_count = 0
    
    for source_dir in source_directories:
        if not source_dir.exists():
            print(f"Source directory does not exist, skipping: {source_dir}")
            continue
        
        if not source_dir.is_dir():
            print(f"Not a directory, skipping: {source_dir}")
            continue
        
        print(f"\nProcessing directory: {source_dir}")
        
        # Check if 'skills' subdirectory exists (e.g., anthropics-skills/skills)
        skills_subdir = source_dir / 'skills'
        if skills_subdir.exists() and skills_subdir.is_dir():
            # Copy from skills subdirectory
            moved, skipped = ProcessSkillDirectory(skills_subdir, destination)
        else:
            # Move directly from current directory
            moved, skipped = ProcessSkillDirectory(source_dir, destination)
        
        moved_count += moved
        skipped_count += skipped
    
    print(f"\nMove completed. Moved: {moved_count}, Skipped: {skipped_count}")

def ProcessSkillDirectory(source_dir: Path, destination: Path) -> Tuple[int, int]:
    """
    Process all skill subdirectories in the source directory
    
    Args:
        source_dir: Source directory
        destination: Destination directory
    
    Returns:
        (number of moved items, number of skipped items)
    """
    moved_count = 0
    skipped_count = 0
    
    for item in source_dir.iterdir():
        if not item.is_dir():
            continue
        
        # Skip hidden directories and special directories
        if item.name.startswith('.') or item.name in ['__pycache__', 'node_modules']:
            continue
        
        destination_path = destination / item.name
        
        if destination_path.exists():
            print(f"  ⚠️  Skill '{item.name}' already exists in destination, skipping.")
            skipped_count += 1
        else:
            try:
                print(f"  📦 Moving '{item.name}' to {destination}")
                shutil.move(str(item), str(destination_path))
                moved_count += 1
            except Exception as e:
                print(f"  ❌ Failed to move '{item.name}': {e}")
                skipped_count += 1
    
    return moved_count, skipped_count

def main():
    # Get the directory where the script is located
    script_dir = Path(__file__).parent
    
    # Define source directory list (relative to script directory)
    source_directories = [
        script_dir / 'anthropics-skills',
        script_dir / 'custom',
        script_dir / 'external',
        script_dir / 'vercel-agent-skills'
    ]
    
    # Destination directory is the current working directory
    destination = Path.cwd()
    
    print(f"Script directory: {script_dir}")
    print(f"Destination directory: {destination}")
    print(f"Number of source directories: {len(source_directories)}")
    
    MoveSkillsFromDirectories(source_directories, destination)

if __name__ == "__main__":
    main()
