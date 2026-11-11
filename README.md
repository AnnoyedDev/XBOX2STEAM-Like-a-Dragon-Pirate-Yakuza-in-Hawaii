# XBOX2STEAM-Like-a-Dragon-Pirate-Yakuza-in-Hawaii
Convert save from XBOX Game Pass into a save compatible on Steam for Like a Dragon : Pirate Yakuza in Hawaii

Convert a savegame from LAD Pirate Yakuza Game Pass into Steam.
Xbox : XOR(msgpack) + XUID(8 o) + CRC32(msgpack) ; Steam : XOR(msgpack) + CRC32(msgpack).
Usage : xbox2steam.py <xbox_entry> <steam_output>
