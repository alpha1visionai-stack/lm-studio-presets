#!/usr/bin/env python3
"""
LM Studio Presets Installer (Cross-Platform)
Installs all JSON presets into ~/.lmstudio/config-presets/
"""

import os
import sys
import shutil
from pathlib import Path

def main():
    script_dir = Path(__file__).resolve().parent
    presets_src = script_dir / "presets"
    
    # Destination directory across OS
    target_dir = Path.home() / ".lmstudio" / "config-presets"
    
    if not presets_src.exists():
        print(f"❌ Error: Presets directory not found at: {presets_src}")
        sys.exit(1)
        
    target_dir.mkdir(parents=True, exist_ok=True)
    
    preset_files = list(presets_src.glob("*.json"))
    
    print(f"\n📦 Installing {len(preset_files)} LM Studio Presets to: {target_dir}")
    print("-" * 60)
    
    for p in preset_files:
        dst = target_dir / p.name
        shutil.copy2(p, dst)
        print(f" ✔ Installed: {p.name}")
        
    print("-" * 60)
    print("✨ All presets installed successfully!")
    print("Restart or open LM Studio to use your presets.\n")

if __name__ == "__main__":
    main()
