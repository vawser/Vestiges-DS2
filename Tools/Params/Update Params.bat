:: Unpack the params first

:: Copy param files to Vestiges param folder
copy /b/v/y "E:\Program Files (x86)\SteamLibrary\steamapps\common\Dark Souls II Scholar of the First Sin\Modding\Mod\Tools\Params\params-bnd-dcx\" "E:\Program Files (x86)\SteamLibrary\steamapps\common\Dark Souls II Scholar of the First Sin\Modding\Mod\Vestiges\param\"

:: Delete the yabber xml file from the Vestiges param folder
del /q "E:\Program Files (x86)\SteamLibrary\steamapps\common\Dark Souls II Scholar of the First Sin\Modding\Mod\Vestiges\param\_yabber-bnd4.xml"

:: Copy param files to Game param folder
copy /b/v/y "E:\Program Files (x86)\SteamLibrary\steamapps\common\Dark Souls II Scholar of the First Sin\Modding\Mod\Tools\Params\params-bnd-dcx\" "E:\Program Files (x86)\SteamLibrary\steamapps\common\Dark Souls II Scholar of the First Sin\Game\Param\"

:: Delete the yabber xml file from the Game param folder
del /q "E:\Program Files (x86)\SteamLibrary\steamapps\common\Dark Souls II Scholar of the First Sin\Game\Param\_yabber-bnd4.xml"

