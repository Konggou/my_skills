import os
import shutil
from pathlib import Path

def get_skills_root():
    # 获取用户主目录
    home = Path.home()
    # 根据操作系统确定技能根目录
    if os.name == 'nt':  # Windows
        return home / '.trae' / 'skills'
    else:  # Linux, macOS, etc.
        return home / '.trae' / 'skills'

def main():
    skills_root = get_skills_root()

    if not skills_root.exists():
        print(f"技能目录 '{skills_root}' 不存在。脚本将退出。")
        return

    nested_skill_paths = [
        skills_root / 'anthropics-skills' / 'skills',
        skills_root / 'vercel-agent-skills' / 'skills',
        skills_root / 'external',
        skills_root / 'custom'
    ]

    for path in nested_skill_paths:
        if path.exists() and path.is_dir():
            print(f"正在处理目录: {path}")
            for skill_dir in path.iterdir():
                if skill_dir.is_dir():
                    destination_path = skills_root / skill_dir.name
                    if destination_path.exists():
                        print(f"技能 '{skill_dir.name}' 已存在于根目录，跳过。")
                    else:
                        print(f"正在移动 '{skill_dir.name}' 到根技能目录。")
                        shutil.move(str(skill_dir), str(skills_root))
        else:
            print(f"目录未找到: {path}，跳过。")

    print("技能移动完成。")

if __name__ == "__main__":
    main()
