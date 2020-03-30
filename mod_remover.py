import os

NAMES = ["Installers", "update", "x64", "bink2w64.dll", "commandline.txt", "common.rpf", "d3dcompiler_46.dll", "d3dcsx_46.dll",
    "GFSDK_ShadowLib.win64.dll", "GFSDK_TXAA.win64.dll", "GFSDK_TXAA_AlphaResolve.win64.dll", "GTA5.exe", "GTAVLanguageSelect.exe",
    "GTAVLauncher.exe", "installscript.vdf", "PlayGTAV.exe", "steam_api64.dll", "x64a.rpf", "x64b.rpf", "x64c.rpf", "x64d.rpf", "x64e.rpf",
    "x64f.rpf", "x64g.rpf", "x64h.rpf", "x64i.rpf", "x64j.rpf", "x64k.rpf", "x64l.rpf", "x64m.rpf", "x64n.rpf", "x64o.rpf", "x64p.rpf",
    "x64q.rpf", "x64r.rpf", "x64s.rpf", "x64t.rpf", "x64u.rpf", "x64v.rpf", "x64w.rpf"]

DIRECTORY = "D:\\Gaming\\Steam\\steamapps\\common\\Grand Theft Auto V"
DESKTOP = "D:\\Desktop"

def main():
    # Create folder to move files to
    folderName = "removed_mods"
    desktopFiles = os.listdir(DESKTOP)
    i = 1
    while(True):
        if folderName in desktopFiles:
            folderName = "removed_mods_" + str(i)
            i += 1
        else:
            DESTINATION = DESKTOP + "\\" + folderName
            os.mkdir(DESTINATION)
            break
    
    # Remove files
    inFolder = os.listdir(DIRECTORY)
    for j in inFolder:
        if j not in NAMES:
            print("moving: " + j + "...")
            os.rename(DIRECTORY + "\\" + j, DESTINATION + "\\" + j)
            print("moved from " + DIRECTORY + " to " + DESTINATION)
            

if __name__ == "__main__":
    print("running")
    main()
    print("finished")
