import os
import argparse
from pathlib import Path
import shutil

ALLOWED_FILES = ['battleye', 'bink2w64.dll', 'commandline.txt', 'common.rpf', 'd3dcompiler_46.dll', 'd3dcsx_46.dll', 'fvad.dll', 'gfsdk_shadowlib.win64.dll', 'gfsdk_txaa.win64.dll', 'gfsdk_txaa_alpharesolve.win64.dll', 'gpuperfapidx11-x64.dll', 'gta5.exe', 'gta5_be.exe', 'gtavlanguageselect.exe', 'gtavlauncher.exe', 'installscript.vdf', 'installscript_sdk.vdf', 'libcurl.dll', 'libtox.dll', 'nvpmapi.core.win64.dll', 'opus.dll', 'opusenc.dll', 'playgtav.exe', 'redistributables', 'steam_api64.dll', 'title.rgl', 'update', 'version.txt', 'x64', 'x64a.rpf', 'x64b.rpf', 'x64c.rpf', 'x64d.rpf', 'x64e.rpf', 'x64f.rpf', 'x64g.rpf', 'x64h.rpf', 'x64i.rpf', 'x64j.rpf', 'x64k.rpf', 'x64l.rpf', 'x64m.rpf', 'x64n.rpf', 'x64o.rpf', 'x64p.rpf', 'x64q.rpf', 'x64r.rpf', 'x64s.rpf', 'x64t.rpf', 'x64u.rpf', 'x64v.rpf', 'x64w.rpf', 'zlib1.dll']


class CustomException(Exception): pass


def is_gta_folder(dir: Path) -> bool:
    files = map(str.lower, os.listdir(dir))
    
    return "gta5.exe" in files


def create_dir() -> str:
    print("Creating directory...")
    dir_path = Path("removed_mods")
    i = 1
    while dir_path.exists():
        print(f"{dir_path} already exists")
        dir_path = Path(f"removed_mods_{i}")
        i += 1
    
    os.mkdir(dir_path)
    print(f"Created directory {dir_path}")
    return dir_path


def remove_files(gtadir: str, outdir=""):
    # Check GTA directory
    if not is_gta_folder(gtadir):
        raise CustomException(f"Could not locate GTA5.exe in {gtadir}")

    dir_path = Path(outdir)
    # Attempt to create the outdir
    if len(outdir.strip()) == 0:
        dir_path = Path(create_dir())
    # Or confirm directory exists
    else:
        if not dir_path.exists():
            raise CustomException(f"Directory {outdir} does not exist!")
        elif not dir_path.is_dir():
            raise CustomException(f"{outdir} is not a directory!")
    
    print(f"Using dir {dir_path}")
    
    # Remove all non-native files from GTA folder
    files = map(str.lower, os.listdir(gtadir))
    for file in files:
        if file not in ALLOWED_FILES:
            print(f"moving {file}...")
            shutil.move(f"{gtadir}\\{file}", f"{dir_path}\\{file}")
            print(f"moved from {gtadir} to {dir_path}")

    print(f"Done. All mods moved to {outdir}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='GTA V Mod Remover',
        description='Removes mods from GTA V',
    )
    parser.add_argument('gtadir')
    parser.add_argument('--outdir', default="")
    args = parser.parse_args()

    try:
        remove_files(args.gtadir, args.outdir)
    except CustomException as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unknown error: {e}")
